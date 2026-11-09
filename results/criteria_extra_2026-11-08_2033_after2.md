# Criteria extra checks — after2

- Produced by: `criteria_extra.py::main`
- 3 trials · 2026-11-08 20:33

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
    "content_id": "4669a0f8-0a90-413d-a519-61b4faeca09d",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "4669a0f8-0a90-413d-a519-61b4faeca09d",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "4669a0f8-0a90-413d-a519-61b4faeca09d",
      "creator_id": "eval_c4_t1_1",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:07+00:00"
    },
    "ok": true
  },
  {
    "content_id": "95f1fba9-dd42-4be3-9661-c0db764bc62e",
    "submit_status": 200,
    "guess": "human",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "95f1fba9-dd42-4be3-9661-c0db764bc62e",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "95f1fba9-dd42-4be3-9661-c0db764bc62e",
      "creator_id": "eval_c4_t1_2",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:07+00:00"
    },
    "ok": true
  },
  {
    "content_id": "c5e79cf2-a6a6-4dab-a1fd-e901343681b1",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "c5e79cf2-a6a6-4dab-a1fd-e901343681b1",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "c5e79cf2-a6a6-4dab-a1fd-e901343681b1",
      "creator_id": "eval_c4_t1_3",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:07+00:00"
    },
    "ok": true
  },
  {
    "content_id": "cd5f4de1-a88b-42c6-83ed-84b09cc22e88",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "cd5f4de1-a88b-42c6-83ed-84b09cc22e88",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "cd5f4de1-a88b-42c6-83ed-84b09cc22e88",
      "creator_id": "eval_c4_t1_4",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:07+00:00"
    },
    "ok": true
  },
  {
    "content_id": "96cd0ccb-9703-4172-8d33-1b7f03340d91",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "96cd0ccb-9703-4172-8d33-1b7f03340d91",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "96cd0ccb-9703-4172-8d33-1b7f03340d91",
      "creator_id": "eval_c4_t1_5",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:07+00:00"
    },
    "ok": true
  }
]
```

**Trial 2**

```json
[
  {
    "content_id": "7fc29c8f-b965-4803-99b5-0740fd3ee52b",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "7fc29c8f-b965-4803-99b5-0740fd3ee52b",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "7fc29c8f-b965-4803-99b5-0740fd3ee52b",
      "creator_id": "eval_c4_t2_1",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:07+00:00"
    },
    "ok": true
  },
  {
    "content_id": "a0189ac8-ae87-4f67-a834-221a53073a2a",
    "submit_status": 200,
    "guess": "human",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "a0189ac8-ae87-4f67-a834-221a53073a2a",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "a0189ac8-ae87-4f67-a834-221a53073a2a",
      "creator_id": "eval_c4_t2_2",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:08+00:00"
    },
    "ok": true
  },
  {
    "content_id": "5a3e8c48-2e9b-43bc-877e-2a561984df5b",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "5a3e8c48-2e9b-43bc-877e-2a561984df5b",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "5a3e8c48-2e9b-43bc-877e-2a561984df5b",
      "creator_id": "eval_c4_t2_3",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:08+00:00"
    },
    "ok": true
  },
  {
    "content_id": "1d017236-d595-445f-8d71-176a6fc44219",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "1d017236-d595-445f-8d71-176a6fc44219",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "1d017236-d595-445f-8d71-176a6fc44219",
      "creator_id": "eval_c4_t2_4",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:08+00:00"
    },
    "ok": true
  },
  {
    "content_id": "0b2ece91-e2b1-4786-98b8-25c8b9c01b89",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "0b2ece91-e2b1-4786-98b8-25c8b9c01b89",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "0b2ece91-e2b1-4786-98b8-25c8b9c01b89",
      "creator_id": "eval_c4_t2_5",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:08+00:00"
    },
    "ok": true
  }
]
```

**Trial 3**

```json
[
  {
    "content_id": "50ca2137-8592-4eee-8dd7-e38236e4a255",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "50ca2137-8592-4eee-8dd7-e38236e4a255",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "50ca2137-8592-4eee-8dd7-e38236e4a255",
      "creator_id": "eval_c4_t3_1",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:08+00:00"
    },
    "ok": true
  },
  {
    "content_id": "ad8a02b2-6b26-4c38-9d1a-b6e8060a02a8",
    "submit_status": 200,
    "guess": "human",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "ad8a02b2-6b26-4c38-9d1a-b6e8060a02a8",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "ad8a02b2-6b26-4c38-9d1a-b6e8060a02a8",
      "creator_id": "eval_c4_t3_2",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:08+00:00"
    },
    "ok": true
  },
  {
    "content_id": "5e043c2f-e42f-4e3d-9d7f-54ba53e9bfce",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "5e043c2f-e42f-4e3d-9d7f-54ba53e9bfce",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "5e043c2f-e42f-4e3d-9d7f-54ba53e9bfce",
      "creator_id": "eval_c4_t3_3",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:08+00:00"
    },
    "ok": true
  },
  {
    "content_id": "550eb012-18ae-4c62-bc54-cd52ca35d1b1",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "550eb012-18ae-4c62-bc54-cd52ca35d1b1",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "550eb012-18ae-4c62-bc54-cd52ca35d1b1",
      "creator_id": "eval_c4_t3_4",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:09+00:00"
    },
    "ok": true
  },
  {
    "content_id": "09f850be-803b-4da6-ada5-899acec34a87",
    "submit_status": 200,
    "guess": "unsure",
    "appeal_status_code": 200,
    "appeal_response": {
      "content_id": "09f850be-803b-4da6-ada5-899acec34a87",
      "message": "Thanks. Your appeal was recorded and a person will review it.",
      "status": "under_review"
    },
    "log_original_decision_kept": true,
    "log_appeal_entry": {
      "content_id": "09f850be-803b-4da6-ada5-899acec34a87",
      "creator_id": "eval_c4_t3_5",
      "event": "appeal",
      "reasoning": "I wrote this myself. This is a test appeal for criterion 4.",
      "status": "under_review",
      "timestamp": "2026-11-09T01:33:09+00:00"
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
