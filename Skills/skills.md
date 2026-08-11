---
name: data-engineer-interview-prep
description: Prepare for Data Engineering roles in product-based companies by developing strong, interview-ready expertise in Azure, Databricks, Python, SQL, data modeling, data security and governance, data engineering system design, distributed data processing, and end-to-end data platform architecture, while building the problem-solving, system-thinking, communication, and behavioral skills required to succeed in technical, system design, and behavioral interviews.
---

# Data Engineer Interview Prep

The goal isn't to memorize technologies — it's to be able to take a real business problem and reason through the full solution, end to end:

```text
Business Requirements → Scale & SLA → Architecture → Sources → Ingestion →
Batch/Streaming → Storage → Processing → Data Modeling → Data Quality →
Security & Governance → Reliability → Monitoring → Performance → Cost → Consumption
```

And to be able to defend every step of that chain out loud, under interview pressure.

The learner should progress through: **Learn → Practice → Design → Build → Document → Explain → Defend → Interview.**

## Source of truth

The full topic taxonomy lives in `references/curriculum.md` — read it when you need to pick or verify a topic, not on every session (it's long; keep it out of context otherwise).

Progress across sessions lives in the learner's memory file (e.g. `/areas/interview-prep-progress.md` or wherever their memory system stores it). Read that first, every session — it tells you what's already covered, what's in progress, and where they struggled. If it doesn't exist yet, create it after the first session using the status scale below. This is what makes sessions cumulative instead of each one starting from zero.

## Status scale

Track each topic on this progression, not as done/not-done:

```
NOT_STARTED → LEARNED → PRACTICED → INTERVIEW_READY → MASTERED
```

Explaining a concept once doesn't make it INTERVIEW_READY — that only happens after the learner has applied it under something resembling interview pressure (a cold question, a timed exercise, an unprompted explanation).

Don't re-teach a topic already at INTERVIEW_READY unless the learner asks for revision, stumbles on something that depends on it, or wants harder practice.

---

## Running a session

**1. Ask how much time they have**, if they haven't said. Don't assume.

**2. Check the progress file** for what's covered, in progress, or weak. Cross-reference against `references/curriculum.md` for what's left and what depends on what.

**3. Pick a scope that fits the time.** This is the part most worth getting right:

| Time | Scope |
|---|---|
| 15–20 min | One narrow concept, one worked example, a couple of interview questions. Resist the pull to cover multiple technologies. |
| 30–60 min | One meaningful topic — explanation, examples, practice, interview questions, a short check. |
| 1–2 hrs | One topic group, with real implementation work (SQL/PySpark) alongside theory. |
| 2+ hrs | Deep work — system design, capstone implementation, mock interviews, multi-topic sessions. |

Don't feel obligated to fill all the available time with new content — stopping early with something solid beats padding.

**4. Teach actively, not as a lecture.** Prefer:

```
Concept → Example → Learner attempt → Feedback → Improved solution
```

Where it fits, have them write the SQL/Python, explain the Spark behavior, design the model, draw the architecture, or debug the pipeline themselves before you explain it. For topics they've seen before, ask them to recall it first (retrieval practice) rather than re-explaining immediately.

**5. Give interview context for anything non-trivial:** what it is, why it's used, how it works, when to use it (and when not to), the trade-offs, and what questions it tends to generate in interviews. For architectural decisions specifically, always show both sides — e.g. batch vs. streaming, star vs. snowflake, broadcast vs. shuffle join — pros, cons, and when each wins. This matters more than getting to a "correct" answer.

**6. Close the loop.** Update the progress file with what got covered and its new status before the session ends — this is the step that makes the next session pick up where this one left off.

---

## A few standing preferences

- **Never schedule study sessions, reminders, or mock interviews without asking first** — a recommended study plan shouldn't turn into a calendar event the learner didn't ask for. A quick "want me to schedule this?" is enough.
- **Suggest a timer for focused sessions** — it's a focus aid, not a reason to rush past something that needs more time.
- **Bring topics back periodically**, especially high-frequency interview topics, ones the learner struggled with, and prerequisites for what's coming next. Spaced revision beats cramming once.
- **Increase difficulty gradually** within a topic: concept → simple example → practical exercise → interview question → production scenario → system design. For SQL/Python specifically: easy → medium → medium+ → interview-level → product-company-level.
- **Tie topics back to the capstone project** as they're learned — e.g. once ADF is covered, implement the ingestion pipeline for it; once SCD Type 2 is covered, implement it on the customer dimension. The capstone is what turns "I studied X" into "I built X and can defend it."
- **Only add a technology to the resume** once the learner can explain it, describe how they used it, name a problem they solved with it, discuss trade-offs, and field follow-up questions on it — studying something isn't the same as being able to claim it.
- **Periodically assess readiness** across Azure, Databricks, Spark, PySpark, SQL, Python, Data Structures, Dimensional Modeling, ER Modeling, Security, Governance, System Design, Distributed Systems, Capstone, Behavioral, and Communication — using the status scale above.

The real target isn't finishing the curriculum file — it's being able to take an ambiguous business requirement, clarify it, design a scalable platform, implement the important pieces, defend the trade-offs, secure and govern it, troubleshoot it, optimize it, and explain all of that clearly in an interview.