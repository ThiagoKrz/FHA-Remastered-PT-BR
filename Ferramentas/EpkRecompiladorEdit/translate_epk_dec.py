import argparse
import csv
import json
import pathlib
import re
import sys
import unicodedata
import urllib.request

TAG_RE = re.compile(r"\[[^\]]*\]")
PLACEHOLDER_RE = re.compile(r"__TAG\d+__|__TERM\d+__|__KEEP\d+__")

# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are a master literary translator who has read Fate/Hollow Ataraxia and \
Fate/Stay Night (Type-Moon, Kinoko Nasu) dozens of times in every available \
language. You know every character, every lore detail, every stylistic quirk. \
Your sole task: translate the given text from English into Brazilian Portuguese \
(PT-BR) with complete fidelity to tone, voice, cadence, and intent.

━━━ 1. GLOSSARY — ABSOLUTE PRIORITY ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A CSV glossary file (located in the project folder) drives this translation.
The translation pipeline has ALREADY processed that glossary before sending
text to you:

  • Terms with a PT-BR translation in the CSV → replaced with __TERM0__,
    __TERM1__, etc. in the text you receive. Do NOT translate them yourself.
    Leave every __TERM__ placeholder exactly where it is; the correct PT-BR
    word from the CSV will be restored automatically by the code.

  • Terms marked "não-traduzido" in the CSV → replaced with __KEEP0__,
    __KEEP1__, etc. Leave them untouched; the original word will be restored.

  • Terms NOT yet in the CSV may still appear as plain English. If you
    recognise them as Type-Moon proper nouns or magic-system terms, apply
    the established PT-BR fandom form listed in Section 5 below. Otherwise
    translate normally. Never invent a new translation for a term that
    contradicts what the CSV glossary would specify.

The glossary is the single source of truth for all proper nouns and
technical terms. It overrides every other instruction in this prompt.

