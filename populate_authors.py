"""
Populate `authors` frontmatter field for paper notes by extracting
author names from the first sentence of the ## Summary section.
"""

import os
import re
import sys

PAPERS_DIR = os.path.join(os.path.dirname(__file__), "content", "papers")

BAD_STARTS = re.compile(
    r'^(This |The |A |An |Uses |Proposes |Reviews |Argues |Scoping |Theoretical '
    r'|Advocates |Based |Building |Drawing |Published |Presents |Report|Survey|Case study)',
    re.IGNORECASE
)
BAD_PHRASES = re.compile(
    r'\b(present chapter|present paper|present article|present the outcomes|present foundational'
    r'|investigat|examine|explor|propos|report qualitative|report on integrating'
    r'|from the University|at Carnegie Mellon|from Columbia University)',
    re.IGNORECASE
)
NON_AUTHOR_WORDS = {
    "ASCILITE", "Springer", "Turkish", "iJET", "Postdigital Science",
    "IEEE Annals", "AI & Society", "CHI", "Voces y Silencios",
    "Bradshaw TechTrends", "Lo UNM", "University of New Mexico",
    "Brown dissertation", "Cheatham Miami U", "Oravec Review of Autor",
    "Degen & Ntoa, Eds", "Choudary, HBR", "Nelson & Stolterman, IJOD",
    "Foundational and Instrumental", "Performance Technology Foundation",
    "Kirschner Sweller Clark", "Review", "January", "IJHSES",
}

def is_bad_authors(value):
    if not value:
        return False
    v = value.strip('"').strip()
    if len(v) > 150:
        return True
    if BAD_STARTS.match(v):
        return True
    if BAD_PHRASES.search(v):
        return True
    if v in NON_AUTHOR_WORDS:
        return True
    return False

# Verbs that typically follow author name lists in academic summaries
STOP_WORDS = re.compile(
    r'\b(investigat|examin|explor|propos|present|report|analyz|analys|argu|conduct|show|demonstrat|develop|introduc|describ|studi|find|document|identif|extend|build|use|apply|offer|call|draw|review|test|evaluat|compare|synthesiz|frame|positions|challenges|situates|position)\w*\b',
    re.IGNORECASE
)

def parse_frontmatter(text):
    """Return (frontmatter_dict_raw, body) splitting on --- delimiters."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    # Parse simple key: value pairs (handles quoted and unquoted values)
    fm = {}
    for line in fm_block.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
    return fm, body

def reconstruct_frontmatter(fm_raw, body, extra_fields):
    """Rebuild the file with updated frontmatter."""
    lines = []
    keys_seen = set()
    for line in fm_raw.strip().splitlines():
        if ":" in line:
            key = line.split(":")[0].strip()
            keys_seen.add(key)
        lines.append(line)
    # Append new fields not already present
    for k, v in extra_fields.items():
        if k not in keys_seen:
            lines.append(f'{k}: "{v}"')
    return "---\n" + "\n".join(lines) + "\n---\n\n" + body

def extract_first_sentence_of_summary(body):
    """Find ## Summary section and return its first sentence."""
    m = re.search(r'^## Summary\s*\n(.*?)(?=\n##|\Z)', body, re.MULTILINE | re.DOTALL)
    if not m:
        return ""
    summary = m.group(1).strip()
    # First sentence ends at . or end of line
    first = re.split(r'(?<=[.!?])\s+', summary)[0]
    return first

NAME = r"[A-Z][a-zA-Zé\-À-ɏ']+"       # single surname token
NAME_SEQ = rf"(?:{NAME}(?:\s+{NAME})*)"           # compound surname (e.g. "Martinez Marroquin")
LIST_SEP = r"(?:,\s*|\s+and\s+)"

def extract_authors_from_filename_pattern(fname):
    """Match 'Surname YYYY Title' pattern at start of filename."""
    base = fname.replace(".md", "")
    m = re.match(r'^([A-Z][a-zA-Z\-]+(?:\s+and\s+[A-Z][a-zA-Z\-]+)?)\s+\d{4}\b', base)
    if m:
        return m.group(1)
    return None

