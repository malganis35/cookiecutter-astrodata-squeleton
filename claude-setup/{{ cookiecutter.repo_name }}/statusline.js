#!/usr/bin/env node
/**
 * Claude Code status line (2 lignes), 100% champs natifs — aucune dépendance.
 *   L1: <branch> | <model> | <dir> | ctx [bar] NN% · used/size
 *   L2: quota | 5h [bar] NN% ↺HH:MM | 7d [bar] NN% ↺jeu 09:00   (si rate_limits présent)
 *
 * Données: https://code.claude.com/docs/en/statusline
 *   - context_window.{used_percentage,total_input_tokens,context_window_size}
 *   - rate_limits.{five_hour,seven_day,spend_limit}.{used_percentage,resets_at}
 *     -> Pro/Max uniquement, après la 1re réponse API ; chaque fenêtre peut manquer.
 *
 * Fuseau des heures de reset: CLAUDE_STATUSLINE_TZ (IANA), sinon fuseau système.
 */
const fs = require("fs");
const { execSync } = require("child_process");

let data = {};
try {
  data = JSON.parse(fs.readFileSync(0, "utf8") || "{}");
} catch {}

const TZ = process.env.CLAUDE_STATUSLINE_TZ || undefined;
const c = (code, s) => `\x1b[${code}m${s}\x1b[0m`;
const sep = c(2, " | ");

const fmt = (n) => {
  if (n == null || isNaN(n)) return "?";
  if (n >= 1_000_000) return (n / 1_000_000).toFixed(1).replace(/\.0$/, "") + "M";
  if (n >= 1_000) return Math.round(n / 1_000) + "k";
  return String(n);
};

// Barre de progression colorée: <50 vert, 50-75 jaune, >75 rouge.
const bar = (pct, width = 10) => {
  const p = Math.max(0, Math.min(100, Number(pct) || 0));
  const filled = Math.round((p / 100) * width);
  const col = p < 50 ? 32 : p <= 75 ? 33 : 31;
  return c(`1;${col}`, "█".repeat(filled)) + c(2, "░".repeat(width - filled));
};

// resets_at (epoch s) -> "HH:MM", ou "jeu 09:00" si > ~20h.
const fmtReset = (ts) => {
  if (!ts) return "";
  const d = new Date(ts * 1000);
  if (isNaN(d.getTime())) return "";
  const hm = d.toLocaleTimeString("fr-FR", {
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
    timeZone: TZ,
  });
  if (ts * 1000 - Date.now() > 20 * 3600 * 1000) {
    const wd = d
      .toLocaleDateString("fr-FR", { weekday: "short", timeZone: TZ })
      .replace(/\.$/, "");
    return `${wd} ${hm}`;
  }
  return hm;
};

// ---------- Ligne 1 ----------
const cwd = data.workspace?.current_dir || data.cwd || process.cwd();
const model = data.model?.display_name || "Claude";
const dirName = cwd.split(/[\\/]/).filter(Boolean).pop() || cwd;

let branch = "";
for (const opts of [{ cwd }, {}]) {
  try {
    branch = execSync("git --no-optional-locks rev-parse --abbrev-ref HEAD", {
      ...opts,
      stdio: ["ignore", "pipe", "ignore"],
    })
      .toString()
      .trim();
    if (branch) break;
  } catch {}
}

const cw = data.context_window || {};
let ctxSeg = "";
if (cw.used_percentage != null) {
  const pct = Math.round(cw.used_percentage);
  const col = pct < 50 ? 32 : pct <= 75 ? 33 : 31;
  const vol =
    cw.total_input_tokens != null && cw.context_window_size != null
      ? ` ${c(2, fmt(cw.total_input_tokens) + "/" + fmt(cw.context_window_size))}`
      : "";
  ctxSeg = `ctx [${bar(cw.used_percentage, 10)}] ${c(col, pct + "%")}${vol}`;
}

const line1 = [
  branch && c(36, branch),
  c(35, model),
  dirName,
  ctxSeg,
]
  .filter(Boolean)
  .join(sep);

// ---------- Ligne 2 (rate_limits) ----------
const rl = data.rate_limits || {};
const win = (label, o, width) => {
  if (!o || o.used_percentage == null) return null;
  const pct = Math.round(o.used_percentage);
  const col = pct < 50 ? 32 : pct <= 75 ? 33 : 31;
  const r = fmtReset(o.resets_at);
  return `${label} [${bar(o.used_percentage, width)}] ${c(col, pct + "%")}${r ? c(2, " ↺" + r) : ""}`;
};
const l2 = [
  win("5h", rl.five_hour, 8),
  win("7d", rl.seven_day, 8),
  win("$", rl.spend_limit, 8),
].filter(Boolean);
const line2 = l2.length ? [c("1;37", "quota"), ...l2].join(sep) : "";

process.stdout.write(line2 ? `${line1}\n${line2}` : line1);
