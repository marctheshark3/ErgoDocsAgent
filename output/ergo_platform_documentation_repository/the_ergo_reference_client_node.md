# The Ergo Reference Client (Node)
Source: docs/node/install.md
Generated: 2025-05-11

## Summary
---
tags:
  - Node
  - Reference Client
  - Installation
  - Setup
  - Guide
---

# The Ergo Reference Client (Node) The Ergo Node is the core software that connects to the Ergo [P2P network](p2p-protocol-overview.md), validates [transactions](transactions.md) and [blocks](block.md), and maintains a copy of the entire [blockchain](protocol.md). Running a node is crucial for the network's decentralization and security. This page outlines the installation options and resources for the Ergo reference client.

## Keywords
node, reference, client, installation, setup, guide, ergo, core, software, network](p2p, protocol, transactions](transactions.md, blocks](block.md, copy, network, decentralization, security, page, option, resource

## Content
## The Ergo Reference Client (Node)
The Ergo Node is the core software that connects to the Ergo P2P network, validates transactions and blocks, and maintains a copy of the entire blockchain. Running a node is crucial for the network's decentralization and security. This page outlines the installation options and resources for the Ergo reference client.
/// details | Alternatives
    {type: info, open: true}
If you're simply looking for a secure place to store your ERG, see the wallets page. Some wallets like Satergo offer an integrated option to install and run a full node.
///
///// details | Installing the Ergo Reference Client
    {type: tip, open: true}
//// details | Minimum Requirements & Pre-requisites
    {type: warning, open: false}
Java
An Ergo node requires a JDK/JRE version >= 9 installed on your system. We recommend using Oracle Java SE or SDKMAN for Unix-based systems:
bash
curl -s "https://get.sdkman.io" | bash
sdk install java 11.0.13.8.1-amzn
Hardware
The minimum hardware requirements are approximately ~20GB of storage for the blockchain and ~8GB of RAM for handling the initial sync. Due to potentially intensive disk I/O during sync, we recommend having at least 4-6GB of RAM available for the node process and using a fast SSD. Running with the -Xmx4G flag on the JVM is advised.
////
//// details | Modes of operation
    {type: notes, open: true}
Ergo node offers various Modes of Operation for user flexibility. For quick sync and full node security, consider setting up a Pruned Full Node.
/// details | Full Archival Node
    {type: tip, open: false}
This mode stores the entire blockchain history. To install from scratch, refer to the manual install page for detailed instructions.
///
/// details | Pruned Full Node
    {type: tip, open: false}
Bootstrap a pruned full node using a verified UTXO set snapshot and NiPoPoWs. This feature allows you to achieve full node security on standard hardware within minutes, eliminating the need to download and validate most of the historical blockcha...
