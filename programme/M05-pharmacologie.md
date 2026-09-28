# M05 — Pharmacologie générale et spéciale

**Phase M · Mécanismes de la maladie** · Prérequis : [F01](F01-mathematiques-statistiques.md), [F05](F05-biochimie-structurale.md), [N03](N03-physiologie-generale.md) · Réinvesti dans : T04, tous les modules C

Comment un médicament atteint sa cible, agit, est éliminé, interagit et nuit. La pharmacologie spéciale est organisée par classes ; la prescription en situation clinique relève de T04 et des modules C.

## Contenu

### 1. Pharmacocinétique
- Absorption : voies d'administration, biodisponibilité, effet de premier passage.
- Distribution : volume de distribution, liaison aux protéines plasmatiques, passage des barrières (hémato-encéphalique, placentaire), passage dans le lait.
- Métabolisme : réactions de phase I (cytochromes P450) et de phase II ; induction et inhibition enzymatiques ; métabolites actifs et toxiques ; prodrogues.
- Élimination : rénale (filtration, sécrétion, réabsorption), biliaire ; cycle entéro-hépatique.
- Paramètres : clairance, demi-vie, AUC, Cmax, Tmax ; état d'équilibre (≈ 5 demi-vies), dose de charge, dose d'entretien ; cinétiques d'ordre 0 et 1 ; modèles à un et deux compartiments.
- Suivi thérapeutique pharmacologique (aminosides, vancomycine, antiépileptiques, lithium, immunosuppresseurs, digoxine).

### 2. Pharmacodynamie
- Cibles : récepteurs, enzymes, canaux, transporteurs.
- Agonistes (entiers, partiels, inverses), antagonistes (compétitifs, non compétitifs) ; affinité, efficacité, puissance.
- Courbes dose-effet et concentration-effet (EC50, Emax, coefficient de Hill) ; courbes dose-réponse quantales ; index et marge thérapeutiques.
- Tolérance, tachyphylaxie, désensibilisation ; effet rebond et syndrome de sevrage.

### 3. Variabilité de la réponse
- Âges extrêmes (nouveau-né, enfant, sujet âgé), grossesse et allaitement.
- Insuffisance rénale, hépatique, cardiaque ; obésité ; dénutrition (hypoalbuminémie).
- Pharmacogénétique (→ M04).
- Interactions pharmacocinétiques (CYP3A4, CYP2D6, glycoprotéine P) et pharmacodynamiques (allongement du QT, syndrome sérotoninergique, hyperkaliémie, saignement, sédation).

### 4. Effets indésirables et vigilance
- Classification (dose-dépendants, immunoallergiques, retardés, tératogènes) ; iatrogénie ; imputabilité ; pharmacovigilance et addictovigilance (→ T04).

### 5. Développement du médicament
- Découverte, études précliniques, phases cliniques I à IV, autorisation de mise sur le marché, génériques, biosimilaires, médicaments orphelins.

### 6. Pharmacologie spéciale
Pour chaque classe : mécanisme, effets, indications principales, effets indésirables, contre-indications, interactions, surveillance.
- **Système nerveux autonome** : sympathomimétiques (adrénaline, noradrénaline, dobutamine, β2-agonistes), α- et β-bloquants, parasympathomimétiques, anticholinestérasiques, anticholinergiques, curares.
- **Cardiovasculaire** : diurétiques, IEC, ARA2, inhibiteurs de la néprilysine, antagonistes des minéralocorticoïdes, inhibiteurs calciques, dérivés nitrés, antiarythmiques (classification de Vaughan-Williams), digoxine, ivabradine, inhibiteurs de SGLT2, vasopresseurs et inotropes.
- **Hémostase** : antiagrégants plaquettaires (aspirine, inhibiteurs de P2Y12), héparines, antivitamines K, anticoagulants oraux directs, thrombolytiques, antidotes (protamine, vitamine K, idarucizumab, andexanet), acide tranexamique.
- **Lipides** : statines, ézétimibe, anti-PCSK9, fibrates.
- **Diabète** : metformine, sulfamides hypoglycémiants, inhibiteurs de la DPP-4, agonistes du GLP-1, inhibiteurs de SGLT2, insulines (analogues rapides et lents).
- **Douleur et inflammation** : paracétamol, AINS, opioïdes (agonistes, agonistes partiels, antagonistes : naloxone), glucocorticoïdes (effets, équivalences, sevrage), colchicine, hypo-uricémiants.
- **Système nerveux central** : antidépresseurs, anxiolytiques et hypnotiques, antipsychotiques, thymorégulateurs, psychostimulants, antiépileptiques, antiparkinsoniens, traitements de la démence, anesthésiques généraux et locaux, antimigraineux.
- **Digestif** : inhibiteurs de la pompe à protons, antiacides, antiémétiques, laxatifs, antidiarrhéiques, aminosalicylés.
- **Respiratoire** : bronchodilatateurs (β2-agonistes et anticholinergiques de courte et longue durée), corticoïdes inhalés, antileucotriènes, antihistaminiques.
- **Endocrinologie et reproduction** : hormones thyroïdiennes, antithyroïdiens de synthèse, contraceptifs hormonaux, traitement hormonal de la ménopause, analogues de la GnRH, bisphosphonates, dénosumab.
- **Anti-infectieux** : voir M02 et C07.
- **Anticancéreux** : cytotoxiques par mécanisme, hormonothérapies, thérapies ciblées, immunothérapies (→ C17).
- **Immunomodulateurs et biothérapies** (→ M01, C08).

### 7. Toxicologie générale
- Mécanismes de toxicité, relation dose-toxicité, toxidromes, principaux antidotes (→ C19).

## Au-delà du socle
- Pharmacométrie (modèles de population), pharmacologie quantitative des systèmes.
- Lecture des dossiers d'autorisation et des essais pivots.

## Items R2C

<!-- r2c:debut -->

*Liste générée par `python tools/r2c.py sync` — ne pas modifier à la main.*

**Items partagés (2), traités principalement ailleurs :**

- 322 — La décision thérapeutique personnalisée : bon usage dans des situations à risque *(principal : T04 Thérapeutique et bon usage du médicament)*
- 330 — Prescription et surveillance des classes de médicaments les plus courantes chez l'adulte et chez l'enfant, hors anti-infectieux (voir item 177). *(principal : T04 Thérapeutique et bon usage du médicament)*

<!-- r2c:fin -->

## Validation du module
- Calculer une dose de charge et une dose d'entretien à partir du volume de distribution, de la clairance et de la concentration cible.
- Prédire l'interaction clarithromycine–simvastatine et son risque (rhabdomyolyse).
- Expliquer l'hyperkaliémie sous IEC + spironolactone chez un insuffisant rénal.
- Pour vingt classes, réciter mécanisme, deux indications, trois effets indésirables majeurs et la surveillance.

## Sources candidates (non vérifiées)
- H. P. Rang, M. M. Dale et al., *Pharmacologie* (traduction française).
- Référentiel du Collège national de pharmacologie médicale.