def extract_authors_from_filename(fname):
    """
    Try to extract authors from parenthetical at end of filename.
    Patterns: (Smith et al., 2024)  (Smith and Jones)  (Smith et al. CMU)
    Returns cleaned author string or None.
    """
    base = fname.replace(".md", "")
    m = re.search(r'\(([^)]+)\)\s*$', base)
    if not m:
        return None
    inner = m.group(1).strip()
    # Strip trailing year or institution
    inner = re.sub(r',?\s*\d{4}$', '', inner).strip()
    inner = re.sub(r'\s+(?:HTW Berlin|CMU|MIT|NYU|UCLA|CUHK|Cornell|Malmo|Imperial|Kookmin|UdeM|Tongji|Purdue|Jonkoping|Microsoft|Google DeepMind|Northeastern|Amazon|CHI|CSCW|UIST|IUI|DIS|FAccT|ICDL|IJHSES|DECIPHER|ASCILITE|ACM|IEEE|Waterloo|IJOD|Int\'l J\. of AI)\s*$', '', inner, flags=re.IGNORECASE).strip()
    # Also strip trailing ", [Conference]" patterns
    inner = re.sub(r',\s*(?:CHI|CSCW|UIST|IUI|DIS|ACM|IEEE|IJHSES|Int\'l J\. of AI|AI & Society)\s*$', '', inner, flags=re.IGNORECASE).strip()
    inner = inner.rstrip('.,').strip()
    if not inner:
        return None
    # Only accept if it looks like an author list (has capital words)
    if not re.search(r'[A-Z]', inner):
        return None
    return inner

def clean_author_string(s):
    """Strip trailing institutional affiliations and verb phrases from an extracted name string."""
    # Remove " from/at/of [Institution/City/University]"
    s = re.sub(r'\s+(?:from|at)\s+(?:the\s+)?(?:University|Carnegie Mellon|Accenture|Politecnico|Cornell|Columbia)\b.*$', '', s, flags=re.IGNORECASE)
    # Remove " present(s) chapter/paper/article/the outcomes/conference/foundational/ephemera"
    s = re.sub(r'\s+present[s]?\s+(?:chapter|paper|article|conference|the\s+outcomes|foundational|ephemera|influential|paper investigates).*$', '', s, flags=re.IGNORECASE)
    # Remove trailing "and colleagues at [place]"
    s = re.sub(r',?\s+and\s+colleagues\s+at\b.*$', ', et al.', s, flags=re.IGNORECASE)
    # Remove trailing prepositions and everything after
    s = re.sub(r'\s+(report|examine|investigate|propose|develop|argue|analyze)\s+.*$', '', s, flags=re.IGNORECASE)
    return s.strip().rstrip('.,')

def extract_authors_from_sentence(sentence):
    """
    Try to extract a clean author string from the first sentence.

    Patterns handled:
      "Smith, Jones, and Lee investigate..." → "Smith, Jones, and Lee"
      "Smith and Newby's foundational..." → "Smith and Newby"
      "Smith and colleagues at..." → "Smith et al."
      "Smith, Jones, and colleagues..." → "Smith, Jones, et al."
      "Smith et al. propose..." → "Smith et al."
    """
    if not sentence:
        return None

    # Strip possessive at end of author block: "Ertmer and Newby's" → treat as "Ertmer and Newby verb"
    sentence = re.sub(r"'s\b", " present", sentence, count=1)

    # Match explicit full lists ending with verb: "A, B, and C verb"
    # NOTE: no IGNORECASE — names must start uppercase; stop words are lowercase in pattern
    full_list = re.match(
        rf'^({NAME_SEQ}(?:{LIST_SEP}{NAME_SEQ})*)\s+' + STOP_WORDS.pattern,
        sentence
    )
    if full_list:
        authors = full_list.group(1).strip().rstrip(",")
        if "," in authors or " and " in authors.lower():
            return authors

    # Match "X, Y, and colleagues" → "X, Y, et al."
    colleagues_multi = re.match(
        rf'^({NAME_SEQ}(?:,\s*{NAME_SEQ})+),?\s+and\s+colleagues',
        sentence
    )
    if colleagues_multi:
        return colleagues_multi.group(1) + ", et al."

    # Match "X and colleagues" → "X et al."
    colleagues = re.match(
        rf'^({NAME_SEQ})\s+and\s+colleagues',
        sentence
    )
    if colleagues:
        return colleagues.group(1) + " et al."

    # Match "X et al.'s" or "X et al."
    et_al = re.match(
        rf'^({NAME_SEQ}(?:,\s*{NAME_SEQ})*)\s+et al\.',
        sentence
    )
    if et_al:
        return et_al.group(1) + " et al."

    return None

