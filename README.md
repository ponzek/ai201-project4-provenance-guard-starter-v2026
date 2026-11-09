# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

My project checks writing using two different signals. They can make
mistakes, so writers can appeal if they disagree with a result.

1. The writer sends their text and creator ID to `/submit`.
2. The service checks the text and gives it a content ID.
3. The model checks how predictable the writing is.
4. The style signal checks sentence lengths, word variety, and punctuation.
5. I combine the scores using 60% model and 40% style. If they disagree
   by more than 0.40, I cap the combined score at 0.65 so it cannot
   receive the AI label.
6. The score determines whether the label is human, AI, or unsure.
7. The service saves the decision in the log and returns the result.
   The writer can use their content ID to submit an appeal.

### A false positive, step by step

This is the recorded case from the Sample Run, content ID `61ecd9a8-ec91-4110-85f8-3a8da8a12cf2`.

1. Someone submits a plain paragraph with short, simple sentences about a cat.
2. The model signal gives 0.843 because the words are easy to predict. The style signal gives 0.6357 because the sentences are short and even. They are only 0.21 apart, so my cap does not apply.
3. The combined score is 0.6 x 0.843 + 0.4 x 0.6357 = 0.7601. That is above 0.70, so the label is AI.
4. The writer sees: "Our tools think this was probably written with the help of AI. They can be wrong. If you wrote it yourself, you can appeal and a person will take a look."
5. They send their content ID and their reasoning to `/appeal`. The service adds an appeal entry to the log with status `under_review`.
6. Nothing else changes. The label and scores stay the same, nothing re-checks the text, nobody is notified, and I have not built a way for a reviewer to finish the appeal.

The cat paragraph was written by my coding assistant as an example of plain writing, not by me.

### Endpoint shapes

**`POST /submit`**

```text
In:  {"text": "...", "creator_id": "..."}
     text is required, up to 20,000 characters. creator_id is optional and defaults to "anonymous".
Out: {"content_id": "...", "guess": "ai | human | unsure", "confidence": 0.0,
      "label": "the full sentence a reader sees", "model_score": 0.0, "style_score": 0.0}
     confidence is the combined AI-like score, not how sure the system is.
Errors: {"error": "...", "message": "..."}
     400 invalid_text, 400 text_too_short, 413 text_too_long, 503 detector_unavailable
```

**`POST /appeal`**

```text
In:  {"content_id": "...", "reasoning": "..."}
Out: {"content_id": "...", "status": "under_review", "message": "..."}
Errors: 400 invalid_content_id, 400 invalid_reasoning, 404 unknown_content_id
```


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable my text is to GPT-2, a language model that runs on my own computer. It reads the first 400 tokens (about 300 words) and I turn the result into a score from 0 to 1. Higher means more AI-like. The formula is `1 / (1 + (perplexity / 45) ** 1.6)`, so a perplexity of 45 gives 0.5.

**Why that might differ between human and AI writing:** An AI picks likely next words, so its writing is often easy for a model to predict. People use odd words and sudden turns that a model does not expect.

**What it can't see:** Predictable is not the same as written by AI. Plain writing with simple words and short sentences looks AI-like to it. A plain test paragraph about a cat got a model score of 0.84. It also only reads the first 400 tokens, and AI text full of rare words can look human to it.

### Signal two — the style signal

**What it measures:** The shape of the text, not what it says. I measure three things: sentence length spread (standard deviation of words per sentence divided by the average), word variety (unique words divided by total words, over the first 100 words), and punctuation density (commas, semicolons, colons, parentheses, quotes, and dashes per word). I flip each one so that higher means more AI-like, then combine them: `0.45 * spread + 0.30 * word variety + 0.25 * punctuation`. Text under five words gets a neutral 0.5. The scaling numbers are my estimates, not tested on real data.

**Why that might differ between human and AI writing:** AI writing often has sentences of similar length and a narrower set of words. Human writing is lumpier, with a short sentence next to a long one.

**What it can't see:** It cannot read, so it does not know what the text means or who wrote it. Typos, splitting sentences, or pasting in a quotation can change the score without changing who wrote it. A one-sentence text has no spread at all, which pushes it toward AI-like.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** I take a weighted average of the two scores. If the two signals disagree by more than 0.40, I cap the combined score just below the AI cutoff, so a disagreement can never end in the AI label. A higher score means more AI-like. It does not mean more confidence. The `confidence` field in the response holds this score.

**The numbers:** Model weight 0.60, style weight 0.40. Disagreement limit 0.40. Cap 0.65. Scores 0.35 or lower are human, 0.70 or higher are AI, and anything between is unsure. They are in `config.py` as `WEIGHT_MODEL_SIGNAL`, `WEIGHT_STYLE_SIGNAL`, `SPLIT_GAP`, `HUMAN_THRESHOLD` and `AI_THRESHOLD`.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:** I submitted a short passage that begins "Climate change is one of the most pressing challenges of our time." The model signal gave 0.9104 because the phrases are very predictable. The style signal gave 0.3506 because the sentences differ in length and it has a lot of commas. They are 0.56 apart, which is more than 0.40. The plain weighted average would have been about 0.6865. My rule capped it at 0.65, and the label was unsure. The label would have been unsure without the cap too, so here the cap only lowered the score. The log entry has content_id `3ed8c83f-c9a8-40fd-a9f8-234ae0bb6615`.

**Four test inputs, side by side**

These are the recorded results. My coding assistant wrote all four passages as examples. Each one is in `logs/audit.jsonl`.

