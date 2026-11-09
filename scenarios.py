"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

# ── Where the test texts came from ───────────────────────────────────────────
#
# MY_WRITING: ten pieces I wrote myself, without AI help — course reflections,
# project notes, two work emails and a personal reflection. Copied word for
# word. This is the set criterion 1 names.
#
# AI_WRITING: ten passages written by my AI coding assistant on purpose for
# criterion 2, one on the same topic as each of mine and about the same length,
# in the order of MY_WRITING. They are AI text, used as the AI side of the
# comparison.

MY_WRITING = [
    # 1. What I learned from the earthquake project
    "One new thing I learned is that seeing more earthquakes in the data doesn't "
    "necessarily mean more earthquakes happened. The technology we use to record "
    "them has improved over time. I liked seeing the readings in order because it "
    "made that easier to understand. I also wondered what the data would look like "
    "on a 3D map where you could see how deep each earthquake was.",
    # 2. Exploring an enrollment dashboard
    "I liked that the enrollment dashboard gave me a quick overview and still let "
    "me explore the data on my own. I could start with the big picture and then "
    "look closer at a group I was curious about. That's something I want to keep "
    "in mind for my own projects. I want people to know where to start, even if "
    "they've never seen the data before.",
    # 3. Why I made Through the Barrier interactive
    "For my quantum tunneling project, I wanted people to be able to change "
    "something and see what happens. If you make the barrier wider, how does that "
    "affect the chance that a particle gets through? I wanted someone to be able "
    "to try it and see the graph change for themselves.",
    # 4. An inventory mistake I could actually picture
    "I chose the Command pattern because I could picture someone typing 500 "
    "instead of 50 while updating inventory. If that happens, they should be able "
    "to undo the change. It also helps to have a record of who made the update, "
    "especially if someone notices the mistake later and needs to figure out what "
    "happened.",
    # 5. How I worked through SQL triggers
    "When I was studying SQL triggers, I kept getting stuck on the keywords. It "
    "helped to read the trigger like a sentence. What happens first? What does the "
    "database do after that? Once I could answer those questions, it was easier to "
    "go back to the code and see what each part was doing.",
    # 6. Comparing quantum and classical models
    "In my handwritten digit project, the classical models did better than the "
    "quantum models. I wanted to show how big the difference was, so I put the "
    "results side by side. Seeing them together made me ask a better question. If "
    "the classical models already do this well, what would I need to see before I "
    "could say the quantum approach helped?",
    # 7. What I look for in my thesis results
    "For my thesis, I'm comparing four ways to generate a mammography report. One "
    "thing I keep coming back to is that a report can sound good and still get an "
    "important detail wrong. It could name the wrong breast or leave out the "
    "BI-RADS assessment. That's why I check those details separately, even when "
    "the generated report reads well.",
    # 8. Email: training video update
    "Hi everyone,\n\nI updated the slides to match the website and arranged them so "
    "the video can pause when it's time for a question. Once we confirm where the "
    "questions go, I can split the video at those points. I'm also seeing where I "
    "can cut a few seconds while keeping the explanations clear.",
    # 9. Email: quick question about the project budget
    "Hi everyone,\n\nThank you for the update! I just want to make sure I "
    "understand what's covered before we move forward. I understand there's a "
    "monthly amount for API access. Are the credits we'd use in the code editor "
    "covered too, or would those need a separate request?",
    # 10. Why finishing my degree matters to me
    "There were times when I doubted myself and wondered how I was going to finish "
    "everything. As a first-generation student, a lot of this was new to me, and "
    "sometimes I had to ask a lot of questions to figure out my next step. Now I'm "
    "working on my thesis and thinking about a doctorate. A few years ago, I don't "
    "know if I would've pictured myself saying that.",
]

