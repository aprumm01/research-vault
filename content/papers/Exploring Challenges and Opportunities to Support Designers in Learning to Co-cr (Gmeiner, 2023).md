---
source_file: hiring and org practice/Exploring Challenges and Opportunities to Support
  Designers in Learning to Co-create with AI-based Manufacturing Design Tools.pdf
type: paper
authors: Frederic Gmeiner
community: GenAI in UX and Design Practice
tags: null
year: 2023
builds_on:
- '[[frameworks/Situated Cognition]]'
- '[[concepts/Human-AI Co-creation]]'
- '[[frameworks/Activity Theory]]'
critiques: []
tensions_with:
- '[[concepts/Democratization of Design]]'
supports:
- '[[concepts/Human-AI Co-creation]]'
- '[[concepts/Explainable AI]]'
- '[[concepts/Cognitive Tension]]'
- '[[concepts/Metacognitive Laziness]]'
- '[[concepts/Deep Learning (Educational)]]'
key_claims:
- Most designers failed to produce satisfying designs in 30-minute sessions despite
  familiarity with task types, suggesting AI assistance introduces new challenges
  rather than simplifying work
- Successful designers learned by systematically testing tool capability boundaries
  early, self-explaining observed AI behaviors to build mental models, and sketching/reflecting
  on design issues outside the AI system
- AI co-creation tools operate as black boxes where designers set objectives then
  review generated designs without understanding internal processes, creating significant
  barriers to developing shared mental models
- Current AI design tools fail to support key collaboration mechanisms from human-human
  collaboration theory, particularly grounding in communication and contextual awareness
- Effective human guidance for AI tool learning requires multi-modal communication
  strategies including screen annotations and mouse gesturing, combined with active
  facilitation through step-by-step instructions and reflection prompts
methodology: '[[methods/Mixed Methods]]'
sample_size: 19
sample_type: trained designers (12 mechanical engineers, 7 architecture/industrial
  designers) without prior AI co-creation experience
context: Think-aloud design sessions using professional AI-based manufacturing design
  tools (Autodesk Fusion360 and SimuLearn)
study_type: empirical
---

# Exploring Challenges and Opportunities to Support Designers in Learning to Co-create with AI-based Manufacturing Design Tools

## Summary
AI-based design tools are proliferating in professional software to assist engineering and industrial designers in complex manufacturing and design tasks. These tools take on more agentic roles than traditional CAD tools and are portrayed as “co-creators.” Through think-aloud studies observing trained designers learning to work with two AI-based tools (Autodesk Fusion360 Generative Design and SimuLearn) on realistic design tasks, this research finds that designers faced significant challenges in understanding AI outputs, communicating design goals, and effectively co-creating. Successful designers learned by systematically testing tool capabilities early, self-explaining AI behaviors, and sketching/reflecting on design issues. Follow-up study with human guides revealed effective support strategies including step-by-step instructions, prompting reflection, and multi-modal communication. Designers expressed desires for more conversational interactions and contextual awareness from AI tools.

## Key Concepts
- Computational co-creation - designers working collaboratively with AI agents that take active autonomous roles in design process
- Generative design tools - AI systems generating design options based on constraints and objectives using topology optimization, genetic algorithms, constraint-based solvers
- Grounding in communication - creating mutual sense through verbal and non-verbal communication between collaborators
- Shared mental models - shared representations of task, abilities/limitations, goals and strategies enabling effective collaboration
- Team learning - study of what actions and conditions contribute to how groups learn to effectively collaborate
- Advanced manufacturing - emerging processes like shape-changing materials requiring AI assistance due to complexity
- Black box interaction - AI tools operating opaquely where designers set objectives then review generated designs without understanding internal processes
- Self-directed learning - learning approach for complex software through trial and error, web forums, and knowledgeable colleagues