| Input | Starts with | model | style | combined | label | Log line |
|---|---|---|---|---|---|---|
| Clearly AI | "The implementation of the proposed framework requires careful consideration..." | 0.8552 | 0.6221 | 0.762 | AI | 1 |
| Clearly human | "Honestly? I burned the toast again, swore at the smoke alarm..." | 0.3119 | 0.0211 | 0.1956 | human | 2 |
| Formal human | "The committee reviewed the proposal and, after considerable deliberation..." | 0.6216 | 0.4789 | 0.5645 | unsure | 11 |
| Lightly edited AI | "The implementation of the proposed framework requires careful consideration..." with "it is" changed to "its", one comma removed, and ", which is tricky" added | 0.6955 | 0.5993 | 0.657 | unsure | 12 |

The lightly edited AI text is the clearly AI text with three tiny changes. Its combined score dropped from 0.762 to 0.657, so the label went from AI to unsure. That is one example, not a test, but it shows small edits can move a result.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 to 0.35 | We think this was probably written by a person. |
| unsure | above 0.35 and below 0.70 | We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you. |
| high-confidence AI | 0.70 to 1.00 | Our tools think this was probably written with the help of AI. They can be wrong. If you wrote it yourself, you can appeal and a person will take a look. |

I checked that all three can be reached with real submissions: a thank-you note scored 0.1995 and got the human label (`bd7471f2-6347-4c60-b0fb-a068d01f971c`), a short paragraph about an old photograph scored 0.6546 and got unsure (`08e98463-ed81-461e-8a33-674080a8c58c`), and a plain paragraph about a cat scored 0.7601 and got the AI label (`61ecd9a8-ec91-4110-85f8-3a8da8a12cf2`).

**Why I worded the "unsure" one this way:** I wanted it to say honestly that the system cannot tell, without sounding like it is accusing anyone. I added "plenty of people write this way" because plain writing can look AI-like to my signals, and "Nothing is being held against you" so the writer does not feel in trouble.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

I ran this with `curl.exe` on Windows, sending the same JSON from a file.

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "We have a cat. The cat is white. The cat sleeps on the bed. I feed the cat each day. I love my cat very much. She loves me too.", "creator_id": "karina"}'
```

```json
{"confidence":0.7601,"content_id":"61ecd9a8-ec91-4110-85f8-3a8da8a12cf2","guess":"ai","label":"Our tools think this was probably written with the help of AI. They can be wrong. If you wrote it yourself, you can appeal and a person will take a look.","model_score":0.843,"style_score":0.6357}
```

These test passages were written by my coding assistant as examples. I did not write them, and none of them is a real writer's work. The cat paragraph is an example of plain, simple writing, which is the kind my signals can wrongly flag. The AI label on it is therefore a wrong call, and the appeal wording below is a test message.

**An appeal**

This uses the same `content_id` as the submission above.

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "61ecd9a8-ec91-4110-85f8-3a8da8a12cf2", "reasoning": "I wrote this myself as a simple paragraph about my cat. Short, plain sentences are how I write."}'
```

```json
{"content_id":"61ecd9a8-ec91-4110-85f8-3a8da8a12cf2","message":"Thanks. Your appeal was recorded and a person will review it.","status":"under_review"}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{"count":3,"entries":[{"combined_score":0.65,"content_id":"3ed8c83f-c9a8-40fd-a9f8-234ae0bb6615","creator_id":"karina","guess":"unsure","label":"We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.","model_score":0.9104,"status":"decided","style_score":0.3506,"timestamp":"2026-10-29T01:40:43+00:00"},{"combined_score":0.7601,"content_id":"61ecd9a8-ec91-4110-85f8-3a8da8a12cf2","creator_id":"karina","guess":"ai","label":"Our tools think this was probably written with the help of AI. They can be wrong. If you wrote it yourself, you can appeal and a person will take a look.","model_score":0.843,"status":"decided","style_score":0.6357,"timestamp":"2026-10-29T01:40:43+00:00"},{"content_id":"61ecd9a8-ec91-4110-85f8-3a8da8a12cf2","creator_id":"karina","event":"appeal","reasoning":"I wrote this myself as a simple paragraph about my cat. Short, plain sentences are how I write.","status":"under_review","timestamp":"2026-10-29T01:40:43+00:00"}]}
```

The original decision (`"status":"decided"`) stays in the log and the appeal is added after it.

**Which entries in `logs/audit.jsonl` are which**

`logs/audit.jsonl` has 12 lines. I kept all of them.

- **Lines 1 to 5:** earlier test entries (creator `me`, plus one rejected empty request). They were made before `criteria.md` was written. The file was missing these five lines before the run below, so they were restored by copying the original entries exactly.
- **Lines 6 to 8:** the other three submissions from this run (the thank-you note for the human label, the photograph paragraph for unsure, and the climate paragraph for the split case).
- **Lines 9 and 10:** the sample run above. Line 9 is the submission and line 10 is the appeal, both with `content_id` `61ecd9a8-ec91-4110-85f8-3a8da8a12cf2`.
- **Lines 11 and 12:** the formal human input and the lightly edited AI input from the four-input table. They were added after the sample run so the table would have a logged result for every row.

**Python version:** All of the scores, requests and log entries above were produced on Python 3.10.10. The course asks for Python 3.11 or newer, and `test.py` flagged that. Afterward I made a second virtual environment with Python 3.13.5, and `test.py` passes there with 9 passed and 0 failed. I did not rerun the sample run on 3.13, so the results above are from 3.10.10.

---

## How I Used AI

**Moment 1**

- *What I asked for:* I had my coding assistant build the service from the starter: the style signal, the combining rule, the three labels, and the `/submit` and `/appeal` routes.
- *What came back:* Working code. Its first test showed that a plain paragraph with short sentences got the AI label, which is the false positive the project warns about. It also left `criteria.md` blank, because the brief says the criteria are mine.
- *What I changed:* I did not change the thresholds after seeing that result. I wrote my own five criteria in `criteria.md` and a note there that the code was started before the criteria. I also wrote the "What This Does" section myself.

**Moment 2**

