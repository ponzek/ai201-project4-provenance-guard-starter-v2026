# Criteria extra checks — before

- Produced by: `criteria_extra.py::main`
- 3 trials · 2026-11-08 20:02

## criterion 3: boundary scores

Passed: run 1: 5/5, run 2: 5/5, run 3: 5/5

**Trial 1**

```json
[
  {
    "score": 0.0,
    "expected": "human",
    "guess": "human",
    "ok": true
  },
  {
    "score": 0.35,
    "expected": "human",
    "guess": "human",
    "ok": true
  },
  {
    "score": 0.525,
    "expected": "unsure",
    "guess": "unsure",
    "ok": true
  },
  {
    "score": 0.7,
    "expected": "ai",
    "guess": "ai",
    "ok": true
  },
  {
    "score": 1.0,
    "expected": "ai",
    "guess": "ai",
    "ok": true
  }
]
```

**Trial 2**

```json
[
  {
    "score": 0.0,
    "expected": "human",
    "guess": "human",
    "ok": true
  },
  {
    "score": 0.35,
    "expected": "human",
    "guess": "human",
    "ok": true
  },
  {
    "score": 0.525,
    "expected": "unsure",
    "guess": "unsure",
    "ok": true
  },
  {
    "score": 0.7,
    "expected": "ai",
    "guess": "ai",
    "ok": true
  },
  {
    "score": 1.0,
    "expected": "ai",
    "guess": "ai",
    "ok": true
  }
]
```

**Trial 3**

```json
[
  {
    "score": 0.0,
    "expected": "human",
    "guess": "human",
    "ok": true
  },
  {
    "score": 0.35,
    "expected": "human",
    "guess": "human",
    "ok": true
  },
  {
    "score": 0.525,
    "expected": "unsure",
    "guess": "unsure",
    "ok": true
  },
  {
    "score": 0.7,
    "expected": "ai",
    "guess": "ai",
    "ok": true
  },
  {
    "score": 1.0,
    "expected": "ai",
    "guess": "ai",
    "ok": true
  }
]
```

## criterion 4: appeals

Passed: run 1: 5/5, run 2: 5/5, run 3: 5/5

**Trial 1**

```json
[
  {
    "content_id": "5c39d24c-9046-482c-be51-71b06aa085ee",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "5c39d24c-9046-482c-be51-71b06aa085ee",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "5c39d24c-9046-482c-be51-71b06aa085ee",
      "creator_id": "eval_c4_t1_1",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:35+00:00"
    },
    "ok": true
  },
  {
    "content_id": "7293ecce-8d99-4ffc-84a9-5b423c364d0d",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "7293ecce-8d99-4ffc-84a9-5b423c364d0d",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "7293ecce-8d99-4ffc-84a9-5b423c364d0d",
      "creator_id": "eval_c4_t1_2",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:35+00:00"
    },
    "ok": true
  },
  {
    "content_id": "47755eab-3dd2-4d53-bcd4-11e7615917c6",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "47755eab-3dd2-4d53-bcd4-11e7615917c6",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "47755eab-3dd2-4d53-bcd4-11e7615917c6",
      "creator_id": "eval_c4_t1_3",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:35+00:00"
    },
    "ok": true
  },
  {
    "content_id": "2f6d50ff-3006-457c-939d-fa6e18f37159",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "2f6d50ff-3006-457c-939d-fa6e18f37159",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "2f6d50ff-3006-457c-939d-fa6e18f37159",
      "creator_id": "eval_c4_t1_4",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:36+00:00"
    },
    "ok": true
  },
  {
    "content_id": "a63e3d38-192e-4a11-9c4e-794048fa11f2",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "a63e3d38-192e-4a11-9c4e-794048fa11f2",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "a63e3d38-192e-4a11-9c4e-794048fa11f2",
      "creator_id": "eval_c4_t1_5",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:36+00:00"
    },
    "ok": true
  }
]
```

**Trial 2**

