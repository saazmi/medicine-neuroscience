# Médecine → Neurosciences

Étude personnelle et exhaustive des connaissances théoriques d'un médecin généraliste — des sciences fondamentales à la clinique — puis approfondissement en neurosciences. Le français est la langue de référence ; une version anglaise accompagne les documents principaux.

*English version: [README.en.md](README.en.md).*

**Objectif :** une maîtrise réelle de la théorie médicale, plus mécanistique que ne l'exige un examen, sans prétention à la pratique.
**Périmètre :** ancré sur les **367 items du R2C** (programme de connaissances du 2e cycle des études médicales en France), complété par les bases du 1er cycle (sciences, anatomie, physiologie) et les spécificités de la médecine générale. Voir [le programme](curriculum/ROADMAP.md).
**Statut :** la structure complète est en place (52 modules, 367 items rattachés) ; le contenu rédigé commence (une leçon). Les notes sont rédigées avec l'aide de l'IA, reliées à leurs sources, et non validées par des enseignants en médecine. Aucun diplôme, aucune équivalence et aucun droit d'exercer ne sont conférés ; rien ici n'est un conseil médical.

## Organisation

| Emplacement | Rôle |
|---|---|
| [`curriculum/ROADMAP.md`](curriculum/ROADMAP.md) | Programme : phases, modules, parcours, niveaux de profondeur |
| [`curriculum/QUALITY.md`](curriculum/QUALITY.md) | Exigences de qualité, politique bilingue, critère de maîtrise |
| [`curriculum/modules.csv`](curriculum/modules.csv) | Liste des 52 modules et statut de rédaction |
| [`curriculum/r2c-items.csv`](curriculum/r2c-items.csv) | Les 367 items du R2C, leur module et le contenu qui les couvre |
| `programme/` | Un fichier par module : contenu à maîtriser, items R2C, validation, sources candidates |
| `lessons/` | Leçons rédigées (FR + EN), figures, code reproductible, exercices et corrigés |
| `templates/` | Gabarits : [leçon](templates/lesson.md) et [fiche maladie](templates/fiche-maladie.md) |
| [`tools/r2c.py`](tools/r2c.py) | Vérification de la couverture et synchronisation des listes d'items |
| `glossary/terms.csv` | Terminologie commune FR–EN |
| `sources/references.md` | Références vérifiées |
| `progress/` | Suivi personnel : modules, objectifs, journal des erreurs |

**Langues :** un fichier sans suffixe est en français et fait foi ; son équivalent anglais porte le suffixe `.en.md`. Les modules et fiches sont en français uniquement. Voir la [politique bilingue](curriculum/QUALITY.md#politique-bilingue).

## Les six phases

| Phase | Contenu |
|---|---|
| **F** Fondamentaux scientifiques | Mathématiques et statistiques, physique et biophysique, chimie générale et organique, biochimie, biologie cellulaire et moléculaire, génétique |
| **N** L'être humain normal | Histologie, embryologie, métabolisme, physiologie et anatomie de chaque appareil |
| **M** Mécanismes et outils | Immunologie, microbiologie, pathologie générale, génétique médicale, pharmacologie, sémiologie et raisonnement, biologie médicale et imagerie |
| **C** Médecine clinique | 19 disciplines, de la cardiologie aux urgences |
| **T** Exercice et populations | Éthique et droit, santé publique, médecine fondée sur les preuves, thérapeutique, médecine générale |
| **X** Approfondissement | Neurosciences |

## Cycle d'étude

1. Lire le module, puis la leçon ou la fiche ; consulter la version anglaise pour la terminologie internationale.
2. Dessiner et expliquer sans notes.
3. Résoudre les questions inédites avant d'ouvrir le corrigé.
4. Consigner les erreurs et les sources qui les corrigent dans [`progress/errors.md`](progress/errors.md).
5. Réviser après environ 1, 7 et 30 jours, en adaptant les intervalles aux résultats.

Lire ne prouve pas la maîtrise : voir le [critère de maîtrise](curriculum/QUALITY.md#critère-de-maîtrise).

## Outils

Python 3 (bibliothèque standard) suffit pour vérifier la couverture :

```bash
python tools/r2c.py
```

NumPy et Matplotlib ne sont nécessaires que pour régénérer les figures des leçons :

```bash
python -m pip install -r requirements.txt
python lessons/001-passive-membrane/plot.py
```

## Git

Dépôt : <https://github.com/saazmi/medicine-neuroscience>.

```bash
git clone https://github.com/saazmi/medicine-neuroscience.git
```

À chaque séance :

```bash
git add programme lessons progress
git commit -m "étude : fiche insuffisance cardiaque, erreurs corrigées"
git push
```

Versionner les notes originales, les liens vers les sources et les figures originales ; renvoyer vers les manuels plutôt que d'ajouter des scans d'ouvrages protégés par le droit d'auteur.
