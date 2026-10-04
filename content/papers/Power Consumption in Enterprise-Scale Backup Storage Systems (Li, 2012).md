---
title: "Power Consumption in Enterprise-Scale Backup Storage Systems"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/li.pdf"
type: paper
authors:
  - Zhichao Li
  - Kevin M. Greenan
  - Andrew W. Leung
  - Erez Zadok
year: 2012
venue: "HotStorage (USENIX Workshop on Hot Topics in Storage and File Systems)"
builds_on:
  - "[[Energy Proportionality]]"
  - "[[DVFS (Dynamic Voltage and Frequency Scaling)]]"
  - "[[MAID (Massive Array of Idle Disks)]]"
supports:
  - "[[Sustainable Data Centers]]"
  - "[[Green Computing]]"
  - "[[Storage System Power Management]]"
critiques:
  - "[[Disk-centric Power Management]]"
tensions_with:
  - "[[Energy Proportional Computing]]"
key_claims:
  - Controllers and enclosures consume significant power independent of disks
  - Idle controller power consumption remains substantial even in newer systems
  - Disk enclosures may consume more power than the drives they house
  - Many drives must be in low-power mode before significant system power savings occur
  - DVFS alone is insufficient for power savings in backup controllers
methodology: "Empirical power measurement study using Fluke 345 Power Quality Clamp Meter and WattsUP Pro ES meter on production EMC enterprise backup storage systems"
study_type: empirical
context: "Enterprise data center backup storage systems consuming up to 40% of total storage system power"
---

## Summary

This paper presents the first empirical study of power consumption in real-world, enterprise-scale, disk-based backup storage systems. The authors measured power consumption across four generations of EMC backup controllers (DD880, DD670, DD860, DDTBD) and two generations of disk enclosures (ES20, ES30). The study challenges conventional assumptions about power management in storage systems, finding that components other than disks—specifically controllers and enclosures—consume substantial power that is often overlooked in power management strategies.

The key insight is that prior work focused almost exclusively on disk power management (spin-down, power-down), but this study reveals that controllers can consume as much power as 100 2TB drives, and enclosures themselves may consume more power than the disks they house. This has significant implications for designing power-efficient backup storage systems.

## Key Concepts

- **Backup Storage Power Profile**: Backup systems have unique characteristics—cold data, periodic workloads, long idle periods—that create opportunities for power management but also require different approaches than primary storage.

- **Controller Power Consumption**: Storage controllers with deduplication capabilities require significant CPU and RAM, leading to idle power consumption of 225-778W depending on the model generation.

- **Enclosure Overhead**: Disk enclosures consume 155-278W even when idle, which can exceed the power consumption of the drives they house (e.g., ES20 consumes more power than its 16 drives).

- **Power Management Techniques**: The study evaluates spin-down (disk head parked, motor stopped) vs. power-down (disk slot powered off). Power-down saves 78% for ES30 but only 44% for ES20.

- **System-Level Power Savings**: Achieving 20% system power savings requires 40-60% of disks to be in low-power mode; only 2 of 6 configurations achieved >50% savings even with all disks powered down.

## Key Findings

1. **Observation 1**: Idle controller power consumption is still significant (225-778W across models).

2. **Observation 2**: Normalized watts per byte decreases with newer generations (2.89W/TB for DD880 vs 0.675W/TB for DDTBD).

3. **Observation 3**: Power increase under load varies significantly across controller models (20-61% increase from idle to loaded).

4. **Observation 4**: Intel C-states (deep sleep) save only 8% of controller power while causing unacceptable latency penalties.

5. **Observation 5**: Idle power varies greatly across enclosure generations (ES20: 278W, ES30: 179W).

6. **Observation 6**: Enclosure power increases only 15-22% under heavy I/O load.

7. **Observation 7**: Disk power-down is more effective than spin-down for both ES20 and ES30.

8. **Observation 8**: Disk enclosures may consume more power than the drives they house, requiring power management beyond just disk-based strategies.

9. **Observation 9**: Many drives must be in low-power mode before significant total system power savings occur.

## Relevance to Sustainable Computing

This paper is highly relevant to sustainable computing research for several reasons:

1. **Data Center Energy**: Storage systems account for up to 40% of data center power, making storage efficiency critical for overall sustainability.

2. **Challenges Energy Proportionality**: The findings show that backup systems do not achieve energy proportionality—active power is only 20-60% higher than idle, meaning systems waste substantial energy when not fully utilized.

3. **Holistic Power Management**: The paper argues that sustainable storage design must look beyond disk-level optimizations to include controller and enclosure efficiency—a systems-level approach to sustainability.

4. **Hardware Refresh Benefits**: Newer hardware generations show improved power efficiency (ES30 uses 36% less idle power than ES20), supporting arguments for hardware refresh cycles as a sustainability strategy.

5. **Design Implications**: Future power-efficient designs should reduce controller and enclosure power consumption, not just focus on disk power management.

## Citation (APA)

Li, Z., Greenan, K. M., Leung, A. W., & Zadok, E. (2012). Power consumption in enterprise-scale backup storage systems. In *Proceedings of the 4th USENIX Workshop on Hot Topics in Storage and File Systems (HotStorage '12)*. USENIX Association.