- *What I asked for:* I asked the assistant to review my criteria against the grading rubric.
- *What came back:* It said criterion 5 could not fail, because the code already handled every bad input on my list, and suggested a harder test.
- *What I changed:* I rewrote criterion 5 and then asked for it to be repeatable. It now lists six invalid inputs and three exact strings, `!!!!!!!!`, `........` and a string of emoji. It says a miss is any of those three returning `guess` equal to "ai". I also told the assistant not to clear the audit log and to keep the earlier test entries.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Stretch

**Declared before building:** I am going for **a second measured improvement**. After my first fix, I will make one more change based on my diagnoses, run my criteria and the attack set again, and say whether it helped.

**Also declared before building (added after the criteria run, before any work on these):**

- **Per-creator limits.** My limiter will count requests per `creator_id` instead of per address. I will test that two writers on the same address get separate limits, and write down which abuse this catches that per-address limits miss, and what it costs.
- **Three attacks on someone else's system.** I will write three attacks against a classmate's Provenance Guard service and report what each one did. This depends on getting access to another team's running service.

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

A real writer submits their own work a few times an hour, maybe a couple more times if they fix a typo. 5 a minute and 50 a day never gets in their way. A script trying to find my thresholds needs hundreds or thousands of tries. At 50 a day that would take weeks for one account. I did not go lower than 5 a minute because the first submission is slow while the model loads, and someone who clicks again out of impatience should not get blocked.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

The `creator_id` they send. If there is no `creator_id`, it falls back to their address. This is good for people who share one address, like a family or a classroom, because each writer gets their own limit. The problem is that anyone can type any `creator_id`, so a script that changes its name on every request never gets blocked.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

From `run_attacks.py::run_flood`, saved in `results/flood_2026-11-08_1839.md`:

```
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
```

Every 429 is written to the audit log. This is one of them from `GET /log`. It has all nine fields, with `null` where there was no decision:

```json
{"combined_score":null,"content_id":null,"creator_id":"flood_tester","event":"rejected","guess":null,"label":null,"limit":"5 per 1 minute","model_score":null,"reason":"rate_limited","status":"rejected","style_score":null,"timestamp":"2026-11-08T23:39:34+00:00"}
```

`results/flood_2026-11-08_1836.md` is an earlier run of the same test, from before I added the missing fields to rejected entries.

### Per-creator limits (stretch)

My limiter counts per `creator_id` (`app.py::rate_limit_key`). It only falls back to the address when there is no usable `creator_id`. The key function came with the starter, so my part was turning it on, testing it, and writing down what it changes. I tested it with `per_creator_check.py`, sending everything from the same address (my laptop). Output in `results/per_creator_2026-11-08_2034.md`:

```
writer_a (6 in a row)                         200 200 200 200 200 429
writer_b (1, right after, same address)       200
script with a new creator_id each time (6)    200 200 200 200 200 200
```

- **What it catches that per-address limits miss:** One writer flooding can't block other writers on the same address. writer_a got cut off, and writer_b, from the same address, still got through. With per-address limits, a family, a classroom or a library sharing one connection would share 5 per minute, and one busy person would lock out everyone else. It also catches a single account sending from many addresses (a phone, then a laptop, then a VPN), because the count follows the `creator_id`, not the address.
- **What it costs:** The `creator_id` is whatever the caller types, and nothing checks it. The script that made up a new `creator_id` each time was never limited (6 out of 6 got through). Per-address limits would have stopped that script after 5. This is also why the 32 text attacks in `attacks.csv` never hit my limit: each one used its own `attacker_<id>`. Real per-creator limits would need logged-in accounts, so a `creator_id` can't be made up.

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

I ran all 56 attacks with `python run_attacks.py --set attack_set --label before`. The full output is in `results/attack_run_2026-11-08_1901_before.md`. Nothing crashed. There were no 500s and no dropped connections.

**How I decided held or broke:**

- **AI text** (evasion and prompt injection): it **broke** if it did not get the AI label. I count "unsure" as getting through, because my unsure label tells the writer "Nothing is being held against you."
- **Human text** (false positive): it **broke** if it got the AI label.
- **Junk and malformed requests:** they **held** if they got a 4xx error, or a result that was not "ai". This is the same rule as my criterion 5.
- **Flood:** it **held** if the limiter started returning 429.

**Result: 14 broke, 42 held.**

| Family | Attacks | Broke | Held |
|---|---|---|---|
| evasion | 10 | 9 | 1 |
| false_positive | 8 | 2 | 6 |
| prompt_injection | 6 | 3 | 3 |
| malformed | 20 | 0 | 20 |
| flood_same_creator | 12 | 0 | 12 |

| ID | Family | Targeting | Status | Guess | Combined | Model | Style | Verdict |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | human | 0.306 | 0.164 | 0.519 | **BROKE** |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.446 | 0.594 | 0.222 | **BROKE** |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.512 | 0.666 | 0.281 | **BROKE** |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.563 | 0.611 | 0.489 | **BROKE** |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.267 | 0.321 | 0.187 | **BROKE** |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.458 | 0.573 | 0.286 | **BROKE** |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.562 | 0.586 | 0.526 | **BROKE** |
| EV08 | evasion | signal one: text below the token window | 200 | human | 0.342 | 0.245 | 0.488 | **BROKE** |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.531 | 0.704 | 0.271 | **BROKE** |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.869 | 0.979 | 0.705 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.548 | 0.618 | 0.445 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.688 | 0.739 | 0.612 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.707 | 0.805 | 0.560 | **BROKE** |
| FP04 | false_positive | a student essay written to a rubric | 200 | unsure | 0.682 | 0.833 | 0.455 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.734 | 0.800 | 0.633 | **BROKE** |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.650 | 0.881 | 0.384 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.650 | 0.882 | 0.459 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | human | 0.344 | 0.322 | 0.375 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.378 | 0.463 | 0.250 | **BROKE** |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.193 | 0.204 | 0.176 | **BROKE** |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.497 | 0.594 | 0.352 | **BROKE** |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.417 | 0.500 | 0.294 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.423 | 0.640 | 0.096 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.510 | 0.558 | 0.438 | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | human | 0.200 | 0.000 | 0.500 | HELD |
| MF04 | malformed | text is only punctuation | 200 | human | 0.207 | 0.011 | 0.500 | HELD |
| MF05 | malformed | text is a very long single word | 200 | unsure | 0.650 | 0.998 | 0.500 | HELD |
| MF06 | malformed | text is emoji only | 200 | unsure | 0.650 | 0.997 | 0.500 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | unsure | 0.650 | 0.906 | 0.500 | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | unsure | 0.424 | 0.239 | 0.700 | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | human | 0.230 | 0.049 | 0.500 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |

