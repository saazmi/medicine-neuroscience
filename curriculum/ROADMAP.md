# Programme

*English version: [ROADMAP.en.md](ROADMAP.en.md).*

## Objectif

Acquérir, en autodidacte, l'ensemble des connaissances théoriques d'un médecin généraliste, avec une compréhension mécanistique plus profonde que celle qu'exige un examen, puis approfondir les neurosciences.

**Ce que « complet » veut dire ici.** Le périmètre clinique est ancré sur un référentiel officiel et vérifiable : les **367 items du R2C**, programme de connaissances du deuxième cycle des études médicales en France, qui définit ce que tout médecin sait avant l'internat ([liste des items](r2c-items.csv), sources S9–S10). Chaque item est rattaché à un module ; l'outil [`tools/r2c.py`](../tools/r2c.py) vérifie qu'aucun n'est oublié. Le R2C présuppose les connaissances du premier cycle (sciences fondamentales, anatomie, physiologie), qui ne font pas l'objet d'une liste officielle comparable : les phases F, N et M les détaillent. Le module T05 ajoute ce qui est propre à la médecine générale.

**Ce que ce dépôt ne peut pas donner.** L'examen clinique, les gestes, le raisonnement au lit du malade, la communication réelle et la responsabilité clinique s'acquièrent en pratique supervisée. Ce programme n'ouvre droit à aucun diplôme, équivalence ou exercice. Les modules en tiennent compte : ils visent la signification et la valeur des signes et des gestes, pas leur exécution.

**Profil de départ.** Solides acquis en mathématiques, physique et ingénierie. Les modules F01 et F02 peuvent être validés rapidement après un test de positionnement ; la chimie et la biologie demandent en général davantage de travail ; l'anatomie ne se déduit pas de premiers principes.

## Architecture

| Phase | Rôle | Modules |
|---|---|---|
| **F — Fondamentaux scientifiques** | Sciences de base nécessaires à la médecine (niveau PASS/LAS et au-delà) | [F01 Mathématiques et statistiques](../programme/F01-mathematiques-statistiques.md) · [F02 Physique et biophysique](../programme/F02-physique-biophysique.md) · [F03 Chimie générale](../programme/F03-chimie-generale.md) · [F04 Chimie organique](../programme/F04-chimie-organique.md) · [F05 Biochimie structurale](../programme/F05-biochimie-structurale.md) · [F06 Biologie cellulaire](../programme/F06-biologie-cellulaire.md) · [F07 Biologie moléculaire et génétique](../programme/F07-biologie-moleculaire-genetique.md) |
| **N — L'être humain normal** | Anatomie, histologie, embryologie, physiologie par appareil | [N01 Histologie et embryologie](../programme/N01-histologie-embryologie.md) · [N02 Métabolisme et nutrition](../programme/N02-metabolisme-nutrition.md) · [N03 Physiologie générale](../programme/N03-physiologie-generale.md) · [N04 Locomoteur](../programme/N04-appareil-locomoteur.md) · [N05 Système nerveux et sens](../programme/N05-systeme-nerveux.md) · [N06 Cardiovasculaire](../programme/N06-cardiovasculaire.md) · [N07 Respiratoire](../programme/N07-respiratoire.md) · [N08 Sang et hémostase](../programme/N08-sang-hemostase.md) · [N09 Rein et liquides](../programme/N09-rein-liquides.md) · [N10 Digestif](../programme/N10-digestif.md) · [N11 Endocrinien](../programme/N11-endocrinien.md) · [N12 Reproduction et croissance](../programme/N12-reproduction-croissance.md) · [N13 Tête, cou et peau](../programme/N13-tete-cou-peau.md) |
| **M — Mécanismes de la maladie et outils** | Ce qui relie le normal au pathologique, et les outils du diagnostic et du traitement | [M01 Immunologie](../programme/M01-immunologie.md) · [M02 Microbiologie](../programme/M02-microbiologie.md) · [M03 Pathologie générale](../programme/M03-pathologie-generale.md) · [M04 Génétique médicale](../programme/M04-genetique-medicale.md) · [M05 Pharmacologie](../programme/M05-pharmacologie.md) · [M06 Sémiologie et raisonnement](../programme/M06-semiologie-raisonnement.md) · [M07 Biologie médicale et imagerie](../programme/M07-biologie-imagerie.md) |
| **C — Médecine clinique** | Les maladies, par discipline ; porte l'essentiel des items R2C | [C01 Cardiologie](../programme/C01-cardiologie-vasculaire.md) · [C02 Pneumologie](../programme/C02-pneumologie.md) · [C03 Hépato-gastro](../programme/C03-hepato-gastro.md) · [C04 Néphro-urologie](../programme/C04-nephrologie-urologie.md) · [C05 Endocrinologie-nutrition](../programme/C05-endocrinologie-nutrition.md) · [C06 Hématologie](../programme/C06-hematologie.md) · [C07 Infectiologie](../programme/C07-infectiologie.md) · [C08 Médecine interne](../programme/C08-medecine-interne.md) · [C09 Rhumatologie-orthopédie](../programme/C09-rhumatologie-orthopedie.md) · [C10 Neurologie](../programme/C10-neurologie.md) · [C11 Psychiatrie-addictologie](../programme/C11-psychiatrie-addictologie.md) · [C12 Pédiatrie](../programme/C12-pediatrie.md) · [C13 Gynécologie-obstétrique](../programme/C13-gynecologie-obstetrique.md) · [C14 Dermatologie](../programme/C14-dermatologie.md) · [C15 Ophtalmologie](../programme/C15-ophtalmologie.md) · [C16 ORL](../programme/C16-orl.md) · [C17 Cancérologie](../programme/C17-cancerologie.md) · [C18 Gériatrie, douleur, palliatif](../programme/C18-geriatrie-douleur-palliatif.md) · [C19 Urgences et réanimation](../programme/C19-urgences-reanimation.md) |
| **T — Exercice médical et populations** | Éthique, droit, santé publique, preuves, thérapeutique, médecine générale | [T01 Éthique et droit](../programme/T01-ethique-droit.md) · [T02 Santé publique](../programme/T02-sante-publique.md) · [T03 Preuves et recherche](../programme/T03-ebm-recherche.md) · [T04 Thérapeutique](../programme/T04-therapeutique.md) · [T05 Médecine générale](../programme/T05-medecine-generale.md) |
| **X — Approfondissement** | Au-delà du généraliste | [X01 Neurosciences approfondies](../programme/X01-neurosciences.md) |