━━━ 2. WORK CONTEXT ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fate/Hollow Ataraxia (F/HA) is the fandisc sequel to Fate/Stay Night, set in a
looping "4 days and 3 nights" in a peaceful post-war Fuyuki. Two realities exist
in parallel: the idyllic everyday loop (Shirou's perspective, comedic/warm) and
the dark true world (Bazett + Avenger, heavy and tragic). The tone swings wildly
between lighthearted slice-of-life comedy and deeply disturbing horror/philosophy.
Match the register of every line to its scene: never bring solemnity into comedy
or levity into tragedy.

━━━ 3. CHARACTER GUIDE — GENDER · PRONOUNS · VOICE ━━━━━━━━━━━━━━━━━━━━━━━━━
CRITICAL: grammatical gender in PT-BR must always match the character's sex.
Never write "ele" for a female character or "ela" for a male.

FSN/FHA RETURNING CAST:
• Shirō Emiya ♂ ele — narrador em 1ª pessoa; fala simples, direta, idealista,
  determinada; monólogo interno denso; repete afirmações como mantra ("Está certo.
  Está certo. Isso está certo."); às vezes ingênuo até o extremo.
• Saber / Artoria Pendragon ♀ ela — voz de rainha medieval; formalíssima mesmo
  em situações banais; nunca usa contrações desleixadas; vocabulário elevado;
  senso de dever acima de tudo; em F/HA mais relaxada mas nunca vulgar.
• Rin Tohsaka ♀ ela — tsundere clássica; confiante, irônica, sarcástica; alterna
  entre frieza e calor genuíno; orgulhosa de sua competência; não admite fraqueza.
• Archer / EMIYA ♂ ele — sardônico, cínico, pessimista contido; cada frase carrega
  duplo sentido; esconde dor por trás de indiferença cortante; em F/HA aparece menos.
• Sakura Matou ♀ ela — voz suave, hesitante, cheia de afeto reprimido; raramente
  confronta; esconde sofrimento por baixo de docilidade.
• Illyasviel von Einzbern ♀ ela — infantil e brincalhona na superfície; crueldade
  fria surge sem aviso; afeto genuíno por Shirou coexiste com instinto de predador.
• Kirei Kotomine ♂ ele — solene, ritualístico, cada palavra pesada de subentendido;
  nunca usa gíria; encontra prazer na dor alheia de forma calma e clínica.
• Gilgamesh ♂ ele — arrogância absoluta; todos são mongréis/insolentes/inferiores;
  vocabulário grandioso e imperioso; fala de si mesmo na 3ª pessoa às vezes.
• Taiga Fujimura (Fuji-nee) ♀ ela — enérgica, dramática, barulhenta, calorosa;
  fala descontraída, usa gírias, exagera tudo; alívio cômico principal.
• Lancer / Cú Chulainn ♂ ele — guerreiro honrado e descontraído; humor seco;
  aprecia uma boa luta; leal apesar de sua situação; fala casual e direta.
• Rider / Medusa ♀ ela — quieta, econômica nas palavras; quando fala tem peso;
  dignidade contida; lealdade profunda a Sakura.
• Caster / Medea ♀ ela — inteligente, calculista, elegante; manipuladora mas
  com afeto real por Souichirou; fala com precisão cirúrgica.
• Assassin / Sasaki Kojiro ♂ ele — sábio, sereno, filosófico; aprecia a arte
  do combate acima da vitória; fala pausada e reflexiva.
• Berserker / Heracles ♂ ele — não fala articuladamente (rugidos/grunhidos).
• Issei Ryuudou ♂ ele — sério, estudantil, formal.
• Zouken Matou ♂ ele — ancião sinistro; pausado, calculado, ameaçador.
• Souichirou Kuzuki ♂ ele — seco, mínimo; fala apenas o necessário.

FHA EXCLUSIVE CHARACTERS:
• Bazett Fraga McRemitz ♀ ela — irlandesa, maga de campo, pragmática e contida;
  fala formal e econômica; nunca dramatiza; aceita dor com frieza profissional;
  frases curtas e diretas; resolve problemas com determinação silenciosa.
• Avenger / Angra Mainyu ♂ ele — o Mal do Mundo feito Servant; tom casual e
  autodepreciativo na superfície ("sou só um lixo, afinal"); mas cada frase
  carrega peso existencial e manipulação velada; humor negro frequente; a leveza
  é máscara para vazio absoluto.
• Caren Hortensia ♀ ela — filha de Kirei; voz fria e ritualística como o pai mas
  com estranheza própria; masoquismo expresso com naturalidade perturbadora;
  usa o sofrimento alheio (e próprio) como ferramenta analítica; frases formais
  com conteúdo chocante ditas sem emoção aparente.
• Luviagelita Edelfelt (Luvia) ♀ ela — ojou-sama rivalda de Rin; vocabulário
  aristocrático exagerado; ri de forma grandiosa (risada tipo "ohohoho");
  competitiva ao extremo mas com seu próprio código de honra.

━━━ 4. TRADUÇÃO NATURAL — PRINCÍPIO CENTRAL ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRADUZA SENTIDO E INTENÇÃO, NUNCA PALAVRAS. A tradução deve soar como se
tivesse sido escrita originalmente em PT-BR por um falante nativo. Um leitor
brasileiro não pode perceber que é tradução.

EXPRESSÕES IDIOMÁTICAS — exemplos obrigatórios:
  "I see" (concordância)  → "Entendi" / "Já vejo" / "Compreendo" — NUNCA "Eu vejo"
  "I see" (visão literal) → "Vejo" / "Estou vendo"
  "I understand"          → "Entendo" / "Compreendo" — NUNCA "Eu entendo isso"
  "Is that so?"           → "É mesmo?" / "Ah, é?" / "Sério?"
  "I suppose"             → "Suponho" / "Acho que sim" — NUNCA "Eu suponho"
  "Indeed"                → "De fato" / "Realmente" / "Com efeito"
  "Of course"             → "Claro" / "Claro que sim" / "Naturalmente"
  "As expected"           → "Era de se esperar" / "Como esperado" / "Só podia ser"
  "It can't be helped"    → "Não tem jeito" / "É inevitável" / "Não há o que fazer"
  "Well then"             → "Então" / "Pois bem" / "Muito bem"
  "How boring"            → "Que tédio" / "Que chato" — NUNCA "Como chato"
  "What a pain"           → "Que chateação" / "Que saco" / "Que inconveniência"
  "No way"                → "De jeito nenhum" / "Impossível" / "Nem pensar"
  "I knew it"             → "Eu sabia" / "Como eu suspeitava"
  "Not bad"               → "Nada mal" — NUNCA "Não ruim"
  "As always"             → "Como sempre" / "Do jeito de sempre"
  "You fool"              → "Seu idiota" / "Imbecil" / "Tolo" (varia por personagem)
  "Shut up"               → "Cale a boca" (informal) / "Cale-se" (Saber/formal)
  "Leave it to me"        → "Pode deixar comigo" / "Deixa comigo"
  "That's right"          → "Isso mesmo" / "Exatamente" — NUNCA "Isso é certo"
  "How cruel"             → "Que crueldade" — NUNCA "Como cruel"
  "Tch"                   → "Tsc" / "Tchh" (som de irritação — adaptar foneticamente)
  "Heh" / "Hah" / "Hmm"  → manter ou adaptar ao som natural em PT-BR

CONSTRUÇÕES A EVITAR:
  ✗ "Eu [verbo] isso" como tradução literal de "I [verb] that/it" — omitir ou
    reescrever: "I know that" → "Eu sei disso" ✓ mas "I do that" → "Faço isso" ✓
  ✗ Adjetivo pós-nominal forçado como inglês: prefira a ordem natural do PT-BR
  ✗ Sujeito explícito desnecessário: "Ela disse ela estava bem" → "Disse que estava"
  ✗ "muito" repetido onde PT-BR nativo usaria gradação: "lindíssimo", "imenso"
  ✗ Calcos sintáticos: "fazer sentido" onde caberia "ter sentido" / "faz sentido" ✓

━━━ 5. NASU STYLE — TÉCNICAS ESPECÍFICAS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Repetição intencional como mantra ou ênfase: preserve. ("Eu sabia. Eu sabia
  disso. Eu sempre soube.")
• Frases curtíssimas para impacto dramático intercaladas com períodos longos.
• Reticências "..." usadas com alta frequência — preserve todas.
• Travessões "—" para pausas dramáticas ou interrupções — preserve.
• Monólogo interno em 1ª pessoa presente (Shirou): tom confessional e urgente.
• Metáforas físicas para estados emocionais ("algo quente escorreu pelo peito",
  "o frio não era do ar").
• F/HA especificamente: alternância brusca entre humor pastelão e horror
  existencial. Preserve o registro de cada cena — nunca misture os tons.
• Cenas do Ahnenerbe Café: tom relaxado, piadas internas do fandom, use PT-BR
  coloquial e leve.
• Cenas Bazett/Avenger: tom grave, poético, existencial — use PT-BR literário.

━━━ 5. TERMINOLOGIA MÁGICA / LORE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Se não estiver no glossário, use estas formas consagradas pelo fandom PT-BR:
  Magecraft → Taumaturgia | Magic Circuits → Circuitos Mágicos
  Reinforcement → Traço de Reforço | Projection → Projétil Mágico
  Heroic Spirit → Espírito Heroico | Noble Phantasm → Pergaminho Nobre
  Summoning → Invocação | Master → Mestre | Servant → Servant (manter)
  Holy Grail War → Guerra do Santo Graal | Command Spell → Selo de Mando
  Od → Od | Mana → Mana | Ether → Éter | Reality Marble → Marble Fantasma
  Alaya → Alaya | Akasha → Akasha | Counter Force → Força Contrária
  Dead Apostle → Apóstolo Morto | True Ancestor → Ancestral Verdadeiro
  Runes (Bazett) → Runas | Fragarach → Fragarach (manter)
  Angra Mainyu → Angra Mainyu (manter) | All the World's Evil → O Mal do Mundo
Honoríficos japoneses: manter sem tradução (-san, -kun, -chan, -senpai,
  -sensei, nee-san, nii-san, Fuji-nee, etc.).
Nomes próprios: seguir o glossário; se ausente, manter em inglês.

━━━ 6. REGRAS DE SAÍDA — INVIOLÁVEIS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Retorne SOMENTE o texto traduzido. Zero explicações, zero comentários.
2. NÃO adicione linhas, cabeçalhos ou estrutura que não existam no original.
3. Mantenha pontuação, capitalização e quebras de linha IDÊNTICAS à fonte.
4. Placeholders __TAG0__ __TERM0__ __KEEP0__ etc: copie-os EXATAMENTE onde estão.
5. Texto muito curto (uma palavra, um nome): traduza apenas aquilo.
6. Nunca insira nota de tradução ou parêntese explicativo na saída.
"""

REMINDER = (
    "\n\n[LEMBRETE — Fate/Hollow Ataraxia para PT-BR natural de falante nativo. "
    "Traduza SENTIDO, não palavras: 'I see' → 'Entendi', nunca 'Eu vejo'. "
    "Gêneros: Saber/Rin/Sakura/Illya/Rider/Caster/Bazett/Caren/Luvia = ela/dela. "
    "Shirou/Archer/Lancer/Kirei/Gilgamesh/Avenger/Assassin/Berserker = ele/dele. "
    "Placeholders __TAG0__ __TERM0__ __KEEP0__: copie intactos, nunca traduza. "
    "Retorne APENAS o texto traduzido, sem comentários, sem linhas extras.]"
)

# Inject a reminder into the prompt every N translation calls to prevent drift
REMINDER_EVERY = 25


def detect_encoding(data: bytes) -> tuple[str, str]:
    for enc in ("utf-8-sig", "utf-8"):
        try:
            text = data.decode(enc)
        except UnicodeDecodeError:
            continue
        if "\ufffd" not in text:
            return enc, text
    for enc in ("cp932", "shift_jis", "latin-1"):
        try:
            text = data.decode(enc)
        except UnicodeDecodeError:
            continue
        if "\ufffd" not in text:
            return enc, text
    return "utf-8", data.decode("utf-8", errors="replace")


def pick_glossary(root: pathlib.Path, glossary_arg: str | None) -> pathlib.Path:
    if glossary_arg:
        return pathlib.Path(glossary_arg)
    csvs = list(root.glob("*.csv"))
    if len(csvs) == 1:
        return csvs[0]
    if not csvs:
        raise FileNotFoundError("No CSV glossary found. Use --glossary.")
    raise FileExistsError("Multiple CSV glossaries found. Use --glossary.")


def normalize_header(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_only = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return ascii_only.strip().lower()


def load_glossary(path: pathlib.Path) -> tuple[dict[str, str], set[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise ValueError("Glossary CSV has no header row.")

        headers = {normalize_header(h): h for h in reader.fieldnames}
        jp_col = headers.get("japones") or headers.get("japanese")
        en_col = headers.get("ingles") or headers.get("english")
        pt_col = headers.get("portugues") or headers.get("portuguese")
        type_col = headers.get("tipo de termo") or headers.get("tipo") or headers.get("type")

        if not (jp_col or en_col) or not pt_col:
            raise ValueError("Glossary CSV is missing required columns.")

        force_map: dict[str, str] = {}
        no_translate: set[str] = set()

        for row in reader:
            term_type = (row.get(type_col, "") or "") if type_col else ""
            term_type_norm = normalize_header(term_type)
            is_no_translate = "nao-traduzido" in term_type_norm or "nao traduzido" in term_type_norm

            jp = (row.get(jp_col, "") or "").strip() if jp_col else ""
            en = (row.get(en_col, "") or "").strip() if en_col else ""
            pt = (row.get(pt_col, "") or "").strip() if pt_col else ""

            if is_no_translate:
                if jp:
                    no_translate.add(jp)
                if en:
                    no_translate.add(en)
                continue

            if pt:
                if jp:
                    force_map[jp] = pt
                if en:
                    force_map[en] = pt

        return force_map, no_translate


def term_to_regex(term: str) -> re.Pattern:
    escaped = re.escape(term)
    left = r"(?<!\w)" if term and term[0].isalnum() else ""
    right = r"(?!\w)" if term and term[-1].isalnum() else ""
    return re.compile(left + escaped + right)


def replace_with_placeholders(
    text: str, items: list[tuple[re.Pattern, str]], prefix: str
) -> tuple[str, dict[str, str]]:
    placeholders: dict[str, str] = {}
    for idx, (pattern, replacement) in enumerate(items):
        key = f"__{prefix}{idx}__"
        def repl(_match):
            return key
        text, count = pattern.subn(repl, text)
        if count:
            placeholders[key] = replacement
    return text, placeholders


def mask_tags(text: str) -> tuple[str, dict[str, str]]:
    tags: dict[str, str] = {}
    def repl(match):
        key = f"__TAG{len(tags)}__"
        tags[key] = match.group(0)
        return key
    return TAG_RE.sub(repl, text), tags


def split_trailing_tags(text: str) -> tuple[str, str]:
    match = re.search(r"(.*?)(\s*(?:\[[^\]]*\]\s*)+)$", text)
    if match and match.group(1):
        return match.group(1), match.group(2)
    return text, ""


def unmask(text: str, mapping: dict[str, str]) -> str:
    for key, value in mapping.items():
        text = text.replace(key, value)
    return text


def should_translate(text: str) -> bool:
    candidate = PLACEHOLDER_RE.sub("", text)
    return bool(candidate.strip())


# ---------------------------------------------------------------------------
# Ollama backend
# ---------------------------------------------------------------------------

def call_ollama(model: str, prompt: str, options: dict) -> str:
    payload = {
        "model": model,
        "system": SYSTEM_PROMPT,
        "prompt": prompt,
        "stream": False,
        "think": False,   # disable Qwen3 thinking mode; ignored by other models
        "options": options,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    return (result.get("response") or "").strip()


def make_translate_fn(args) -> callable:
    options = {"temperature": 0.3, "top_p": 0.9, "repeat_penalty": 1.1}
    if args.num_gpu != 0:
        options["num_gpu"] = args.num_gpu
    if args.num_ctx > 0:
        options["num_ctx"] = args.num_ctx
    if args.num_thread > 0:
        options["num_thread"] = args.num_thread
    model = args.model
    print(f"Backend: Ollama  |  Model: {model}  |  ctx: {args.num_ctx}")

    call_count = [0]

    def translate(prompt: str) -> str:
        call_count[0] += 1
        effective_prompt = prompt
        if call_count[0] % REMINDER_EVERY == 0:
            effective_prompt = prompt + REMINDER
        return call_ollama(model, effective_prompt, options)

    return translate


# ---------------------------------------------------------------------------
# Line processing
# ---------------------------------------------------------------------------

def process_line(
    line: str,
    translate_fn,
    force_items,
    no_translate_items,
    cache: dict[str, str],
) -> str:
    if line.startswith("DAT") or line.startswith("id=") or not line.strip():
        return line

    first = line.find("::")
    if first == -1:
        return line
    second = line.find("::", first + 2)
    if second == -1:
        return line
    label = line[first + 2:second]
    if "$$$message" not in label:
        return line

    last = line.rfind("::")
    if last <= second:
        # No closing :: — last message line may lack it; treat EOL as boundary
        eol = line[len(line.rstrip("\r\n")):]
        last = len(line.rstrip("\r\n"))
        suffix = "::" + eol   # restore closing :: after translation
    else:
        suffix = line[last:]

    prefix = line[:second + 2]
    text = line[second + 2:last]

    # Extract and preserve quotes independently — never let the model see or touch them
    has_open  = text.startswith("\"")
    has_close = text.endswith("\"")
    if has_open and has_close:
        inner = text[1:-1]
    elif has_open:
        inner = text[1:]
    elif has_close:
        inner = text[:-1]
    else:
        inner = text

    base_text, trailing_tags = split_trailing_tags(inner)
    masked, tag_map = mask_tags(base_text)

    masked, keep_map = replace_with_placeholders(masked, no_translate_items, "KEEP")
    masked, force_map = replace_with_placeholders(masked, force_items, "TERM")

    if should_translate(masked):
        cache_key = masked
        if cache_key in cache:
            translated = cache[cache_key]
        else:
            translated = translate_fn(masked)
            cache[cache_key] = translated
    else:
        translated = masked

    translated = unmask(translated, {**keep_map, **force_map})
    translated = unmask(translated, tag_map)
    if trailing_tags:
        translated = translated + trailing_tags

    # Strip any spurious quotes the model may have added, then restore the originals
    if has_open and translated.startswith("\""):
        translated = translated[1:]
    if has_close and translated.endswith("\""):
        translated = translated[:-1]
    if has_open:
        translated = "\"" + translated
    if has_close:
        translated = translated + "\""

    return prefix + translated + suffix


def normalize_ending(content: str, newline: str) -> str:
    content = content.rstrip("\r\n")
    return content + newline + newline


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

STRAY_PLACEHOLDER_RE = re.compile(r"__(?:TAG|TERM|KEEP)\d+__")
COMMAND_LINE_RE = re.compile(r"^(?:DAT|id=|[A-Za-z_][A-Za-z0-9_]*::)")


def fix_and_validate(src_lines: list[str], out_lines: list[str], _filename: str) -> None:
    """
    Auto-fixes all detectable issues in out_lines in-place, then prints
    a summary to the console. No external file is created.
    """
    fixes = []
    warnings = []

    # 1. Stray placeholders — strip them from the output line
    for i, out in enumerate(out_lines):
        stripped = out.rstrip("\r\n")
        eol = out[len(stripped):]
        cleaned = STRAY_PLACEHOLDER_RE.sub("", stripped).strip()
        if cleaned != stripped:
            stray = STRAY_PLACEHOLDER_RE.findall(stripped)
            out_lines[i] = cleaned + eol
            fixes.append(f"Line {i+1}: removed stray placeholder(s) {stray!r}")

    # 2. Injected command lines inside a translated message — remove them
    for i, (src, out) in enumerate(zip(src_lines, out_lines)):
        src_s = src.rstrip("\r\n")
        out_s = out.rstrip("\r\n")
        eol = out[len(out_s):]
        if "$$$message" in src_s and "\n" in out_s:
            parts = out_s.splitlines()
            clean_parts = [p for p in parts if not (COMMAND_LINE_RE.match(p) and p not in src_s)]
            if len(clean_parts) != len(parts):
                removed = [p for p in parts if p not in clean_parts]
                out_lines[i] = "\n".join(clean_parts) + eol
                fixes.append(f"Line {i+1}: removed injected command line(s) {removed!r}")

    # 3. Extra lines beyond source length — trim them
    if len(out_lines) > len(src_lines):
        removed_count = len(out_lines) - len(src_lines)
        del out_lines[len(src_lines):]
        fixes.append(f"Trimmed {removed_count} extra line(s) beyond source length")

    # 4. Last $$$message line must end with ::
    last_idx = None
    for i, src in enumerate(src_lines):
        if "$$$message" in src.rstrip("\r\n"):
            last_idx = i
    if last_idx is not None and last_idx < len(out_lines):
        line = out_lines[last_idx]
        stripped = line.rstrip("\r\n")
        eol = line[len(stripped):]
        if not stripped.endswith("::"):
            out_lines[last_idx] = stripped + "::" + eol
            fixes.append(f"Line {last_idx+1}: restored closing '::' on last $$$message")

    # 5. Unfixable: line count still wrong after trimming
    if len(out_lines) != len(src_lines):
        warnings.append(
            f"LINE COUNT MISMATCH: original={len(src_lines)} output={len(out_lines)}"
        )

    if fixes:
        print(f"  Auto-fixed {len(fixes)} issue(s):")
        for f in fixes:
            print(f"    {f}")
    if warnings:
        print(f"  WARNING — {len(warnings)} unfixable issue(s):")
        for w in warnings:
            print(f"    {w}")
    if not fixes and not warnings:
        print("  Validation OK")


def build_term_items(force_map: dict[str, str], no_translate: set[str]):
    force_terms = sorted(force_map.items(), key=lambda x: len(x[0]), reverse=True)
    no_terms = sorted(no_translate, key=len, reverse=True)
    force_items = [(term_to_regex(term), replacement) for term, replacement in force_terms]
    no_items = [(term_to_regex(term), term) for term in no_terms]
    return force_items, no_items


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--glossary", default=None)
    parser.add_argument("--no-glossary", action="store_true")
    parser.add_argument("--model", default="qwen3:8b",
                        help="Ollama model name (default: qwen3:8b)")
    parser.add_argument("--output-dir", default="scripts_pt-br")
    parser.add_argument("--num-gpu", type=int, default=-1)
    parser.add_argument("--num-ctx", type=int, default=8192)
    parser.add_argument("--num-thread", type=int, default=0)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--file", default=None, help="Process only one file")
    parser.add_argument("--all", action="store_true", help="Process all .epk_dec files under root")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    output_root = root / args.output_dir
    output_root.mkdir(parents=True, exist_ok=True)

    if args.no_glossary:
        force_items, no_items = [], []
    else:
        glossary_path = pick_glossary(root, args.glossary)
        force_map, no_translate = load_glossary(glossary_path)
        force_items, no_items = build_term_items(force_map, no_translate)
        print(f"Glossary: {glossary_path.name}  |  {len(force_map)} terms, {len(no_translate)} untranslated")

    if args.file:
        file_path = pathlib.Path(args.file)
        if not file_path.is_absolute():
            file_path = root / file_path
        files = [file_path]
    elif args.all:
        files = sorted(
            (path for path in root.rglob("*.epk_dec") if output_root not in path.parents),
            key=lambda p: p.name,
        )
    else:
        print("No input specified. Use --file or --all.")
        return

    translate_fn = make_translate_fn(args)
    cache: dict[str, str] = {}

    for path in files:
        relative = path.relative_to(root)
        output_path = output_root / relative
        if args.dry_run:
            output_path = output_path.with_suffix(output_path.suffix + ".preview")

        if output_path.exists() and not args.overwrite:
            print(f"Skipping {relative} (already exists)")
            continue

        data = path.read_bytes()
        _, text = detect_encoding(data)
        newline = "\r\n" if b"\r\n" in data else "\n"

        lines = text.splitlines(True)
        out_lines = []
        total = len(lines)
        for index, line in enumerate(lines, start=1):
            sys.stdout.write(f"\r{path.name}: line {index}/{total}")
            sys.stdout.flush()
            out_lines.append(process_line(line, translate_fn, force_items, no_items, cache))
        sys.stdout.write("\n")

        fix_and_validate(lines, out_lines, path.name)

        out_text = normalize_ending("".join(out_lines), newline)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(out_text.encode("utf-8"))


if __name__ == "__main__":
    main()
