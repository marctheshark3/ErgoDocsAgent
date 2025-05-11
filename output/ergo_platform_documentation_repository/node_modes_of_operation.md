# Node Modes of Operation
Source: docs/node/modes.md
Generated: 2025-05-11

## Summary
---
tags:
  - Node
  - Modes
  - Full Node
  - Pruned Node
  - Light Node
  - Digest Node
  - Stateless Node
  - SPV
  - Configuration
  - Comparison
---

# Node Modes of Operation

*(Back to: [Node Installation](install.md))* The [Ergo node](install.md) offers several modes of operation, allowing users to balance resource requirements (disk space, memory, bandwidth) with security assumptions and desired functionality. Choosing the right mode depends on your specific use case, such as running a backend for a dApp, securing personal funds, or simply verifying transactions. The primary modes are configured using settings in your `ergo.conf` file, mainly `node.stateType` and `node.blocksToKeep`. Bootstrapping options like `node.utxoBootstrap` and `node.nipopowBootstrap` can significantly speed up the initial synchronization for certain modes but do not define the mode itself.

## Keywords
node, modes, full, pruned, light, digest, stateless, configuration, comparison, operation, installation](install.md, ergo, node](install.md, mode, user, resource, requirement, disk, space, memory

## Content
## Node Modes of Operation
(Back to: Node Installation)
The Ergo node offers several modes of operation, allowing users to balance resource requirements (disk space, memory, bandwidth) with security assumptions and desired functionality. Choosing the right mode depends on your specific use case, such as running a backend for a dApp, securing personal funds, or simply verifying transactions.
The primary modes are configured using settings in your ergo.conf file, mainly node.stateType and node.blocksToKeep. Bootstrapping options like node.utxoBootstrap and node.nipopowBootstrap can significantly speed up the initial synchronization for certain modes but do not define the mode itself.
Here's a comparison of the main operational modes:

### Mode Comparison
| Feature / Mode        | Archival Full Node | Pruned Full Node | Digest (Stateless) Node¹ | Light SPV Client |
| :-------------------- | :------------------------------------------- | :-------------------------------------------- | :-------------------------------------------------- | :------------------------------------------ |
| Primary Goal      | Max Security, Full History                   | Full Security, Reduced Storage                | Full Security, Minimal Storage                      | Tx Verification, Minimal Resources          |
| Key Config        | stateType="utxo"blocksToKeep=-1      | stateType="utxo"blocksToKeep > 0      | stateType="digest"blocksToKeep > 0         | N/A (Client Software)                       |
| Bootstrapping     | Full Sync from Genesis | Full Sync / UTXO Snapshot (utxoBootstrap=true) / NiPoPoW (nipopowBootstrap=true) | Full Sync / NiPoPoW (nipopowBootstrap=true) / UTXO Snapshot¹ | NiPoPoW Sync |
| Storage (Initial) | Very High (100s GB+) | Medium (Snapshot: ~1-2GB + Recent Blocks) | Low (Headers + State: ~1-3GB + Recent Blocks) | Very Low (MBs) |
| Storage (Ongoing) | High (Grows with chain) | Medium (Grows slowly with blocksToKeep) | Low (Grows slowly with blocksToKeep) | Very Low |
| Resource Needs    | High (CPU/RAM/Disk IO) | Moderate | Moderate-Low | Very Low |
| Sync Time         | Very Long          | Fast (with bootstrap) | Fast (with bootstrap) | Very Fast |
| Full Tx Validation| Yes                | Yes (for kept blocks) | Yes (for kept blocks, via ADProofs) | No (Header validation only) |
| API Support       | Full               | Full (for available data) | Limited (May lack endpoints requiring full UTXO set) | N/A (Relies on Full Node API) |
| Wallet Compatibility| Full (incl. restore) | New Wallets OK; No Restore | New Wallets OK; No Restore; Potential issues with standard P2P tx submission reported² | Verification only; Relies on Full Node for tx submission/balance |
| Use Cases         | Mining, Archiving, Max...

### Further Reading
Configuration File
Pruned Full Node Details
Light Full (Digest) Node Details (Covers stateType="digest")
Light SPV Clients / NiPoPoWs
History Pruning (blocksToKeep)