## Theoretical Framework
**Group Cognition and Human-Human Collaboration**: Study draws on theories of human-human collaboration to inform human-AI co-creation, including:
- Grounding in communication (creating mutual understanding through verbal/non-verbal communication)
- Theory of mind (awareness of own and others' beliefs, intentions, knowledge, perspectives)
- Shared mental models (shared representations of task, abilities, goals, strategies)
- Adaptive coordination of actions among team members

**Team Learning**: Framework studying what actions help people learn to collaborate effectively, including:
- Active negotiation processes involving constructive conflict, argumentation, and resolution
- Joint information processing
- Coordination of actions
- Development of shared mental models through negotiation between team members

**Design Process Theory**: Recognition that design problems are ill-defined requiring teams to navigate problem and solution spaces through iterative process of generating ideas, building prototypes, and testing.

## Methods
**Study 1: Think-Aloud Design Sessions**

**Participants**: 19 trained designers (12 mechanical engineers, 7 architecture/industrial designers) without prior AI co-creation experience

**Tasks**: 
- Engine bracket task: Mechanical engineers designed light/strong mounting bracket for ship engine using Autodesk Fusion360 Generative Design (topology optimization generating multiple options)
- Bottle holder task: Architecture/industrial designers created bottle holder from shape-changing materials using SimuLearn (ML-based research tool built on Rhino3d)

**Procedure**: 
- 30-minute moderated think-aloud session with observation
- Semi-structured retrospective interview
- Task completion times: Engine bracket 54-160 minutes (M=104), Bottle holder 63-255 minutes (M=154)

**Data Collection**:
- Video/audio recordings and machine-generated transcripts of think-aloud sessions
- Audio recordings and transcripts of post-task interviews
- 3D designs created during sessions

**Analysis**:
- Reflexive thematic analysis using iterative inductive coding and affinity diagramming (ATLAS.ti)
- Tracking of feature usage and parameter specification patterns across iterations
- Assessment of design outcomes against requirements

**Study 2: Human-Human Collaboration Study** (mentioned but details not fully extracted in sample)
- Observed how human guides assisted new users of AI tools in learning to co-create
- Identified effective support strategies

## Main Arguments
- AI co-creation tools present significant learning curve despite designers valuing AI assistance - most participants failed to produce satisfying designs even when familiar with task type, suggesting AI assistance introduces new challenges rather than simplifying work
- Effective co-creation with AI requires different skills than working with complex CAD tools alone - particularly developing shared mental models with non-human collaborators operating as black boxes
- Successful learning strategies involve: (1) systematically testing tool capability boundaries early, (2) self-explaining observed AI behaviors to build mental models, (3) sketching and reflecting on design issues outside the AI system
- Human-human collaboration theories (grounding, shared mental models, team learning) provide valuable but underutilized lenses for designing human-AI co-creation support
- Current AI design tools fail to support key collaboration mechanisms - designers wished for more conversational interactions, contextual awareness, and clearer communication pathways for design goals
- Supporting human-AI co-creation learning requires multi-modal communication strategies (screen annotations, mouse gesturing) and active facilitation (step-by-step instructions, reflection prompts, alternative strategy suggestions)

## Limitations & Critiques
**Study Design Limitations**:
- Think-aloud method may not capture all cognitive processes or may alter natural work patterns
- Limited to novice users without prior AI co-creation experience - may not reflect experienced users' strategies
- Two specific tools (Fusion360, SimuLearn) in manufacturing domain may not generalize to other AI design contexts
- Relatively small sample (19 participants) limits statistical generalizability
- Short 30-minute sessions may not allow sufficient time for deeper learning

**Task and Context Limitations**:
- Realistic but constrained design tasks may not reflect full complexity of professional design work
- No longitudinal observation of learning over extended time periods
- Laboratory setting may not capture organizational or team dynamics present in professional contexts
- Focus on individual learning may miss collaborative team learning dynamics

**Analysis Limitations**:
- Reflexive thematic analysis is interpretive and dependent on researchers' perspectives
- No quantitative validation of identified challenges or success patterns
- Limited exploration of how different designer backgrounds (engineering vs architecture/industrial) may require different support approaches

**Theoretical Gaps**:
- Paper acknowledges but does not fully resolve tension between human-human collaboration theories and unique characteristics of AI collaborators
- Limited discussion of when/whether AI should behave like human collaborators vs embracing different interaction paradigms

## Connections
- [[communities/GenAI in UX and Design Practice]] - Research community
