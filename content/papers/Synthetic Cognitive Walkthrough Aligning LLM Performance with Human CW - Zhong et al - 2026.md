# Synthetic Cognitive Walkthrough: Aligning Large Language Model's Performance with Human Cognitive Walkthrough

**Authors:** Ruican Zhong, David W. McDonald, Gary Hsieh  
**Affiliation:** University of Washington  
**Year:** 2026  
**Type:** Empirical Research Paper  
**Field:** Human-Computer Interaction, Usability Evaluation, AI Agents

---

## Overview of the Document

This paper explores whether Large Language Models can automate cognitive walkthrough (CW), one of the most rigorous usability evaluation methods in HCI. The research team from University of Washington addresses a fundamental question: can LLMs not just navigate interfaces but *evaluate* them in ways comparable to human evaluators—identifying failure points, assessing learnability, and providing actionable insights about interface design?

The motivation is practical: cognitive walkthrough is powerful but expensive. Traditional CW requires expert evaluators to systematically step through interfaces, thinking aloud about whether users would understand how to accomplish tasks. This process reveals usability issues early, when they're still inexpensive to fix. But recruiting, scheduling, compensating, and working with evaluators requires significant time and resources—creating a bottleneck that often leads teams to skip rigorous evaluation entirely.

The research is grounded in comparative empirical analysis rather than theoretical claims. The authors test LLM-prompted cognitive walkthrough against 10 human evaluators on two mobile applications (a language learning app and a booking app), analyzing task completion rates, navigation path alignment, and—critically—whether LLMs identify the same failure points humans would notice. They test two state-of-the-art models (GPT-4 and Gemini-2.5-pro) across 6 user tasks per app, producing 16 LLM runs compared against human baseline.

The findings reveal a nuanced picture: LLMs achieved higher task completion rates than humans (100% for GPT-4, 97.2% for Gemini vs. 88.2% for humans) and followed more optimal navigation paths. However, LLMs identified only 3 failure points compared to humans' aggregated 5—suggesting they navigate *too successfully*, missing the struggles that reveal learnability issues. Behavioral analysis shows humans conduct breadth-first search when uncertain (exploring multiple options before committing), while LLMs make mistakes from memory issues or looping, representing fundamentally different failure modes.

---

## Research Overview

**Central Research Question:** Can LLMs simulate human behavior in cognitive walkthrough to identify comparable usability issues, and how do their navigation patterns and failure identification differ from human evaluators?

The research doesn't ask whether LLMs can *complete tasks* (prior work established they can navigate interfaces). Instead, it asks whether LLMs can *evaluate learnability* the way CW demands—assessing whether typical users would understand the interface without getting lost or confused.

**Cognitive Walkthrough Methodology:**

CW is specifically focused on how users navigate systems and accomplish tasks through interface exploration. Unlike heuristic evaluation (which uses general principles to identify problems), CW evaluates the overall user journey through assessing whether users can accomplish intended tasks.

The method requires evaluators to "walkthrough" the interface asking four key questions at each step:
1. Will users try to achieve the right result?
2. Will users notice that the correct action is available?
3. Will users associate the correct action with the result they're trying to achieve?
4. After the action is performed, will users see that progress is made toward the goal?

Throughout this process, evaluators think-aloud, making their reasoning visible. The data collected enables researchers to uncover:
- How users conceptualize the design
- Whether task completion success rates are ultimately understandable
- Whether users' paths align with correct/optimal paths
- **Potential failure points** that reflect usability issues

The third dimension—failure points—contributes significantly to evaluation value, as these directly identify potential breakdowns in interface learnability.

**Two-Agent Pipeline Design:**

To automate CW, the researchers designed two AI agents mimicking the roles typical of CW sessions:

**1. Facilitator Agent:** Acts as researcher, guiding the evaluator through the CW session. Ensures the evaluator provides formatted output and specific insights. Provides guidance when evaluators are stuck, conduct repeated actions, or feel uncertain about next steps. Also helps select appropriate screenshots to present based on evaluator actions—pulling from a pre-compiled database of app screens and navigation transitions.

