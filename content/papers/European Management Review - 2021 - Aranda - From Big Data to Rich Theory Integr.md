---
title: 'From Big Data to Rich Theory: Integrating Critical Discourse Analysis with
  Structural Topic Modeling'
authors: Ana M. Aranda, Kathrin Sele, Helen Etchanchu, Jonne Y. Guyt, Eero Vaara
year: 2021
type: paper
tags:
- paper
- methods
- critical-discourse-analysis
- topic-modeling
- mixed-methods
source_file: European Management Review - 2021 - Aranda - From Big Data to Rich Theory  Integrating
  Critical Discourse Analysis with.pdf
community: GenAI in UX and Design Practice
builds_on:
- '[[frameworks/Critical Theory]]'
- '[[methods/Mixed Methods Research]]'
- '[[frameworks/Actor-Network Theory]]'
critiques:
- '[[concepts/Technological Determinism]]'
tensions_with: []
supports:
- '[[concepts/Reflexive Delegation]]'
- '[[concepts/Human-in-the-Loop Pedagogy]]'
key_claims:
- Integrating Critical Discourse Analysis with Structural Topic Modeling creates a
  powerful mixed-methods approach that enables scholars to analyze large textual datasets
  while maintaining depth, contextualization, and critical stance
- Neither the researcher nor the actual technique performs analysis in isolation;
  in CDA the researcher guides and is guided by analytical methods, while in STM choices
  made by the researcher shape outcomes and vice versa, creating a mutually constitutive
  process
- 'The combination of CDA and STM overcomes individual method limitations through
  complementarity: STM provides systematic, replicable topic identification in large
  corpora, while CDA provides deep qualitative interpretation of power dynamics and
  legitimation strategies'
- An explanatory transformative mixed-methods design that moves from quantitative
  to qualitative analysis (but remains iterative) ensures the critical ideological
  stance inherent to CDA is maintained throughout computational analysis
- Analysis of 3,688 tobacco industry articles (1986-2016) demonstrates that the integrated
  approach reveals complex discursive dynamics invisible to either method alone, showing
  anti-smoking groups mainly draw on health discourse while legal discourse is shared
  between government and industry
methodology: '[[methods/Mixed Methods Research]]'
sample_size: 3688
sample_type: newspaper articles from The New York Times
context: US tobacco industry discourse 1986-2016
study_type: empirical
---

# From Big Data to Rich Theory: Integrating Critical Discourse Analysis with Structural Topic Modeling

**Authors:** Ana M. Aranda, Kathrin Sele, Helen Etchanchu, Jonne Y. Guyt, Eero Vaara

**Year:** 2021

## Overview of the Document

This article represents a significant methodological contribution to management research by bridging qualitative and quantitative approaches to discourse analysis. The authors come from diverse institutional backgrounds across Europe: Ana M. Aranda from Católica Lisbon School of Business and Economics, Kathrin Sele from Aalto University School of Business and Vrije Universiteit Amsterdam, Helen Etchanchu from Montpellier Business School, Jonne Y. Guyt from Amsterdam Business School, and Eero Vaara from Saïd Business School at the University of Oxford. This international collaboration brings together scholars with expertise in critical management studies, discourse analysis, organizational theory, and computational methods.

The document is a methodological article published in the European Management Review, one of the leading European journals in management studies. It sits at the intersection of multiple fields including management research, organizational studies, applied linguistics, and computational social sciences. The significance of this work lies in its response to a pressing challenge facing contemporary researchers: how to analyze the increasingly large volumes of textual data that characterize our mediatized and digitized society while maintaining the depth and critical perspective that qualitative discourse analysis provides.

The authors position their work within the context of what Wodak (2001) calls "discursive swarming," where social and organizational phenomena become increasingly pervasive and discursively interwoven. Traditional Critical Discourse Analysis (CDA) methods, while powerful for in-depth analysis, struggle with the manual processing of vast text corpora in a systematic and reproducible manner. This often leads to premature sampling, early selection of focal texts, and difficulties in operationalizing concepts like intertextuality and interdiscursivity. The article addresses these limitations by proposing a structured integration of CDA with Structural Topic Modeling (STM), offering both theoretical justification and practical guidance for researchers facing similar methodological challenges.

## Research Overview

