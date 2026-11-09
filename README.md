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
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



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