The facilitator implements a fail-safe mechanism: when a loop is detected (evaluator stuck), it automatically sends: "The action you provided is not available on the screen or would not result in an available action here. Please revise your action." This helps the agent break out of loops, similar to how human facilitators guide sessions.

**2. Evaluator Agent:** Performs the role of the potential interface user, navigating through the interface with think-aloud articulation. Given screens of an app and a user task, analyzes and determines where to interact next to complete the user task and provides rationale for actions.

The prompt design went through iterative refinement:

*Initial naive version:* "Act as a facilitator in a CW and provide guidance to users as they explore an interface." This failed because evaluators didn't provide enough explanation, and facilitators couldn't provide additional guidance when evaluators got stuck.

*Improved version with loop detection:* Adding instructions for evaluators to first identify all plausible next steps, rate likelihood of each option, then decide. This mechanism of "thinking through all possibilities before deciding" produced substantial performance improvement.

*Final version with confusion handling:* Additional instructions noting that if seeing the same screens repeatedly, it means looping and should consider other options. This modification produced stable, reasonable performance.

**Study Design:**

**Apps Selected:** Two mobile applications representing commonly used categories:
- **Language learning app** (Lifestyle category): 5 user tasks
- **Booking app** (Education category): 5 user tasks  

Total of 6 tasks curated (varying difficulty, 1-38 steps, average 7.4 steps). Authors surveyed correct path sets containing all possible pathways users could take to accomplish tasks—this serves as reference for comparing navigation paths.

**LLM Evaluation:** Testing GPT-4 (OpenAI) and Gemini-2.5-pro (Google):
- GPT-4: 5 runs per task on language app, 5 runs per task on booking app (16 total runs)
- Gemini-2.5-pro: 3 runs per task on each app (12 total runs)

**Human Evaluation:** 10 participants recruited via social media, no prior CW experience required:
- 5 assigned to language app, 5 to booking app
- Demographics: Age 18-23 (majority), 4 men/5 women/1 nonconforming
- 8/10 reported frequent use of similar apps (at least 2-5 times/month)
- No prior experience with tested apps
- Sessions conducted via Zoom, recorded and transcribed, ~55 minutes each
- Compensation: $25 per participant

---

## Theories of Knowledge

The paper builds on intersecting research areas: cognitive walkthrough methodology, automated usability evaluation, UI understanding and navigation with AI, and user simulation.

**Cognitive Walkthrough as Formative Evaluation:** CW emerged as a usability inspection method focused on learnability. Unlike summative methods that measure final outcomes, CW provides formative insights during development—identifying where users would struggle *before* deployment. The method can be conducted with early prototypes using screenshots via wizard-of-oz approaches where facilitators present appropriate screens given evaluators' interactions.

As CW and other usability methods became increasingly utilized in human-centered design, researchers explored automation strategies. In a 2001 review, Ivory and Hearst found automation greatly underexplored: of about 110 evaluated usability methods, only 33% had any automation support. For CW specifically, only one tool existed—software to assist with documentation—and full automation required formal interface specifications. The challenge: automated tools need good understanding of interfaces and ability to approximate human behavior.

**Early Automation Efforts:** Previous work developed formal grammars for UI design and used Model Human Processor to simulate human behavior for predicting task performance. However, for complex interactions, these models are time-intensive to build and maintain, resulting in limited uptake.

**UI Understanding and Navigation:** Machine learning advances have enabled significant progress in UI understanding. Deep learning techniques with annotated datasets demonstrate feasibility of determining UI elements and interactivity for mobile and web interfaces. Research on MLLMs specifically trained for user interfaces shows they can identify UI element existence, types, and purpose.

Concurrently, researchers developed methods for UI navigation and task automation. Studies show deep learning can pair natural language commands to web UI action sequences, with models achieving 70.59% accuracy predicting ground-truth sequences. GPT-3 with few-shot prompting achieves 45% accuracy. ResponsibleTA uses LLM-based coordinators and executors, verifying command completeness with accuracy of 63.5%. ChatGPT/GPT-3.5 (61%) and AutoDroid combines commonsense knowledge with domain-specific knowledge, achieving 90.9% action generation accuracy and 71.3% task completion.

