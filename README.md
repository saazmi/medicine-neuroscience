# Médecine → Neurosciences

Étude personnelle, visuelle et mathématique des sciences médicales fondamentales, puis des neurosciences. Le français est la langue de référence ; une version anglaise accompagne les documents principaux.

*English version: [README.en.md](README.en.md).*

**Statut :** dépôt de départ ; une leçon de démonstration, pas un cursus médical complet. Les notes sont rédigées avec l'aide de l'IA, reliées à leurs sources, et non validées de façon indépendante par des enseignants en médecine.
**Objectif :** viser la maîtrise théorique des sciences précliniques, puis approfondir les neurosciences. Aucun diplôme ni équivalence clinique n'est conféré.

Commencer par [le programme](curriculum/ROADMAP.md) et [les exigences de qualité](curriculum/QUALITY.md), puis la [leçon de démonstration](lessons/001-passive-membrane/lesson.md) ([version anglaise](lessons/001-passive-membrane/lesson.en.md)). Cette leçon illustre le format pédagogique ; elle ne prétend pas que la modélisation de la membrane remplace la biologie cellulaire d'introduction.

## Organisation

| Emplacement | Rôle |
|---|---|
| `curriculum/` | Programme, prérequis et exigences de preuve |
| `lessons/001-passive-membrane/` | Leçon (FR + EN), figure, code Python reproductible, exercices et corrigé |
| `templates/lesson.md` | Structure d'une future leçon |
| `glossary/terms.csv` | Terminologie commune FR–EN |
| `sources/references.md` | Références, rôle de chaque source et date de vérification |
| `progress/tracker.csv` | Suivi par objectif |
| `progress/errors.md` | Journal des erreurs |

**Langues :** un fichier sans suffixe (`lesson.md`, `questions.md`…) est en français et fait foi ; son équivalent anglais porte le suffixe `.en.md`. Voir la [politique bilingue](curriculum/QUALITY.md#politique-bilingue).

## Cycle d'étude

1. Lire la version française ; consulter la version anglaise pour vérifier le sens ou la terminologie internationale.
2. Dessiner et expliquer sans notes.
3. Résoudre les questions inédites avant d'ouvrir le corrigé.
4. Consigner les erreurs et les sources qui les corrigent.
5. Réviser après environ 1, 7 et 30 jours, en adaptant les intervalles aux résultats.

Lire une leçon ne prouve pas qu'elle est maîtrisée. Règle de progression personnelle : au moins 80 % aux questions inédites, aucune erreur conceptuelle centrale non résolue, et une explication différée réussie. C'est une règle d'étude, pas un seuil d'examen officiel ni une preuve d'équivalence.

## Git

Le dépôt est publié sur GitHub : <https://github.com/saazmi/medicine-neuroscience>.

```bash
git clone https://github.com/saazmi/medicine-neuroscience.git
```

Avant le premier commit, définir son identité localement :

```bash
git config user.name "Votre nom"
git config user.email "Votre adresse"
```

À chaque séance :

```bash
git add lessons glossary progress
git commit -m "étude : expliquer la réponse membranaire et corriger les erreurs d'unités"
git push
```

Versionner les notes originales, les liens vers les sources et les figures originales ; renvoyer vers les manuels plutôt que d'ajouter des scans d'ouvrages protégés par le droit d'auteur.

## Reproduire la figure

Python 3 avec NumPy et Matplotlib n'est nécessaire que pour régénérer les graphiques. Les fichiers Markdown et les images PNG/SVG fournies fonctionnent sans Python.

```bash
python -m pip install -r requirements.txt
python lessons/001-passive-membrane/plot.py
```

Voir les [références](sources/references.md) pour la provenance. Les équations utilisent la syntaxe mathématique Markdown ; l'affichage dépend de l'éditeur. Les schémas et calculs complètent la compréhension biologique, l'étude anatomique et l'analyse critique des preuves ; ils ne les remplacent pas.
