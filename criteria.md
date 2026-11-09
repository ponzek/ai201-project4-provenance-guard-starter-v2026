# Acceptance criteria — Provenance Guard

These are my five targets for checking whether my service works. The code was started before I wrote these criteria.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---

## 1. Avoid wrongly accusing human writers

I will test 10 human-written passages. No more than 1 out of 10
should receive the high-confidence AI label in each of three trials.

**Why this target:** I do not want someone who wrote their own work
to be wrongly accused of using AI. Simple writing can get a high AI
score, so I want my system to be careful.

> **Revised in unit 8:** The 10 passages are pieces I wrote myself without
> AI help: course reflections, project notes, two work emails and a personal
> reflection. They are copied word for word into `scenarios.py` as
> `MY_WRITING`, in the scenario named "my own writing", so anyone can run the
> same set with `python run_eval.py`. The target has not changed: no more than
> 1 of the 10 gets `guess` equal to "ai" in each of three trials.
>
> **Why revised:** My unit 7 feedback said a reader could not put together
> the test set, because I said "10 human-written passages" without saying
> whose writing or where it came from. I wrote this revision before running
> the test.

---

## 2. Check the difference between scores

I will test 10 human-written passages and 10 AI-generated passages
with similar topics and lengths. The average combined score (the
`confidence` field) for the AI set should be at
least 0.20 higher than the average for the human set in each of three trials.
I will record where the passages came from before testing.

**Why this target:** My two signals check predictability and writing
patterns. I want their combined scores to show a noticeable difference
between these groups, even though they cannot prove who wrote something.

---

## 3. Make all three labels possible

I will check that scores of 0 and 0.35 return human, 0.525 returns
unsure, and 0.70 and 1 return AI. I will also submit 12 passages and
check that each of the three labels appears at least once.

**Why this target:** My cutoffs are 0.35 and 0.70. I want to check
that both boundaries work and that the system can say unsure
instead of forcing every result into human or AI.

---

## 4. Make sure appeals are recorded

I will appeal five different submissions using their content IDs.
All five appeals should be confirmed and added to the log with
the status under_review and the writer's reasoning. The original
decisions should stay in the log.

**Why this target:** Both signals can make mistakes. Writers need
a way to challenge a result, and I want to keep a record of both
the original decision and their appeal.

---

## 5. Handle invalid and meaningless input safely

I will test six invalid inputs: missing text, empty text, text containing
only spaces, a number instead of text, text containing 20,001
characters, and a request body that is not valid JSON. All six should
return a 4xx response with a clear JSON error and no successful
submission.

I will also submit these three exact strings as `text`:

1. `!!!!!!!!`
2. `........`
3. `😀😀😀😀😀😀😀😀`

For each one, success means either a 4xx JSON error, or a successful
response whose `guess` is not `"ai"`. If any of the three returns
`guess` equal to `"ai"`, I miss this target.

**Why this target:** My service accepts up to 20,000 characters, and
missing or invalid text should get a clear error instead of a
misleading label. The second part is the harder test: my style signal
returns a neutral 0.5 when there are fewer than five words, and the
model signal may find repeated symbols very predictable, which could push
the combined score toward the AI label. Accusing someone because of
symbols with no meaning is the kind of wrong accusation I most want
to avoid.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
