---
source_file: "2026/i609-sustainability/li.pdf"
type: paper
authors: "Zhichao Li, Kevin M. Greenan, Andrew W. Leung, Erez Zadok"
community: "Sustainable Computing"
tags: [sustainability, i609, storage-systems, power-management, data-centers, backup-systems]
---

# Power Consumption in Enterprise-Scale Backup Storage Systems

## Summary

This paper presents the first empirical study of power consumption in real-world, large-scale, enterprise disk-based backup storage systems. The authors, Zhichao Li and Erez Zadok from Stony Brook University along with Kevin M. Greenan and Andrew W. Leung from EMC Corporation's Backup Recovery Systems Division, address a critical gap in the literature: while power management in backup systems has been extensively theorized, no prior published studies had measured actual power consumption in production environments. This research is significant because data centers account for approximately 1.5% of global electricity consumption, with storage systems consuming up to 40% of that power. Backup storage systems are particularly important targets for power efficiency because they store mostly cold data, have significant idle periods, and must compete with tape-based alternatives on operational costs. The study measured several generations of EMC controllers (DD880, DD670, DD860, DDTBD) and enclosures (ES20, ES30) using professional power meters, revealing nine key observations that challenge conventional assumptions about power management in storage systems. The findings are directly relevant to the sustainable computing field as they provide empirical data to guide future power-efficient storage system designs.

## Research Overview

The central research question addresses a fundamental knowledge gap: How does power consumption actually behave in enterprise-scale backup storage systems under real-world conditions? Prior to this study, "power management in backup storage systems is often based on assumptions and commonly held beliefs that may not hold true in practice" (Li et al., p. 1). The authors employ an empirical measurement methodology, using a Fluke 345 Power Quality Clamp Meter and a WattsUP Pro ES power meter to measure power consumption across multiple system configurations. The methodology involved measuring controllers and enclosures separately to isolate component-level consumption, testing systems under three scenarios: idle, loaded, and power-managed states. Key concepts include: (1) Power Use Effectiveness (PUE), a standard metric for data center efficiency; (2) deduplication ratios, which affect controller CPU and memory requirements; (3) spin-down versus power-down modes for disk management; and (4) the distinction between controller power consumption and enclosure power consumption. The research measured systems "representing several different generations of production hardware using various backup workloads and power management techniques" (Li et al., p. 1).

## Theoretical Framework

The study builds on the theoretical premise of energy proportionality, which "states that systems should consume power proportional to the amount of work performed" (Li et al., p. 6). This concept, introduced by Barroso and Holzle, serves as a benchmark against which the authors evaluate their findings. The authors also engage with conventional wisdom in the field, specifically the assumption that "disks are the main contributor to power in a storage system" (Li et al., p. 3). The theoretical framework encompasses concepts of tiered storage architecture, where backup systems store data in higher storage tiers with cold data accessed only during failures. The study employs the concept of normalized power consumption (watts per terabyte of storage capacity) to enable meaningful comparisons across different controller generations. Additionally, the framework addresses Intel C-states for CPU power management, "a small set of CPU power-saving states, which represent a range of CPU states from fully active to mostly powered-off" (Li et al., p. 4).

## Central Arguments

The paper's central argument challenges the conventional focus on disk-based power management for storage systems. The authors contend that "components other than disks consume a significant amount of power, even at large scales" (Li et al., p. 6), necessitating a more holistic approach to power efficiency. This argument is supported through nine formal observations derived from empirical measurements:

**Observation 1**: "The idle controller power consumption is still significant" (Li et al., p. 3). Even without workload, controllers consume substantial power (225W to 778W depending on model).

**Observation 5**: "The idle power consumption varies greatly across enclosures with new ones being more power efficient" (Li et al., p. 5). The ES30 enclosure consumes 179W idle compared to ES20's 278W.

**Observation 8**: "Disk enclosures may consume more power than the drives they house. As a result, effective power management of the storage subsystem may require more than just disk-based power-management" (Li et al., p. 5).

