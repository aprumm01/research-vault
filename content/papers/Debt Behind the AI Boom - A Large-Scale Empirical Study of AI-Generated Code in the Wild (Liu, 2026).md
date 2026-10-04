---
title: "Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/Liu26.pdf"
type: paper
authors:
  - Yue Liu
  - Ratnadira Widyasari
  - Yanjie Zhao
  - Ivana Clairine Irsan
  - Junkai Chen
  - David Lo
year: 2026
venue: "arXiv preprint (arXiv:2603.28592v2)"
builds_on:
  - "[[Technical Debt]]"
  - "[[Code Quality]]"
  - "[[AI Code Generation]]"
  - "[[Software Maintenance]]"
supports:
  - "[[AI-Assisted Development]]"
  - "[[Static Analysis]]"
critiques:
  - "[[AI Coding Assistants]]"
  - "[[Developer Trust in AI]]"
tensions_with:
  - "[[AI Productivity Benefits]]"
key_claims:
  - "AI coding assistants introduce technical debt in 89.3% code smells, 6.0% correctness issues, and 4.7% security issues"
  - "More than 15% of commits from every AI coding assistant introduce at least one issue"
  - "22.7% of tracked AI-introduced issues still survive at the latest repository revision"
  - "AI commits fix more code smells than they introduce, but introduce more correctness and security issues than they fix"
  - "Claude has the highest issue rate per commit (1.95) while Devin has the lowest (0.89)"
methodology: "Large-scale empirical study using static analysis (ESLint, Pylint, Semgrep) on commit-level differential analysis"
study_type: empirical
context: "Analysis of 302.6K AI-authored commits from 6,299 GitHub repositories across five AI coding assistants (GitHub Copilot, Claude, Cursor, Gemini, Devin)"
---

## Summary

This paper presents the first large-scale empirical study of technical debt introduced by AI coding assistants in production repositories. The authors analyze 302.6K verified AI-authored commits from 6,299 GitHub repositories, covering five major AI coding assistants: GitHub Copilot, Claude, Cursor, Gemini, and Devin. Using static analysis tools (ESLint for JavaScript/TypeScript, Pylint for Python, and Semgrep for security), they perform commit-level differential analysis to precisely attribute code smells, correctness issues, and security issues to individual AI-authored commits.

The study's key contribution is tracking the lifecycle of AI-introduced issues from introduction to either resolution or persistence at HEAD. This longitudinal approach reveals that while AI assistants can fix existing issues, they also introduce new technical debt that often persists in production codebases.

## Key Concepts

- **Technical Debt**: Design or implementation choices that prioritize short-term speed over long-term quality, increasing future maintenance costs
- **AI Attribution Rules**: Methods to identify AI-authored commits using Git metadata (actor logins, author emails, author names, Co-authored-by trailers)
- **Commit-Level Differential Analysis**: Comparing code before and after each AI-authored commit to identify introduced vs. fixed issues
- **Debt Lifecycle Analysis**: Tracking whether AI-introduced issues persist or get resolved over time
- **Survival Rate**: Percentage of AI-introduced issues that still exist at the repository's latest revision (HEAD)

## Key Findings

### RQ1: Types and Patterns of AI-Introduced Debt
- **484,366 total issues** identified across 3,946 repositories (62.6% of all repos) and 27,677 commits (9.1% of commits)
- Distribution: **89.3% code smells**, **6.0% correctness issues**, **4.7% security issues**
- Top code smells: broad exception handling (8.5%), unused variables/parameters (5.8%), unused arguments (5.0%)
- Top correctness issues: undefined variable/reference (4.9%), redeclared symbol (0.4%)
- Top security issues: path traversal via path.join/resolve (1.8%), unsafe format strings (1.0%)

### RQ2: Comparison Across AI Coding Assistants
- All five tools introduce similar patterns of technical debt
- **>15% of commits** from every tool introduce at least one issue
- Issue rates vary: GitHub Copilot (17.4%), Claude (24.4%), Cursor (25.7%), Gemini (29.1%), Devin (23.8%)
- Issues per commit: Claude highest (1.95), Devin lowest (0.89)

### RQ3: Persistence of AI-Introduced Debt
- **Net impact**: AI fixes 7,069 more code smells than it introduces, but introduces 3,742 more correctness issues and 7,342 more security issues than it fixes
- **22.7% survival rate**: 105,364 of 464,900 tracked issues still survive at HEAD
- Issues persist across all age cohorts, including issues >9 months old
- Cumulative surviving issues grew from hundreds in early 2025 to over 100K by February 2026

### Programming Language Differences
- Python: dominated by exception handling and dynamic typing issues
- JavaScript/TypeScript: dominated by scoping and variable declaration patterns
- Code smells are the most common issue type in both languages

## Relevance to Sustainable Computing

This research has significant implications for sustainable computing and software development practices:

1. **Hidden Maintenance Costs**: The persistent accumulation of AI-introduced technical debt represents hidden long-term costs that are not captured in short-term productivity metrics. Organizations must account for these costs when evaluating AI-assisted development.

2. **Quality vs. Speed Tradeoff**: The study reveals a tension between AI's productivity benefits and its quality implications. While AI accelerates development, it also introduces debt that requires human effort to remediate.

3. **Resource Implications**: Security and correctness issues that persist in production can lead to vulnerabilities, outages, and remediation efforts that consume computational and human resources.

4. **Sustainable AI Adoption**: The findings suggest that sustainable adoption of AI coding assistants requires:
   - Stronger code review practices for AI-generated code
   - Enhanced static analysis and security checks in CI/CD pipelines
   - Developer awareness that AI-generated code requires the same scrutiny as human-written code
   - Tool improvements to catch quality issues before code is merged

5. **Long-term Codebase Health**: The 22.7% survival rate of AI-introduced issues suggests that without deliberate intervention, AI-assisted development can degrade codebase health over time, creating sustainability challenges for software projects.

## Citation (APA)

Liu, Y., Widyasari, R., Zhao, Y., Irsan, I. C., Chen, J., & Lo, D. (2026). Debt behind the AI boom: A large-scale empirical study of AI-generated code in the wild. *arXiv preprint arXiv:2603.28592*.