The central research question guiding this work is explicitly stated: "How can we integrate CDA with STM to advance management research?" (Aranda et al., 2021, p. 173). This question emerges from the recognition that while discourse analysis has become increasingly popular in management studies, the field lacks systematic guidance on how to analyze large textual datasets while preserving the critical, contextualized approach that defines CDA.

The research was conducted by the five authors collaboratively, drawing on their collective expertise in discourse analysis, topic modeling, and management research. The study employs an explanatory transformative mixed-methods research design, which the authors argue is "particularly suitable to study issues of power and inequities" where "methodological choices are made with conscious awareness of contextual and historical factors" (Mertens, 2012, p. 808, as cited in Aranda et al., 2021). This design ensures that the critical ideological stance inherent to CDA is maintained throughout the integration with STM.

The empirical illustration focuses on discursive legitimation struggles within the US tobacco industry between 1986 and 2016. The authors collected 3,688 newspaper articles from The New York Times using the keywords "tobacco," "smok!" and "cigarette." As Aranda et al. (2021) explain, "We followed research that has identified the NYT as arguably the most influential newspaper in the US" (Fiss and Hirsch, 2005, as cited on p. 714). The data collection involved careful pre-processing, including "filtering out stop-words that carry no thematic meaning" and stemming words throughout the text corpus (p. 723). 

The methods combine computational techniques with interpretive analysis. The STM approach uses machine learning to identify latent topics within the corpus by exploiting the fact that "terms belonging to a specific topic tend to co-occur more regularly than by chance" (Blei, 2012, as cited in Aranda et al., 2021, p. 336). The authors incorporated metadata including publication year and actor groups (Tobacco Industry, Government, and Anti-Smoking groups) to trace how topics evolve and to show which actors are associated with specific topics. The CDA component then provides deep qualitative interpretation of these topics, examining legitimation strategies using Van Leeuwen's (2007) framework of authorization, rationalization, moralization, and mythopoiesis.

A key methodological insight is captured in the authors' statement: "Neither the researcher nor the actual technique or tool performs the analysis in isolation. In CDA, the researcher guides and is guided by particular analytical methods... In STM, choices made by the researcher shape the outcomes of the estimation and vice versa" (Aranda et al., 2021, p. 484). This mutually constitutive process enables a dialogue that avoids both paradigmatic closure and relativism.

## Theories of Knowledge

The article engages with several theoretical frameworks that inform both its methodological approach and its epistemological positioning. At its foundation lies **Critical Discourse Analysis (CDA)**, which the authors trace back to applied linguistics and define as an approach that "considers language a social practice and sees discourse as both socially conditioned and constitutive" (Fairclough and Wodak, 1997, as cited in Aranda et al., 2021, p. 236). CDA encompasses multiple related but distinct approaches including Fairclough's original critical work (1989, 2016), socio-cognitive approaches (Van Dijk, 2016), discourse-historical approaches (Reisigl and Wodak, 2016), and multimodal social actor approaches (Van Leeuwen, 2016).

What unites these CDA approaches is their understanding that "discourses do not only reflect reality but are the very means of constructing and reproducing it" (Aranda et al., 2021, p. 238). The critical dimension of CDA focuses on revealing "taken-for-granted assumptions in society or ideologies, that is, fundamentally different assumptions, values, and worldviews, shared by people and reflected in discourses" (Fairclough, 1989, 2003; Van Dijk, 1998; Forchtner and Wodak, 2018, as cited on p. 242). CDA scholars engage in both "text or discourse immanent critique" and "socio-diagnostic critique," which focuses on detecting problematic aspects in discursive practices (Reisigl and Wodak, 2016, as cited on p. 250).

**Structural Topic Modeling (STM)** represents the quantitative methodological framework. Building on the Latent Dirichlet Allocation (LDA) model pioneered by Blei et al. (2003), STM "generalizes the LDA model by incorporating metadata (i.e., additional contextual or structural information about a document) into the model" (Roberts et al., 2016, 2019, as cited in Aranda et al., 2021, p. 367). The key theoretical advantage is that "while LDA models can only reveal the latent topics within a given text, STM allows making inferences about how an observed variable of interest affects a particular topic" (Roberts et al., 2016, as cited on p. 378).