**Things I noticed:**

- **RQ10 and RQ11 never reached my route.** Neither had a `creator_id` my service could read, so they counted against my own address. RQ02, RQ06, RQ07, RQ08 and RQ09 had already used up that address's 5 per minute, so these two got a 429 before my code ever saw them. I marked them held because nothing broke, but my route was never really tested on them.
- **MF05, MF06 and MF07 only held because of my cap.** The model gave a long row of "a", a row of emoji, and Arabic text scores of 0.91 to 0.998. The style signal gave 0.5 because it found fewer than five words. The signals were more than 0.40 apart, so my rule capped the score at 0.65. Without the cap, all three would have been labelled AI.
- **MF03 (control characters) and MF04 (punctuation) got the human label.** That is not an accusation, so they held by my rule. But the service still told someone "We think this was probably written by a person" about text with no words in it.
- **PI05 did not get into the log.** I checked its entry in `logs/audit.jsonl` by eye. The fake `"guess": "human"` inside the text did not become a field, and the entry says `"guess": "unsure"`.
- **The flood rows say "20 rapid submissions" but the file has 12 rows.** I ran all 12. The first 5 got through, and the other 7 got a 429.

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

From `logs/audit.jsonl`. In order: the two false positives (FP03 and FP05), the prompt injection that got the human label (PI02), two evasions that got the human label (EV01 and EV08), junk saved only by the cap (MF05), junk labelled human (MF03), a 413 rejection (MF08), a 429 from the flood rows, and a 429 from RQ10, which never reached my route.

