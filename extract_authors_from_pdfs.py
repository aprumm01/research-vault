"""
Extract authors from local PDFs and write them to vault notes.
Fuzzy-matches missing-author vault notes to PDFs in Research docs folder,
reads the first page of each PDF with pdfplumber, and writes authors: frontmatter.
"""

import os
import re
import glob
from difflib import SequenceMatcher

try:
    import pdfplumber
except ImportError:
    print("ERROR: pdfplumber not installed. Run: pip install pdfplumber")
    raise

PAPERS_DIR = os.path.join(os.path.dirname(__file__), "content", "papers")
MISSING_FILE = os.path.join(os.path.dirname(__file__), "missing_authors.txt")
RESEARCH_DOCS = r"C:\Users\adamp\Desktop\IU Classes\Research docs"

# --- Helpers ---

def normalize(s):
    s = s.lower()
    s = re.sub(r'[_\-,.!?:;\'\"()\[\]{}]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def title_from_note(fname):
    base = fname.replace('.md', '')
    base = re.sub(r'\s*\([^)]+\)\s*$', '', base)
    return base.strip()

def score(note_name, pdf_name):
    n = normalize(title_from_note(note_name))
    p = normalize(os.path.splitext(os.path.basename(pdf_name))[0])
    return SequenceMatcher(None, n, p).ratio()

def get_all_pdfs():
    pdfs = []
    for root, dirs, files in os.walk(RESEARCH_DOCS):
        # Skip non-document directories
        skip = {'My writing', 'notes', 'Obsidian Synthesis', 'synth users'}
        dirs[:] = [d for d in dirs if d not in skip]
        for f in files:
            if f.lower().endswith('.pdf'):
                pdfs.append(os.path.join(root, f))
    return pdfs

def parse_frontmatter_raw(text):
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", text
    return text[3:end], text[end + 4:]

def insert_authors_field(text, authors):
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
    return "---" + "\n".join(lines) + rest

# --- Author extraction from PDF first page ---

AUTHOR_PATTERNS = [
    # "By Author1 and Author2" or "By: Author1"
    re.compile(r'\bby[:\s]+([A-Z][a-zA-Zé\-À-ɏ\'\s,]+?)(?:\n|,\s*\n|\s{2,}|\bAbstract\b|\bDepartment\b|\bUniversity\b|\bInstitute\b)', re.IGNORECASE),
    # Lines with "Author1, Author2" followed by affiliation keyword
    re.compile(r'^([A-Z][a-zA-Zé\-À-ɏ\']+(?:[\s,]+(?:and\s+)?[A-Z][a-zA-Zé\-À-ɏ\']+){1,8})\s*\n(?=.*(?:University|Institute|Department|College|School|Lab|Center|Centre|Faculty))', re.MULTILINE),
]

# Common "stop" words that indicate we've left the author section
NOT_AUTHOR = re.compile(
    r'\b(Abstract|Introduction|Keywords|Received|Accepted|Published|Available|DOI|doi|http|IEEE|Volume|Issue|Copyright|Journal|Conference|Proceedings|©)\b',
    re.IGNORECASE
)

def clean_name_list(s):
    """Clean a raw extracted author string."""
    # Remove line breaks and extra whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    # Remove trailing punctuation
    s = s.rstrip('.,;:')
    return s

def looks_like_authors(s):
    """Heuristic: does this string look like a list of personal names?"""
    if not s or len(s) > 250:
        return False
    if NOT_AUTHOR.search(s):
        return False
    # Should have at least one capitalized word
    if not re.search(r'[A-Z][a-z]', s):
        return False
    # Reject if it looks like a title (starts with The/A/An + adj/noun)
    if re.match(r'^(The|A|An|This|In|For|On|With|From|To)\b', s, re.IGNORECASE):
        return False
    return True

def extract_authors_from_text(text):
    """Extract author names from the first page text of a PDF."""
    # Only look at first ~3000 chars (title page / abstract)
    sample = text[:3000]

    # Strategy 1: Look for explicit author byline patterns
    for pat in AUTHOR_PATTERNS:
        m = pat.search(sample)
        if m:
            candidate = clean_name_list(m.group(1))
            if looks_like_authors(candidate):
                return candidate

    # Strategy 2: Find lines that look like author lists
    # Typically: after title, before abstract, short lines with names
    lines = sample.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) > 150:
            continue
        # Skip lines that look like titles (too long or start with article words)
        if len(line) > 100:
            continue
        # Look for patterns like "Firstname Lastname, Firstname Lastname"
        # or "F. Lastname and G. Lastname"
        name_pat = re.compile(
            r'^([A-Z][a-zA-Zé\-À-ɏ\'\.]+(?:\s+[A-Z][a-zA-Zé\-À-ɏ\'\.]+)+)'
            r'(?:(?:[,;]\s*|\s+and\s+)([A-Z][a-zA-Zé\-À-ɏ\'\.]+(?:\s+[A-Z][a-zA-Zé\-À-ɏ\'\.]+)+))*'
            r'\s*$'
        )
        if name_pat.match(line):
            # Check it's not just a single word
            if ' ' in line and looks_like_authors(line):
                # Make sure the next few lines have affiliation-like content
                context = ' '.join(lines[i:i+5])
                if re.search(r'University|Institute|Department|College|School|Lab\b|Center|Centre|Faculty|Research|LLC|Inc\.|Corp\b', context, re.IGNORECASE):
                    return clean_name_list(line)

    return None