The integration of these methods is grounded in **mixed-methods research theory**, specifically the transformative paradigm articulated by Mertens (2012). As the authors explain, transformative mixed methods are "particularly suitable to study issues of power and inequities, and the methodological choices are 'made with conscious awareness of contextual and historical factors'" (p. 808, as cited in Aranda et al., 2021, p. 529). This paradigm considers researchers as agents interested in advancing advocacy issues, aligning with CDA's commitment to taking a stance toward phenomena under investigation.

The epistemological positioning navigates the tension between paradigms. The authors acknowledge that "CDA is based on a position that combines the idea of the social construction of empirical phenomena with an appreciation for the importance of the social and material reality outside the researcher's interpretations" (Fairclough, 2005, as cited on p. 449), while "the origins of STM reflect a positivist tradition rooted in machine learning and data sciences" (p. 453). They resolve this tension through the concept of **complementarity** (Deetz, 1996; Creswell et al., 2003), arguing that "the foci of these methods can be seen as complementary" (p. 508) because CDA has always been intended as an approach that "can, and should, be combined with other theoretical and methodological perspectives" (Fairclough, 2003, as cited on p. 505).

Additional theoretical foundations include **legitimation theory**, drawing on Van Leeuwen's (2007) framework which identifies four key strategies: authorization (legitimation by reference to authority), rationalization (legitimation by reference to goals and knowledge), moralization (legitimation by reference to value systems), and mythopoiesis (legitimation through narratives that project the future). These concepts provide the analytical lens through which the authors interpret the discursive struggles in their tobacco industry case study.

## Central Arguments

The central argument of this article is that integrating Critical Discourse Analysis with Structural Topic Modeling creates a powerful mixed-methods approach that enables management scholars to analyze large textual datasets while maintaining the depth, contextualization, and critical stance that characterize traditional CDA. As the authors state in their research question, they seek to demonstrate "How we can integrate CDA with STM to advance management research" (Aranda et al., 2021, p. 173).

This overarching argument unfolds through several interconnected sub-arguments. First, the authors contend that contemporary researchers face an unprecedented challenge: "In today's mediatized and digitized society, sense is made and reality constructed in and through discourses. Accordingly, many social and organizational phenomena are increasingly pervasive and discursively interwoven, leading to what Wodak (2001) calls 'discursive swarming'" (p. 84). This creates a situation where scholars "are often confronted with an overwhelmingly large and unstructured amount of data, which despite its advantages creates some challenges" (p. 88). The key challenge relates to "the manual processing and analysis of large text corpora in a systematic and reproducible manner" (Wodak and Meyer, 2016, as cited on p. 92).

Second, the authors argue that while both CDA and STM have individual limitations, their integration overcomes these weaknesses through complementarity. They explain that "combining both approaches overcomes their limitations and provides great potential for exploring phenomena that matter in our mediatized society" (p. 32). Specifically, "if scholars are confronted with big data, STM may serve as a basis for the traditionally in-depth and focused approach in CDA, as its crucial idea is to inductively derive an understanding of key topics that can be aggregated to form discourses in a transparent and replicable manner" (DiMaggio et al., 2013; Chandra et al., 2016, as cited on p. 161).

A crucial sub-argument addresses the epistemological tensions between the methods. The authors acknowledge that "these different epistemological stances suggest that rigor is not achieved in the same way. While CDA relies on reflexivity, STM calls upon validity and reliability measures" (p. 458). However, they argue that "the role of subjectivity in interpretation is precisely what may allow for bridging the two paradigms" (Gioia and Pitre, 1990, as cited on p. 469). They support this by noting that "interpretation is happening in various steps of the STM estimation process" (Hannigan et al., 2019, as cited on p. 471) and that "Neither the researcher nor the actual technique or tool performs the analysis in isolation" (p. 477).

The authors further argue for a specific type of mixed-methods design. They "propose an explanatory 'transformative strategy' (Creswell, 2009, p. 215) for combining CDA with STM. Such an approach ensures the critical ideological stance inherent to CDA" (p. 511). This design is sequential, moving "from mainly quantitative to mainly qualitative analysis. However, the process must be seen as iterative, as several interpretations guide the estimation of the STM while the derived estimates inform CDA" (p. 538).

The practical contribution is articulated through their eight-step model. As they explain, "Our stepwise model aims at capitalizing on the advantages of combining CDA and STM for zooming in and out of large textual data" (p. 574). The model provides "practical and theoretical guidance to conduct a critical analysis of large textual data" (p. 34), addressing the gap that "we still lack knowledge on how to best integrate CDA and STM in empirical analysis" (p. 126).