```json
{"timestamp": "2026-11-09T00:01:53+00:00", "content_id": "4ecaffe1-9e4f-4977-af76-a6d9be27f79f", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.5601, "combined_score": 0.7071, "label": "Our tools think this was probably written with the help of AI. They can be wrong. If you wrote it yourself, you can appeal and a person will take a look.", "status": "decided"}
{"timestamp": "2026-11-09T00:01:54+00:00", "content_id": "6125beab-0279-4589-8c53-51f328dc97c5", "creator_id": "attacker_FP05", "guess": "ai", "model_score": 0.8005, "style_score": 0.6333, "combined_score": 0.7336, "label": "Our tools think this was probably written with the help of AI. They can be wrong. If you wrote it yourself, you can appeal and a person will take a look.", "status": "decided"}
{"timestamp": "2026-11-09T00:01:54+00:00", "content_id": "c4ff34b7-f3fc-4c30-8b78-5d555cf99183", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.1759, "combined_score": 0.193, "label": "We think this was probably written by a person.", "status": "decided"}
{"timestamp": "2026-11-09T00:01:51+00:00", "content_id": "e1042610-bb6f-45d5-9889-08abc8a3466c", "creator_id": "attacker_EV01", "guess": "human", "model_score": 0.1635, "style_score": 0.5187, "combined_score": 0.3056, "label": "We think this was probably written by a person.", "status": "decided"}
{"timestamp": "2026-11-09T00:01:52+00:00", "content_id": "2400b209-7755-42b1-a506-c0439ad21c84", "creator_id": "attacker_EV08", "guess": "human", "model_score": 0.2452, "style_score": 0.4879, "combined_score": 0.3423, "label": "We think this was probably written by a person.", "status": "decided"}
{"timestamp": "2026-11-09T00:01:56+00:00", "content_id": "bcbb86fe-2b20-429a-a5fd-5a588a6bfcd8", "creator_id": "attacker_MF05", "guess": "unsure", "model_score": 0.9976, "style_score": 0.5, "combined_score": 0.65, "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.", "status": "decided"}
{"timestamp": "2026-11-09T00:01:55+00:00", "content_id": "4ece8e2c-e90d-4b5e-9099-2d66e3382c64", "creator_id": "attacker_MF03", "guess": "human", "model_score": 0.0, "style_score": 0.5, "combined_score": 0.2, "label": "We think this was probably written by a person.", "status": "decided"}
{"timestamp": "2026-11-09T00:01:56+00:00", "content_id": null, "creator_id": "attacker_MF08", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "text_too_long"}
{"timestamp": "2026-11-09T00:01:57+00:00", "content_id": null, "creator_id": "attacker_flood", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
{"timestamp": "2026-11-09T00:01:57+00:00", "content_id": null, "creator_id": "unknown", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

FP03. It is a person writing carefully in English as a second language about their first month in a new country. My service gave it the AI label with a score of 0.707, just over my 0.70 line. The model signal gave it 0.805 because short, simple, correct sentences are easy to predict. The style signal gave 0.560, which was not far enough away to trigger my cap. This is the writer I most wanted to protect. They are the most likely to be accused and the least likely to feel able to argue back.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing flagged as AI | ≤ 1 of 10 | 2/10 | 2/10 | 2/10 | MISSED |
| 2. AI set average minus my writing's average | ≥ +0.20 | −0.023 | −0.023 | −0.023 | MISSED |
| 3. Boundary scores correct, and all three labels appear in 12 passages | 5 of 5 boundaries, 3 of 3 labels | 5/5, 2 of 3 labels | 5/5, 2 of 3 labels | 5/5, 2 of 3 labels | MISSED |
| 4. Appeals confirmed and logged, original kept | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Invalid input gets a 4xx, junk text never gets "ai" | 6 of 6 and 3 of 3 | 6/6, 3/3 | 6/6, 3/3 | 6/6, 3/3 | MET |

**How I ran it:** `python run_eval.py --label before` ran the scenarios in `scenarios.py` three times. Its output is in `results/run_2026-11-08_2002_before.md`. Three of my checks can't be sent by `run_eval.py`: the boundary scores (criterion 3), the appeals (criterion 4), and a body that is not valid JSON (criterion 5). I wrote `criteria_extra.py` for those and ran it three times with `python criteria_extra.py --label before`. Its output is in `results/criteria_extra_2026-11-08_2002_before.md`. I changed nothing between trials.

All three trials came out exactly the same. Neither signal is random, so that is expected.

**How I decided each verdict:**

1. **MISSED.** 2 of my 10 pieces got the AI label in every trial. My target allows at most 1.
2. **MISSED.** The AI set averaged 0.5325 and my writing averaged 0.5557. The AI set scored 0.023 *lower* than my writing, and my target needed it to be at least 0.20 higher.
3. **MISSED.** All five boundary scores gave the right label in every trial. But across the 12 passages, the human label never appeared (0 human, 10 unsure, 2 ai). My target needs all three labels.
4. **MET.** All 5 appeals in every trial came back `under_review`. Each one added an appeal entry to the log with my reasoning, and the original decision stayed in the log.
5. **MET.** All six invalid inputs got a 4xx in every trial. Of the three junk strings, `!!!!!!!!` and `........` got a 400, and the emoji string got "unsure". None got "ai".

**Real output from one trial** (trial 1 of each):

**Criterion 1.** From `run_eval.py::main`, in `results/run_2026-11-08_2002_before.md`. These are my two pieces that got the AI label, plus my lowest-scoring piece for comparison.

```json
{"status": 200, "guess": "ai", "confidence": 0.7021, "model_score": 0.7713, "style_score": 0.5983, "label": "Our tools think this was probably written with the help of AI. They can be wrong. If you wrote it yourself, you can appeal and a person will take a look.", "sent": "I liked that the enrollment dashboard gave me a quick overview and sti"}
{"status": 200, "guess": "ai", "confidence": 0.7208, "model_score": 0.7379, "style_score": 0.6952, "label": "Our tools think this was probably written with the help of AI. They can be wrong. If you wrote it yourself, you can appeal and a person will take a look.", "sent": "For my quantum tunneling project, I wanted people to be able to change"}
{"status": 200, "guess": "unsure", "confidence": 0.3769, "model_score": 0.3399, "style_score": 0.4325, "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.", "sent": "For my thesis, I'm comparing four ways to generate a mammography repor"}
```

**Criterion 2.** From `run_eval.py::main`, in `results/run_2026-11-08_2002_before.md`. These are the highest and lowest AI passages, and one from the middle. The highest still only got "unsure", and the AI passage on my thesis topic got "human".

```json
{"status": 200, "guess": "unsure", "confidence": 0.6859, "model_score": 0.7674, "style_score": 0.5637, "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.", "sent": "Understanding SQL triggers can be challenging, particularly when it co"}
{"status": 200, "guess": "human", "confidence": 0.3111, "model_score": 0.3642, "style_score": 0.2314, "label": "We think this was probably written by a person.", "sent": "This thesis compares four approaches to generating mammography reports"}
{"status": 200, "guess": "unsure", "confidence": 0.5572, "model_score": 0.7253, "style_score": 0.305, "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.", "sent": "Being a first-generation student comes with unique challenges, includi"}
```

**Criterion 3.** The boundary scores are from `criteria_extra.py::boundary_trial`, which calls `scoring.py::score_to_label`, in `results/criteria_extra_2026-11-08_2002_before.md`:

```json
{"score": 0.0, "expected": "human", "guess": "human", "ok": true}
{"score": 0.35, "expected": "human", "guess": "human", "ok": true}
{"score": 0.525, "expected": "unsure", "guess": "unsure", "ok": true}
{"score": 0.7, "expected": "ai", "guess": "ai", "ok": true}
{"score": 1.0, "expected": "ai", "guess": "ai", "ok": true}
```

The label counts for the 12 passages are from `run_eval.py::main` ("label coverage" in `results/run_2026-11-08_2002_before.md`): `{"human": 0, "unsure": 10, "ai": 2}`

**Criterion 4.** From `criteria_extra.py::appeal_trial`, in `results/criteria_extra_2026-11-08_2002_before.md`. This is the first of the five:

```json
{"content_id": "5c39d24c-9046-482c-be51-71b06aa085ee", "submit_status": 200, "guess": "unsure", "appeal_status_code": 200, "appeal_response": {"content_id": "5c39d24c-9046-482c-be51-71b06aa085ee", "message": "Thanks. Your appeal was recorded and a person will review it.", "status": "under_review"}, "log_original_decision_kept": true, "log_appeal_entry": {"content_id": "5c39d24c-9046-482c-be51-71b06aa085ee", "creator_id": "eval_c4_t1_1", "event": "appeal", "reasoning": "I wrote this myself. This is a test appeal for criterion 4.", "status": "under_review", "timestamp": "2026-11-09T01:02:35+00:00"}, "ok": true}
```

**Criterion 5.** From `run_eval.py::main`, in `results/run_2026-11-08_2002_before.md`. In order: missing text, empty text, only spaces, a number, 20,001 characters, `!!!!!!!!`, `........`, emoji. I shortened the 20,001-character `sent` value.

```json
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "{\"creator_id\": \"eval_c5_missing\"}"}
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "(empty text)"}
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "     "}
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "{\"text\": 12345, \"creator_id\": \"eval_c5_number\"}"}
{"status": 413, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa..."}
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "!!!!!!!!"}
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "........"}
{"status": 200, "guess": "unsure", "confidence": 0.65, "model_score": 0.9921, "style_score": 0.5, "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.", "sent": "😀😀😀😀😀😀😀😀"}
```

`run_eval.py` does not save the error message, so here are the matching rejection entries from `logs/audit.jsonl`, written by `audit.py::log_rejection`. They show why each one was refused:

```json
{"timestamp": "2026-11-09T01:02:34+00:00", "content_id": null, "creator_id": "eval_c5_missing", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "invalid_text"}
{"timestamp": "2026-11-09T01:02:34+00:00", "content_id": null, "creator_id": "eval_c5_20001", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "text_too_long"}
{"timestamp": "2026-11-09T01:02:34+00:00", "content_id": null, "creator_id": "eval_c5_bangs", "guess": null, "model_score": null, "style_score": null, "combined_score": null, "label": null, "status": "rejected", "event": "rejected", "reason": "text_too_short"}
```

The sixth invalid input, a body that is not valid JSON, is from `criteria_extra.py::invalid_json_trial`:

```json
{"sent": "{\"text\": \"not closed", "status": 400, "response": {"error": "invalid_text", "message": "Send JSON with a non-empty 'text' string."}, "ok": true}
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