**AI-Powered User Evaluation:** Recent applications use AI agents for usability testing. SimUser demonstrated LLM-powered agents navigating interfaces while simulating users' thoughts and reasons, with 20 rounds of feedback covering 70% of usage scenarios from 48 human participants and uncovering 80% of usability issues identified by humans. UXAgent provides action and reasoning traces, generating thousands of simulated users with different personas. While appreciated as a tool for iteration support, participants found reasoning traces hard to read and interpret. Research also examined GPT-4 for walkthroughs of "upload a photo" tasks, determining appropriate subtasks and actions.

**The Critical Gap:** Prior work established LLMs can navigate UIs and complete tasks, but focused on maximizing accuracy in task completion. In CW context, the goal is evaluating interface learnability—requiring LLMs to have *comparable* task completion rates to humans. If agents are too successful (or even too unsuccessful), they won't help uncover the same usability issues. The evaluation also overlooks navigation path differences and failure mode analysis. Finally, practitioners are unlikely to train/fine-tune their own models—empirical data on off-the-shelf model performance for CW is needed.

---

## Central Arguments

The paper makes several interconnected claims about the utility and limitations of LLM-automated cognitive walkthrough.

**Main Thesis:** While LLMs can navigate interfaces and complete tasks at rates comparable to or exceeding humans, they do not simulate human behavior patterns—their success modes and failure modes differ fundamentally, affecting their utility for identifying learnability issues through cognitive walkthrough.

**First, LLMs achieve higher task completion than humans—which is a limitation, not an advantage.** The results show:
- GPT-4: 100% completion (all 16 runs completed all tasks)
- Gemini-2.5-pro: 97.2% completion  
- Humans: 88.2% completion (6 of 10 encountered difficulties)

In traditional usability testing, higher completion would be cause for celebration. But in CW evaluation context, the goal is to *simulate typical users* to reveal where they would struggle. If the evaluating agent succeeds where humans fail, it misses identifying real usability problems. As the authors note: "If the agents are too unsuccessful (or even too successful) at navigating the interface, they will not help uncover the same set of usability issues that real users may face."

**Second, LLMs follow more optimal paths but miss human navigation patterns.** Jensen-Shannon Divergence analysis comparing navigation paths to the correct path set revealed:
- Humans: M = 0.28 divergence
- GPT-4: M = 0.05 divergence (p < .0001, significantly lower)
- Gemini: M = 0.10 divergence (p < .001, significantly lower)

Lower divergence means paths closer to optimal. But this "better" performance actually indicates LLMs aren't simulating how humans *actually* explore interfaces. When humans complete tasks successfully, they still take more steps (M = 10.37) compared to GPT (M = 7.56, p < .001) and Gemini (M = 7.50, p < .001).

**Third, failure point identification differs—LLMs find fewer issues.** The qualitative analysis revealed:
- Humans (aggregated): Identified 5 distinct failure points across tasks
- LLMs (aggregated across 16 runs): Identified 3 failure points

Importantly, **all LLM-identified failure points were also identified by humans**, but LLMs missed 2 failure points humans consistently noticed. This suggests LLMs can provide *some* usability insights but not comprehensive coverage.

**Fourth, behavioral differences reveal fundamentally different reasoning patterns:**

*Humans exhibit breadth-first search under uncertainty:* When unsure about next steps, humans explore multiple options before committing. Thematic analysis revealed: "humans were more prone to conduct breadth-first search when they were uncertain about the next steps."

*LLMs make different types of mistakes:* "Humans were more prone to making mistakes due to memory issues"—forgetting earlier context or goals. LLMs, despite having perfect memory of conversation history, occasionally loop or choose irrelevant options, suggesting reasoning failures rather than memory failures.

---

## Evidence

The researchers provide quantitative task completion analysis, path navigation comparison, and detailed qualitative examination of behavioral differences.

**Task Completion Results (Study 1):**

