# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 20:24
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `9aea8cf0-ef7e-4c11-8f40-61471d3f76d5` | human | 0.306 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `26a3b422-d954-4bd9-a38a-1a44e5080e1f` | unsure | 0.446 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `0ca0fabd-77b6-448b-8561-3e4cd631a325` | unsure | 0.512 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `0825ec35-d4df-4794-a119-0fca91d71242` | unsure | 0.563 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `82ec16a9-af36-459d-8dc3-518ee3ed4208` | human | 0.267 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `24b3c052-897d-4fa8-a068-2c134369aa07` | unsure | 0.458 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `3c8cef33-9c53-433d-8c75-006ed18e618d` | unsure | 0.562 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `de1abd04-0ea5-4e20-a865-3751d1fa89d4` | human | 0.342 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `4581fc69-388e-4533-a419-6c2d83153465` | unsure | 0.531 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `2f2e211f-d229-4ed9-b992-0dc232cb9209` | ai | 0.869 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `4c5d1269-7b42-495e-9672-5bced46b3592` | unsure | 0.548 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `a5b78278-3379-41a8-96d8-6364b170bdbc` | unsure | 0.688 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `49f8294d-b3f8-4d56-8bd5-d7c1b3b7da23` | unsure | 0.707 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `d34b2d23-4896-44fe-a0ab-ae42ce39a90e` | unsure | 0.682 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `94cd040d-b2aa-4442-bab1-be3ba6c3563e` | unsure | 0.734 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `bab477a8-49b0-4ae6-b99f-c1cf01686e78` | unsure | 0.682 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `9d8e1c9c-2acf-4590-9e69-0542a1da1feb` | unsure | 0.700 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `40242fd4-93b8-441e-8d7e-639863f3bda8` | human | 0.344 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `e47b9cbc-75ad-4d36-a92a-ad4fa7cc2daa` | unsure | 0.378 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `097860ef-d28e-420b-b6e7-9d6376d554c6` | human | 0.193 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `b971df10-c3c9-448a-b5ae-25e7d6e0d6bb` | unsure | 0.497 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `e52cd01b-71ca-403f-9d29-43c5745dbb5d` | unsure | 0.417 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `848283bb-7eaa-4525-9554-426d422a4eab` | unsure | 0.423 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `d0a0686a-5319-4b5e-b475-a1b2cd5eeb53` | unsure | 0.510 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `24566b09-22d3-4276-836b-b3cef747562b` | human | 0.200 |  |
| MF04 | malformed | text is only punctuation | 200 | `97fb7488-7efb-47e9-a7df-0488bb2cae4d` | human | 0.207 |  |
| MF05 | malformed | text is a very long single word | 200 | `b3c7abf2-e4b4-4bcc-9f7a-0df844acead2` | unsure | 0.700 |  |
| MF06 | malformed | text is emoji only | 200 | `99b038d5-98cf-4143-8329-43fe90f47d14` | unsure | 0.700 |  |
| MF07 | malformed | text is right-to-left script | 200 | `43fdf776-da71-45c9-bca7-e59c86dc6563` | unsure | 0.700 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `ba5b7d64-0e94-4026-90b5-18c2eeee3fa0` | unsure | 0.424 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `33556b32-730e-4e5e-9ab1-26065435e1dc` | human | 0.230 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7102e91c-c6f2-4712-8c43-87c0a46a1a4d` | human | 0.297 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `853e9e9c-d782-4610-86cb-681c15b1fc6e` | human | 0.297 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e7026201-4a37-4f18-8b99-cc5e130bb4f0` | human | 0.297 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4142abc0-0d92-49a2-9da4-31d56de410ce` | human | 0.297 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `81281de8-40bf-4abb-a221-202f6f6b2d9f` | human | 0.297 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "9aea8cf0-ef7e-4c11-8f40-61471d3f76d5",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3056,
  "model_score": 0.1635,
  "style_score": 0.5187,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "26a3b422-d954-4bd9-a38a-1a44e5080e1f",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4455,
  "model_score": 0.5943,
  "style_score": 0.2222,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "0ca0fabd-77b6-448b-8561-3e4cd631a325",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5123,
  "model_score": 0.6662,
  "style_score": 0.2814,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "0825ec35-d4df-4794-a119-0fca91d71242",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5626,
  "model_score": 0.6114,
  "style_score": 0.4893,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "82ec16a9-af36-459d-8dc3-518ee3ed4208",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2674,
  "model_score": 0.3212,
  "style_score": 0.1867,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "24b3c052-897d-4fa8-a068-2c134369aa07",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4579,
  "model_score": 0.5727,
  "style_score": 0.2857,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "3c8cef33-9c53-433d-8c75-006ed18e618d",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5622,
  "model_score": 0.5862,
  "style_score": 0.5261,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "de1abd04-0ea5-4e20-a865-3751d1fa89d4",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3423,
  "model_score": 0.2452,
  "style_score": 0.4879,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "4581fc69-388e-4533-a419-6c2d83153465",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.531,
  "model_score": 0.7042,
  "style_score": 0.2713,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "2f2e211f-d229-4ed9-b992-0dc232cb9209",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8694,
  "model_score": 0.9792,
  "style_score": 0.7046,
  "label": "Our tools think this was probably written with the help of AI. They can be wrong. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "4c5d1269-7b42-495e-9672-5bced46b3592",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5483,
  "model_score": 0.6175,
  "style_score": 0.4445,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "a5b78278-3379-41a8-96d8-6364b170bdbc",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6878,
  "model_score": 0.7387,
  "style_score": 0.6115,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "49f8294d-b3f8-4d56-8bd5-d7c1b3b7da23",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7071,
  "model_score": 0.8051,
  "style_score": 0.5601,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "d34b2d23-4896-44fe-a0ab-ae42ce39a90e",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6818,
  "model_score": 0.8329,
  "style_score": 0.4552,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "94cd040d-b2aa-4442-bab1-be3ba6c3563e",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7336,
  "model_score": 0.8005,
  "style_score": 0.6333,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "bab477a8-49b0-4ae6-b99f-c1cf01686e78",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6824,
  "model_score": 0.8814,
  "style_score": 0.384,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "9d8e1c9c-2acf-4590-9e69-0542a1da1feb",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7,
  "model_score": 0.8816,
  "style_score": 0.4589,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "40242fd4-93b8-441e-8d7e-639863f3bda8",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3435,
  "model_score": 0.3223,
  "style_score": 0.3752,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "e47b9cbc-75ad-4d36-a92a-ad4fa7cc2daa",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3775,
  "model_score": 0.4625,
  "style_score": 0.25,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "097860ef-d28e-420b-b6e7-9d6376d554c6",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.193,
  "model_score": 0.2044,
  "style_score": 0.1759,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "b971df10-c3c9-448a-b5ae-25e7d6e0d6bb",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4973,
  "model_score": 0.5943,
  "style_score": 0.3518,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "e52cd01b-71ca-403f-9d29-43c5745dbb5d",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4175,
  "model_score": 0.4998,
  "style_score": 0.2941,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "848283bb-7eaa-4525-9554-426d422a4eab",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4226,
  "model_score": 0.6401,
  "style_score": 0.0964,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "d0a0686a-5319-4b5e-b475-a1b2cd5eeb53",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5103,
  "model_score": 0.5583,
  "style_score": 0.4384,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "24566b09-22d3-4276-836b-b3cef747562b",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.2,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "97fb7488-7efb-47e9-a7df-0488bb2cae4d",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2067,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "b3c7abf2-e4b4-4bcc-9f7a-0df844acead2",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.7,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "99b038d5-98cf-4143-8329-43fe90f47d14",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.7,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "43fdf776-da71-45c9-bca7-e59c86dc6563",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.7,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "ba5b7d64-0e94-4026-90b5-18c2eeee3fa0",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.4237,
  "model_score": 0.2395,
  "style_score": 0.7,
  "label": "We can't tell. This text has some features of both human and AI writing, and plenty of people write this way. Nothing is being held against you.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "33556b32-730e-4e5e-9ab1-26065435e1dc",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.2295,
  "model_score": 0.0492,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "7102e91c-c6f2-4712-8c43-87c0a46a1a4d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2972,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "853e9e9c-d782-4610-86cb-681c15b1fc6e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2972,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "e7026201-4a37-4f18-8b99-cc5e130bb4f0",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2972,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "4142abc0-0d92-49a2-9da4-31d56de410ce",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2972,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "81281de8-40bf-4abb-a221-202f6f6b2d9f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2972,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