Through their tobacco industry case study, the authors demonstrate that "the combination of both approaches yields a fine-grained understanding of broad but theoretically relevant patterns" (p. 1318), enabling them to capture "the breadth and depth of discourses used by different actors in the tobacco debates" (p. 37). They show how their approach reveals complex dynamics that neither method alone could uncover, such as how "anti-smoking groups mainly draw on health discourse. The legal discourse is mainly used among the government and the industry. Interestingly, the regulatory and marketing discourses are used somewhat equally by all three actors, albeit from opposite perspectives" (p. 1117).

## Evidence

The authors provide multiple forms of evidence to support their methodological arguments, ranging from theoretical justification to detailed empirical demonstration. The evidence can be organized into several categories: justification for the integration, technical demonstration of the methods, and empirical validation through the case study.

**Evidence for the Need to Integrate Methods**

The authors establish the necessity of their approach by documenting the limitations of existing methods. They cite evidence that manual CDA analysis faces challenges "with the increasing availability of texts" because "manual analysis has become more difficult, impractical, or in some instances, even unmanageable, complicating the identification of discourses and their dynamics" (p. 1338). They support this with references to difficulties in "accounting for context, intertextuality, and interdiscursivity—a central feature of CDA—in a meaningful way" due to "difficulties in moving between analytical levels" (Leitch and Palmer, 2010, as cited on p. 1436).

For STM, they present evidence that while the method has "several distinct advantages over other text analysis methods that require manual input and a priori decision making" (Blei et al., 2003; DiMaggio et al., 2013; Schmiedel et al., 2018, as cited on p. 330), it still requires "a great deal of interpretation" and "CDA can provide critically oriented and theoretically grounded guidance once the topics are derived" (p. 1517).

**Technical Evidence from Method Application**

The article provides detailed technical evidence from applying their eight-step model to the tobacco industry case. In Step 2 (data collection), they document their systematic approach: "Our initial search resulted in 6,336 articles. In order to validate our sample, we manually skimmed through these articles and discarded those that: had length issues (e.g., were too short or extremely long), were not related to the US, or were unrelated to the tobacco debates (e.g., obituaries). After pre-processing the data, our final sample consisted of 3,688 articles with a mean word count of 701" (p. 714).

For Step 3 (topic definition), they present diagnostic statistics showing that "we observe that both semantic coherence and held-out likelihood improve significantly up until somewhere between 40–50 topics, but observe decreasing improvements for these criteria beyond that number of topics" (p. 831). They explain their decision process: "While new themes emerged as we increased the number of topics, we seemingly reached theoretical saturation at 43 topics. Indeed, for the 43-topic solution, we could assign an exact thematic meaning to almost all topics, which indicates that the model identifies the main discourses in the debate" (p. 896).

The authors provide visual evidence through multiple figures. Figure 3 shows diagnostic values across different numbers of topics, demonstrating the trade-offs between model complexity and interpretability. Figure 4 presents a correlation graph revealing four main discourse clusters: "In the upper part, we see a cluster around health, which relates to smoking's health consequences. There is a cluster around marketing in the middle, which is related to the advertising strategies of the tobacco companies. On the lower left-hand side, the legal cluster represents the lawsuits faced by the industry. On the lower right-hand side, there is a regulatory cluster that comprises different tobacco control regulations" (p. 921).

**Evidence from Qualitative Analysis**

The deep qualitative evidence comes from their CDA of selected texts. Table 3 provides detailed examples of legitimation strategies, showing how different actors used discourse in 2013 around menthol cigarettes. For instance, they document how "Anti-smoking groups referenced European health ministers as expert authorities" (authorization), while "the tobacco industry's claims sustain that flavors should be regulated only for young people, for it foresees that regulating them broadly will deter smokers from switching to an allegedly less harmful product" (mythopoiesis) (p. 1465).

They trace the evolution of topics over time, noting that "the articles associated with the increasing discussions about youth in and after 2013 showed a debate on smoking among children and teens. Within this debate, anti-smoking groups referenced statistics supporting the increase in youth smoking (rationalization) and projected that e-cigarettes would eventually lead young people to smoke regular cigarettes (mythopoesis)" (p. 1277).

