---
source_file: Does Ai Development Polarized Job Market Evidence from Dynamic Panel
  Analysis.pdf
type: paper
authors: Evidence from Dynamic Panel Analysis
community: AI and Future of Work
tags: null
year: 2024
builds_on:
- '[[frameworks/Sociotechnical]]'
- '[[concepts/Technological Determinism]]'
critiques: []
tensions_with: []
supports:
- '[[concepts/Technological Unemployment]]'
key_claims:
- AI development measured by patents has statistically significant positive effect
  on unemployment, with two-step GMM coefficient showing increased AI innovation associates
  with higher unemployment rates
- 85 million job positions will face displacement because of artificial intelligence
  by 2025, while simultaneously generating 97 million new roles primarily requiring
  advanced technology skills in data science, machine learning, and engineering
- Labor market hysteresis exists with lagged unemployment rate (coefficient 0.181,
  p<0.001) significantly affecting current unemployment, demonstrating persistence
  in unemployment patterns
- R&D expenditure shows insignificant effect on unemployment, suggesting current innovation
  is more automation-intensive than labor-augmenting
- Industries with high AI-related patenting experience lower employment growth, confirming
  labor-substitution effects particularly in economies with poor reskilling infrastructure
methodology: '[[methods/Meta-Analysis]]'
sample_size: 69
sample_type: countries with macroeconomic panel data
context: Global labor markets across developed and developing nations, 2000-2022
study_type: empirical
---

# Does Ai Development Polarized Job Market Evidence from Dynamic Panel Analysis

## Summary
The research examines how artificial intelligence affects unemployment patterns by employing modern statistical methods with macroeconomic information. The study utilizes Generalized Method of Moments (GMM) techniques for data analysis using data ranging from 2000 to 2022 covering 69 countries. The findings suggest that a total of 85 million job positions will face displacement because of artificial intelligence in 2025, while the technology will simultaneously generate more than 95 million new roles that primarily require advanced technology skills in data science, machine learning, and engineering fields. The research argues that employers need to invest in workforce training programs and reskilling efforts that enable workers to handle innovative changes while ensuring they obtain job security. The study demonstrates the significance of theoretical frameworks including technological determinism and job polarization to comprehend how AI leads to job displacement effects.

## Key Concepts
- [[Job polarization]] - Disappearance of middle-wage jobs while high and low-wage positions grow
- [[Technological unemployment]] - Job displacement resulting from AI replacing routine and intellectual tasks
- [[Labor market hysteresis]] - Past unemployment rates directly affecting present unemployment levels
- [[Technological determinism]] - Technology as shaping force in culture and society
- [[Creative destruction]] - Automation as force that transforms rather than eliminates jobs
- [[Reinstatement effect]] - Positive spillover effects from automation that can offset job losses
- [[Workforce reskilling]] - Training programs to adapt workers to AI-driven job requirements
- [[AI patent innovation]] - Metric for measuring AI development and adoption across countries

## Theoretical Framework
- [[Technological Determinism Theory]] - Society's use of technology reveals its underlying characteristics (Veblen; Biannually, 2024)
- [[Job Polarization Theory]] - Middle-class employment disappearing while high and low-wage jobs grow (Goos & Manning, 2007; Acemoglu & Autor, 2011)
- [[Schumpeterian creative destruction]] - Automation viewed as transformative force rather than pure job eliminator
- [[Labor market hysteresis theory]] - Persistence of unemployment effects over time (Nickell, 1986)

## Methods
- Generalized Method of Moments (GMM) - One-step and two-step estimators
- Dynamic panel data analysis with panel data from 69 countries (2000-2022)
- Control variables: GDP growth, R&D expenditure, population growth, foreign direct investment
- Independent variable: AI patents (logAIP) as proxy for AI development
- Post-estimation diagnostics: Arellano-Bond AR tests, Hansen test, Sargan test
- Robustness checks using pooled OLS, fixed effects, and random effects models

## Main Arguments
- AI development measured by patents has statistically significant positive effect on unemployment, indicating increased AI innovation associates with higher unemployment (two-step GMM coefficient significant)
- AI primarily displaces workers by replacing routine and intellectual tasks during early adoption phases, creating technological unemployment
- The study finds evidence of labor market hysteresis - lagged unemployment rate (0.181***) significantly affects current unemployment, showing persistence in unemployment patterns
- While AI may displace 85 million jobs by 2025, it simultaneously creates 95 million new positions requiring advanced technical skills in data science, ML, and engineering
- R&D expenditure shows insignificant effect on unemployment, suggesting current innovation is more automation-intensive than labor-augmenting
- Job displacement effects are strongest in economies with poor reskilling infrastructure and lag in educational/institutional adjustment
- The relationship between AI and unemployment is more complex in two-step GMM than one-step, suggesting endogeneity issues that require careful modeling
- Industries with high AI-related patenting experience lower employment growth, confirming labor-substitution effects
- Policymakers must implement decisive strategies including digital skills programs, adaptive education systems, and targeted upskilling to ensure AI benefits don't come at cost of structural unemployment

## Limitations & Critiques
- Preprint status - paper has not been peer reviewed, limiting validation of findings
- AI patents as sole proxy for AI development may not capture full scope of AI adoption (excludes proprietary corporate AI without patents)
- Static approach in robustness checks (pooled OLS, fixed/random effects) less suitable for dynamic phenomena than GMM
- Limited discussion of sectoral variation - treats all industries uniformly despite different AI adoption rates
- Control variables incomplete - missing industry sector specifications and place-based economic conditions
- Temporal dynamics insufficiently explored - findings are somewhat static despite using dynamic panel methods
- Model sensitivity between one-step and two-step GMM suggests potential specification issues
- No explicit treatment of AI regulation or intellectual property frameworks mentioned as research gap but not addressed in analysis
- Geographic scope (69 countries) includes developed and developing nations but doesn't adequately account for structural differences in labor markets
- Short-term vs long-term effects not clearly distinguished - displacement may be temporary adjustment period

## Connections
- [[communities/AI and Future of Work]] - Research community
