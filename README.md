# Medicine → Neuroscience / Médecine → Neurosciences

Bilingual, visual, mathematical self-study of foundational medicine.
Étude personnelle bilingue, visuelle et mathématique des sciences médicales fondamentales.

**Status / Statut:** starter repository; one demonstration lesson, not a complete medical course. Teaching notes are AI-assisted, source-linked, and not independently reviewed by medical faculty.
**Objectif:** viser la maîtrise théorique des sciences précliniques, puis approfondir les neurosciences. Aucun diplôme ni équivalence clinique n'est conféré.

Start with [the curriculum](curriculum/ROADMAP.md), [quality standards](curriculum/QUALITY.md), then the demonstration in [English](lessons/001-passive-membrane/lesson.en.md) or [French](lessons/001-passive-membrane/lesson.fr.md). The demonstration is a preview of the teaching style, not a claim that membrane modeling replaces introductory cell biology.

## Navigation

| Location | Purpose / Rôle |
|---|---|
| `curriculum/` | Scope, prerequisites, and evidence standards / Programme et exigences |
| `lessons/001-passive-membrane/` | Two language versions, graph, reproducible Python, exercises and solutions |
| `templates/lesson.md` | Reusable lesson structure / Structure d'une future leçon |
| `glossary/terms.csv` | Shared EN–FR terminology / Terminologie commune |
| `sources/references.md` | Linked references, source role, and review date |
| `progress/tracker.csv` | Objective-level tracking / Suivi par objectif |
| `progress/errors.md` | Error log / Journal des erreurs |

## Study cycle / Cycle d'étude

1. Read in either language; use the second version to check meaning. / Lire dans une langue, puis vérifier le sens dans l'autre.
2. Draw and explain without notes. / Dessiner et expliquer sans notes.
3. Solve unseen questions before opening solutions. / Résoudre avant de consulter le corrigé.
4. Record mistakes and supporting references. / Consigner les erreurs et leurs sources.
5. Revisit after approximately 1, 7, and 30 days, adapting intervals to performance. / Réviser à intervalles adaptés aux résultats.

Reading a lesson is not evidence of mastery. A self-imposed progression rule is at least 80% on unseen questions, no unresolved central misconception, and a successful delayed explanation. This is a study heuristic, not an official examination threshold or proof of equivalence.

## Git

The ZIP includes a local Git repository and its initial commit. Extract it, open the folder in VS Code, and run these commands in Git Bash:

```bash
git status
git log --oneline
```

Before your own first commit, set your chosen identity locally:

```bash
git config user.name "Your name"
git config user.email "Your chosen email"
```

For each learning session:

```bash
git add lessons glossary progress
git commit -m "study: explain membrane response and correct unit errors"
```

No remote is configured. You can later attach your own GitHub, GitLab, or other remote. Commit original notes, source links, and original figures; link to textbooks instead of putting copyrighted book scans in the repository.

## Reproduce the figure / Reproduire la figure

Python 3 with NumPy and Matplotlib is required only to regenerate the plots. Markdown and the included PNG/SVG work without Python.

```bash
python -m pip install -r requirements.txt
python lessons/001-passive-membrane/plot.py
```

See [references](sources/references.md) for provenance. Equations use Markdown math; display support depends on the editor. The diagrams and calculations supplement biological understanding, anatomical study, and evidence appraisal.