**Evidence of Integration Benefits**

The authors demonstrate the value of integration by showing insights that neither method alone could reveal. They explain how "we uncovered that the texts discussing menthol had a strong relationship with topic #30 (youth access)" (p. 1266), a connection that becomes meaningful through the combination of STM's pattern detection and CDA's interpretive depth. This leads to the finding that the "connection reflects a debate about whether and how menthol cigarettes lure young people" (p. 1271).

**Limitations of the Evidence**

The authors acknowledge methodological limitations. They note decisions made during data cleaning, such as "Following standard practice (Hannigan et al., 2019), we stemmed words (reduced 'company' and 'companies' to their stem 'compan') throughout the text corpus. Alternative decisions to make when cleaning the data, which we have not used, are whether to lemmatize the words or whether only to use certain parts of the documents (e.g., nouns/verbs)" (p. 728). They also acknowledge that "there is statistically no way to determine how many topics are needed to explain a given text corpus best" (p. 783), requiring judgment calls throughout the process.

The authors are explicit about the scope of their evidence, stating that "collecting more data is not always needed; sometimes, a single text can be just as informative as an extensive collection" (see Vaara and Tienari, 2008, as cited on p. 1530), and urging "scholars to critically assess whether and why 'more is better' in their particular setting" (p. 1531).

## Conclusion

This article makes a substantial contribution to management research methodology by demonstrating how Critical Discourse Analysis and Structural Topic Modeling can be systematically integrated to address the challenges of analyzing large textual datasets. For a student who needs to recall this work six months from now, the key takeaway is that the authors provide both theoretical justification and practical guidance for bridging qualitative and quantitative approaches to discourse analysis in a way that preserves the critical, contextualized perspective of CDA while leveraging the pattern-detection capabilities of computational methods.

The work's primary contribution lies in its eight-step model, which moves sequentially from choosing a theoretical focus, through collecting and analyzing large textual data with STM, to zooming in on specific texts for deep CDA interpretation, and finally to developing integrated findings. The tobacco industry case study spanning thirty years demonstrates that this approach can reveal both broad patterns across thousands of documents and the nuanced legitimation strategies employed by different actors at specific moments in time.

The authors position their work as a response to the contemporary reality of "discursive swarming" (Wodak, 2001) where organizational and social phenomena are increasingly mediatized and textually dispersed. Traditional CDA methods, while powerful, struggle with the scale of modern textual data. Conversely, computational methods like topic modeling, while capable of processing vast amounts of text, lack the theoretical depth and critical perspective necessary for understanding power dynamics and ideological struggles. The integration proposed here aims to capture both breadth and depth.

Several important tensions remain unresolved but productively managed in this work. The epistemological differences between CDA's critical constructivism and STM's positivist origins are acknowledged but bridged through the concept of complementarity and the recognition that interpretation occurs throughout both approaches. The authors advocate for a "transformative strategy" that maintains CDA's critical stance while incorporating STM's analytical capabilities.

What remains open is the broader question of applicability. The authors note that "not all steps need always to be taken and that usually, the analysis progresses iteratively rather than in a linear manner" (p. 1540), suggesting that their model should be adapted rather than rigidly followed. They also acknowledge that their approach is most valuable when confronting truly large datasets, cautioning researchers to "critically assess whether and why 'more is better' in their particular setting" (p. 1531).

The work opens several avenues for future research. First, while the tobacco case demonstrates the approach's utility for studying legitimation struggles, the model could be applied to other management phenomena such as organizational change, innovation processes, or stakeholder engagement. Second, the integration of CDA with STM could be extended to other computational methods beyond topic modeling. Third, the epistemological dialogue between critical and computational approaches could be further developed, particularly regarding questions of validity, reliability, and reflexivity in mixed-methods designs.

For management researchers, this article provides essential guidance on navigating the increasingly common situation of having access to large textual datasets while wanting to maintain theoretical sophistication and critical perspective. The authors successfully demonstrate that rigorous computational analysis and interpretive depth are not mutually exclusive but can be mutually reinforcing when thoughtfully integrated. The enduring value of this work lies not just in the specific eight-step model but in its demonstration that paradigmatic differences need not be barriers to methodological innovation when researchers explicitly attend to epistemological assumptions and maintain theoretical clarity throughout the research process.

