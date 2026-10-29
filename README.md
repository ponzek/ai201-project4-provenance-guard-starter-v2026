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

`logs/audit.jsonl` has 10 lines. I kept all of them.

- **Lines 1 to 5:** earlier test entries (creator `me`, plus one rejected empty request). They were made before `criteria.md` was written. The file was missing these five lines before the run below, so they were restored by copying the original entries exactly.
- **Lines 6 to 8:** the other three submissions from this run (the thank-you note for the human label, the photograph paragraph for unsure, and the climate paragraph for the split case).
- **Lines 9 and 10:** the sample run above. Line 9 is the submission and line 10 is the appeal, both with `content_id` `61ecd9a8-ec91-4110-85f8-3a8da8a12cf2`.

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

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



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
