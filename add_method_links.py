"""Add method wikilinks to papers' Connections sections."""
import os
import re

PAPERS_DIR = os.path.join('.', 'content', 'papers')

# Map: paper filename -> list of method wikilinks to add
ADDITIONS = {
    "Synthetic Heuristic Evaluation AI vs Human-Powered Usability (Zhong et al., 2025).md": [
        "Heuristic Evaluation",
    ],
    "Synthetic Cognitive Walkthrough Aligning LLM Performance with Human CW (Zhong et al., 2026).md": [
        "Cognitive Walkthrough",
    ],
    "Avenir-UX Automated UX Evaluation via Simulated Human Web Interaction with GUI Grounding (Tan et al., 2026).md": [
        "Think Aloud Protocol",
    ],
    "Agent AB Automated and Scalable AB Testing on Live Websites with LLM Agents (Lu et al., 2025).md": [
        "A/B Testing",
        "Behavioral Trace Analysis",
    ],
    "SimAB Simulating AB Tests with Persona-Conditioned AI Agents (Rieder et al., 2026).md": [
        "A/B Testing",
    ],
    "Mind the Sim2Real Gap in User Simulation for Agentic Tasks (Zhou et al., 2026).md": [
        "Behavioral Trace Analysis",
    ],
    "UXAgent A System for Simulating Usability Testing of Web Design with LLM Agents (Lu et al., 2025).md": [
        "Heuristic Evaluation",
        "Behavioral Trace Analysis",
    ],
    "UXAgent An LLM-Agent-Based Usability Testing Framework for Web Design (Lu et al., 2025).md": [
        "Heuristic Evaluation",
        "Behavioral Trace Analysis",
    ],
    "UXCascade Scalable Usability Testing with Simulated User Agents (Holter et al., 2026).md": [
        "Heuristic Evaluation",
    ],
    "LLM Agent Meets Agentic AI Can LLM Agents Simulate Customers (Sun et al., 2025).md": [
        "Behavioral Trace Analysis",
    ],
}

ANCHOR = "- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]"

for fname, methods in sorted(ADDITIONS.items()):
    fpath = os.path.join(PAPERS_DIR, fname)
    if not os.path.exists(fpath):
        print(f"NOT FOUND: {fname[:60]}")
        continue
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        text = f.read()

    # Skip if already has the first method link
    if f"[[{methods[0]}]]" in text:
        print(f"SKIP (already present): {fname[:60]}")
        continue

    # Build insertion lines
    new_lines = "\n".join(f"- [[{m}]] - `` [EXTRACTED]" for m in methods)

    if ANCHOR in text:
        new_text = text.replace(ANCHOR, ANCHOR + "\n" + new_lines)
    else:
        # Fallback: append to Connections section
        new_text = text + "\n" + new_lines

    with open(fpath, 'w', encoding='utf-8-sig') as f:
        f.write(new_text)

    short = fname[:65].encode('ascii', errors='replace').decode()
    print(f"  [OK] {short}")
    for m in methods:
        print(f"       + [[{m}]]")

print("\nDone.")
