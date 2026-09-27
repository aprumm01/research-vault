---
source_file: "2026/i609-sustainability/Liu26.pdf"
type: paper
authors: "Yue Liu, Ratnadira Widyasari, Yanjie Zhao, Ivana Clairine Irsan, Junkai Chen, David Lo"
community: "Sustainable Computing"
tags: [sustainability, i609, AI-coding-assistants, technical-debt, code-quality, software-maintenance, empirical-study]
---

# Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild

## Summary

This paper presents the first large-scale empirical study examining technical debt introduced by AI coding assistants in production software repositories. The authors, Yue Liu, Ratnadira Widyasari, Ivana Clairine Irsan, Junkai Chen, and David Lo from Singapore Management University, along with Yanjie Zhao from Huazhong University of Science and Technology, address a critical gap in understanding the long-term maintenance costs of AI-assisted software development. Published on arXiv in April 2026, this research is timely given that the 2025 Stack Overflow Developer Survey found 84% of professional developers use or plan to use AI coding tools. The study analyzed 302.6K AI-authored commits from 6,299 GitHub repositories across five major AI coding assistants (GitHub Copilot, Claude, Cursor, Gemini, and Devin), identifying 484,366 distinct issues. The research is particularly significant for sustainable computing because it reveals hidden maintenance costs that accumulate over time: 22.7% of tracked AI-introduced issues still survive at the latest repository revision, including issues introduced more than nine months earlier. This represents a previously unquantified form of technical sustainability debt that affects the long-term viability of software systems.

## Research Overview

The study addresses three interconnected research questions: "RQ1: What kinds of technical debt are introduced by AI coding assistants?" "RQ2: How does technical debt vary across AI coding assistants?" and "RQ3: To what extent does AI-introduced technical debt persist in the codebase?" (Liu et al., 2026, p. 5). The methodology employs a three-stage approach: (1) data collection using GitHub Archive and BigQuery to identify AI-authored commits through Git metadata signals, (2) commit-level quality analysis using static analysis tools (ESLint for JavaScript/TypeScript, Pylint for Python, Semgrep for security), and (3) debt lifecycle analysis tracking issues from introduction to resolution. The key innovation is differential attribution: "For each AI-authored commit c, we analyze two versions of the source code: the version at c's parent commit (before) and the version at c itself (after)" (Liu et al., 2026, p. 4). Technical debt is operationalized through three categories: code smells (maintainability problems), correctness issues (code defects causing failures), and security issues (vulnerabilities and insecure patterns). The study tracks issue survival by checking "whether it still exists at the repository's latest revision (i.e., HEAD)" (Liu et al., 2026, p. 5).

## Theoretical Framework

The study draws on the established concept of technical debt, defined as "design or implementation choices that prioritize short-term speed over long-term quality" (Liu et al., 2026, p. 2). The authors cite Cunningham's original framing that "these shortcuts may help in the short term, but they increase the future cost of maintaining and evolving the software" (Liu et al., 2026, p. 2). The research extends the concept of self-admitted technical debt (SATD), "which studies the subset of technical debt that developers explicitly document" (Liu et al., 2026, p. 11), to AI-attributed technical debt where AI involvement is explicitly visible in Git metadata. Key theoretical constructs include: code smells as "maintainability problems that make code harder to understand, debug, and evolve" (Liu et al., 2026, p. 6); correctness issues as "code defects that can cause the program to fail during execution" (Liu et al., 2026, p. 7); and survival rate as the proportion of introduced issues that persist to the current codebase state. The framework acknowledges that "AI-assisted code and human-written code are often interleaved during development, and AI usage is not always explicitly recorded in the repository history" (Liu et al., 2026, p. 2).

## Central Arguments

The paper advances a central thesis that AI coding assistants systematically introduce technical debt into production codebases, creating hidden long-term maintenance costs. The main argument is articulated as: "AI-generated code introduces technical debt in the form of code smells (89.3%), correctness issues (6.0%), and security issues (4.7%). Among them, code smells are by far the most common" (Liu et al., 2026, p. 8).

**Sub-claim 1 - Pervasiveness**: "More than 15% of commits from every AI coding assistant introduce at least one issue, although the rates vary across tools" (Liu et al., 2026, p. 8). The rates range from 17.4% for GitHub Copilot to 29.1% for Gemini.

**Sub-claim 2 - Consistency across tools**: "Technical debt patterns vary across AI coding assistants, but the overall trend is consistent. Across all five tools, code smells remain the dominant form of AI-introduced debt" (Liu et al., 2026, p. 8). Claude has the highest issue rate per commit (1.95), while Devin has the lowest (0.89).

**Sub-claim 3 - Persistence**: "AI-authored commits fix slightly more code smells than they introduce, but introduce more correctness and security issues than they fix. Overall, 22.7% of tracked AI-introduced issues still survive at HEAD, including issues introduced more than nine months earlier" (Liu et al., 2026, p. 9). The net impact shows AI reduces code smells by 7,069 but increases correctness issues by 3,742 and security issues by 7,342.

