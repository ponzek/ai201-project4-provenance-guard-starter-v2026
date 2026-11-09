# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 20:31
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `73760a84-93f7-4960-9591-44bdcafdbac5` | human | 0.306 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `54bdeaae-24ca-4a97-a30f-bc40972d5008` | human | 0.446 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `5b8a89b6-1b75-46b1-8c08-9af4b554bf30` | unsure | 0.512 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `076da43e-d09b-4a84-b8b6-e2a34c125a5a` | unsure | 0.563 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `2f6f0ef3-b876-4b62-9a9d-5763130321f7` | human | 0.267 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `bb127d48-87e3-4b1f-9a64-68cf91050acc` | unsure | 0.458 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `10c41f39-7b3b-4ae1-92aa-9babd23a6258` | unsure | 0.562 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `4829ac16-8e3f-42d5-b71a-17a2fe10d5d1` | human | 0.342 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `b4f320a7-ab52-464e-a766-86791e81741b` | unsure | 0.531 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `9b9a1f0a-1fb8-493d-b8dd-bdca881ff449` | ai | 0.869 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `52936333-5eb1-42ba-93ac-841c94622398` | unsure | 0.548 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `1deca723-b79b-43f5-8be5-609a41717dea` | unsure | 0.688 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `22079e1f-0894-4728-afa4-df21737d247f` | unsure | 0.707 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `16f8b453-9e8b-4520-bd62-bee3fa1d781b` | unsure | 0.682 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `5161b9bf-2a6c-492f-b61e-96477ea8dd6b` | unsure | 0.734 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `cdc6db75-2a3c-4093-b404-afcd7e1fdf8c` | unsure | 0.682 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `7fdad754-da45-41d5-b46f-a104a075d841` | unsure | 0.700 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `75d80d1d-7767-4f55-995f-491ca31e3c80` | human | 0.344 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `335a3b4f-9cdc-42ad-8119-3db50eb09be6` | human | 0.378 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `4e4f17b0-5fbe-4121-86d4-34d587b2eb38` | human | 0.193 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `2651a0ce-5374-4482-8dfa-60620423609c` | unsure | 0.497 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `9ab73699-dd2b-452c-a8bc-388d97d89f44` | human | 0.417 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `f1100ea4-1ec7-41e8-93d4-e1a334847b85` | human | 0.423 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `328b0b46-1f97-4b58-885d-63595a2759d2` | unsure | 0.510 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `3b2c9360-abdb-4d20-87cf-fe2b539fc9e8` | human | 0.200 |  |
| MF04 | malformed | text is only punctuation | 200 | `bdc067c5-c1fc-45b7-a162-79005e1e7e9c` | human | 0.207 |  |
| MF05 | malformed | text is a very long single word | 200 | `c3e03f37-2caf-4a54-a3ec-a323247509f1` | unsure | 0.700 |  |
| MF06 | malformed | text is emoji only | 200 | `8cf01520-bf79-4f01-95aa-870c0ee5f322` | unsure | 0.700 |  |
| MF07 | malformed | text is right-to-left script | 200 | `928d8ef5-badc-419b-9603-2d3be164d6d8` | unsure | 0.700 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `9dbee17c-13d0-4e80-8547-1af28dd6d7eb` | human | 0.424 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `e2a5074e-d61f-4ec7-a1b8-af7dc8138009` | human | 0.230 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5a0efc3a-ae4e-4e1c-a5d3-37fea35fbe31` | human | 0.297 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0931548d-4f75-48a3-a171-68a1957feafb` | human | 0.297 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7c2c3eb5-58da-4764-8965-11671428f560` | human | 0.297 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8002c9c2-e5e1-495c-be1d-a8918862d990` | human | 0.297 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6eeefc1e-cb20-472f-a6ed-a7a86254442d` | human | 0.297 |  |
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
  "content_id": "73760a84-93f7-4960-9591-44bdcafdbac5",
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
  "content_id": "54bdeaae-24ca-4a97-a30f-bc40972d5008",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.4455,
  "model_score": 0.5943,
  "style_score": 0.2222,
  "label": "We think this was probably written by a person.",
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
  "content_id": "5b8a89b6-1b75-46b1-8c08-9af4b554bf30",
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
  "content_id": "076da43e-d09b-4a84-b8b6-e2a34c125a5a",
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
  "content_id": "2f6f0ef3-b876-4b62-9a9d-5763130321f7",
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
  "content_id": "bb127d48-87e3-4b1f-9a64-68cf91050acc",
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
  "content_id": "10c41f39-7b3b-4ae1-92aa-9babd23a6258",
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
  "content_id": "4829ac16-8e3f-42d5-b71a-17a2fe10d5d1",
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
  "content_id": "b4f320a7-ab52-464e-a766-86791e81741b",
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
  "content_id": "9b9a1f0a-1fb8-493d-b8dd-bdca881ff449",
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
  "content_id": "52936333-5eb1-42ba-93ac-841c94622398",
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
  "content_id": "1deca723-b79b-43f5-8be5-609a41717dea",
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
  "content_id": "22079e1f-0894-4728-afa4-df21737d247f",
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
  "content_id": "16f8b453-9e8b-4520-bd62-bee3fa1d781b",
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
  "content_id": "5161b9bf-2a6c-492f-b61e-96477ea8dd6b",
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
  "content_id": "cdc6db75-2a3c-4093-b404-afcd7e1fdf8c",
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
  "content_id": "7fdad754-da45-41d5-b46f-a104a075d841",
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
  "content_id": "75d80d1d-7767-4f55-995f-491ca31e3c80",
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
  "content_id": "335a3b4f-9cdc-42ad-8119-3db50eb09be6",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3775,
  "model_score": 0.4625,
  "style_score": 0.25,
  "label": "We think this was probably written by a person.",
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
  "content_id": "4e4f17b0-5fbe-4121-86d4-34d587b2eb38",
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
  "content_id": "2651a0ce-5374-4482-8dfa-60620423609c",
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
  "content_id": "9ab73699-dd2b-452c-a8bc-388d97d89f44",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.4175,
  "model_score": 0.4998,
  "style_score": 0.2941,
  "label": "We think this was probably written by a person.",
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
  "content_id": "f1100ea4-1ec7-41e8-93d4-e1a334847b85",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.4226,
  "model_score": 0.6401,
  "style_score": 0.0964,
  "label": "We think this was probably written by a person.",
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
  "content_id": "328b0b46-1f97-4b58-885d-63595a2759d2",
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
  "content_id": "3b2c9360-abdb-4d20-87cf-fe2b539fc9e8",
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
  "content_id": "bdc067c5-c1fc-45b7-a162-79005e1e7e9c",
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
  "content_id": "c3e03f37-2caf-4a54-a3ec-a323247509f1",
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
  "content_id": "8cf01520-bf79-4f01-95aa-870c0ee5f322",
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
  "content_id": "928d8ef5-badc-419b-9603-2d3be164d6d8",
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
  "content_id": "9dbee17c-13d0-4e80-8547-1af28dd6d7eb",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.4237,
  "model_score": 0.2395,
  "style_score": 0.7,
  "label": "We think this was probably written by a person.",
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
  "content_id": "e2a5074e-d61f-4ec7-a1b8-af7dc8138009",
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
  "content_id": "5a0efc3a-ae4e-4e1c-a5d3-37fea35fbe31",
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
  "content_id": "0931548d-4f75-48a3-a171-68a1957feafb",
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
  "content_id": "7c2c3eb5-58da-4764-8965-11671428f560",
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
  "content_id": "8002c9c2-e5e1-495c-be1d-a8918862d990",
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
  "content_id": "6eeefc1e-cb20-472f-a6ed-a7a86254442d",
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
