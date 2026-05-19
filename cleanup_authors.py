"""
Audit and clean up bad `authors:` values written by populate_authors.py.
Removes values that are clearly not author names.
"""

import os
import re

PAPERS_DIR = os.path.join(os.path.dirname(__file__), "content", "papers")

# Sentence starters that indicate a summary fragment, not author names
BAD_STARTS = re.compile(
    r'^(This |The |A |An |Uses |Proposes |Reviews |Argues |Scoping |Theoretical '
    r'|Advocates |Based |Building |Drawing |Published |Presents |Report|Survey|Case study'
    r'|Founding Editor|Series Editor|Editorial Board|Computing Systems|Science and Engineering'
    r'|New Industry|Development Courses|Entry-Level|Educational Technology Publications'
    r'|Study Dissertation|Empirical Research Paper|Interaction Design|claiming that'
    r'|Intelligent Color Platform|SchoolofArts|UCLAHCIResearch|United States'
    r'|AI-AssistedDesign|User Experiences)',
    re.IGNORECASE
)

# Phrases that indicate the value is a sentence, not a name list
BAD_PHRASES = re.compile(
    r'\b(present chapter|present paper|present article|present the outcomes|present foundational'
    r'|investigat|examine|explor|propos|report qualitative|report on integrating'
    r'|from the University|at Carnegie Mellon|from Columbia University)',
    re.IGNORECASE
)

# Known non-author words that get wrongly extracted from filenames
NON_AUTHOR_WORDS = {
    # Journals, conferences, publishers - not author names
    "ASCILITE", "Springer", "Turkish", "iJET", "Postdigital Science",
    "IEEE Annals", "AI & Society", "CHI", "Voces y Silencios",
    "Bradshaw TechTrends", "Lo UNM", "University of New Mexico",
    "Brown dissertation", "Cheatham Miami U", "Oravec Review of Autor",
    "Degen & Ntoa, Eds", "Choudary, HBR", "Nelson & Stolterman, IJOD",
    "Foundational and Instrumental", "Performance Technology Foundation",
    "Kirschner Sweller Clark",
    # Single-word non-name identifiers
    "Review", "IJHSES", "Indiana", "Informa",
    "Computing Systems", "Science and Engineering",
    "New Industry Needs", "Development Courses",
    "Entry-Level Professionals", "Empirical Research Paper",
    "Interaction Design", "United States",
}

def is_bad_authors(value):
    if not value:
        return False
    v = value.strip('"').strip()

    # Too long = sentence fragment
    if len(v) > 150:
        return True

    # Starts with a sentence word
    if BAD_STARTS.match(v):
        return True

    # Contains internal sentence phrases
    if BAD_PHRASES.search(v):
        return True

    # Single known bad word
    if v in NON_AUTHOR_WORDS:
        return True

    # Partial word (ends with hyphen)
    if v.endswith('-'):
        return True

    # Repository/doubled-characters artifacts (e.g., "UUNNMM DDiiggiittaall")
    if 'repository' in v.lower() or 'rreeppoossiittoorryy' in v.lower():
        return True

    # Values that are only institution names (contain these words but no comma or "and")
    if re.search(r'\b(University|Institute|Department|College|School|Lab\b|Center|Centre|Faculty|Research|LLC|Inc\.|Corp\b|Expertise Center)\b', v, re.IGNORECASE):
        if not re.search(r',|\band\b', v, re.IGNORECASE):
            return True

    # Contains lab/org names mixed with people (TIDALLab, HCIInstitute repeated, etc.)
    if re.search(r'(?:Lab|Institute|Research|Dept|Group){2,}', v, re.IGNORECASE):
        return True
    if re.search(r'\b(TIDALLab|HCIInstitute|GoogleDeepMind|UCLAHCIResearch)\b', v):
        return True

    return False

def parse_frontmatter_raw(text):
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", text
    return text[3:end], text[end + 4:]

def clear_authors_field(text):
    """Remove the authors: line from frontmatter."""
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    fm = text[3:end]
    rest = text[end:]
    lines = [l for l in fm.splitlines() if not l.strip().startswith("authors:")]
    return "---" + "\n".join(lines) + rest

def main():
    files = [f for f in os.listdir(PAPERS_DIR) if f.endswith(".md")]
    cleared = []
    kept = 0
    no_authors = 0

    for fname in sorted(files):
        fpath = os.path.join(PAPERS_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        # Find authors line
        m = re.search(r'^authors:\s*(.+)$', text, re.MULTILINE)
        if not m:
            no_authors += 1
            continue

        value = m.group(1).strip().strip('"')
        if is_bad_authors(value):
            new_text = clear_authors_field(text)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_text)
            safe = fname[:70].encode('ascii', errors='replace').decode('ascii')
            safe_val = value[:80].encode('ascii', errors='replace').decode('ascii')
            print(f"  CLEARED: {safe}")
            print(f"    was: {safe_val}")
            cleared.append(fname)
        else:
            kept += 1

    print(f"\n{'='*60}")
    print(f"Cleared (bad values): {len(cleared)}")
    print(f"Kept (good values):   {kept}")
    print(f"No authors field:     {no_authors}")

if __name__ == "__main__":
    main()
