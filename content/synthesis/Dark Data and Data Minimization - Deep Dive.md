---
type: topic-synthesis
name: "Dark Data and Data Minimization"
paper_count: 5
tags: [sustainability, data-management, dark-data, data-disposal, digital-hoarding, green-IT]
---

# Dark Data and Data Minimization: The 55-90% Problem

## Summary

This synthesis examines one of the most striking yet underappreciated findings in sustainable computing research: between 55% and 90% of organizational data is never analyzed or used for any productive purpose. This "dark data" represents a massive hidden environmental liability, consuming energy for storage, cooling, and backup without generating value. Five papers from the sustainability corpus converge on this problem from different angles: legal risk (Grimm), organizational behavior (Jackson & Hodgkinson), archival science (van Bussel et al.), database theory (Milo), and psychology (Sweeten et al.). Together, they reveal that the dark data problem is not primarily technical but behavioral, organizational, and systemic. The solution requires not just better deletion tools but fundamental shifts in how we think about data value, retention defaults, and the hidden costs of digital accumulation.

## Key Definitions

**Dark Data**: Data collected, processed, and stored by an organization that is never analyzed or used for any productive purpose. Estimates range from 55-90% of enterprise data. It consumes storage, energy, and creates legal/security risk while generating zero value.

**Dark Iterations** *(emerging concept)*: Design artifacts generated (especially via AI tools) that are never meaningfully evaluated, compared, or learned from. They're produced, briefly glanced at, and abandoned in project files. They consume computational resources to generate and storage to retain, while contributing nothing to design decisions.

The shared pattern: **generation/collection outpaces analysis/evaluation**. The capability to produce exceeds the capacity to think.

## Related Papers

1. **Grimm, D. J. (2019)**. The dark data quandary. *American University Law Review, 68*(3), 761-821.
2. **Jackson, T. W., & Hodgkinson, I. R. (2023)**. Keeping a lower profile: reducing digital carbon footprints. *Journal of Business Strategy, 44*(6), 363-370.
3. **van Bussel, G.-J., Smit, N., & van de Pas, J. (2015)**. Digital archiving, green IT and environment. *Electronic Journal of Information Systems Evaluation, 18*(2), 187-198.
4. **Milo, T. (2019)**. Getting rid of data. *Journal of Data and Information Quality, 12*(1), Article 1, 1-7.
5. **Sweeten, G., Sillence, E., & Neave, N. (2018)**. Digital hoarding behaviours. *Computers in Human Behavior, 85*, 54-60.

## Research Overview

### The Scale of the Problem

The papers converge on a startling consensus: the majority of data organizations collect is never used. Grimm's legal analysis establishes the upper bound:

> "80-90% of enterprise data is 'dark' (never analyzed)" and "less than 1% of unstructured data is ever analyzed."

Jackson and Hodgkinson provide a more conservative but still striking estimate:

> "55% of organizational data is 'dark'---collected, processed, and stored without ever being used for productive purposes. This represents a massive carbon liability hiding in plain sight."

Van Bussel et al. add granularity by categorizing data by retention value:

> "Almost 75 percent of all data and records in an organization can be permanently deleted over time" and "only 5 percent of all data would have to be retained for longer than twenty years."

Milo frames the urgency in terms of infrastructure capacity:

> "By the year 2020 the demand for storage will outstrip production by six zettabytes---nearly double the available storage capacity."

### The Environmental Cost

This isn't merely a storage management problem. Dark data has real environmental consequences:

Jackson and Hodgkinson identify four carbon footprint sources from unnecessary data:
1. **Storage**: Energy for data center infrastructure maintaining unused data
2. **Processing**: Computational resources for data that serves no purpose
3. **Transmission**: Network energy for moving redundant information
4. **Backup**: Multiple copies of unnecessary data compound impact

Van Bussel et al. provide empirical evidence of the energy savings achievable through systematic deletion:

> "The model can be used to reduce [1] the amount of data (45 percent, using ARLs and Retention Schedules) and [2] the electricity consumption for data storage (resulting in a (calculated) cost reduction of 35 percent)."

They also note the accelerating nature of the problem:

> "The annual growth rate in the amount of data is almost 40%, creating a 'data deluge'" and "the data deluge (and the use of more and more ICT resources to manage this deluge) threatens [1] to drown all positive effects of Green IT and [2] to raise energy costs exponentially."

## Theoretical Framework

### Why Data Accumulates: The Storage Imperative

Grimm identifies a fundamental asymmetry driving data accumulation:

> "Storage is cheap; analysis is expensive."

This creates what he calls the "storage imperative":

> "'We have all become hoarders'---retaining data simply because we can."

