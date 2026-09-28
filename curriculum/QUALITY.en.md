# Information quality

*Version française (référence) : [QUALITY.md](QUALITY.md).*

**Highest quality means traceable, accurate, appropriately qualified and examinable.** Complexity and recency alone are not quality criteria.

## Requirements for all content

- Define learning objectives and prerequisites; state the target depth (core, mastery, beyond — see the [curriculum](ROADMAP.en.md#depth-levels)).
- Link each clinical piece to the R2C items it covers ([`r2c-items.csv`](r2c-items.csv)) and to the foundations it uses (F, N, M modules).
- Use textbooks, national teaching-college references and university material for settled foundations.
- Use reviews to map a research question, then examine primary studies for specific experimental claims.
- Record source title, section, link or DOI, edition/date where known, and verification date.
- Identify established knowledge, teaching models, contested claims and open questions.
- State equation assumptions, signs, units and boundary conditions.
- Distinguish simulated data from measurements.
- Explain how each visual could mislead.
- Include retrieval, image/graph interpretation, transfer questions and delayed assessment.
- Keep corrections in Git and log the misconception.

## Treatment guidelines

- Every treatment plan cites the issuing body, country and year of the guideline used. Guidelines differ between countries (the R2C follows French guidance) and age: a sheet relying on a guideline older than five years must be rechecked.
- Favour principles (mechanism, demonstrated benefit, level of evidence) over memorising doses.
- Prescriptions and management plans written here are study exercises, never care instructions.

## Source limits

An AI explanation is a draft teaching aid, not independent evidence. A source check is not the same as expert review. "Candidate sources" listed in modules have not been verified yet and must not be cited as evidence until they appear in [`sources/references.md`](../sources/references.md) with a verification date.

## Bilingual policy

French is the primary language and the reference version. A file without a language suffix is French; its English counterpart uses the `.en.md` suffix. If the two diverge, the French version is authoritative and the English version must be corrected.

English versions exist for the README, this document, the curriculum and the lessons. Both versions share objectives, variables, source identifiers, and figure filenames. Translate meaning, not just words. Keep one FR–EN glossary; introduce the full term before abbreviations. Every correction affecting scientific meaning must be applied in both versions. Figures carry bilingual labels, French first.

Written in French only: modules (`programme/`), disease sheets, templates, references and progress logs. The glossary provides the matching English terminology.

## Authoring and review

Authoring statuses: `planned`, `draft`, `source_checked`, `expert_reviewed`. Record reviewer and date only when a review actually occurred. Module authoring status lives in [`modules.csv`](modules.csv); all modules are currently `draft`. Lesson 001 is `source_checked`, not `expert_reviewed`.

Learning statuses are separate: `not_started`, `studying`, `assessed`, `retained` (retained after a delayed check). They live in `progress/`.

Status values stay in English in the CSV files so they remain stable and easy to filter.

## Mastery criterion

Reading is not mastery. Self-imposed progression rule: at least 80% on unseen questions, no unresolved central misconception, a successful delayed explanation without notes, and completion of the module's "Validation du module" tasks. This is a study heuristic, not an official exam threshold.