def read_pdf_authors(pdf_path):
    """Extract author text from a PDF file."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            if not pdf.pages:
                return None
            # Try first two pages
            for page in pdf.pages[:2]:
                text = page.extract_text()
                if text:
                    authors = extract_authors_from_text(text)
                    if authors:
                        return authors
    except Exception as e:
        return None
    return None

def main():
    with open(MISSING_FILE, encoding='utf-8') as f:
        missing = [l.strip() for l in f if l.strip().endswith('.md')]

    # Filter out junk files
    missing = [f for f in missing if not re.match(r'^\._\d*\.md$', f) and f not in ('._1.md', '._2.md', '._3.md', 'ğ.md')]

    print(f"Loading PDFs from {RESEARCH_DOCS}...")
    all_pdfs = get_all_pdfs()
    print(f"  Found {len(all_pdfs)} PDFs\n")

    updated = 0
    no_match = []
    no_authors = []

    for fname in sorted(missing):
        fpath = os.path.join(PAPERS_DIR, fname)
        if not os.path.exists(fpath):
            continue

        # Find best PDF match
        best_score = 0
        best_pdf = None
        for pdf in all_pdfs:
            s = score(fname, pdf)
            if s > best_score:
                best_score = s
                best_pdf = pdf

        if best_score < 0.60:
            no_match.append((fname, best_score, best_pdf))
            continue

        # Try to extract authors from PDF
        authors = read_pdf_authors(best_pdf)

        pdf_short = os.path.basename(best_pdf)[:60].encode('ascii', errors='replace').decode()
        fname_short = fname[:60].encode('ascii', errors='replace').decode()

        if not authors:
            no_authors.append((fname, best_pdf))
            print(f"  [NO AUTHORS] {fname_short}")
            print(f"               PDF: {pdf_short} (score={best_score:.2f})")
            continue

        # Write to vault note
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()

        new_text = insert_authors_field(text, authors)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_text)

        print(f"  [OK] {fname_short}")
        print(f"       PDF:  {pdf_short} ({best_score:.2f})")
        print(f"       Auth: {authors[:80].encode('ascii', errors='replace').decode()}")
        updated += 1

    print(f"\n{'='*60}")
    print(f"Updated: {updated}")
    print(f"No PDF match (score < 0.60): {len(no_match)}")
    print(f"PDF matched but no authors extracted: {len(no_authors)}")

    if no_match:
        print("\n--- NO MATCH ---")
        for fname, s, pdf in sorted(no_match, key=lambda x: -x[1]):
            safe = fname[:60].encode('ascii', errors='replace').decode()
            best = os.path.basename(pdf)[:40].encode('ascii', errors='replace').decode() if pdf else 'None'
            print(f"  {s:.2f}  {safe}  [best: {best}]")

    if no_authors:
        print("\n--- PDF MATCHED, NO AUTHORS EXTRACTED ---")
        for fname, pdf in no_authors:
            safe = fname[:60].encode('ascii', errors='replace').decode()
            print(f"  {safe}")

if __name__ == '__main__':
    main()
