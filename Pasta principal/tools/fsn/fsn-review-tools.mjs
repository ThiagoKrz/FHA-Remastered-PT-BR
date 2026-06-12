#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";

const ROOT = process.cwd();
const DIRS = {
  en: path.join(ROOT, "scripts_EN"),
  pt: path.join(ROOT, "scripts_PT-BR"),
  jp: path.join(ROOT, "scripts_JP"),
};
const GLOSSARY_PATH = path.join(
  ROOT,
  "standards",
  "type-moon",
  "GLOSSARIO_TYPEMOON_OPERACIONAL.json",
);

const ROW_RE = /^(\d+)::(\$\$\$[^$]+\$\$\$)::(.*)::$/;
const TAG_RE = /\[[^\]]+\]/g;
const JP_RE = /[ぁ-ゟ゠-ヿ一-龯]/;
const BAD_CHAR_RE = /�|[\x00-\x08\x0B\x0C\x0E-\x1F]/;
const MOJIBAKE_RE = /Ã|Â/;
const JAPANESE_QUOTES_RE = /[「」『』]/;

const COMMON_EN = new Set(
  [
    "the",
    "and",
    "that",
    "this",
    "you",
    "your",
    "with",
    "have",
    "will",
    "can",
    "could",
    "would",
    "should",
    "there",
    "here",
    "what",
    "when",
    "where",
    "why",
    "how",
    "from",
    "about",
    "into",
    "like",
    "just",
    "only",
    "even",
    "then",
    "now",
    "not",
    "but",
    "for",
    "are",
    "was",
    "were",
    "has",
    "had",
    "his",
    "her",
    "him",
    "she",
    "they",
    "them",
    "their",
    "all",
    "one",
    "two",
    "more",
    "less",
    "going",
    "think",
    "know",
    "because",
  ].join(" ").split(/\s+/),
);

const LORE_CASE_RE =
  /\b(servant|servants|servo|servos|master|masters|mestre|mestres|holy grail|santo graal|guerra do santo graal|noble phantasm|fantasma nobre|fantasmas nobres|true name|nome verdadeiro|command spell|command spells|command seal|command seals|selo de comando|selos de comando|heroic spirit|esp[ií]rito heroico|esp[ií]ritos heroicos|bounded field|campo limitado)\b/i;

const WATCH_TERMS = [
  "Alteration",
  "Angra Mainyu",
  "Avalon",
  "Azoth Blade",
  "Black Shadow",
  "Blood Fort Andromeda",
  "Caliburn",
  "Caster's Master",
  "Crest Worm",
  "Dress of Heaven",
  "Ea",
  "Einzbern Castle",
  "Excalibur",
  "Fuyuki City",
  "Gae Bolg",
  "Gate of Babylon",
  "Greater Grail",
  "Heaven's Feel",
  "Holy Church",
  "Holy Shroud",
  "Jeweled Sword",
  "Kanshou",
  "Kanshou and Bakuya",
  "Kirei Kotomine",
  "Leyline",
  "Lesser Grail",
  "Magic Circuit",
  "Magic Circuits",
  "Magic Crest",
  "Magic Energy",
  "Magic Resistance",
  "Matou Family",
  "Matou Zouken",
  "Medea",
  "Medusa",
  "Moonfall",
  "Prana",
  "Projection",
  "Projection magecraft",
  "Reinforcement",
  "Reality Marble",
  "Rho Aias",
  "Rule Breaker",
  "Ryuudou Temple",
  "Shadow",
  "Strengthening",
  "Supernal Disassembler",
  "Third Dress",
  "Third Magic",
  "Tohsaka Family",
  "Trace",
  "Unlimited Blade Works",
  "Zelretch",
];

const CASE_SENSITIVE_WATCH = new Set(["Trace"]);

const TERM_KEYWORDS = [
  "Alteration",
  "Andromeda",
  "Angra",
  "Association",
  "Avalon",
  "Azoth",
  "Babylon",
  "Bakuya",
  "Blade",
  "Blood",
  "Bolg",
  "Bounded",
  "Breaker",
  "Caliburn",
  "Castle",
  "Church",
  "Circuit",
  "Circuits",
  "Command",
  "Crest",
  "Dress",
  "Ea",
  "Einzbern",
  "Energy",
  "Excalibur",
  "Feel",
  "Field",
  "Fort",
  "Fuyuki",
  "Gae",
  "Gate",
  "Grail",
  "Heaven",
  "Heroic",
  "Holy",
  "Kanshou",
  "Leyline",
  "Magic",
  "Magecraft",
  "Mainyu",
  "Marble",
  "Matou",
  "Moonfall",
  "Noble",
  "Phantasm",
  "Prana",
  "Projection",
  "Reality",
  "Reinforcement",
  "Resistance",
  "Rho",
  "Rule",
  "Ryuudou",
  "Shadow",
  "Shroud",
  "Spirit",
  "Strengthening",
  "Sword",
  "Third",
  "Trace",
  "Unlimited",
  "Works",
  "Zelretch",
];

