# CleanMatch ✨

[![CI](https://github.com/malganis35/dedup-lens/actions/workflows/ci.yml/badge.svg)](https://github.com/malganis35/dedup-lens/actions)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![CleanMatch Logo](docs/cleanmatch.png)

## Description
CleanMatch est un outil intelligent de dédoublonnage de bases de données tiers (fournisseurs, clients). Il utilise des algorithmes de similarité textuelle floue pour identifier les doublons potentiels malgré les fautes de frappe, les abréviations juridiques ou les différences de casse, permettant ainsi de nettoyer vos catalogues de données rapidement et avec une revue humaine sécurisée.

## 🚀 Features
- **Normalisation avancée** : Suppression automatique des accents, ponctuations, standardisation des abréviations et des suffixes légaux (SARL, SAS, etc.).
- **Blocking Multi-Clés** : Indexation hybride (littérale, phonétique Metaphone/Soundex, et préfixes) pour garantir un recall élevé même avec des fautes de frappe sévères.
- **Filtrage Sémantique** : Exclusion intelligente des mots vides business (SOCIETE, GROUPE, LES) pour éviter les blocs géants.
- **Interface Scalable** : Pagination native de la revue pour traiter des milliers de clusters sans ralentissement.
- **Audit & Logs** : Système de logging permanent avec rotation et compression pour le debug en production.
- **Conformité Enterprise** : Hachage technique (MD5) compatible avec les systèmes en mode FIPS.
- **Export Excel** : Génération de fichiers de correction et de datasets enrichis avec retour visuel (couleurs).
- **Modèle Freemium** : Prêt pour le déploiement public avec limitation automatique des ressources.
- **Mode PRO** : Activation d'une version illimitée via une simple variable d'environnement.

## 🏗️ Architecture
Le pipeline de traitement suit un flux logique modulaire. Pour une explication détaillée des algorithmes et des stratégies de dédoublonnage, consultez le fichier **[ARCHITECTURE.md](ARCHITECTURE.md)**.

```text
[Données Brutes] --> [Normalisation] --> [Blocking (Indexation)]
                          |                      |
                          v                      v
                  [Calcul de Score] <--- [Paires candidates]
                          |
                          v
                  [Clustering (Union-Find)] --> [Review UI] --> [Export Final]
```

## 🛠️ Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-compte/cleanmatch.git
cd cleanmatch
```

2. Installez les dépendances avec [uv](https://github.com/astral-sh/uv) :
```bash
uv sync
```

3. Lancez l'application :
```bash
make run
```

## 📖 Usage Pas-à-pas

1. **Upload** : Chargez votre fichier CSV ou Excel dans le premier onglet. Sélectionnez la colonne contenant les noms à traiter.
2. **Review** : Naviguez dans l'onglet "Revue & Validation" pour traiter les clusters détectés. Utilisez la **pagination** pour parcourir de gros volumes d'erreurs.
3. **Export** : Téléchargez vos résultats sous forme de mappings de correction stylisés.

> [!TIP]
> Utilisez le curseur de "Seuil de similarité" pour ajuster la sensibilité. Un seuil de 50.0 est le nouveau défaut pour maximiser le rappel initial.

## 🎁 Freemium & PRO Mode

CleanMatch est conçu pour être partagé publiquement (ex: LinkedIn) tout en restant un outil professionnel puissant.

- **Version Free (Défaut)** :
    - Limitée aux **100 premières lignes** du fichier uploadé.
    - Mode "Exhaustif" $O(N^2)$ désactivé pour protéger les ressources serveur.
    - Note de confidentialité RGPD intégrée.
- **Mode PRO (Plein)** :
    - Aucune limite de lignes.
    - Accès complet aux options avancées (mode exhaustif).
    - Suppression des avertissements et disclaimers freemium.

### Activer le Mode PRO
Définissez la variable d'environnement suivante avant de lancer l'application :
```bash
export CLEANMATCH_PRO_MODE=True
make run
```

## ⚙️ Configuration
Le moteur utilise plusieurs constantes modifiables dans `src/cleanmatch/constants.py` :
- `DEFAULT_SIMILARITY_THRESHOLD` : Seuil par défaut (50.0).
- `LEGAL_SUFFIXES` : Liste des formes juridiques à ignorer.
- `STOP_WORDS` : Mots vides à ignorer lors de la création des blocs (SOCIETE, GROUPE...).
- `ABBREVIATIONS` : Dictionnaire de normalisation (ST -> SAINT, CIE -> COMPAGNIE).
- `SCORING_WEIGHTS` : Pondération entre Ratio, Token Sort et Token Set.
- `MAX_FREE_ROWS` : Limite de la version gratuite (défaut : 100).
- `CLEANMATCH_PRO_MODE` : Variable d'environnement pour basculer en version illimitée.

## 👨‍💻 Développement

Pour contribuer au projet :

1. Initialisez l'environnement de développement :
```bash
make dev
```

2. Vérifiez la qualité du code (Lint/Type/Test) :
```bash
make all
```

3. Lancez les tests rapidement :
```bash
make test-fast
```

## 🤝 Contribution
1. Créez une branche (`git checkout -b feature/ma-feature`).
2. Utilisez des **Conventional Commits** (`feat:`, `fix:`, `docs:`, etc.).
3. Vérifiez que `make check` passe à 100%.
4. Ouvrez une Pull Request.

## 📄 License
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