Figure 3 presents completion rates showing all but one of 16 LLM runs completed all tasks successfully, while 6 of 10 human participants encountered difficulties. Statistical analysis via ANOVA with post-hoc pairwise t-tests revealed significant differences between humans and both LLM conditions, but comparing those who did complete tasks:
- Humans took more steps: M = 10.37 vs. GPT M = 7.56 (t(15.24) = 8.22, p < .001) and Gemini M = 7.50 (t(13.05) = 7.49, p < .001)

**Navigation Path Alignment:**

Using Jensen-Shannon Divergence (JS Divergence) based on Kullback-Leibler divergence to measure similarity between navigation pathways, with correct path set as reference:
- Human JS scores: M = 0.28
- GPT-4 JS scores: M = 0.05 (t(13.27) = 7.25, p < .0001)
- Gemini JS scores: M = 0.10 (t(12.06) = 4.70, p < .001)

Both LLM conditions achieved statistically significantly lower (more optimal) JS scores than humans, indicating their paths aligned more closely with ideal navigation.

**Failure Point Analysis:**

The qualitative coding of rationales extracted from both LLM transcripts and human transcripts identified potential failure points—instances where confusion or uncertainty indicated interface issues. Using thematic analysis on rationales from 3 GPT runs, 5 participant transcripts initially, then analyzing all transcripts and runs with the finalized codebook:

*Examples of Human-Identified Failure Points LLMs Missed:*
- Visual hierarchy confusion where secondary elements appeared more prominent than primary actions
- Terminology mismatches where interface labels didn't match users' mental models  
- Missing affordances where interactive elements didn't look clickable

*Examples of Failure Points Both Identified:*
- Navigation loops where users/agents couldn't find the "back" or "exit" function
- Ambiguous icons requiring explanation
- Multi-step processes lacking progress indicators

**Behavioral Pattern Analysis:**

The thematic analysis revealed distinct behavioral signatures:

*Breadth-First vs. Depth-First Search:*

Human transcript excerpt (language app, exploring course options):
> "I see 'Start Lesson' but I'm not sure if this is the right one... let me check what's in 'Explore' first... okay there's courses here too... and what about this 'Profile' section... okay now I understand the structure, I'll go back to 'Start Lesson'"

LLM transcript excerpt (same task):
> "I will click on 'Start Lesson' to begin the first lesson."

The human explores multiple paths before committing; the LLM commits immediately.

*Memory vs. Reasoning Failures:*

Human transcript excerpt (booking app):
> "Wait, what was I supposed to search for again? Was it Amsterdam or London?"

LLM transcript excerpt (looping scenario):
> "I will click on the search bar again... [after 3 repetitions] I will click on the search bar again..."

Humans forget goals; LLMs repeat ineffective actions.

**Consistency Analysis:**

Running GPT-4 multiple times (5 runs per task) revealed high consistency—when the model identified a failure point in one run, it typically identified it in other runs as well. This suggests LLM-based CW could provide reliable (if incomplete) usability insights.

---

## Conclusion

This research demonstrates that current LLMs can automate aspects of cognitive walkthrough but do not replicate human evaluator behavior—creating both opportunities and limitations for their use in usability evaluation.

**The Core Insight: Success is a Problem**

The finding that LLMs complete tasks more successfully than humans inverts the usual performance metric. In traditional AI evaluation, higher task completion represents progress. In CW simulation, it represents misalignment. The goal isn't to build the best possible interface navigator—it's to simulate typical users who would struggle with poorly designed interfaces.

This suggests a fundamental tension: as LLMs improve at UI understanding and navigation, they may become *less* useful for identifying usability issues through simulation. The models trained on vast corpora of interface patterns have internalized design conventions that typical users haven't.

**Practical Implications:**

Despite limitations, the research identifies valuable use cases:

**1. Scaling Walkthrough Coverage:** Even identifying 60% of human-identified issues (3 of 5) provides value if it enables testing more interfaces, more tasks, or more iterations. The automated approach reduces time from hours to minutes—enabling rapid iteration.

**2. Complement Rather Than Replace:** LLMs can screen for obvious issues before human evaluation, reducing the burden on human evaluators who can then focus on subtle learnability problems.

**3. Think-Aloud Insights:** Even when navigation differs from humans, LLM-generated rationales provide design feedback. The think-aloud protocols explain *why* the agent chose specific paths, surfacing assumptions about interface affordances.