**Sub-claim 4 - Systemic nature**: "Technical debt cannot be solved by switching between AI coding tools. Our cross-tool comparison shows that this problem cannot be solved simply by switching from one assistant to another" (Liu et al., 2026, p. 10).

## Evidence

The study provides robust quantitative evidence across multiple dimensions.

**Dataset scale**: "Our final analysis dataset therefore includes 6,299 public GitHub repositories with 302.6K analyzed AI-attributed commits" (Liu et al., 2026, p. 5). Table I shows distribution: GitHub Copilot (118,012 commits), Claude (138,249), Cursor (19,587), Gemini (12,429), and Devin (14,302).

**Issue prevalence**: "In total, we identified 484,366 introduced issues across 3,946 repositories (62.6% of 6,299 repositories) and 27,677 commits (9.1% of 302,579 commits)" (Liu et al., 2026, p. 6). Table II breaks down by type: Code Smells (432,748 issues, 89.3%), Correctness Issues (28,931, 6.0%), Security Issues (22,687, 4.7%).

**Net impact analysis**: Figure 8 demonstrates that while AI-authored commits fix 439,817 code smells, they introduce 432,748, yielding a net reduction of 7,069. However, for correctness issues (25,189 fixed vs. 28,931 introduced = net +3,742) and security issues (15,345 fixed vs. 22,687 introduced = net +7,342), AI introduces more problems than it resolves.

**Survival analysis**: "Overall, 105,364 out of 464,900 tracked AI-introduced issues still survive at HEAD, corresponding to a survival rate of 22.7%" (Liu et al., 2026, p. 9). Table VI shows survival varies by age: issues older than 9 months have 22.8% survival, 6-9 months show 19.4%, 3-6 months show 28.2%, and issues under 3 months show 21.3%.

**Validation**: "For issue validity, the raw agreement was 95/99 = 0.960, with Cohen's kappa = 0.851, indicating almost perfect agreement. For survival classification, the raw agreement was 97/99 = 0.980, with Cohen's kappa = 0.960" (Liu et al., 2026, p. 6).

**Limitations**: The study acknowledges that it "focuses on public GitHub repositories with at least 100 stars and production source files in Python, JavaScript, and TypeScript" (Liu et al., 2026, p. 11) and may not generalize to private repositories or other languages. Additionally, "AI-assisted contributions that leave no such trace are outside the scope of our dataset" (Liu et al., 2026, p. 11).

## Conclusion

This study fundamentally reframes the sustainability implications of AI-assisted software development. The key insight for long-term recall is that AI coding tools trade immediate productivity gains for accumulated maintenance burden, with over one-fifth of introduced issues persisting indefinitely. The cumulative number of surviving issues "keeps growing over time, climbing from just a few hundred issues in early 2025 to over 100k surviving issues by February 2026" (Liu et al., 2026, p. 9). For practitioners, this means that "developers should not treat all AI-generated code as equally trustworthy, and they should pay particular attention to changes that may introduce correctness or security vulnerabilities" (Liu et al., 2026, p. 10). The finding that switching between tools does not solve the problem suggests this is a systemic characteristic of current AI coding technology. From a sustainability perspective, this technical debt represents ongoing computational and human resource costs that compound over time. Future research should examine "what factors make AI-introduced debt more likely to persist (e.g., repository maturity, review intensity, or task type)" (Liu et al., 2026, p. 11) and extend analysis to architectural, documentation, and test-related debt.

## APA Citation

Liu, Y., Widyasari, R., Zhao, Y., Irsan, I. C., Chen, J., & Lo, D. (2026). Debt behind the AI boom: A large-scale empirical study of AI-generated code in the wild. *arXiv preprint arXiv:2603.28592v2*. https://arxiv.org/abs/2603.28592

## Discussion Questions

1. The study found that AI coding assistants fix more code smells than they introduce but create net increases in correctness and security issues. What does this pattern suggest about the fundamental capabilities and limitations of current large language models for code generation?

2. Given that 22.7% of AI-introduced issues survive indefinitely, how should organizations factor this hidden maintenance cost into their ROI calculations for AI coding tool adoption?

3. The paper shows that Claude has the highest issue rate per commit (1.95) while also being a top contributor. How should development teams balance the productivity benefits of AI assistance against the quality risks identified in this study?

4. From a sustainability perspective, how might the accumulating technical debt from AI-generated code affect the long-term energy consumption of software systems through increased debugging, refactoring, and security remediation cycles?

## Connections

- [[topics/Sustainable Computing]]
- [[topics/Software Engineering]]
- [[topics/AI Coding Assistants]]
- [[topics/Technical Debt]]
- [[communities/Sustainable Computing]]
- [[topics/Code Quality]]
