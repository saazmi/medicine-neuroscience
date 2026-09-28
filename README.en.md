# Medicine → Neuroscience

*Version française (référence) : [README.md](README.md).*

Personal, exhaustive study of the theoretical knowledge of a general practitioner — from basic sciences to clinical medicine — followed by advanced neuroscience. French is the primary language; English companions accompany the main documents.

**Goal:** genuine mastery of medical theory, more mechanistic than an exam requires, with no claim to clinical practice.
**Scope:** anchored on the **367 items of the R2C** (the knowledge curriculum of the second cycle of French medical school), complemented by first-cycle foundations (sciences, anatomy, physiology) and what is specific to general practice. See [the curriculum](curriculum/ROADMAP.en.md).
**Status:** the full structure is in place (52 modules, 367 items assigned); written content is just starting (one lesson). Notes are AI-assisted, source-linked, and not reviewed by medical faculty. No degree, equivalence or right to practise is conferred; nothing here is medical advice.

## Layout

| Location | Purpose |
|---|---|
| [`curriculum/ROADMAP.en.md`](curriculum/ROADMAP.en.md) | Curriculum: phases, modules, path, depth levels |
| [`curriculum/QUALITY.en.md`](curriculum/QUALITY.en.md) | Quality standards, bilingual policy, mastery criterion |
| [`curriculum/modules.csv`](curriculum/modules.csv) | The 52 modules and their authoring status |
| [`curriculum/r2c-items.csv`](curriculum/r2c-items.csv) | The 367 R2C items, their module, and the content covering them |
| `programme/` | One file per module (French): content to master, R2C items, validation, candidate sources |
| `lessons/` | Written lessons (FR + EN), figures, reproducible code, exercises and solutions |
| `templates/` | Templates: lesson and disease sheet |
| [`tools/r2c.py`](tools/r2c.py) | Coverage check and item-list synchronisation |
| `glossary/terms.csv` | Shared FR–EN terminology |
| `sources/references.md` | Verified references |
| `progress/` | Personal tracking: modules, objectives, error log |

**Languages:** a file without a suffix is French and is the reference version; its English counterpart uses the `.en.md` suffix. Modules and disease sheets are French only. See the [bilingual policy](curriculum/QUALITY.en.md#bilingual-policy).

## The six phases

| Phase | Content |
|---|---|
| **F** Scientific foundations | Mathematics & statistics, physics & biophysics, general & organic chemistry, biochemistry, cell & molecular biology, genetics |
| **N** The normal human | Histology, embryology, metabolism, physiology and anatomy of every system |
| **M** Mechanisms and tools | Immunology, microbiology, general pathology, medical genetics, pharmacology, clinical semiology & reasoning, laboratory medicine & imaging |
| **C** Clinical medicine | 19 disciplines, from cardiology to emergency medicine |
| **T** Practice and populations | Ethics & law, public health, evidence-based medicine, therapeutics, general practice |
| **X** Extension | Neuroscience |

## Study cycle

1. Read the module, then the lesson or sheet; use the English version for international terminology.
2. Draw and explain without notes.
3. Solve unseen questions before opening solutions.
4. Record mistakes and the sources that correct them in [`progress/errors.md`](progress/errors.md).
5. Revisit after approximately 1, 7, and 30 days, adapting intervals to performance.

## Tools

```bash
python tools/r2c.py
```

```bash
python -m pip install -r requirements.txt
python lessons/001-passive-membrane/plot.py
```

## Git

Repository: <https://github.com/saazmi/medicine-neuroscience>.

```bash
git clone https://github.com/saazmi/medicine-neuroscience.git
```
