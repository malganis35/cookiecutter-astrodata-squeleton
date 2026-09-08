"""Post-generation hook.

cookiecutter runs this with CWD = generated project directory (the `.claude/` folder).
`.mcp.json` doit vivre a la racine du projet (norme Claude Code), pas dans `.claude/`,
donc on le remonte d'un niveau.
"""

import shutil
import sys
from pathlib import Path

GENERATED_DIR = Path.cwd()               # .../<project>/.claude
PROJECT_ROOT = GENERATED_DIR.parent      # .../<project>

src = GENERATED_DIR / ".mcp.json"
dst = PROJECT_ROOT / ".mcp.json"

if not src.exists():
    sys.exit(0)

if dst.exists():
    print(f"[post_gen] {dst} existe deja : .mcp.json laisse dans {GENERATED_DIR.name}/ "
          f"pour eviter d'ecraser la config existante. Fusionne-le manuellement.")
    sys.exit(0)

shutil.move(str(src), str(dst))
print(f"[post_gen] .mcp.json deplace vers {dst}")
