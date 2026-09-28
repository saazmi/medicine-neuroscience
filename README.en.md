# Medicine → Neuroscience

*Version française (référence) : [README.md](README.md).*

Visual, mathematical self-study of foundational medicine, followed by neuroscience. French is the primary language of this repository; English companions accompany the main documents.

**Status:** starter repository; one demonstration lesson, not a complete medical course. Teaching notes are AI-assisted, source-linked, and not independently reviewed by medical faculty.
**Goal:** theoretical mastery of the preclinical sciences, then deeper neuroscience. No degree or clinical equivalence is conferred.

Start with [the curriculum](curriculum/ROADMAP.en.md) and [quality standards](curriculum/QUALITY.en.md), then the [demonstration lesson](lessons/001-passive-membrane/lesson.en.md) ([French version](lessons/001-passive-membrane/lesson.md)). The demonstration previews the teaching style; it does not claim that membrane modeling replaces introductory cell biology.

## Layout

| Location | Purpose |
|---|---|
| `curriculum/` | Scope, prerequisites, and evidence standards |
| `lessons/001-passive-membrane/` | Lesson (FR + EN), figure, reproducible Python, exercises and solutions |
| `templates/lesson.md` | Reusable lesson structure |
| `glossary/terms.csv` | Shared FR–EN terminology |
| `sources/references.md` | Linked references, source role, and review date |
| `progress/tracker.csv` | Objective-level tracking |
| `progress/errors.md` | Error log |

**Languages:** a file without a suffix (`lesson.md`, `questions.md`…) is French and is the reference version; its English counterpart uses the `.en.md` suffix. Files without an English counterpart (template, references, logs) are French only. See the [bilingual policy](curriculum/QUALITY.en.md#bilingual-policy).

## Study cycle

1. Read the French version; use the English version to check meaning or international terminology.
2. Draw and explain without notes.
3. Solve unseen questions before opening solutions.
4. Record mistakes and supporting references.
5. Revisit after approximately 1, 7, and 30 days, adapting intervals to performance.

Reading a lesson is not evidence of mastery. A self-imposed progression rule is at least 80% on unseen questions, no unresolved central misconception, and a successful delayed explanation. This is a study heuristic, not an official examination threshold or proof of equivalence.

## Git

The repository is published at <https://github.com/saazmi/medicine-neuroscience>.

```bash
git clone https://github.com/saazmi/medicine-neuroscience.git
```

For each learning session:

```bash
git add lessons glossary progress
git commit -m "étude : expliquer la réponse membranaire et corriger les erreurs d'unités"
git push
```

Commit original notes, source links, and original figures; link to textbooks instead of putting copyrighted book scans in the repository.

## Reproduce the figure

Python 3 with NumPy and Matplotlib is required only to regenerate the plots. Markdown and the included PNG/SVG work without Python.

```bash
python -m pip install -r requirements.txt
python lessons/001-passive-membrane/plot.py
```

See [references](sources/references.md) for provenance. Equations use Markdown math; display support depends on the editor. The diagrams and calculations supplement biological understanding, anatomical study, and evidence appraisal.
