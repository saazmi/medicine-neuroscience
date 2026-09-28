# Qualité de l'information

*English version: [QUALITY.en.md](QUALITY.en.md).*

**La qualité exige des sources traçables, une précision explicite, des limites clairement posées et une compréhension vérifiable.** La complexité et la nouveauté ne sont pas, à elles seules, des critères de qualité.

## Exigences pour tout contenu

- Définir les objectifs d'apprentissage et les prérequis ; indiquer le niveau visé (socle, maîtrise, au-delà — voir le [programme](ROADMAP.md#niveaux-de-profondeur)).
- Rattacher chaque contenu clinique aux items R2C qu'il couvre ([`r2c-items.csv`](r2c-items.csv)) et aux bases qu'il mobilise (modules F, N, M).
- Utiliser manuels, référentiels des collèges d'enseignants et enseignements universitaires pour les bases établies.
- Situer une question de recherche à l'aide de synthèses (revues), puis examiner les études originales pour chaque affirmation expérimentale précise.
- Tracer le titre de la source, la section, le lien ou DOI, l'édition ou la date connue, et la date de vérification.
- Distinguer connaissances établies, modèles pédagogiques, affirmations débattues et questions ouvertes.
- Expliciter les hypothèses, conventions de signe, unités et conditions aux limites de chaque équation.
- Distinguer données simulées et mesures.
- Expliquer comment chaque représentation visuelle pourrait induire en erreur.
- Inclure rappel, interprétation d'images et de graphiques, questions de transfert et contrôle différé.
- Versionner les corrections dans Git et consigner l'erreur conceptuelle correspondante.

## Recommandations thérapeutiques

- Toute conduite thérapeutique cite l'organisme, le pays et l'année de la recommandation utilisée. Les recommandations diffèrent entre pays (le R2C s'appuie sur les recommandations françaises) et vieillissent : une fiche dont la recommandation a plus de cinq ans est à revérifier.
- Privilégier la compréhension des principes (mécanisme, bénéfice démontré, niveau de preuve) sur la mémorisation de posologies.
- Les ordonnances et conduites rédigées ici sont des exercices d'étude, jamais des instructions de soin.

## Limites des sources

Une explication produite avec l'IA reste un brouillon pédagogique à contrôler, pas une preuve indépendante. Une vérification bibliographique ne vaut pas validation par un enseignant. Les « sources candidates » citées dans les modules n'ont pas encore été vérifiées : elles ne doivent pas être citées comme preuve tant qu'elles ne figurent pas dans [`sources/references.md`](../sources/references.md) avec une date de vérification.

## Politique bilingue

Le français est la langue principale et la version de référence. Un fichier sans suffixe de langue est en français ; son équivalent anglais porte le suffixe `.en.md`. En cas de divergence, la version française fait foi et la version anglaise doit être corrigée.

Ont une version anglaise : le README, ce document, le programme et les leçons. Les deux versions partagent objectifs, notations, identifiants de sources et noms de fichiers des figures. Traduire le sens, pas seulement les mots. Un seul glossaire FR–EN sert de référence terminologique ; introduire le terme complet avant toute abréviation. Toute correction affectant le sens scientifique doit être reportée dans les deux langues. Les figures portent des libellés bilingues, français en premier.

Sont rédigés en français uniquement : les modules (`programme/`), les fiches maladie, les gabarits, les références et les journaux de suivi. Le glossaire fournit la terminologie anglaise correspondante.

## Rédaction et validation

Statuts de rédaction : `planned` (prévu), `draft` (brouillon), `source_checked` (sources contrôlées), `expert_reviewed` (relu par un expert). N'indiquer un relecteur et une date que si une relecture a réellement eu lieu. Le statut de rédaction des modules est tenu dans [`modules.csv`](modules.csv) ; tous sont actuellement `draft`. La leçon 001 est `source_checked`, pas `expert_reviewed`.

Statuts d'apprentissage, distincts : `not_started` (non commencé), `studying` (en cours), `assessed` (évalué), `retained` (retenu après contrôle différé). Ils sont tenus dans `progress/`.

Les valeurs de statut restent en anglais dans les fichiers CSV pour rester stables et faciles à filtrer.

## Critère de maîtrise

Lire ne prouve pas la maîtrise. Règle de progression personnelle : au moins 80 % aux questions inédites, aucune erreur conceptuelle centrale non résolue, une explication orale ou écrite réussie sans notes après un délai, et la réussite des tâches de la section « Validation du module ». C'est une règle d'étude, pas un seuil d'examen officiel.