**Limitations Acknowledged:**

The paper honestly identifies several constraints:

**Sample Size:** 10 human participants provides baseline but limited statistical power. Larger studies could reveal whether the 3-of-5 failure point ratio holds more broadly.

**App Selection:** Two apps from Lifestyle and Education categories may not generalize to enterprise software, accessibility-focused interfaces, or specialized domains.

**Task Design:** Researchers curated tasks to ensure failure points existed. Real-world CW might encounter interfaces with different usability issue distributions.

**Model Specificity:** Testing GPT-4 and Gemini-2.5-pro provides snapshots of 2026 capabilities, but model updates could change performance characteristics—for better or worse.

**Future Directions Identified:**

The paper concludes by noting that the research highlights opportunities to use LLMs to support CW objectives, specifically:

**Failure Point Prediction (Study 2 teaser):** The authors explore whether LLMs can be prompted to predict potential navigational failure points explicitly—rather than discovering them through simulation. Two approaches tested: with-context (LLM navigates first, then predicts) vs. without-context (LLM predicts from screenshots alone). Early results show with-context approach consistently predicts human-identified failure points, while without-context proves less effective and inconsistent.

This suggests LLMs might be more valuable as analytical tools (examining interfaces to predict issues) than as user simulators (navigating interfaces to discover issues).

Six months from now, when you return to this research, remember: the key finding isn't that LLMs can or can't do cognitive walkthrough—it's that LLMs succeed *differently* than humans, following more optimal paths and missing the exploratory struggles that reveal learnability issues. This makes them useful for scaling evaluation coverage but not for replacing human evaluators' nuanced identification of how typical users would experience interface confusion.

---

## APA Citation

Zhong, R., McDonald, D. W., & Hsieh, G. (2026). Synthetic cognitive walkthrough: Aligning large language model's performance with human cognitive walkthrough. In *Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '26), April 13–17, 2026, Barcelona, Spain.* ACM. https://doi.org/XXXXXXX.XXXXXXX

---

## Discussion Questions

1. **The Success Paradox:** If LLMs become better at UI navigation, does that make them worse at simulating typical users for evaluation? How should we balance model capability improvements with simulation fidelity requirements?

2. **Optimal as Enemy of Realistic:** The LLMs followed more optimal paths than humans—arguably "correct" behavior for an AI assistant but problematic for usability evaluation. Should we deliberately degrade LLM performance to match human baselines, and if so, how?

3. **Failure Point Coverage:** LLMs identified 3 of 5 human-found issues. Is 60% coverage valuable if it scales to 10x more interfaces and iterations, or does missing 40% of issues make the method unreliable for deployment decisions?

4. **Breadth-First vs. Depth-First:** The behavioral difference—humans exploring multiple options when uncertain vs. LLMs committing immediately—reflects different reasoning strategies. Can we prompt LLMs to explore more tentatively, and would that improve their ability to identify confusion points?

5. **Generalization Across Domains:** The study tested mobile apps in Lifestyle and Education categories. How might LLM performance differ for enterprise software, medical interfaces, accessibility-focused designs, or cultural-specific applications? What characteristics make interfaces more or less suitable for LLM-based CW?

---

## Bias Check

This summary aims to fairly represent the research contributions while acknowledging the limitations and boundary conditions. The paper takes a measured stance—demonstrating that LLMs can automate aspects of CW while clearly documenting where they differ from human evaluators. I have attempted to maintain that balanced perspective, highlighting both the task completion successes and the fundamental behavioral differences that limit simulation fidelity.

The main limitation in my summary is that I cannot fully reproduce the detailed thematic analysis codebook, complete participant transcript excerpts, and all statistical analyses from the appendices. Readers seeking to replicate the coding methodology or understand the full range of identified failure points should consult the original paper.

**Accuracy Score: 9/10**

I have verified this summary against the paper content and it accurately represents the study design, comparative results, behavioral analysis, and theoretical positioning. The one-point deduction reflects that some qualitative coding details and complete transcript examples are necessarily compressed in this format.