Organizations store data hoping future tools will unlock value, but this hope rarely materializes. Grimm describes organizations as "compulsive data hoarders" driven by declining storage costs (Kryder's Law) and the Big Data narrative promising future value extraction.

### The Capability Gulf

Grimm introduces a crucial concept: the "capability gulf" between storage technology and analytical tools:

> "Global data volumes are increasing faster than analytical capacity."

This means the dark data problem is structural, not temporary. Even as analytical capabilities improve, storage growth outpaces them. The result is an ever-growing backlog of unanalyzed data.

### Value-Based Retention: The Archival Science Contribution

Van Bussel et al. bring archival science theory to bear on the problem through **Archival Retention Levels (ARLs)**, which:

> "Define detailed functional (organizational) responsibilities for the retention, storage and archiving of unique, authentic, relevant and contextual data and records."

Their **Information Value Chain (IVC)** theory provides a framework for assessing data worth based on:

> "Economic, social, cultural, financial, administrative, fiscal and/or legal value."

The key insight is that most data loses value rapidly:

> "Only 5 percent of all data would have to be retained for longer than twenty years."

### The Behavioral Dimension: Five Barriers to Deletion

Sweeten et al.'s qualitative study identifies five psychological barriers that prevent people from deleting data:

**1. "Just in Case" Anxiety**
> "I struggle really hard deleting folders. I always fear that what they contain will be very important to me in the future. Even though I do not use them, I still do not wish to delete them just in case."

**2. Evidentiary Value**
> "Also keep as proof that I was asked to do a certain task" and "Proof I have passed a message on / booked a job in / expressed concern / chased something up with a supplier etc."

**3. Laziness/Time Constraints**
> "I'm just too lazy to delete them. Life is busy and I feel that I have better things to do than to spend my life going through my backlog of e-mails and sorting them out."

**4. Emotional Attachment**
> "No I like to keep everything. Photos are special, I wouldn't want to get rid of them. It would be difficult because I would feel that I'm deleting little bits of me and my past."

**5. "Not My Server, Not My Problem"**
> "I'm not bothered about my inbox. Did not think there would be 9201 emails in my deleted though. I do not see data as a physical thing and we have unlimited data at work so I don't really care."

This fifth barrier is particularly significant for sustainability: when individuals don't perceive storage limits or costs, they have no incentive to manage data responsibly.

## Central Arguments

### Argument 1: Dark Data is a Legal and Security Risk

Grimm argues that dark data creates "invisible risk" that organizations cannot manage:

> "Organizations cannot comply with data protection laws if they don't know what data they have."

Under HIPAA, unanalyzed medical data may contain protected health information triggering compliance obligations. Under FTC Section 5, the agency has pursued companies for:

> "Creating unnecessary risks to personal information by storing it indefinitely" (Ceridian Corp case).

### Argument 2: Dark Data Distorts Big Data's Promise

Grimm challenges the foundational claims of Big Data analytics:

> "The 'N=All' myth: Big Data claims comprehensiveness but operates only on visible data."

Because 80-90% of enterprise data is dark, any Big Data analysis is necessarily incomplete. This matters for legal proceedings where algorithmic evidence may be introduced:

> "Courts should recognize that Big Data conclusions may be incomplete" and "question what data was excluded from analysis."

### Argument 3: Data Disposal Must Become a First-Class Concern

Milo argues for a paradigm shift from storage-centric to disposal-centric data management:

> "If we do not learn how to effectively dispense with some of this data, then we will simply drown."

She calls for "dispose by design" frameworks rather than ad hoc solutions:

> "Every single initiative has to battle, almost from scratch, the same tough challenges. The ad hoc solutions, even when successful, are application-specific and rarely sharable."

### Argument 4: Unlimited Storage Enables Hoarding

Sweeten et al.'s most sustainability-relevant finding is that unlimited cloud storage removes natural constraints:

> "The fact that there is a sense of unlimited space acts as a barrier to deleting data at all."

When storage appears free and infinite, the psychological incentives all favor accumulation. This creates a tragedy of the commons in organizational data management.

### Argument 5: Knowledge Reuse is Climate Action

Jackson and Hodgkinson reframe data minimization as sustainability practice:

> "Digital decarbonization is not just about efficient data centers---it's about reducing the demand for data storage in the first place."

They propose a three-step framework:
1. **Search**: Does this already exist?
2. **Sanity Check**: Is creating this worth the carbon cost?
3. **Knowledge Reuse**: How can I build on what exists?

> "Every file stored has a carbon footprint. Every email sent consumes energy. Digital minimalism is climate action."

## Evidence and Case Studies

### Van Bussel et al.'s Green Archiving Case Studies

**Case Study 2** (ARL Schedules pilot, March-May 2014) in an international trade corporation:
> "Global data storage capacity was 45 TB (including the headquarters' 18 TB storage capacity). The conclusion of this pilot study was that the use of ARL checklists would diminish global data storage capacity with 30 percent. 37 percent of the company's data storage capacity was used for duplicate files."

**Case Study 3** (Records Schedule analysis, January-March 2015):
> "Almost 10 percent (3.5 TB) of all data and records stored in February 2015 could be disposed of immediately, because they had no 'value' anymore for the organization as all possible retention periods had passed."

### Grimm's FTC Enforcement Examples

Regulatory action demonstrates real consequences for data hoarding:

- **Accretive Health**: Failed to remove data no longer needed for business purposes
- **Ceridian Corp**: "Created unnecessary risks to personal information by storing it indefinitely"
- **DSW Inc.**: Stored information in multiple files without business need
- **Upromise**: Inadvertently collected sensitive data due to overly narrow filter definitions

### Sweeten et al.'s Qualitative Evidence

Participants revealed the psychological toll of data accumulation:

On **productivity impacts**:
> "When something is too cluttered it makes it difficult to be efficient. I waste too much time looking for things when they are out of order."

On **psychological impacts**:
> "Stressful. Although not actually taking up physical space, it 'feels' clutter like."

On **cybersecurity**:
> "If a hacker hacked into my laptop, they could find all my pictures, all my music taste and most importantly all my interactions via email... This could then lead to a potential digital impersonation of me."

## Conclusion

The convergence of five distinct research traditions---legal scholarship, business strategy, archival science, database theory, and psychology---on the dark data problem reveals its systemic nature. The 55-90% of data that is never analyzed represents not just wasted storage but wasted energy, wasted cooling water, and unnecessary carbon emissions.

The path forward requires action at multiple levels:

**Individual**: Adopt the "search before create" mindset. Recognize that every file has a carbon footprint.

**Organizational**: Implement value-based retention policies using archival science frameworks. Make storage costs visible to users. Default to deletion rather than retention.

**Technical**: Develop "dispose by design" systems that make deletion the path of least resistance. Build provenance tracking so organizations know what they have.

**Policy**: Recognize that GDPR's data minimization requirements align with environmental sustainability. Mandatory data inventories and retention limits serve both privacy and climate goals.

The ultimate insight is that **the dark data problem is a design problem**. As long as systems default to infinite retention and hide storage costs from users, data will accumulate. Sustainable computing requires making the environmental cost of data visible and building systems where thoughtful deletion is easier than mindless accumulation.

## APA Citations

Grimm, D. J. (2019). The dark data quandary. *American University Law Review, 68*(3), 761-821.

Jackson, T. W., & Hodgkinson, I. R. (2023). Keeping a lower profile: reducing digital carbon footprints. *Journal of Business Strategy, 44*(6), 363-370. https://doi.org/10.1108/JBS-03-2022-0048

Milo, T. (2019). Getting rid of data. *Journal of Data and Information Quality, 12*(1), Article 1, 1-7. https://doi.org/10.1145/3326920

Sweeten, G., Sillence, E., & Neave, N. (2018). Digital hoarding behaviours: Underlying motivations and potential negative consequences. *Computers in Human Behavior, 85*, 54-60. https://doi.org/10.1016/j.chb.2018.03.031

van Bussel, G.-J., Smit, N., & van de Pas, J. (2015). Digital archiving, green IT and environment: Deleting data to manage critical effects of the data deluge. *Electronic Journal of Information Systems Evaluation, 18*(2), 187-198.

## Discussion Questions

1. Given that 55-90% of data is never used, what would happen if organizations implemented automatic deletion after a retention period expires? What safeguards would be needed?

2. The "not my server, not my problem" barrier suggests individuals don't perceive storage costs. How might interface design make the environmental cost of data visible without being intrusive?

3. Grimm argues dark data creates legal risk, while Jackson & Hodgkinson argue it creates environmental cost. Which framing is more likely to motivate organizational action?

4. Sweeten et al. found emotional attachment to digital possessions parallels physical hoarding. Should sustainability interventions account for this emotional dimension, or focus on structural defaults?

5. Van Bussel et al. achieved 45% storage reduction through systematic value assessment. What barriers prevent wider adoption of such approaches, and how might they be overcome?

## Connections

- [[topics/Sustainable Computing]]
- [[topics/Barriers to Data Deletion]]
- [[topics/Design Defaults as Sustainability Lever]]
- [[topics/Jevons Paradox in Computing]]
- [[papers/The Dark Data Quandary]]
- [[papers/Keeping a lower profile - Reducing digital carbon footprints]]
- [[papers/Digital Archiving Green IT and Environment - Deleting Data to Manage the Data Deluge]]
- [[papers/Getting Rid of Data - Systematic Data Disposal for Big Data Management]]
- [[papers/Digital Hoarding Behaviours - Underlying Motivations and Potential Negative Consequences]]