const ALLOWED_SINGLE_TERMS = new Set([
  "Alteration",
  "Association",
  "Avalon",
  "Caliburn",
  "Church",
  "Ea",
  "Excalibur",
  "Grail",
  "Leyline",
  "Moonfall",
  "Prana",
  "Projection",
  "Shadow",
  "Strengthening",
  "Trace",
  "Zelretch",
]);

function usage() {
  console.log(`Uso:
  node tools/fsn/fsn-review-tools.mjs scene <arquivo.epk_dec> [--max N]
  node tools/fsn/fsn-review-tools.mjs terms [--top N] [--min N]

Exemplos:
  node tools/fsn/fsn-review-tools.mjs scene 2ismqb2mflbv9ci88imeh44msr.epk_dec
  node tools/fsn/fsn-review-tools.mjs terms --top 80 --min 2`);
}

function fileExists(filePath) {
  try {
    return fs.statSync(filePath).isFile();
  } catch {
    return false;
  }
}

function readFile(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function parseDat(filePath) {
  if (!fileExists(filePath)) {
    return { exists: false, filePath, header: [], rows: [], errors: [] };
  }

  const text = readFile(filePath);
  const lines = text.split(/\r?\n/);
  const header = lines.slice(0, 2);
  const rows = [];
  const errors = [];

  if (header[0] !== "DAT") {
    errors.push(`Linha 1 esperada: DAT; encontrada: ${header[0] ?? "<vazia>"}`);
  }
  if (header[1] !== "id=qid::label=str::text=lstr::") {
    errors.push(
      `Linha 2 esperada: id=qid::label=str::text=lstr::; encontrada: ${
        header[1] ?? "<vazia>"
      }`,
    );
  }

  for (let index = 2; index < lines.length; index += 1) {
    const raw = lines[index];
    if (!raw || !raw.trim()) continue;
    const match = raw.match(ROW_RE);
    const textPart = match?.[3] ?? "";
    const tags = [...raw.matchAll(TAG_RE)].map((m) => m[0]);
    rows.push({
      lineNo: index + 1,
      raw,
      valid: Boolean(match),
      id: match?.[1] ?? null,
      label: match?.[2] ?? null,
      text: textPart,
      visible: stripTags(textPart).trim(),
      tags,
    });
  }

  for (const row of rows) {
    if (!row.valid) {
      errors.push(`Linha ${row.lineNo} malformada`);
    }
  }

  return { exists: true, filePath, header, rows, errors };
}

function stripTags(text) {
  return text.replace(TAG_RE, "");
}

function tagsKey(row) {
  return row.tags.join("|");
}

function normalizeSpaces(text) {
  return text.replace(/\s+/g, " ").trim();
}

function englishScore(text) {
  const tokens = text
    .toLowerCase()
    .match(/[a-z][a-z']+/g);
  if (!tokens || tokens.length < 4) return 0;
  const hits = tokens.filter((token) => COMMON_EN.has(token)).length;
  return hits / tokens.length;
}

function isEnglishish(text) {
  if (/[A-Za-z]+n't\b|I'm\b|you're\b|You\b.*\bthe\b/.test(text)) return true;
  const score = englishScore(text);
  return score >= 0.26 && /[A-Za-z]{2}/.test(text);
}

function rowByLabel(rows) {
  const map = new Map();
  for (const row of rows) {
    if (row.label && !map.has(row.label)) map.set(row.label, row);
  }
  return map;
}

function truncate(text, size = 150) {
  const clean = normalizeSpaces(text);
  if (clean.length <= size) return clean;
  return `${clean.slice(0, size - 1)}…`;
}

function compareRowsByLabel(pt, en) {
  const ptMap = rowByLabel(pt.rows);
  const enMap = rowByLabel(en.rows);
  const missingInPt = [];
  const extraInPt = [];
  const shared = [];

  for (const row of en.rows) {
    if (!row.label) continue;
    const match = ptMap.get(row.label);
    if (!match) missingInPt.push(row);
    else shared.push([match, row]);
  }
  for (const row of pt.rows) {
    if (!row.label) continue;
    if (!enMap.has(row.label)) extraInPt.push(row);
  }

  return { ptMap, enMap, missingInPt, extraInPt, shared };
}

function analyzeScene(fileName, maxItems = 30) {
  const paths = {
    pt: path.join(DIRS.pt, fileName),
    en: path.join(DIRS.en, fileName),
    jp: path.join(DIRS.jp, fileName),
  };

  const pt = parseDat(paths.pt);
  const en = parseDat(paths.en);
  const jp = parseDat(paths.jp);
  const issues = [];

  if (!pt.exists) issues.push("Arquivo PT-BR ausente.");
  if (!en.exists) issues.push("Arquivo EN ausente.");
  if (!jp.exists) issues.push("Arquivo JP ausente.");
  for (const err of pt.errors) issues.push(`PT-BR: ${err}`);
  for (const err of en.errors) issues.push(`EN: ${err}`);

  let structural = null;
  let suspicious = [];
  let sameIndexMismatch = [];

  if (pt.exists && en.exists) {
    structural = compareRowsByLabel(pt, en);

    const minRows = Math.min(pt.rows.length, en.rows.length);
    for (let i = 0; i < minRows; i += 1) {
      const ptRow = pt.rows[i];
      const enRow = en.rows[i];
      if (ptRow.label !== enRow.label || ptRow.id !== enRow.id) {
        sameIndexMismatch.push({
          index: i + 1,
          pt: ptRow,
          en: enRow,
        });
      }
    }

    for (const [ptRow, enRow] of structural.shared) {
      const reasons = [];
      if (tagsKey(ptRow) !== tagsKey(enRow)) reasons.push("tags divergentes");
      if (/\[l\]\[r\]/.test(ptRow.text)) reasons.push("[l][r] provável bug");
      if (BAD_CHAR_RE.test(ptRow.raw)) reasons.push("byte/lixo ou �");
      if (MOJIBAKE_RE.test(ptRow.raw)) reasons.push("mojibake provável");
      if (JAPANESE_QUOTES_RE.test(ptRow.raw)) reasons.push("aspas japonesas");
      if (JP_RE.test(stripTags(ptRow.text))) reasons.push("japonês fora de tag");
      if (isEnglishish(ptRow.visible)) reasons.push("PT parece inglês");
      if (LORE_CASE_RE.test(ptRow.visible)) reasons.push("termo de lore/capitalização para revisar");

      const ptLen = ptRow.visible.length;
      const enLen = enRow.visible.length;
      if (enLen >= 25 && ptLen > 0) {
        const ratio = ptLen / enLen;
        if (ratio < 0.22 || ratio > 3.4) reasons.push(`tamanho suspeito (${ratio.toFixed(2)}x)`);
      }
      if (enLen >= 10 && ptLen === 0) reasons.push("PT vazio com EN preenchido");

      if (reasons.length) {
        suspicious.push({ pt: ptRow, en: enRow, reasons });
      }
    }
  }

  const classification = classifyScene(pt, en, structural, sameIndexMismatch, suspicious);
  return {
    fileName,
    pt,
    en,
    jp,
    classification,
    issues,
    structural,
    sameIndexMismatch: sameIndexMismatch.slice(0, maxItems),
    sameIndexMismatchTotal: sameIndexMismatch.length,
    suspicious: suspicious.slice(0, maxItems),
    suspiciousTotal: suspicious.length,
  };
}

function classifyScene(pt, en, structural, sameIndexMismatch, suspicious) {
  if (!pt.exists || !en.exists) return "BLOQUEADO: arquivo de referência ausente";
  if (pt.errors.length || en.errors.length) return "BUG ESTRUTURAL: cabeçalho ou linhas malformadas";
  if (
    pt.rows.length !== en.rows.length ||
    structural?.missingInPt.length ||
    structural?.extraInPt.length ||
    sameIndexMismatch.length
  ) {
    return "DESSYNC: revisar/remapear antes de traduzir";
  }
  if (suspicious.length) return "REVISÃO PONTUAL: estrutura bate, mas há linhas suspeitas";
  return "OK ESTRUTURAL: pronto para revisão literária";
}

function printSceneReport(report) {
  const { fileName, pt, en, jp, structural } = report;
  console.log(`Arquivo: ${fileName}`);
  console.log(`Status: ${report.classification}`);
  console.log("");
  console.log(`Linhas: PT-BR ${pt.rows.length} | EN ${en.rows.length} | JP ${jp.rows.length}`);
  console.log(`Existe: PT-BR ${pt.exists ? "sim" : "não"} | EN ${en.exists ? "sim" : "não"} | JP ${jp.exists ? "sim" : "não"}`);
  console.log("");

  if (report.issues.length) {
    console.log("Problemas estruturais:");
    for (const issue of report.issues) console.log(`- ${issue}`);
    console.log("");
  }

  if (structural) {
    console.log("Sincronia por label:");
    console.log(`- Ausentes no PT-BR: ${structural.missingInPt.length}`);
    console.log(`- Extras no PT-BR: ${structural.extraInPt.length}`);
    console.log(`- Fora da mesma posição por id/label: ${report.sameIndexMismatchTotal}`);
    console.log("");

    if (structural.missingInPt.length) {
      console.log("Primeiros labels ausentes no PT-BR:");
      for (const row of structural.missingInPt.slice(0, 12)) {
        console.log(`- ${row.label} | EN linha ${row.lineNo}: ${truncate(row.visible)}`);
      }
      console.log("");
    }

    if (structural.extraInPt.length) {
      console.log("Primeiros labels extras no PT-BR:");
      for (const row of structural.extraInPt.slice(0, 12)) {
        console.log(`- ${row.label} | PT linha ${row.lineNo}: ${truncate(row.visible)}`);
      }
      console.log("");
    }
  }

  if (report.sameIndexMismatch.length) {
    console.log("Primeiras quebras de ordem/conteúdo por posição:");
    for (const item of report.sameIndexMismatch) {
      console.log(`- Posição ${item.index}`);
      console.log(`  EN ${item.en.label} linha ${item.en.lineNo}: ${truncate(item.en.visible)}`);
      console.log(`  PT ${item.pt.label} linha ${item.pt.lineNo}: ${truncate(item.pt.visible)}`);
    }
    console.log("");
  }

  if (report.suspicious.length) {
    console.log(`Linhas suspeitas (${report.suspiciousTotal} total):`);
    for (const item of report.suspicious) {
      console.log(`- ${item.pt.label} | PT linha ${item.pt.lineNo} | ${item.reasons.join(", ")}`);
      console.log(`  EN: ${truncate(item.en.visible)}`);
      console.log(`  PT: ${truncate(item.pt.visible)}`);
    }
    console.log("");
  }

  console.log("Recomendação:");
  if (report.classification.startsWith("DESSYNC")) {
    console.log("- Usar o EN como esqueleto canônico e remapear a cena antes de revisar o texto.");
  } else if (report.classification.startsWith("BUG ESTRUTURAL")) {
    console.log("- Corrigir cabeçalho/linhas malformadas antes de qualquer revisão literária.");
  } else if (report.classification.startsWith("REVISÃO PONTUAL")) {
    console.log("- Corrigir apenas as linhas suspeitas, comparando EN e JP quando o sentido estiver duvidoso.");
  } else {
    console.log("- Seguir para revisão literária e aplicação fina do glossário.");
  }
}

function flattenGlossaryTerms() {
  const raw = readFile(GLOSSARY_PATH);
  const glossary = JSON.parse(raw);
  const keys = new Set();
  const values = new Set();
  for (const [section, entries] of Object.entries(glossary)) {
    if (!section.startsWith("glossario_") && section !== "aliases_de_faccao_por_personagem") continue;
    if (!entries || typeof entries !== "object" || Array.isArray(entries)) continue;
    for (const [key, value] of Object.entries(entries)) {
      keys.add(key.toLowerCase());
      if (typeof value === "string") values.add(value.toLowerCase());
    }
  }
  return { keys, values };
}

function listFiles(dir) {
  return fs.readdirSync(dir).filter((name) => name.endsWith(".epk_dec")).sort();
}

function extractVisibleRows(dir) {
  const rows = [];
  for (const file of listFiles(dir)) {
    const parsed = parseDat(path.join(dir, file));
    for (const row of parsed.rows) {
      rows.push({ file, ...row });
    }
  }
  return rows;
}

function containsGlossaryTerm(term, glossary) {
  const lower = normalizeCandidate(term).toLowerCase();
  if (glossary.keys.has(lower) || glossary.values.has(lower)) return true;
  if (lower.endsWith("s") && glossary.keys.has(lower.slice(0, -1))) return true;
  const possessive = lower.match(/^[a-z][a-z'’ -]+?'s (.+)$/);
  if (possessive && glossary.keys.has(possessive[1])) return true;
  return false;
}

function addCandidate(candidates, term, row) {
  const clean = normalizeCandidate(term);
  if (!clean || clean.length < 3) return;
  if (!candidates.has(clean)) {
    candidates.set(clean, { term: clean, count: 0, examples: [], seen: new Set() });
  }
  const entry = candidates.get(clean);
  const seenKey = `${row.file}:${row.lineNo}:${row.label}`;
  if (entry.seen.has(seenKey)) return;
  entry.seen.add(seenKey);
  entry.count += 1;
  if (entry.examples.length < 3) {
    entry.examples.push({
      file: row.file,
      line: row.lineNo,
      label: row.label,
      text: truncate(row.visible, 220),
    });
  }
}

function normalizeCandidate(term) {
  let clean = term
    .replace(/^["'“”‘’\s]+|["'“”‘’.,!?;:\s]+$/g, "")
    .replace(/\s+/g, " ")
    .trim();
  clean = clean.replace(/^(?:If|So|Are|Because|All|The|A|An|My|His|Her|Their|This|That)\s+(?:the\s+)?/i, "");
  clean = clean.replace(/'s$/i, "");
  return clean.trim();
}

function scanTerms({ top = 80, min = 2 } = {}) {
  const glossary = flattenGlossaryTerms();
  const rows = extractVisibleRows(DIRS.en);
  const candidates = new Map();

  for (const row of rows) {
    const visible = row.visible;
    if (!visible) continue;

    for (const term of WATCH_TERMS) {
      if (containsGlossaryTerm(term, glossary)) continue;
      const flags = CASE_SENSITIVE_WATCH.has(term) ? "" : "i";
      const re = new RegExp(`\\b${escapeRegExp(term)}\\b`, flags);
      if (re.test(visible)) addCandidate(candidates, term, row);
    }

    const capitalized = visible.match(
      /\b(?:\p{Lu}[\p{L}'’]+|\p{Lu}{2,})(?:(?:[- ](?:of|the|and|Of|The|And))?[- ](?:\p{Lu}[\p{L}'’]+|\p{Lu}{2,})){0,5}\b/gu,
    );
    if (!capitalized) continue;
    for (const phrase of capitalized) {
      const clean = normalizeCandidate(phrase);
      if (!clean || containsGlossaryTerm(clean, glossary)) continue;
      if (!hasTermKeyword(clean)) continue;
      if (!clean.includes(" ") && !ALLOWED_SINGLE_TERMS.has(clean)) continue;
      if (/^(I|You|He|She|They|This|That|Then|There|Anyway|So|But|Well|Okay|Right)$/.test(clean)) continue;
      addCandidate(candidates, clean, row);
    }
  }

  const results = [...candidates.values()]
    .filter((entry) => entry.count >= min)
    .sort((a, b) => b.count - a.count || a.term.localeCompare(b.term))
    .slice(0, top)
    .map(({ seen, ...entry }) => entry);

  return {
    scannedRows: rows.length,
    totalCandidates: candidates.size,
    shown: results.length,
    min,
    results,
  };
}

function hasTermKeyword(text) {
  return TERM_KEYWORDS.some((keyword) => {
    const re = new RegExp(`\\b${escapeRegExp(keyword)}\\b`, "u");
    return re.test(text);
  });
}

function printTermReport(report) {
  console.log("Varredura de candidatos ao glossário FSN");
  console.log(`Linhas EN lidas: ${report.scannedRows}`);
  console.log(`Candidatos brutos: ${report.totalCandidates}`);
  console.log(`Exibindo: ${report.shown} com mínimo de ${report.min} ocorrência(s)`);
  console.log("");
  for (const item of report.results) {
    console.log(`- ${item.term} (${item.count})`);
    for (const ex of item.examples) {
      console.log(`  ${ex.file}:${ex.line} ${ex.label}: ${ex.text}`);
    }
  }
}

function escapeRegExp(text) {
  return text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function readOption(args, name, fallback) {
  const index = args.indexOf(name);
  if (index === -1 || index + 1 >= args.length) return fallback;
  const value = Number(args[index + 1]);
  return Number.isFinite(value) ? value : fallback;
}

const [command, maybeFile, ...rest] = process.argv.slice(2);

if (!command || command === "help" || command === "--help") {
  usage();
  process.exit(0);
}

if (command === "scene") {
  if (!maybeFile) {
    usage();
    process.exit(1);
  }
  const max = readOption(rest, "--max", 30);
  printSceneReport(analyzeScene(path.basename(maybeFile), max));
} else if (command === "terms") {
  const args = [maybeFile, ...rest].filter(Boolean);
  const top = readOption(args, "--top", 80);
  const min = readOption(args, "--min", 2);
  printTermReport(scanTerms({ top, min }));
} else {
  usage();
  process.exit(1);
}