def process_papers():
    files = [f for f in os.listdir(PAPERS_DIR) if f.endswith(".md")]
    updated = 0
    skipped_has_authors = 0
    no_authors_found = []

    for fname in sorted(files):
        fpath = os.path.join(PAPERS_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        fm_raw_block, body = parse_frontmatter_raw(text)
        fm, _ = parse_frontmatter(text)

        # Skip if already has authors
        if fm.get("authors", "").strip():
            skipped_has_authors += 1
            continue

        # Skip non-paper types
        if fm.get("type", "").strip().strip('"') not in ("paper", ""):
            continue

        first = extract_first_sentence_of_summary(body)
        authors = extract_authors_from_sentence(first)

        # Fallback: extract from filename parenthetical
        if not authors:
            authors = extract_authors_from_filename(fname)

        # Fallback: extract from "Surname YYYY Title" filename pattern
        if not authors:
            authors = extract_authors_from_filename_pattern(fname)

        if authors:
            authors = clean_author_string(authors)
            if not authors:
                no_authors_found.append(fname)
                continue
            # Reject known-bad values before writing
            if is_bad_authors(authors):
                no_authors_found.append(fname)
                continue
            # Insert authors field after 'year' line or after 'type' line
            new_text = insert_authors_field(text, authors)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_text)
            safe = fname[:70].encode('ascii', errors='replace').decode('ascii')
            print(f"  [OK] {safe}")
            print(f"       -> {authors}")
            updated += 1
        else:
            no_authors_found.append(fname)

    print(f"\n{'='*60}")
    print(f"Updated: {updated}")
    print(f"Already had authors: {skipped_has_authors}")
    print(f"No authors extracted: {len(no_authors_found)}")
    if no_authors_found:
        out_path = os.path.join(os.path.dirname(__file__), "missing_authors.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(no_authors_found))
        print(f"\nFiles needing manual authors written to: missing_authors.txt")

def parse_frontmatter_raw(text):
    """Return (frontmatter_block_str, body) without parsing."""
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", text
    fm_block = text[3:end]
    body = text[end + 4:]
    return fm_block, body

def insert_authors_field(text, authors):
    """Insert authors: field into frontmatter after 'year:' or 'type:' line."""
    authors_escaped = authors.replace('"', '\\"')
    field_line = f'authors: "{authors_escaped}"'

    if not text.startswith("---"):
        return text

    end = text.find("\n---", 3)
    if end == -1:
        return text

    fm = text[3:end]
    rest = text[end:]

    lines = fm.splitlines()
    insert_after = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("year:"):
            insert_after = i
            break
    if insert_after == -1:
        for i, line in enumerate(lines):
            if line.strip().startswith("type:"):
                insert_after = i
                break
    if insert_after == -1:
        insert_after = len(lines) - 1

    lines.insert(insert_after + 1, field_line)
    new_fm = "\n".join(lines)
    return "---" + new_fm + rest

if __name__ == "__main__":
    process_papers()
