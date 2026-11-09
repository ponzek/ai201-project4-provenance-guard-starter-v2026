#!/usr/bin/env python3
"""
Per-creator limits check.  <- UNIT 8 STRETCH

    python app.py                 # in one terminal
    python per_creator_check.py   # in another

The limiter counts requests per creator_id (app.py::rate_limit_key), falling
back to the caller's address only when there is no usable creator_id. All of
these requests come from the same address (this laptop), so:

  1. writer_a sends 6 in a row       -> 5 x 200, then 429
  2. writer_b sends 1 right after    -> 200, because writer_b has its own count
  3. one script sends 6, each with a
     new made-up creator_id          -> 6 x 200, never limited

Part 2 is what per-creator limiting buys: people sharing an address don't block
each other. Part 3 is what it costs: anyone can type a new creator_id.

Writes results/per_creator_<date>.md.
"""

import datetime as dt
import json
import uuid

import requests

import config

URL = f"http://{config.HOST}:{config.PORT}"
TEXT = ("I am checking that two writers on the same connection each get their "
        "own rate limit, and that one writer cannot use up the other's.")


def send(creator):
    r = requests.post(f"{URL}/submit", json={"text": TEXT, "creator_id": creator}, timeout=90)
    return r.status_code


def main():
    run_tag = uuid.uuid4().hex[:6]
    a = [send(f"writer_a_{run_tag}") for _ in range(6)]
    b = [send(f"writer_b_{run_tag}")]
    rotating = [send(f"script_{run_tag}_{i}") for i in range(6)]

    results = {"writer_a (6 in a row)": a,
               "writer_b (1, right after, same address)": b,
               "script with a new creator_id each time (6)": rotating}
    for name, codes in results.items():
        print(f"{name:<45} {' '.join(map(str, codes))}")

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    path = config.RESULTS_DIR / f"per_creator_{stamp}.md"
    path.write_text("# Per-creator limits check\n\n"
                    "- Produced by: `per_creator_check.py::main`\n"
                    f"- {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}, all from one address\n\n"
                    "```json\n" + json.dumps(results, indent=2) + "\n```\n",
                    encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()