```json
[
  {
    "content_id": "b797250a-2b88-41f3-abdf-fc7c06e928c1",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "b797250a-2b88-41f3-abdf-fc7c06e928c1",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "b797250a-2b88-41f3-abdf-fc7c06e928c1",
      "creator_id": "eval_c4_t2_1",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:36+00:00"
    },
    "ok": true
  },
  {
    "content_id": "1a3b630c-6457-4cc4-b336-235c99640c16",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "1a3b630c-6457-4cc4-b336-235c99640c16",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "1a3b630c-6457-4cc4-b336-235c99640c16",
      "creator_id": "eval_c4_t2_2",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:36+00:00"
    },
    "ok": true
  },
  {
    "content_id": "6f0b3927-b1f6-497b-adab-05df65aa9b93",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "6f0b3927-b1f6-497b-adab-05df65aa9b93",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "6f0b3927-b1f6-497b-adab-05df65aa9b93",
      "creator_id": "eval_c4_t2_3",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:36+00:00"
    },
    "ok": true
  },
  {
    "content_id": "e4ad46a7-f0ff-40c6-8f8b-324b2a9f2713",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "e4ad46a7-f0ff-40c6-8f8b-324b2a9f2713",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "e4ad46a7-f0ff-40c6-8f8b-324b2a9f2713",
      "creator_id": "eval_c4_t2_4",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:37+00:00"
    },
    "ok": true
  },
  {
    "content_id": "d884135f-690e-4a39-8251-86f6371413da",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "d884135f-690e-4a39-8251-86f6371413da",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "d884135f-690e-4a39-8251-86f6371413da",
      "creator_id": "eval_c4_t2_5",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:37+00:00"
    },
    "ok": true
  }
]
```

**Trial 3**

```json
[
  {
    "content_id": "3bed759a-fb8a-4161-9365-c9aef990cd21",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "3bed759a-fb8a-4161-9365-c9aef990cd21",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "3bed759a-fb8a-4161-9365-c9aef990cd21",
      "creator_id": "eval_c4_t3_1",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:37+00:00"
    },
    "ok": true
  },
  {
    "content_id": "af987601-c435-47a8-a428-5a3f3e705908",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "af987601-c435-47a8-a428-5a3f3e705908",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "af987601-c435-47a8-a428-5a3f3e705908",
      "creator_id": "eval_c4_t3_2",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:37+00:00"
    },
    "ok": true
  },
  {
    "content_id": "f309b608-2a20-4a58-8a95-286fb27e0a39",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "f309b608-2a20-4a58-8a95-286fb27e0a39",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "f309b608-2a20-4a58-8a95-286fb27e0a39",
      "creator_id": "eval_c4_t3_3",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:38+00:00"
    },
    "ok": true
  },
  {
    "content_id": "ca1468b3-9321-4e75-837e-69a78d3defeb",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "ca1468b3-9321-4e75-837e-69a78d3defeb",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "ca1468b3-9321-4e75-837e-69a78d3defeb",
      "creator_id": "eval_c4_t3_4",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:38+00:00"
    },
    "ok": true
  },
  {
    "content_id": "274ed73e-b88e-444b-bfb9-4e1bb1efa289",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "274ed73e-b88e-444b-bfb9-4e1bb1efa289",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "274ed73e-b88e-444b-bfb9-4e1bb1efa289",
      "creator_id": "eval_c4_t3_5",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:02:38+00:00"
    },
    "ok": true
  }
]
```

## criterion 5: body that is not valid JSON

Passed: run 1: 1/1, run 2: 1/1, run 3: 1/1

**Trial 1**

```json
[
  {
    "sent": "{\"text\": \"not closed",
    "status": 400,
    "response": {
      "error": "invalid_text",
      "message": "Send JSON with a non-empty 'text' string."
    },
    "ok": true
  }
]
```

**Trial 2**

```json
[
  {
    "sent": "{\"text\": \"not closed",
    "status": 400,
    "response": {
      "error": "invalid_text",
      "message": "Send JSON with a non-empty 'text' string."
    },
    "ok": true
  }
]
```

**Trial 3**

```json
[
  {
    "sent": "{\"text\": \"not closed",
    "status": 400,
    "response": {
      "error": "invalid_text",
      "message": "Send JSON with a non-empty 'text' string."
    },
    "ok": true
  }
]
```
