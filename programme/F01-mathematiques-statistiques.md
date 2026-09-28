# F01 — Mathématiques, probabilités et statistiques

**Phase F · Fondamentaux scientifiques** · Prérequis : aucun · Réinvesti dans : F02, M05, M07, T02, T03

Le médecin raisonne sous incertitude : probabilités diagnostiques, taille d'effet d'un traitement, cinétique d'un médicament. Ce module fournit les outils ; les modules T02 et T03 les appliquent. Avec une formation en mathématiques, faire le test de positionnement puis se concentrer sur les parties 5 à 7.

## Contenu

### 1. Outils d'analyse
- Fonctions exponentielle, logarithme (népérien, décimal), puissances ; échelles logarithmiques (pH, décibels, courbes dose-effet).
- Dérivées, intégrales ; aire sous la courbe (AUC en pharmacocinétique).
- Équations différentielles du premier ordre : décroissance exponentielle, demi-vie, modèle à un compartiment, charge d'un condensateur (leçon 001).
- Systèmes linéaires, notions d'algèbre linéaire (reconstruction d'images).
- Analyse dimensionnelle, ordres de grandeur, conversions d'unités (mmol/L ↔ mg/dL, mmHg ↔ kPa).
- Incertitudes de mesure, propagation d'erreurs, chiffres significatifs.
- Proportions, pourcentages, taux, rapports ; pièges (pourcentage de pourcentage, variation relative vs absolue).

### 2. Probabilités
- Axiomes, probabilité conditionnelle, indépendance, théorème de Bayes.
- Variables aléatoires discrètes et continues ; espérance, variance.
- Lois : Bernoulli, binomiale, Poisson, normale, log-normale, exponentielle ; lois dérivées (Student, χ², Fisher).
- Loi des grands nombres, théorème central limite.

### 3. Statistique descriptive
- Types de variables (qualitatives nominales/ordinales, quantitatives discrètes/continues).
- Position (moyenne, médiane, mode), dispersion (variance, écart-type, étendue, quartiles, écart interquartile), forme (asymétrie).
- Représentations : histogramme, boîte à moustaches, nuage de points, courbe de survie ; graphiques trompeurs.

### 4. Estimation
- Population, échantillon, fluctuation d'échantillonnage, estimateurs sans biais.
- Erreur standard vs écart-type.
- Intervalles de confiance d'une moyenne, d'une proportion, d'une différence, d'un rapport.
- Calcul du nombre de sujets nécessaire.

### 5. Tests statistiques
- Logique des tests : H0/H1, risque α, risque β, puissance, valeur p et ses mésinterprétations ; tests uni- et bilatéraux.
- Comparaison de moyennes : Student (indépendant, apparié), Welch, ANOVA ; comparaisons multiples (Bonferroni, taux de fausses découvertes).
- Comparaison de proportions : χ², test exact de Fisher, McNemar.
- Tests non paramétriques : Wilcoxon, Mann-Whitney, Kruskal-Wallis.
- Corrélation (Pearson, Spearman) ≠ causalité ; régression linéaire simple et multiple ; régression logistique (odds ratio ajusté).
- Analyse de survie : Kaplan-Meier, test du log-rank, modèle de Cox, hazard ratio, censure.
- Essais d'équivalence et de non-infériorité (marge).

### 6. Évaluation des tests diagnostiques
- Sensibilité, spécificité, valeurs prédictives positive et négative, dépendance à la prévalence.
- Rapports de vraisemblance, probabilité pré-test → post-test (Bayes, nomogramme de Fagan).
- Courbe ROC, aire sous la courbe, choix d'un seuil ; tests en série et en parallèle.
- Reproductibilité : coefficient kappa, Bland-Altman.

### 7. Mesures d'association et d'impact
- Risque, cote, risque relatif, odds ratio, différence de risque, NNT/NNH, fraction attribuable.
- Incidence, prévalence, taux standardisés (→ T02).

### 8. Outils pratiques
- Tableur ; bases de R ou Python (lecture de données, statistiques descriptives, un test, une courbe de survie).

## Au-delà du socle
- Inférence bayésienne (a priori, vraisemblance, a posteriori ; intervalles de crédibilité).
- Causalité : graphes acycliques orientés, facteurs de confusion, contrefactuels, appariement sur score de propension.
- Modèles mixtes, données répétées ; méta-analyse (effets fixes/aléatoires, hétérogénéité I², biais de publication).
- Apprentissage automatique : surapprentissage, validation, calibration d'un modèle prédictif.

## Items R2C

<!-- r2c:debut -->

*Liste générée par `python tools/r2c.py sync` — ne pas modifier à la main.*

Aucun item du R2C n'est rattaché directement à ce module : il fournit les bases que les items présupposent.

<!-- r2c:fin -->

## Validation du module
- Calculer la valeur prédictive positive d'un test (sensibilité 95 %, spécificité 95 %) pour une prévalence de 1 % (≈ 16 %) et expliquer le résultat à un patient.
- Pour dix scénarios d'étude, choisir et justifier le test statistique.
- Interpréter « HR = 0,75 (IC 95 % 0,62–0,91) » : sens, signification, pertinence clinique.
- Reproduire une courbe de Kaplan-Meier et un test du log-rank sur un jeu de données public.

## Sources candidates (non vérifiées)
- Cours de biostatistique de PASS/LAS d'une faculté de médecine francophone.
- J. Bouyer, *Méthodes statistiques. Médecine – Biologie*.
- *OpenIntro Statistics* (manuel libre, en anglais).
