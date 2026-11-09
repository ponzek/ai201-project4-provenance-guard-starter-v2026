#!/usr/bin/env python3
"""
The parts of my criteria that run_eval.py can't send.  <- UNIT 8, MILESTONE 3

    python app.py                                  # in one terminal
    python criteria_extra.py --label before        # in another

run_eval.py only sends {"text", "creator_id"} bodies to /submit. Three of my
checks need something else, so they live here and run three trials each, the
same as run_eval.py:

    criterion 3   the boundary scores 0, 0.35, 0.525, 0.70 and 1 go through
                  scoring.py::score_to_label and come back human, human,
                  unsure, ai, ai.
    criterion 4   submit five texts, appeal each content_id, then check the
                  appeal was confirmed, the log has an appeal entry with status
                  under_review and my reasoning, and the original decision is
                  still there.
    criterion 5   the sixth invalid input: a body that is not valid JSON. It
                  can't be written as a dict in scenarios.py.

Like run_eval.py, this records what came back. The verdicts go in the README.
Writes results/criteria_extra_<date>_<label>.md.
"""

import argparse
import datetime as dt
import json
import sys

import config
import scenarios
import scoring

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"

BOUNDARIES = [(0.0, "human"), (0.35, "human"), (0.525, "unsure"), (0.70, "ai"), (1.0, "ai")]

APPEAL_REASON = "I wrote this myself. This is a test appeal for criterion 4."


def boundary_trial():
    results = []
    for score, expected in BOUNDARIES:
        guess, _ = scoring.score_to_label(score)
        results.append({"score": score, "expected": expected, "guess": guess,
                        "ok": guess == expected})
    return results


def appeal_trial(requests, url, trial, timeout):
    results = []
    # Five of my own pieces, the last five in MY_WRITING.
    for i, text in enumerate(scenarios.MY_WRITING[5:], 1):
        creator = f"eval_c4_t{trial}_{i}"
        sub = requests.post(f"{url}/submit", json={"text": text, "creator_id": creator},
                            timeout=timeout)
        sub_body = sub.json()
        content_id = sub_body.get("content_id")

        app = requests.post(f"{url}/appeal",
                            json={"content_id": content_id, "reasoning": APPEAL_REASON},
                            timeout=timeout)
        app_body = app.json()

        entries = [e for e in requests.get(f"{url}/log", timeout=timeout).json()["entries"]
                   if e.get("content_id") == content_id]
        original = [e for e in entries if e.get("status") == "decided"]
        appeals = [e for e in entries if e.get("event") == "appeal"]

        results.append({
            "content_id": content_id,
            "submit_status": sub.status_code,
            "guess": sub_body.get("guess"),
            "appeal_status_code": app.status_code,
            "appeal_response": app_body,
            "log_original_decision_kept": len(original) == 1,
            "log_appeal_entry": appeals[-1] if appeals else None,
            "ok": (app.status_code == 200
                   and app_body.get("status") == "under_review"
                   and len(original) == 1
                   and len(appeals) == 1
                   and appeals[0].get("status") == "under_review"
                   and appeals[0].get("reasoning") == APPEAL_REASON),
        })
    return results


def invalid_json_trial(requests, url, timeout):
    response = requests.post(f"{url}/submit", data=b'{"text": "not closed',
                             headers={"Content-Type": "application/json"},
                             timeout=timeout)
    try:
        body = response.json()
    except ValueError:
        body = {"not_json": response.text[:200]}
    return [{"sent": '{"text": "not closed', "status": response.status_code,
             "response": body, "ok": 400 <= response.status_code < 500 and "error" in body}]


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--timeout", type=float, default=90.0)
    args = parser.parse_args()

    import requests

    checks = {"criterion 3: boundary scores": [], "criterion 4: appeals": [],
              "criterion 5: body that is not valid JSON": []}
    for trial in range(1, args.trials + 1):
        checks["criterion 3: boundary scores"].append(boundary_trial())
        checks["criterion 4: appeals"].append(appeal_trial(requests, args.url, trial, args.timeout))
        checks["criterion 5: body that is not valid JSON"].append(
            invalid_json_trial(requests, args.url, args.timeout))

    lines = [f"# Criteria extra checks{f' — {args.label}' if args.label else ''}", "",
             "- Produced by: `criteria_extra.py::main`",
             f"- {args.trials} trials · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]
    for name, trials in checks.items():
        summary = ", ".join(f"run {i}: {sum(r['ok'] for r in t)}/{len(t)}"
                            for i, t in enumerate(trials, 1))
        print(f"{name}  ->  {summary}")
        lines += [f"## {name}", "", f"Passed: {summary}", ""]
        for i, results in enumerate(trials, 1):
            lines += [f"**Trial {i}**", "", "```json", json.dumps(results, indent=2,
                                                                   ensure_ascii=False), "```", ""]

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"criteria_extra_{stamp}{label}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()