**Observation 9**: "To save a significant amount of power, many drives must be in a low power mode" (Li et al., p. 6). The study found that 40-60% of disks must be spun down to achieve meaningful (20%) power savings.

A sub-claim addresses the limitations of Dynamic Voltage and Frequency Scaling (DVFS): "Placing today's Intel CPUs into deep C state saves only a small amount of power and significantly harms controller performance" (Li et al., Observation 4, p. 4).

## Evidence

The authors provide extensive quantitative evidence supporting their claims. For controller power consumption, they measured four EMC controllers showing idle power ranging from 225W (DD670) to 778W (DDTBD). "DDTBD consumes almost 3.5x more power than DD670" (Li et al., p. 3), demonstrating significant variation across models despite the DD880 and DD860 having similar hardware profiles. The power increase from idle to loaded states varied considerably: "For some models, active power consumption is only 20% higher than idle, while it is up to 60% higher for others" (Li et al., p. 6).

For enclosure measurements, the ES20 idle power (278W) was found to be "55% higher than the idle ES30, at 179W" (Li et al., p. 5). Critically, "with all disks powered down, ES20 consumes 155W, which is more than the 123W saved by powering down the disks" (Li et al., p. 5), directly supporting Observation 8.

The system-level analysis revealed that achieving 20% power savings requires "over 40% of the disks must be spun down to save 20% of the total power" (Li et al., p. 6). In the worst case configuration (DDTBD with ES20), "19 of the 32 enclosures must have their disks spun down to achieve a 20% savings" (Li et al., p. 6).

**Limitations**: The authors acknowledge several constraints. First, their measurement methodology "prevented us from identifying the internal components that contribute to this difference" (Li et al., p. 3) in power consumption between similar hardware profiles. Second, "only DDTBD was the only model that supported the Intel C states" (Li et al., p. 4), limiting generalizability of DVFS findings. Third, the HVAC water consumption data used came from "one simple dataset from one location" (Li et al., p. 5) and may not be representative.

## Conclusion

This foundational study establishes that power management in enterprise backup storage systems requires a fundamentally different approach than previously assumed. The key insight for long-term recall is the inversion of conventional wisdom: infrastructure components (controllers, enclosures, fans, power supplies) consume as much or more power than the storage media itself, meaning disk-only power management strategies are inherently limited. The finding that newer hardware generations show improved power efficiency per terabyte (DDTBD: 0.675W/TB vs. DD880: 2.89W/TB) suggests that hardware refresh cycles can significantly impact sustainability outcomes. For practitioners, the implication is clear: power management must address the entire storage subsystem, not just drives. The study also reveals that energy proportionality remains elusive in current systems, with some configurations showing only 20% power increase under load despite significant utilization increases. Future research directions include measuring aged systems with active background jobs, investigating primary storage systems, and decomposing power consumption to individual components (CPUs, RAM). This paper provides essential baseline data for any subsequent work on sustainable storage system design.

## APA Citation

Li, Z., Greenan, K. M., Leung, A. W., & Zadok, E. (n.d.). Power consumption in enterprise-scale backup storage systems. In *Proceedings of the USENIX Conference on File and Storage Technologies (FAST)*. Stony Brook University; EMC Corporation.

## Discussion Questions

1. Given that enclosures can consume more power than the drives they house, how should data center operators balance the trade-off between storage density (more drives per enclosure) and power efficiency in sustainable system design?

2. The study found that 40-60% of disks must be in low-power mode to achieve 20% system power savings. What implications does this have for backup scheduling strategies and service-level agreements in enterprise environments?

3. How might the emergence of solid-state drives (SSDs) and NVMe storage change the power consumption dynamics observed in this study, particularly regarding the controller-to-storage power ratio?

4. The authors note that systems are not achieving energy proportionality. What architectural changes would be needed to create backup storage systems that consume power proportional to actual workload?

## Connections

- [[topics/Sustainable Computing]]
- [[topics/Data Center Energy Efficiency]]
- [[topics/Storage System Architecture]]
- [[communities/Sustainable Computing]]
- [[topics/Power Management]]
