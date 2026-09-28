# X01 — Neurosciences approfondies

**Phase X · Approfondissement** · Prérequis : [N03](N03-physiologie-generale.md), [N05](N05-systeme-nerveux.md), [C10](C10-neurologie.md), [F01](F01-mathematiques-statistiques.md) · Modules liés : C11

Extension au-delà du médecin généraliste, fidèle à l'objectif initial du dépôt : comprendre le système nerveux jusqu'au niveau de la recherche. À aborder après le socle médical correspondant (N05, C10, C11), pas à sa place.

## Contenu

### 1. Neurobiologie cellulaire et moléculaire
- Biophysique des canaux ioniques ; excitabilité dendritique ; transmission synaptique quantique ; plasticité synaptique et homéostatique ; glie et neuro-immunologie.

### 2. Neurosciences des systèmes
- Vision (codage dans le cortex visuel), motricité (planification, apprentissage moteur, cervelet), mémoire (hippocampe, consolidation), décision et récompense (dopamine, erreur de prédiction), émotions, sommeil.

### 3. Neurosciences computationnelles
- Modèles de neurones : membrane passive ([leçon 001](../lessons/001-passive-membrane/lesson.md)), intègre-et-tire, Hodgkin-Huxley, modèles réduits ; théorie du câble.
- Réseaux : dynamique, attracteurs, oscillations ; codage neuronal (taux, temporel, populationnel) ; théorie de l'information ; apprentissage (règles hebbiennes, apprentissage par renforcement).

### 4. Méthodes
- Électrophysiologie (patch-clamp, enregistrements extracellulaires), imagerie calcique, optogénétique, IRM fonctionnelle, EEG/MEG ; analyse des données (tri des potentiels d'action, statistiques, décodage).

### 5. Neurosciences cliniques et translationnelles
- Biomarqueurs des maladies neurodégénératives ; neuromodulation (stimulation cérébrale profonde, stimulation magnétique transcrânienne) ; interfaces cerveau-machine ; psychiatrie computationnelle.

### 6. Lecture de la recherche
- Articles fondateurs et revues récentes ; reproduction d'un résultat publié avec code ouvert.

## Au-delà du socle
- Ce module est lui-même un approfondissement : définir un projet de recherche personnel reproductible.

## Items R2C

<!-- r2c:debut -->

*Liste générée par `python tools/r2c.py sync` — ne pas modifier à la main.*

Aucun item du R2C n'est rattaché directement à ce module : il fournit les bases que les items présupposent.

<!-- r2c:fin -->

## Validation du module
- Implémenter un modèle de Hodgkin-Huxley et reproduire le seuil et la période réfractaire.
- Reproduire la figure principale d'un article de neurosciences computationnelles à partir de son code ou de ses données.

## Leçons rédigées
- [001 — Membrane passive](../lessons/001-passive-membrane/lesson.md)

## Sources candidates
- S1, S2 (*Neuronal Dynamics*), S7 (Bear et al.), S8 (Neuromatch) — voir [références](../sources/references.md).
- E. R. Kandel et al., *Principles of Neural Science* (non vérifié).
