# Layer 1: On-chain Scalability in Ergo
Source: docs/dev/protocol/scaling/layer1.md
Generated: 2025-05-11

## Summary
---
tags:
- Sharding
- Sub Block Confirmation Protocols
- Microblocks
---
# Layer 1: On-chain Scalability in Ergo

Layer 1, the foundational protocol layer of a blockchain system, is responsible for core functions such as transaction processing, consensus mechanisms, and security protocols. Ergo's Layer 1 is designed with a focus on scalability, incorporating features that boost transaction processing capacity and overall throughput. ## Current Scalability Features

### Extended UTXO Model (EUTXO)
Ergo utilizes an enhanced version of Bitcoin's UTXO model, known as EUTXO, which enables:

- Turing Complete smart contracts
- Parallel transaction processing
- Higher throughput compared to account-based models
- Efficient state management

### Protocol Optimizations
Recent developments have improved the protocol's efficiency through:

- Removal of unused complexity from the Sigma protocol
- Enhanced code readability and maintenance
- Refined transaction ordering and mempool tracking
- Regular node version updates addressing performance

## Mainnet 5.0 and Beyond

### Just-in-Time Costing
The introduction of [Just in time costing](jitc.md) in Node V5 has led to:

- 5-10x increase in block capacity
- Improved transaction processing capability
- More efficient resource utilization

### Miner Parameter Adjustments
Developers are actively exploring:

- Increased block size parameters
- Enhanced transaction size limits
- Optimized mining efficiency
- Improved difficulty calculations through Autolykos updates

## Future Scalability Enhancements

### Microblocks and the Ergo Block Extension Section

Ergo's [block](block.md) structure includes extension sections containing:

- Mandatory and arbitrary key-value data
- Anchors for microblock creation
- Support for service chains
- Potential for generic sidechain implementation

These features enable:

- Faster block generation times
- Improved transaction throughput
- Support for velvet or soft forks
- Creation of Aspen-style service chains


### Sub-Block Confirmation Protocols

Ergo is actively developing sub-block confirmation protocols that will:

- Group transactions into sub-blocks
- Reduce confirmation times
- Increase overall throughput
- Improve transaction processing efficiency This development is guided by EIP-15 and builds upon established research from platforms like:

- [Bitcoin-NG](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-eyal.pdf)
- [Flux](https://www.usenix.org/system/files/atc20-li-chenxing.pdf)




### Sharding
Sharding represents a promising avenue for future scalability improvements by:

- Partitioning the blockchain database into smaller segments
- Enabling parallel transaction processing
- Maintaining security while improving throughput

For detailed information, refer to:

## Keywords
sharding, block, confirmation, protocols, microblocks, layer, chain, scalability, ergo, protocol, system, core, function, transaction, processing, consensus, mechanism, security, focus, feature

## Content
## Layer 1: On-chain Scalability in Ergo
Layer 1, the foundational protocol layer of a blockchain system, is responsible for core functions such as transaction processing, consensus mechanisms, and security protocols. Ergo's Layer 1 is designed with a focus on scalability, incorporating features that boost transaction processing capacity and overall throughput.

#### Extended UTXO Model (EUTXO)
Ergo utilizes an enhanced version of Bitcoin's UTXO model, known as EUTXO, which enables:
Turing Complete smart contracts
Parallel transaction processing
Higher throughput compared to account-based models
Efficient state management

#### Protocol Optimizations
Recent developments have improved the protocol's efficiency through:
Removal of unused complexity from the Sigma protocol
Enhanced code readability and maintenance
Refined transaction ordering and mempool tracking
Regular node version updates addressing performance

#### Just-in-Time Costing
The introduction of Just in time costing in Node V5 has led to:
5-10x increase in block capacity
Improved transaction processing capability
More efficient resource utilization

#### Miner Parameter Adjustments
Developers are actively exploring:
Increased block size parameters
Enhanced transaction size limits
Optimized mining efficiency
Improved difficulty calculations through Autolykos updates

#### Microblocks and the Ergo Block Extension Section
Ergo's block structure includes extension sections containing:
Mandatory and arbitrary key-value data
Anchors for microblock creation
Support for service chains
Potential for generic sidechain implementation
These features enable:
Faster block generation times
Improved transaction throughput
Support for velvet or soft forks
Creation of Aspen-style service chains

#### Sub-Block Confirmation Protocols
Ergo is actively developing sub-block confirmation protocols that will:
Group transactions into sub-blocks
Reduce confirmation times
Increase overall throughput
Improve transaction processing efficiency
This development is guided by EIP-15 and builds upon established research from platforms like:
Bitcoin-NG
Flux

#### Sharding
Sharding represents a promising avenue for future scalability improvements by:
Partitioning the blockchain database into smaller segments
Enabling parallel transaction processing
Maintaining security while improving throughput
For detailed information, refer to:
On the Security and Performance of Blockchain Sharding
Sharding and Atomic Composability on Ergo

#### Ergo Improvement Proposals (EIPs)
EIPs serve as the primary mechanism for protocol enhancement through:
Community-driven proposals
Focused scalability improvements
Systematic implementation processes
Regular protocol updates

#### Node Version Updates
Regular updates to the Ergo node software provide:
Bug fixes and performance enhancements
New scalability features
Improved difficulty calculations
Refined Autolykos implementation

### Research and Development
Ongoing research continues to explore:
Advanced sharding techniques
Novel consensus mechanisms
Improved transaction ordering
Enhanced mempool management
For the latest developments in these areas, refer to Flux: Revisiting Near Blocks for Proof-of-Work Blockchains.