La liste de référence des modules est [`modules.csv`](modules.csv) ; le suivi personnel est dans [`progress/modules.csv`](../progress/modules.csv).

## Parcours recommandé

Le parcours est progressif mais pas strictement linéaire : chaque phase revient sur les précédentes (apprentissage en spirale).

1. **Positionnement.** Tester F01–F07 ; valider rapidement ce qui est acquis, combler les lacunes (chimie, biochimie, biologie cellulaire en priorité).
2. **Normal + mécanismes.** Étudier N par appareil, en intercalant M01–M03 dès que N03 est acquis. L'anatomie se travaille en continu (atlas, dessins de mémoire, imagerie en coupe).
3. **Outils.** M04–M07 avant d'aborder la clinique, M06 en particulier.
4. **Clinique.** Étudier chaque module C juste après la révision du module N correspondant (C01 après N06, C02 après N07, etc.). Ordre suggéré : C01, C02, C04, C03, C05, C06, C07, C08, C09, C10, C11, C14, C15, C16, C12, C13, C17, C18, C19.
5. **Transversal, tout au long du parcours.** T03 dès F01 ; T01 et T02 en lectures régulières ; T04 avec chaque module C ; T05 en fin de phase C.
6. **Approfondissement.** X01 après N05, C10 et C11.

Aucun calendrier n'est fixé avant le positionnement et la connaissance de la disponibilité hebdomadaire. À titre d'ordre de grandeur, les deux premiers cycles des études médicales durent six ans à temps plein ; un parcours théorique autodidacte reste un projet de plusieurs années.

## Niveaux de profondeur

Chaque module et chaque fiche distinguent trois niveaux :

- **Socle** : ce que tout médecin doit savoir (équivalent du rang A du R2C).
- **Maîtrise** : ce qu'un médecin doit savoir en prenant ses fonctions d'interne (rang B), avec les mécanismes explicites.
- **Au-delà du socle** : physiopathologie moléculaire, essais fondateurs, controverses, questions ouvertes. C'est ce niveau qui distingue une maîtrise réelle d'une préparation d'examen ; il ne doit pas être abordé avant le socle.

## Unités de contenu

- **Module** (`programme/`) : périmètre, contenu à maîtriser, items R2C, validation, sources candidates.
- **Leçon** (`lessons/NNN-nom/`, gabarit [`templates/lesson.md`](../templates/lesson.md)) : une notion transversale expliquée, avec figure et modèle quantitatif si utile. Exemple : [leçon 001](../lessons/001-passive-membrane/lesson.md).
- **Fiche maladie** (`programme/fiches/<module>/`, gabarit [`templates/fiche-maladie.md`](../templates/fiche-maladie.md)) : une maladie ou une situation clinique. Chaque fiche rédigée est déclarée dans la colonne `contenu` de [`r2c-items.csv`](r2c-items.csv), ce qui alimente le taux de couverture.

## Suivi de la couverture

```bash
python tools/r2c.py
```

Affiche le nombre d'items R2C disposant d'un contenu rédigé et signale toute incohérence (item sans module, module sans fichier, liste d'items non synchronisée). Après une modification de `r2c-items.csv` ou `modules.csv`, lancer `python tools/r2c.py sync`.

## Prochaines étapes de rédaction

1. Rédiger un test de positionnement pour la phase F.
2. Vérifier les sources candidates de chaque module et les enregistrer dans [`sources/references.md`](../sources/references.md).
3. Rédiger les premières fiches des items les plus fréquents en médecine générale.
4. Ajouter la liste officielle des situations de départ du R2C (entrées par symptôme) et la relier à M06.