I have 3 missed criteria and 14 broken attacks. They come down to three problems.

**Problem 1: plain human writing gets the AI label.** (Criterion 1, FP03, FP05)

- **What broke:** Two of my own pieces (the dashboard reflection, 0.702, and Through the Barrier, 0.721) and two attack inputs (FP03, a non-native speaker, 0.707, and FP05, technical documentation, 0.734).
- **Stage: signal one, then the combining rule, then the label mapping.**
- **Mechanism:** All four are written in short, clear sentences with common words. GPT-2 finds that easy to predict, so perplexity is low and the model signal is high (0.738 to 0.805). My style signal makes the same mistake for the same kind of writing. Even sentence lengths and few commas read as AI to it, so it gave 0.560 to 0.695. Because both signals were high, they were never more than 0.40 apart, and my cap never applied. The cap only protects a writer when the signals *disagree*, not when they are wrong together. The model signal counts for 0.6, so it pushed all four just over 0.70. Three of the four were less than 0.03 over the line.

**Problem 2: my signals measure plainness, not who wrote it.** (Criterion 2, criterion 3, and why most evasions only needed to reach "unsure")

- **What broke:** The AI set averaged 0.5325 and my writing averaged 0.5557, so the gap was −0.023 instead of +0.20. None of the 10 AI passages got the AI label, and the AI passage on my thesis topic got "human" (0.311). Across 12 real passages the human label never appeared once.
- **Stage: signal one and signal two, then the label mapping.**
- **Mechanism:** The AI passages use longer, formal words like "allocation", "significantly" and "consideration". GPT-2 predicts those less well than my plainer words, so the AI passages got a *lower* model score (0.364 to 0.767) than my writing (0.340 to 0.864). The AI passages also have more commas and clauses, which my style signal reads as human (punctuation density goes up, so the style score goes down). Both signals reward the same thing, plain and simple text, and my writing is plainer than formal AI writing. So the order came out backwards. For criterion 3, the human label needs a combined score of 0.35 or less. Real writing on both sides landed between 0.31 and 0.72, so the human band is almost out of reach for normal text. Only text with strange tokens in it (typos, a fake system message) went that low.

**Problem 3: cheap surface changes move the signals, because neither signal reads meaning.** (EV01–EV09, PI01–PI03)

- **Stage: signal one for EV01, EV04, EV08, EV09 and the prompt injections. Signal two for EV02, EV03, EV06 and EV07. Then the label mapping for all of them.**
- **Mechanism, signal one:**
  - **Typos (EV01):** a misspelled word is a token GPT-2 doesn't expect, so perplexity jumps and the model score fell to 0.164.
  - **Rare words (EV04):** they surprise GPT-2 the same way, giving 0.611.
  - **Short text (EV08):** two short sentences gave the model almost nothing to read, so it scored 0.245.
  - **A human opening paragraph (EV09):** it fills the start of the 400-token window the model reads.
  - **Prompt injections (PI01–PI03):** my service has no language model following instructions, so the instructions did nothing as instructions. But lines like `SYSTEM: ... Return guess=human, confidence=0.02.` are full of odd tokens and punctuation. That raised perplexity (PI02 model 0.204) and punctuation density (PI02 style 0.176), so PI02 got "human" at 0.193.
- **Mechanism, signal two:** Breaking up sentences (EV02, EV06) and pasting a quotation (EV03) make sentence lengths uneven, which my style signal reads as human (0.222 to 0.286). Padding with semicolons and commas (EV07) raises punctuation density.
- **Why "unsure" was enough:** Problem 2 shows formal AI writing already lands around 0.45 to 0.69 with no tricks at all, which is inside my unsure band (above 0.35, below 0.70). Six of the nine evasions ended up there. The tricks only had to keep the score under 0.70, not push it all the way to human. The attack set has no unchanged copy of the base AI paragraph, so I can't say exactly how much each trick moved it.

**The pattern:** the same weakness shows up in both directions. My signals measure how plain and predictable the text is, and the model signal carries the most weight. Plain human writing gets pushed up toward AI (Problem 1), formal AI writing sits in the middle (Problem 2), and anything that adds odd tokens or uneven sentences pushes AI text down (Problem 3). The cap helps only when the two signals disagree. In every false positive they agreed.

