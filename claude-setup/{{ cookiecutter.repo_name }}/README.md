# Configuration Claude Code de ce projet

Ce dossier `.claude/` configure le comportement de [Claude Code](https://code.claude.com/docs)
quand tu ouvres ce projet. Ce README explique **chaque fichier**, à quoi il sert, et ce
qu'il faut savoir pour démarrer.

> Si tu débutes : tu n'as **rien à installer ni configurer** pour commencer. Lance
> `claude` à la racine du projet, accepte les quelques demandes d'autorisation au
> premier lancement, et c'est parti. Le reste de ce document explique ce qui tourne
> en coulisses.

---

## Prérequis

| Outil | Pourquoi | Vérifier |
|---|---|---|
| [`uv`](https://docs.astral.sh/uv/) | gestion des dépendances et exécution (`uv run …`) | `uv --version` |
| [Node.js](https://nodejs.org) | la status line et le hook de formatage sont des scripts Node (zéro dépendance npm) | `node --version` |
| `git` | Claude s'appuie dessus pour voir les changements | `git --version` |

`ruff` (formatage / lint) est installé automatiquement via `uv` — il est dans les
dépendances de dev du projet.

---

## Les deux fichiers de réglages

Claude Code lit **deux** fichiers de réglages, fusionnés :

| Fichier | Portée | Versionné (git) | Contenu |
|---|---|---|---|
| `settings.json` | **partagé** — tout le monde sur le projet | ✅ oui | garde-fous d'équipe : permissions, hook de formatage |
| `settings.local.json` | **perso** — toi, sur cette machine | ❌ non (dans `.gitignore`) | tes préférences : mode par défaut, status line, notifications |

En cas de conflit, `settings.local.json` gagne.

### `settings.json` (partagé)

**Permissions** — Claude demande une autorisation avant chaque action sensible. Ce
fichier pré-règle certains cas :

- `allow` : commandes sûres et fréquentes exécutées **sans demander**
  (`uv sync`, `uv run pytest`, `uv run ruff …`, `git status/diff/log/show/branch`).
- `ask` : toujours **demander confirmation**, même si une règle plus large autorisait
  (`git rebase`, `git reset` — ça réécrit l'historique).
- `deny` : **interdit**, Claude ne peut pas le faire
  (`rm -rf`, `git push`, `pip install`, lecture/écriture de `.env`, lecture de `*.pem`).

> `git push` est bloqué : c'est volontaire pour ce projet. Tu pousses toi-même, à la
> main, en connaissance de cause.

**Hook `PostToolUse`** — après chaque modification de fichier par Claude, lance
`.claude/hooks/ruff-format.js` (voir plus bas).

### `settings.local.json` (perso)

Créé pour toi avec des valeurs utiles quand on débute. Tu peux tout changer.

| Clé | Effet |
|---|---|
| `permissions.defaultMode: "plan"` | chaque session démarre en **mode plan** : Claude explore et propose un plan **sans rien modifier** tant que tu n'as pas validé. Tu en sors avec `Shift+Tab`. Idéal pour apprendre. |
| `permissions.allow` / `ask` | tes autorisations perso, en plus de celles du fichier partagé |
| `enabledMcpjsonServers` | serveurs MCP (voir `.mcp.json`) que tu pré-approuves, pour éviter le prompt au démarrage |
| `preferredNotifChannel: "terminal_bell"` | un « bip » quand Claude a fini ou attend ta réponse |
| `includeCoAuthoredBy: true` | ajoute une ligne `Co-Authored-By: Claude` dans les commits créés par Claude |
| `cleanupPeriodDays: 30` | durée de conservation locale de l'historique des conversations |
| `statusLine` | active la barre d'état personnalisée (voir plus bas) |

---

## `statusline.js` — la barre d'état

Affiche deux lignes en bas de Claude Code :

```
main | Sonnet 5 | lab-claude | ctx [█░░░░░░░░░] 13% 131k/1M
quota | 5h [██░░░░░░] 24% ↺13:55 | 7d [██████░░] 78% ↺ven 23:19
```

- **Ligne 1** : branche git · modèle · dossier · **remplissage de la fenêtre de
  contexte** (barre + % + tokens utilisés / taille max). Vert < 50 %, jaune ≤ 75 %,
  rouge au-delà.
- **Ligne 2** : **quotas d'abonnement** Claude (fenêtre 5 h et fenêtre 7 jours) avec
  l'heure de réinitialisation. N'apparaît que pour les abonnés Pro/Max, et seulement
  après la première réponse de Claude dans la session.

100 % basé sur les données que Claude Code fournit nativement — **aucune dépendance,
aucun appel réseau**. Fuseau horaire des heures de reset : variable d'environnement
`CLAUDE_STATUSLINE_TZ` (ex. `Europe/Paris`), sinon celui du système.

---

## `hooks/ruff-format.js` — formatage automatique

Après chaque fois que Claude crée ou modifie un fichier `.py`, ce script lance
`ruff check --fix` puis `ruff format` sur ce fichier.

Résultat : le code est **toujours propre**, et tu ne relis jamais un diff pollué par
des questions de style. Les corrections sûres de `ruff` (imports inutiles, etc.) sont
appliquées silencieusement — tu les vois dans le diff.

Si `ruff` échoue, le hook ne bloque rien : il affiche juste un avertissement.

---

## `agents/code-quality-reviewer.md` — sous-agent de revue

Un « sous-agent » spécialisé que Claude peut lancer (ou que tu peux invoquer) pour
**relire les changements récents** : bugs, sécurité, robustesse API, maintenabilité,
couverture de tests. Il ne modifie rien, il rend un rapport classé par sévérité
(🔴 bloquant / 🟡 à corriger / 🟢 suggestions).

À comparer avec la commande intégrée `/code-review`, plus puissante — cet agent est
surtout là comme exemple de checklist sur-mesure.

---

## `skills/pr-description/SKILL.md` — modèle de description de PR

Une « skill » : un mode d'emploi que Claude charge tout seul quand c'est pertinent
(ici : quand tu demandes de rédiger une description de pull request). Elle impose un
format `What / Why / Changes` à partir du `git diff`.

Invocation explicite possible : `/pr-description`.

---

## `.mcp.json` (à la racine du projet, pas dans `.claude/`)

Déclare les serveurs [MCP](https://code.claude.com/docs/en/mcp) — des outils externes
que Claude peut utiliser :

| Serveur | Usage |
|---|---|
| `playwright` | piloter un navigateur (tests end-to-end, captures d'écran) |
| `powerbi-modeling-mcp` | manipuler un modèle Power BI / Tabular (nécessite .NET + un modèle ouvert ou un endpoint XMLA) |

**Au premier lancement**, Claude Code te demande si tu fais confiance à ces serveurs.
Pour ne plus être sollicité, ajoute leur nom dans `enabledMcpjsonServers` de ton
`settings.local.json`.

---

## Bien démarrer

1. `claude` à la racine du projet.
2. Au premier lancement, accepte : les **hooks**, les **serveurs MCP**, et la
   **status line** (Claude Code demande une validation par sécurité).
3. La session démarre en **mode plan** : décris ta tâche, lis le plan proposé,
   valide-le pour que Claude passe à l'action.

### Gotchas

- **Un changement dans `settings.json` / `settings.local.json` n'est pris en compte
  qu'au redémarrage** de `claude`.
- La **ligne 2 de la status line** (quotas) est vide tant que tu n'as pas envoyé au
  moins un message dans la session, et si tu n'es pas abonné Pro/Max.
- Le **quota hebdomadaire exact** n'est visible qu'avec la commande `/usage`.
- `powerbi-modeling-mcp` démarre même sans modèle Power BI ouvert, mais ne pourra
  rien faire — c'est normal.

### Commandes utiles

| Commande | Effet |
|---|---|
| `/help` | aide générale |
| `/permissions` | voir / modifier les autorisations |
| `/mcp` | état des serveurs MCP |
| `/usage` | consommation détaillée de ton abonnement |
| `/code-review` | revue de code approfondie |
| `Shift+Tab` | changer de mode (plan / normal / auto-accept) |