## APA Citation

Aranda, A. M., Sele, K., Etchanchu, H., Guyt, J. Y., & Vaara, E. (2021). From big data to rich theory: Integrating critical discourse analysis with structural topic modeling. *European Management Review*, *18*(3), 197–214. https://doi.org/10.1111/emre.12452

## Discussion Questions

1. **Epistemological Integration:** The authors argue that CDA's critical constructivism can be integrated with STM's positivist origins through "complementarity" and the recognition that interpretation occurs in both approaches. Do you find this resolution convincing, or do fundamental epistemological tensions remain that could compromise either the critical stance of CDA or the validity claims of STM? How might researchers navigate situations where these tensions become more acute?

2. **Scalability and Depth Trade-offs:** The eight-step model proposes moving from computational analysis of large datasets to close reading of selected texts. At what point does the selection of texts for deep CDA analysis reintroduce the sampling biases and premature focusing that the use of STM was meant to overcome? How can researchers ensure that their "zooming in" choices are systematically justified rather than driven by confirmatory bias or convenience?

3. **Applicability Beyond Legitimation Studies:** The tobacco industry case focuses on discursive legitimation struggles, which align well with CDA's traditional concerns with power and ideology. How well would this integrated approach work for other management research questions, such as studies of organizational learning, innovation processes, or routine organizational practices where power dynamics may be less explicit? What modifications to the model might be necessary?

4. **The Role of Context in Algorithmic Analysis:** CDA emphasizes that discourses must be understood in their "historical and socio-political context" (p. 259). However, STM's inclusion of metadata (time, actors, document type) represents a relatively thin conceptualization of context compared to traditional CDA. How can researchers using this integrated approach ensure they capture the rich contextual understanding that CDA requires, particularly regarding aspects like institutional history, cultural background, or situational specifics that may not be easily coded as metadata?

## Bias Check

In preparing this summary, I aimed to present the authors' methodological argument and empirical demonstration as comprehensively as possible, maintaining fidelity to their theoretical positioning and practical guidance. I emphasized their systematic integration of CDA and STM because this represents the article's core contribution, and I highlighted both the theoretical justification and the technical details of implementation because these are essential for researchers who might want to apply the approach.

I may have leaned toward presenting the integration as more seamless than it actually is. While the authors acknowledge epistemological tensions and practical challenges, my summary perhaps emphasizes the resolution of these tensions more than the ongoing negotiation they require. The authors themselves are quite explicit about the difficulties and judgment calls involved throughout the process, and a more critical reading might question whether the complementarity they propose fully resolves the paradigmatic differences or simply manages them pragmatically.

I also may have given less attention to the limitations of their specific empirical case. The tobacco industry example, while rich and well-executed, represents a particular type of phenomenon (highly mediatized, strongly contested, with clear opposing actors) that may be unusually well-suited to this approach. Other management phenomena with less media coverage, more ambiguous actor positions, or more subtle discursive dynamics might not yield such clear results.

My summary focuses heavily on the methodological innovation and less on the substantive findings about tobacco discourse. This reflects my interpretation that the article's primary contribution is methodological, but another reader might argue that the tobacco case demonstrates important substantive insights about legitimation processes in contested industries that deserve more emphasis.

**Accuracy score: 8/10**

I am confident that this summary accurately represents the authors' arguments, theoretical frameworks, and methodological procedures. The score is not perfect because: (1) in the interest of length management, I necessarily compressed some of the technical details about STM estimation and diagnostic statistics; (2) I may have somewhat oversimplified the epistemological resolution the authors propose; and (3) the article contains extensive references to prior literature that I could not fully capture. However, I believe any PhD student reading this summary six months from now would have a solid, accurate understanding of the article's contribution and would be able to engage meaningfully with both its methodological innovations and its application to discourse analysis in management research.

## Key Concepts
- [[Critical Discourse Analysis]]
- [[Structural Topic Modeling]]
- [[mixed methods]]
- [[legitimation theory]]
- [[transformative research design]]

## Methods Used
- [[methods/Critical Discourse Analysis]]
- [[methods/Structural Topic Modeling]]
- [[methods/Mixed Methods]]

## Connections
- [[methods/Mixed Methods]] - Research methodology
- [[communities/GenAI in UX and Design Practice]] - Research community