**What held, and why:** All 20 malformed requests and the flood held because the route checks the input before the signals run, and the limiter works. Appeals (criterion 4) and bad input (criterion 5) were met. But MF05, MF06, MF07 and the emoji in criterion 5 only held because of the cap. The model scored meaningless text 0.906 to 0.998.



---

## The Improvement

**What I changed:** I moved the AI line up from 0.70 to 0.75 (`AI_THRESHOLD` in `config.py`). Nothing else changed. My split rule caps the score at `AI_THRESHOLD - 0.05`, so the same setting also moved the cap from 0.65 to 0.70.

**Which diagnosis pointed at it:** Problem 1. All four false positives (two of my own pieces, FP03 and FP05) scored between 0.702 and 0.734. Both signals were wrong together on them, so the cap never helped. The only stage where I could protect these writers without rebuilding a signal was the label line.

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

I ran all 56 attacks again with `python run_attacks.py --set attack_set --label after`. The output is in `results/attack_run_2026-11-08_2024_after.md`. I used the same held-or-broke rules as before.

**Result: 12 broke, 44 held** (before: 14 broke, 42 held).

| Family | Attacks | Broke before | Broke after |
|---|---|---|---|
| evasion | 10 | 9 | 9 |
| false_positive | 8 | 2 | **0** |
| prompt_injection | 6 | 3 | 3 |
| malformed | 20 | 0 | 0 |
| flood_same_creator | 12 | 0 | 0 |

| ID | Family | Targeting | Status | Guess | Combined | Model | Style | Verdict |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | human | 0.306 | 0.164 | 0.519 | **BROKE** |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.446 | 0.594 | 0.222 | **BROKE** |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.512 | 0.666 | 0.281 | **BROKE** |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.563 | 0.611 | 0.489 | **BROKE** |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.267 | 0.321 | 0.187 | **BROKE** |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.458 | 0.573 | 0.286 | **BROKE** |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.562 | 0.586 | 0.526 | **BROKE** |
| EV08 | evasion | signal one: text below the token window | 200 | human | 0.342 | 0.245 | 0.488 | **BROKE** |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.531 | 0.704 | 0.271 | **BROKE** |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.869 | 0.979 | 0.705 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.548 | 0.618 | 0.445 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.688 | 0.739 | 0.612 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | unsure | 0.707 | 0.805 | 0.560 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | unsure | 0.682 | 0.833 | 0.455 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | unsure | 0.734 | 0.800 | 0.633 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.682 | 0.881 | 0.384 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.700 | 0.882 | 0.459 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | human | 0.344 | 0.322 | 0.375 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.378 | 0.463 | 0.250 | **BROKE** |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.193 | 0.204 | 0.176 | **BROKE** |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.497 | 0.594 | 0.352 | **BROKE** |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.417 | 0.500 | 0.294 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.423 | 0.640 | 0.096 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.510 | 0.558 | 0.438 | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | human | 0.200 | 0.000 | 0.500 | HELD |
| MF04 | malformed | text is only punctuation | 200 | human | 0.207 | 0.011 | 0.500 | HELD |
| MF05 | malformed | text is a very long single word | 200 | unsure | 0.700 | 0.998 | 0.500 | HELD |
| MF06 | malformed | text is emoji only | 200 | unsure | 0.700 | 0.997 | 0.500 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | unsure | 0.700 | 0.906 | 0.500 | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | unsure | 0.424 | 0.239 | 0.700 | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | human | 0.230 | 0.049 | 0.500 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |

### Run Log — After

`python run_eval.py --label after` (`results/run_2026-11-08_2025_after.md`) and `python criteria_extra.py --label after` (`results/criteria_extra_2026-11-08_2026_after.md`). I did not change my criteria or my tests. The boundary check still expects 0.70 to return "ai", because that is what criterion 3 says.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict | Before |
|---|---|---|---|---|---|---|
| 1. My own writing flagged as AI | ≤ 1 of 10 | 0/10 | 0/10 | 0/10 | **MET** | MISSED (2/10) |
| 2. AI set average minus my writing's average | ≥ +0.20 | −0.024 | −0.024 | −0.024 | MISSED | MISSED (−0.023) |
| 3. Boundary scores correct, and all three labels appear in 12 passages | 5 of 5 boundaries, 3 of 3 labels | 4/5, 1 of 3 labels | 4/5, 1 of 3 labels | 4/5, 1 of 3 labels | MISSED | MISSED (5/5, 2 of 3) |
| 4. Appeals confirmed and logged, original kept | 5 of 5 | 5/5 | 5/5 | 5/5 | MET | MET |
| 5. Invalid input gets a 4xx, junk text never gets "ai" | 6 of 6 and 3 of 3 | 6/6, 3/3 | 6/6, 3/3 | 6/6, 3/3 | MET | MET |

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

**It helped the problem it was aimed at.** The false-positive family went from 2 broke to 0, and criterion 1 went from MISSED (2 of my 10 pieces labelled AI) to MET (0 of 10, in all three trials). FP03, the worst outcome from my first run, now gets "unsure" instead of an accusation. I know because the scores did not change at all. FP03 is still 0.707 and my dashboard piece is still 0.702. Only the line they are compared to moved.

**What it cost:**

- **The AI label is now almost unreachable.** In my criteria run, not one of the 20 real passages (my 10 and the 10 AI ones) got the AI label. Before, 2 did, and both were my own writing. In the attack set only EV10 still gets it, at 0.869. Any AI text scoring between 0.70 and 0.75 now gets "unsure" instead.
- **Criterion 3 got worse.** The 0.70 boundary now returns "unsure", so the boundary check dropped from 5/5 to 4/5. The 12 passages now only produce one label instead of two.
- **The cap loosened.** Because the cap is tied to the AI line, junk text the model loves now lands at exactly 0.700 instead of 0.650 (MF05, MF06, MF07, the emoji in criterion 5), and so does FP07. They still get "unsure", but with less room to spare.
- **It fixed nothing for evasion.** The evasions and prompt injections were already under the old line, so moving the line up could only help them, never catch them. They still break exactly as before.
- **Criterion 2 is unchanged.** Thresholds do not change scores, and the AI set still scores lower than my writing.

