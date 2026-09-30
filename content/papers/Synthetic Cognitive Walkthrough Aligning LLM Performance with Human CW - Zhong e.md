---
source_file: "synth users/Synthetic Cognitive Walkthrough Aligning LLM Performance with Human CW - Zhong et al - 2026.pdf"
type: paper
authors: "Performance with Human Cognitive Walkthrough"
community: "GenAI in UX and Design Practice"
tags:
---

# Synthetic Cognitive Walkthrough Aligning LLM Performance with Human CW - Zhong et al - 2026

## Summary
Synthetic Cognitive Walkthrough: Aligning Large Language Model’s Performance with Human Cognitive Walkthrough RUICAN ZHONG, University of Washington, USA DAVID W MCDONALD, University of Washington, USA GARY HSIEH, University of Washington, USA Conducting usability testing like cognitive walkthrough (CW) can be costly Recent developments in large language models (LLMs), with visual reasoning and UI navigation capabilities, present opportunities to automate CW.

## Key Concepts
- Synthetic cognitive walkthrough using LLMs (GPT-4 and Gemini-2.5-pro) to automate usability testing
- Four key CW questions: right result, notice action, associate action with result, see progress
- Task completion rate, path navigation patterns, and potential failure points as evaluation dimensions
- Breadth-first search (human) vs rational single-path selection (LLM) in navigation behavior
- Wizard-of-oz approach for early prototype evaluation using screenshots
- LLM optimized for performance vs simulating human behavior for usability testing
- Prompting strategies to align LLM behavior with human CW patterns

## Theoretical Framework
[[frameworks/Cognitive Walkthrough]] - Usability evaluation method focused on learnability

## Methods
comparative study, experimental

## Main Arguments
- LLMs can navigate interfaces and provide reasonable rationales but do not fully replicate human CW behavior
- LLMs outperform humans in task completion rates and follow more optimal navigation paths
- LLMs identify fewer potential failure points than humans in initial walkthroughs
- With additional prompting, LLMs can predict human-identified failure points and align performance
- Humans exhibit exploratory breadth-first search when uncertain; LLMs maintain rational single-path behavior
- LLMs can be leveraged for scaling usability testing if designers understand behavioral differences
- LLMs offer valuable complement to traditional usability testing rather than direct replacement

## Limitations & Critiques
- Manual setup of screen dataset required - not yet fully end-to-end automated (though tools like Claude computer use emerging)
- Only tested on mobile interfaces - web interfaces may exhibit different LLM behaviors
- LLM rational behavior may stem from training optimization rather than simulating human uncertainty
- Prompting to reduce randomness may have inadvertently suppressed exploratory behavior
- Does not address whether LLMs can replicate domain expert walkthroughs vs novice user behavior
- Limited discussion of cost-benefit analysis for LLM-based CW vs traditional methods
- No exploration of how LLM performance varies across interface complexity or task types

## Connections
- [[communities/GenAI in UX and Design Practice]] - Research community
