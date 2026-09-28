# Curriculum

*Version française (référence) : [ROADMAP.md](ROADMAP.md).*

## Goal

Self-directed acquisition of the full theoretical knowledge of a general practitioner, with deeper mechanistic understanding than an exam requires, followed by advanced neuroscience.

**What "complete" means here.** The clinical scope is anchored on an official, checkable standard: the **367 items of the R2C**, the knowledge curriculum of the second cycle of French medical school, which defines what every doctor knows before residency ([item list](r2c-items.csv), sources S9–S10). Every item is assigned to a module, and [`tools/r2c.py`](../tools/r2c.py) checks that none is missing. The R2C assumes first-cycle knowledge (basic sciences, anatomy, physiology) for which no comparable official list exists; phases F, N and M spell it out. Module T05 adds what is specific to general practice.

**What this repository cannot provide.** Physical examination, procedures, bedside reasoning, real communication and clinical responsibility are learned under supervision. This curriculum confers no degree, equivalence or right to practise. Modules therefore target the meaning and value of signs and procedures, not their execution.

**Starting profile.** Strong mathematics, physics and engineering background. F01 and F02 can be validated quickly after a diagnostic test; chemistry and biology usually need more work; anatomy cannot be derived from first principles.

## Architecture

| Phase | Role | Modules |
|---|---|---|
| **F — Scientific foundations** | Basic sciences medicine relies on | F01 Mathematics & statistics · F02 Physics & biophysics · F03 General chemistry · F04 Organic chemistry · F05 Structural biochemistry · F06 Cell biology · F07 Molecular biology & genetics |
| **N — The normal human** | Anatomy, histology, embryology, physiology by system | N01 Histology & embryology · N02 Metabolism & nutrition · N03 General physiology · N04 Musculoskeletal · N05 Nervous system & senses · N06 Cardiovascular · N07 Respiratory · N08 Blood & haemostasis · N09 Kidney & body fluids · N10 Digestive · N11 Endocrine · N12 Reproduction & growth · N13 Head, neck & skin |
| **M — Mechanisms of disease and tools** | Linking normal to pathological; diagnostic and therapeutic tools | M01 Immunology · M02 Microbiology · M03 General pathology · M04 Medical genetics · M05 Pharmacology · M06 Clinical semiology & reasoning · M07 Laboratory medicine & imaging |
| **C — Clinical medicine** | Diseases by discipline; carries most R2C items | C01 Cardiology · C02 Pulmonology · C03 Gastroenterology & hepatology · C04 Nephrology & urology · C05 Endocrinology & nutrition · C06 Haematology · C07 Infectious diseases · C08 Internal medicine & immunopathology · C09 Rheumatology & orthopaedics · C10 Neurology · C11 Psychiatry & addiction · C12 Paediatrics · C13 Obstetrics & gynaecology · C14 Dermatology · C15 Ophthalmology · C16 ENT · C17 Oncology · C18 Geriatrics, pain & palliative care · C19 Emergency, intensive care & anaesthesia |
| **T — Practice and populations** | Ethics, law, public health, evidence, therapeutics, general practice | T01 Ethics & law · T02 Public health · T03 Evidence & research · T04 Therapeutics · T05 General practice |
| **X — Extension** | Beyond the generalist | X01 Advanced neuroscience |

Module syllabi are written in French only (see the [bilingual policy](QUALITY.en.md#bilingual-policy)); the file list is [`modules.csv`](modules.csv).

## Recommended path

1. **Diagnostic.** Test F01–F07; validate what is known quickly, fill gaps (chemistry, biochemistry, cell biology first).
2. **Normal + mechanisms.** Study N by system, interleaving M01–M03 once N03 is secure. Anatomy is continuous work.
3. **Tools.** M04–M07 before clinical modules, especially M06.
4. **Clinical.** Study each C module right after revising its N module. Suggested order: C01, C02, C04, C03, C05, C06, C07, C08, C09, C10, C11, C14, C15, C16, C12, C13, C17, C18, C19.
5. **Cross-cutting, throughout.** T03 from F01; T01 and T02 as regular reading; T04 alongside each C module; T05 at the end of phase C.
6. **Extension.** X01 after N05, C10 and C11.

No timetable is fixed before the diagnostic. For scale, the first two cycles of medical school take six full-time years; a self-directed theoretical path remains a multi-year project.

## Depth levels

- **Core**: what every doctor must know (R2C rank A).
- **Mastery**: what a doctor needs on day one of residency (rank B), with explicit mechanisms.
- **Beyond the core**: molecular pathophysiology, landmark trials, controversies, open questions — tackled only after the core.

## Coverage tracking

```bash
python tools/r2c.py
```

Reports how many R2C items have written content and flags inconsistencies. After editing `r2c-items.csv` or `modules.csv`, run `python tools/r2c.py sync`.