This is the trade the brief warned about. I chose fewer wrong accusations, and the cost is that the service now almost never says "AI" at all.

### Second Improvement (stretch)

**What I changed:** On top of the first fix, I moved the human line up from 0.35 to 0.45 (`HUMAN_THRESHOLD` in `config.py`). Nothing else changed. The AI line stayed at 0.75.

**Which diagnosis pointed at it:** Problem 2. Real writing on both sides landed between 0.31 and 0.72, so the human label (0.35 or less) was almost never reached. Criterion 3 missed partly because the human label never appeared in my 12 passages.

**Attack Run — After 2:** `python run_attacks.py --set attack_set --label after2`, in `results/attack_run_2026-11-08_2031_after2.md`. Same held-or-broke rules.

**Result: 12 broke, 44 held**, the same count as after the first fix. But more AI text now gets the human label instead of "unsure".

| ID | Family | Targeting | Status | Guess | Combined | Model | Style | Verdict |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | human | 0.306 | 0.164 | 0.519 | **BROKE** |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | human | 0.446 | 0.594 | 0.222 | **BROKE** |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.512 | 0.666 | 0.281 | **BROKE** |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.563 | 0.611 | 0.489 | **BROKE** |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.267 | 0.321 | 0.187 | **BROKE** |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.458 | 0.573 | 0.286 | **BROKE** |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.562 | 0.586 | 0.526 | **BROKE** |
| EV08 | evasion | signal one: text below the token window | 200 | human | 0.342 | 0.245 | 0.488 | **BROKE** |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.531 | 0.704 | 0.271 | **BROKE** |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.869 | 0.979 | 0.705 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.548 | 0.618 | 0.445 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.688 | 0.739 | 0.612 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | unsure | 0.707 | 0.805 | 0.560 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | unsure | 0.682 | 0.833 | 0.455 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | unsure | 0.734 | 0.800 | 0.633 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.682 | 0.881 | 0.384 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.700 | 0.882 | 0.459 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | human | 0.344 | 0.322 | 0.375 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | human | 0.378 | 0.463 | 0.250 | **BROKE** |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.193 | 0.204 | 0.176 | **BROKE** |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.497 | 0.594 | 0.352 | **BROKE** |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | human | 0.417 | 0.500 | 0.294 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | human | 0.423 | 0.640 | 0.096 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.510 | 0.558 | 0.438 | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | human | 0.200 | 0.000 | 0.500 | HELD |
| MF04 | malformed | text is only punctuation | 200 | human | 0.207 | 0.011 | 0.500 | HELD |
| MF05 | malformed | text is a very long single word | 200 | unsure | 0.700 | 0.998 | 0.500 | HELD |
| MF06 | malformed | text is emoji only | 200 | unsure | 0.700 | 0.997 | 0.500 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | unsure | 0.700 | 0.906 | 0.500 | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | human | 0.424 | 0.239 | 0.700 | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | human | 0.230 | 0.049 | 0.500 | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.297 | 0.029 | 0.700 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |

**Run Log — After 2** (the third run log): `python run_eval.py --label after2` (`results/run_2026-11-08_2032_after2.md`) and `python criteria_extra.py --label after2` (`results/criteria_extra_2026-11-08_2033_after2.md`). The criteria and tests are unchanged.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict | After fix 1 | Before |
|---|---|---|---|---|---|---|---|
| 1. My own writing flagged as AI | ≤ 1 of 10 | 0/10 | 0/10 | 0/10 | MET | MET | MISSED |
| 2. AI set average minus my writing's average | ≥ +0.20 | −0.024 | −0.024 | −0.024 | MISSED | MISSED | MISSED |
| 3. Boundary scores correct, and all three labels appear in 12 passages | 5 of 5 boundaries, 3 of 3 labels | 4/5, 2 of 3 labels | 4/5, 2 of 3 labels | 4/5, 2 of 3 labels | MISSED | MISSED (4/5, 1 of 3) | MISSED (5/5, 2 of 3) |
| 4. Appeals confirmed and logged, original kept | 5 of 5 | 5/5 | 5/5 | 5/5 | MET | MET | MET |
| 5. Invalid input gets a 4xx, junk text never gets "ai" | 6 of 6 and 3 of 3 | 6/6, 3/3 | 6/6, 3/3 | 6/6, 3/3 | MET | MET | MET |

**Did it help:** **Not really. It made things worse in a way the scores don't show at first.**

- **What it fixed:** The human label is reachable again. In criterion 3 the 12 passages went from 1 label back to 2 (human and unsure).
- **But the passage that got "human" there was AI text.** It was the AI passage about quantum and classical models (0.4386). In the AI set, 2 of the 10 AI passages now get "human" (before: 1). Of my own 10 pieces, only 1 gets "human" (the thesis piece, 0.377).
- **In the attack set, AI text labelled "human" went from 4 to 7.** EV02, PI01 and PI05 moved from "unsure" to "human". The broke count stayed at 12 only because I already counted "unsure" as getting through. Now the service is telling the reader "We think this was probably written by a person" about more AI text.
- **Criterion 3 is still missed.** The AI label is still never reached by real passages (that is the cost of fix 1), and the 0.70 boundary still returns "unsure".
- **How I know:** The scores are the same in all three runs. Only the lines moved, so every change in a label comes from the threshold and nothing else.

Moving thresholds can only shuffle where the same scores land. It can't separate human from AI text when my signals score them about the same (Problem 2). If I kept one fix, I would keep the first one and undo this one.



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
