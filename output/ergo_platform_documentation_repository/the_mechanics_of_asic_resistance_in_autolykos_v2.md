# The Mechanics of ASIC Resistance in Autolykos v2
Source: docs/mining/asic.md
Generated: 2025-05-11

## Summary
---
tags:
  - ASIC Resistance
  - Autolykos
  - Mining
  - Algorithm
  - Technical
---

# The Mechanics of ASIC Resistance in Autolykos v2

Ergo's Autolykos v2 employs a dynamic strategy to resist Application-Specific Integrated Circuits (ASICs). The system achieves this through scheduled memory table adjustments, effectively increasing the minimum GPU vRAM requirements for mining over time. This ensures that any ASIC built to mine Ergo today will find itself inefficient following future updates.

## Unpacking Memory-Hardness: Lessons from Ethereum and Beyond

Ethereum demonstrated that 'memory-hard' algorithms could still be manipulated by ASICs with on-board memory. Ergo's Autolykos v2 takes a different approach. Let's examine why ASICs with limited memory cannot compete effectively and explore the necessity of storing **_list R_**.

## Keywords
asic, resistance, autolykos, mining, algorithm, technical, mechanics, ergo, strategy, application, specific, integrated, circuits, system, memory, table, adjustment, vram, requirement, time

## Content
## The Mechanics of ASIC Resistance in Autolykos v2
Ergo's Autolykos v2 employs a dynamic strategy to resist Application-Specific Integrated Circuits (ASICs). The system achieves this through scheduled memory table adjustments, effectively increasing the minimum GPU vRAM requirements for mining over time. This ensures that any ASIC built to mine Ergo today will find itself inefficient following future updates.

### Unpacking Memory-Hardness: Lessons from Ethereum and Beyond
Ethereum demonstrated that 'memory-hard' algorithms could still be manipulated by ASICs with on-board memory. Ergo's Autolykos v2 takes a different approach. Let's examine why ASICs with limited memory cannot compete effectively and explore the necessity of storing list R.

#### Diving Deeper into Autolykos
To fully grasp the intricacies of Autolykos v2, we recommend going through the technical breakdown line by line. Here, we provide a high-level overview:
Line 8: This line serves as a gatekeeper, filtering out machines that do not meet the memory requirements.
Hash Generation: In the absence of list R, an ASIC would require multiple cores to dynamically generate 31-byte numerical hashes.
Single-Core Loop Limitations: The process of generating 32 r values in a single cycle is not efficient, resulting in sparse output.
Computational Requirements: To compute a single nonce per hash cycle based on a given J, at least 32 instances of Blake2b256 running dropMsb(H(j||h||M)) are required.
Cost and Efficiency: The practice of storing list R proves to be cost-effective as fetching data from memory is quicker than performing repeated Blake2b256 hash calculations.

#### Comparative Analysis: Ethash vs. Autolykos
Ethash involves N elements when hashing, while Autolykos involves N elements for fetching 32 r values based on indexes generated. Autolykos is more memory-hard due to its higher reliance on memory bandwidth.

### Potential Autolykos Optimizations and Constraints
Hashing Speed: Speeding up the Blake2b256 function can reduce the time to fill list R, though this would entail a considerable investment in specialized hardware.
Memory Bandwidth: Despite minor advantages for Ethash ASIC miners in read speed, this is expected to become negligible as GPU technology advances.

### Blake2b256: Why It Matters
Blake2b256, unlike other hashing algorithms, emphasizes addition operations over XOR, making it both secure and computationally demanding. This makes it difficult for ASICs to gain a significant advantage.

#### Key Features and Considerations
Efficiency: FPGAs can achieve up to 3Mh/W, double the efficiency of the best Nvidia cards.
Availability: A chip shortage and lack of public miners make FPGAs currently non-competitive.
ROI: If you could buy an E300 at retail prices today, the Return on Investment (ROI) would take approximately 52 years.

#### Community Perspective: To FPGA or Not to FPGA?
The decision to allow or restrict FPGAs is up to the Ergo community. While FPGAs are more efficient, GPUs are more accessible, fostering greater decentralization.

### The SRAM Dilemma in FPGA Mining
SRAM, despite its faster read/write capabilities, is not a feasible long-term option for Ergo mining due to its lower density and the algorithm's increasing memory requirements.
By understanding these components, we can appreciate how Autolykos v2 aims to create a more ASIC-resistant, secure, and ultimately, decentralized network.
