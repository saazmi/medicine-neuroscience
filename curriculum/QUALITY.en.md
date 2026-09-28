# Information quality

*Version française (référence) : [QUALITY.md](QUALITY.md).*

**Highest quality means traceable, accurate, appropriately qualified and examinable.** Complexity and recency alone are not quality criteria.

For every substantial lesson:

- Define learning objectives and prerequisites.
- Write the French reference version first, then an aligned English version, using stable concept identifiers.
- Use textbooks and university material for settled foundations.
- Use reviews to map a research question, then examine primary studies for specific experimental claims.
- Record source title, section, link or DOI, edition/date where known, and verification date.
- Identify established knowledge, teaching models, contested claims and open questions.
- State equation assumptions, signs, units and boundary conditions.
- Distinguish simulated data from measurements.
- Explain how each visual could mislead.
- Include retrieval, image/graph interpretation, transfer questions and delayed assessment.
- Keep corrections in Git and log the misconception.

An AI explanation is a draft teaching aid, not independent evidence. A source check is not the same as expert review. For current clinical practice, consult current professional guidance; an old foundational textbook cannot establish today's treatment recommendations.

## Bilingual policy

French is the primary language and the reference version. A file without a language suffix is French; its English counterpart uses the `.en.md` suffix. If the two diverge, the French version is authoritative and the English version must be corrected.

Both versions share objectives, variables, source identifiers, and figure filenames. Translate meaning, not just words. Keep one FR–EN glossary; introduce the full term before abbreviations. Every correction affecting scientific meaning must be applied in both versions. Figures carry bilingual labels, French first, rather than being duplicated.

Working documents (template, references, progress logs) are written in French only.

## Authoring and review

Use statuses: `planned`, `draft`, `source_checked`, `expert_reviewed`. Record reviewer and date only when a review actually occurred. Learning status is separate: `not_started`, `studying`, `assessed`, `retained`. The demonstration is `source_checked`, not `expert_reviewed`.

Status values stay in English in the CSV files so they remain stable and easy to filter.