AI_WRITING = [
    # 1. earthquake data
    "One key insight from analyzing earthquake data is that an increase in "
    "recorded earthquakes does not necessarily indicate an increase in seismic "
    "activity. Advances in monitoring technology have significantly improved our "
    "ability to detect smaller events. Viewing the readings chronologically helps "
    "clarify this trend. Additionally, a three-dimensional visualization could "
    "provide valuable insight into the depth of each event.",
    # 2. enrollment dashboard
    "The enrollment dashboard effectively balances a high-level overview with the "
    "ability to explore the data independently. Users can begin with the overall "
    "picture and then drill down into specific groups of interest. This approach "
    "is an important consideration for any data project, as it ensures that users "
    "have a clear starting point, even if they are unfamiliar with the data.",
    # 3. interactive quantum tunneling
    "The goal of this quantum tunneling project was to create an interactive "
    "experience that allows users to explore the concept directly. By adjusting "
    "the width of the barrier, users can observe how it affects the probability of "
    "a particle passing through. This hands-on approach helps make an abstract "
    "concept more intuitive and engaging.",
    # 4. Command pattern for inventory
    "The Command pattern is well suited to inventory management because it "
    "supports undoing changes when errors occur. For example, if a user "
    "accidentally enters 500 instead of 50, the change can be easily reversed. "
    "The pattern also makes it possible to maintain a clear record of who made "
    "each update, which is valuable for identifying and resolving mistakes.",
    # 5. SQL triggers
    "Understanding SQL triggers can be challenging, particularly when it comes to "
    "the syntax and keywords involved. A helpful strategy is to read the trigger "
    "as a sequence of events: what happens first, and what the database does in "
    "response. Breaking it down in this way makes it much easier to understand "
    "the purpose of each part of the code.",
    # 6. quantum vs classical models
    "In the handwritten digit classification project, the classical models "
    "consistently outperformed the quantum models. Presenting the results side by "
    "side made the size of this difference clear. This comparison also raises an "
    "important question: given the strong performance of classical models, what "
    "evidence would be needed to demonstrate a meaningful advantage for the "
    "quantum approach?",
    # 7. mammography report evaluation
    "This thesis compares four approaches to generating mammography reports. A "
    "key consideration is that a report may read fluently while still containing "
    "critical errors, such as identifying the wrong breast or omitting the BI-RADS "
    "assessment. For this reason, it is important to evaluate these clinical "
    "details separately, regardless of how well the generated report reads.",
    # 8. email: training video
    "Hi team,\n\nI have updated the slides to align with the website and "
    "structured them so that the video can pause at each question. Once we "
    "finalize the placement of the questions, I will split the video at those "
    "points. I am also reviewing opportunities to shorten the video while "
    "ensuring the explanations remain clear.",
    # 9. email: project budget
    "Hi team,\n\nThank you for the update. Before we proceed, I would like to "
    "confirm my understanding of what is covered. I understand that there is a "
    "monthly allocation for API access. Could you please clarify whether the "
    "credits used in the code editor are also included, or whether those would "
    "require a separate request?",
    # 10. first-generation student reflection
    "Being a first-generation student comes with unique challenges, including "
    "moments of self-doubt and uncertainty about how to navigate each step. "
    "Asking questions and seeking guidance are essential parts of the journey. "
    "Today, working on a thesis and considering a doctorate represents a "
    "significant milestone, one that may once have seemed out of reach.",
]


SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # Pass: at most 1 of these 10 gets guess "ai", in every trial.
        "texts": MY_WRITING,
    },
    {
        "name": "score gap: AI set",
        "criterion": 2,
        # Pass: average confidence of this set is at least 0.20 higher than the
        # average of "my own writing" (the human set), in every trial.
        "texts": AI_WRITING,
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # 12 passages: six of mine and six AI ones. Pass: human, unsure and ai
        # each appear at least once. The boundary-score half of criterion 3
        # (0, 0.35, 0.525, 0.70, 1) is checked in criteria_extra.py.
        "texts": MY_WRITING[:6] + AI_WRITING[:6],
    },
    # Criterion 4 (appeals) needs a submission and then an appeal on its
    # content_id, which run_eval.py can't do. It's in criteria_extra.py.
    {
        "name": "bad and meaningless input",
        "criterion": 5,
        # Pass: the first five get a 4xx JSON error. The last three get either a
        # 4xx or a guess that is not "ai". The sixth invalid input, a body that
        # isn't valid JSON, can't be written as a dict, so it's in
        # criteria_extra.py. Every body has its own creator_id so the rate
        # limiter counts them separately.
        "bodies": [
            {"creator_id": "eval_c5_missing"},                      # no text field
            {"text": "", "creator_id": "eval_c5_empty"},            # empty text
            {"text": "     ", "creator_id": "eval_c5_spaces"},      # only spaces
            {"text": 12345, "creator_id": "eval_c5_number"},        # a number
            {"text": "a" * 20001, "creator_id": "eval_c5_20001"},   # 20,001 characters
            {"text": "!!!!!!!!", "creator_id": "eval_c5_bangs"},
            {"text": "........", "creator_id": "eval_c5_dots"},
            {"text": "😀😀😀😀😀😀😀😀", "creator_id": "eval_c5_emoji"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
