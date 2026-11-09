# Criteria extra checks — after

- Produced by: `criteria_extra.py::main`
- 3 trials · 2026-11-08 20:26

## criterion 3: boundary scores

Passed: run 1: 4/5, run 2: 4/5, run 3: 4/5

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
    "guess": "unsure",
    "ok": false
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
    "guess": "unsure",
    "ok": false
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
    "guess": "unsure",
    "ok": false
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
    "content_id": "211665be-cc41-4d55-98ca-d2a305513f7b",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "211665be-cc41-4d55-98ca-d2a305513f7b",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "211665be-cc41-4d55-98ca-d2a305513f7b",
      "creator_id": "eval_c4_t1_1",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:19+00:00"
    },
    "ok": true
  },
  {
    "content_id": "1b7643d7-1f13-4888-b629-e14b0184b37d",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "1b7643d7-1f13-4888-b629-e14b0184b37d",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "1b7643d7-1f13-4888-b629-e14b0184b37d",
      "creator_id": "eval_c4_t1_2",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:19+00:00"
    },
    "ok": true
  },
  {
    "content_id": "16765ff3-99b3-4bea-bc4b-c365e7cd2d36",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "16765ff3-99b3-4bea-bc4b-c365e7cd2d36",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "16765ff3-99b3-4bea-bc4b-c365e7cd2d36",
      "creator_id": "eval_c4_t1_3",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:19+00:00"
    },
    "ok": true
  },
  {
    "content_id": "8d94562e-b0f5-4e4a-bad2-6736dd58b475",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "8d94562e-b0f5-4e4a-bad2-6736dd58b475",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "8d94562e-b0f5-4e4a-bad2-6736dd58b475",
      "creator_id": "eval_c4_t1_4",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:20+00:00"
    },
    "ok": true
  },
  {
    "content_id": "8c7ff8dc-5f43-4df1-8128-d0b5061415c0",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "8c7ff8dc-5f43-4df1-8128-d0b5061415c0",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "8c7ff8dc-5f43-4df1-8128-d0b5061415c0",
      "creator_id": "eval_c4_t1_5",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:20+00:00"
    },
    "ok": true
  }
]
```

**Trial 2**

```json
[
  {
    "content_id": "55ddf209-7799-423d-b7c6-d326412a1950",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "55ddf209-7799-423d-b7c6-d326412a1950",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "55ddf209-7799-423d-b7c6-d326412a1950",
      "creator_id": "eval_c4_t2_1",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:20+00:00"
    },
    "ok": true
  },
  {
    "content_id": "e0cff164-52eb-4bcd-b28a-2bd9d9c3c151",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "e0cff164-52eb-4bcd-b28a-2bd9d9c3c151",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "e0cff164-52eb-4bcd-b28a-2bd9d9c3c151",
      "creator_id": "eval_c4_t2_2",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:20+00:00"
    },
    "ok": true
  },
  {
    "content_id": "17d801fe-610b-4756-a91a-bdfe4758a131",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "17d801fe-610b-4756-a91a-bdfe4758a131",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "17d801fe-610b-4756-a91a-bdfe4758a131",
      "creator_id": "eval_c4_t2_3",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:20+00:00"
    },
    "ok": true
  },
  {
    "content_id": "d8e59a1c-73fb-4510-a978-31c20d5197f4",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "d8e59a1c-73fb-4510-a978-31c20d5197f4",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "d8e59a1c-73fb-4510-a978-31c20d5197f4",
      "creator_id": "eval_c4_t2_4",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:20+00:00"
    },
    "ok": true
  },
  {
    "content_id": "903d23ba-3223-457c-9e8d-213d4eed924f",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "903d23ba-3223-457c-9e8d-213d4eed924f",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "903d23ba-3223-457c-9e8d-213d4eed924f",
      "creator_id": "eval_c4_t2_5",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:21+00:00"
    },
    "ok": true
  }
]
```

**Trial 3**

```json
[
  {
    "content_id": "a2554416-6f92-47c4-a17e-c761084af1dc",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "a2554416-6f92-47c4-a17e-c761084af1dc",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "a2554416-6f92-47c4-a17e-c761084af1dc",
      "creator_id": "eval_c4_t3_1",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:21+00:00"
    },
    "ok": true
  },
  {
    "content_id": "51bf52c5-a10d-4ee9-b302-b089cc7876b6",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "51bf52c5-a10d-4ee9-b302-b089cc7876b6",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "51bf52c5-a10d-4ee9-b302-b089cc7876b6",
      "creator_id": "eval_c4_t3_2",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:21+00:00"
    },
    "ok": true
  },
  {
    "content_id": "62ba008c-6803-4703-b95b-2be05ebaa288",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "62ba008c-6803-4703-b95b-2be05ebaa288",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "62ba008c-6803-4703-b95b-2be05ebaa288",
      "creator_id": "eval_c4_t3_3",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:21+00:00"
    },
    "ok": true
  },
  {
    "content_id": "45769576-1b75-4587-a5c9-06a96d080c02",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "45769576-1b75-4587-a5c9-06a96d080c02",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "45769576-1b75-4587-a5c9-06a96d080c02",
      "creator_id": "eval_c4_t3_4",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:21+00:00"
    },
    "ok": true
  },
  {
    "content_id": "fa0f88c7-8ff7-4339-b85e-d06a429b5129",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "fa0f88c7-8ff7-4339-b85e-d06a429b5129",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "fa0f88c7-8ff7-4339-b85e-d06a429b5129",
      "creator_id": "eval_c4_t3_5",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:26:21+00:00"
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
