# Merkle Trees in Ergo
Source: dev/data-model/structures/merkle/merkle-tree.md
Generated: 2025-05-11

## Summary
---
tags:
  - Merkle Tree
  - Data Structures
  - Cryptography
---

# Merkle Trees in Ergo

*(Back to: [Data Structures](../data-structures.md) | [Data Model](../../data-model.md))*

## Overview

**Merkle Trees** are a fundamental [data structure](data-structures.md) in the Ergo blockchain, ensuring the integrity and authenticity of data. They play a crucial role in various blockchain operations, from verifying [transactions](../../protocol/transactions.md) within [blocks](../../data-model/block.md) to securing additional metadata in the [Extension Block](../../data-model/extension-section.md). While similar to the Merkle Tree implementation in Bitcoin—where trees are constructed for block transactions and transaction witnesses (introduced with [SegWit](https://en.bitcoin.it/wiki/Segregated_Witness))—Ergo extends this concept by combining transactions and their corresponding [spending proofs](../.. /protocol/tx/signing.md) into a single Merkle Tree.

## Keywords
merkle, tree, data, structures, cryptography, trees, ergo, datum, structures](, /data, structures.md, model](, structure](data, blockchain, integrity, authenticity, role, operation, verifying, blocks](

## Content
## Merkle Trees in Ergo
(Back to: Data Structures | Data Model)

### Overview
Merkle Trees are a fundamental data structure in the Ergo blockchain, ensuring the integrity and authenticity of data. They play a crucial role in various blockchain operations, from verifying transactions within blocks to securing additional metadata in the Extension Block. While similar to the Merkle Tree implementation in Bitcoin—where trees are constructed for block transactions and transaction witnesses (introduced with SegWit)—Ergo extends this concept by combining transactions and their corresponding spending proofs into a single Merkle Tree.
The Merkle Tree format in Ergo follows a specific structure and encoding scheme that is essential for developers working with Merkle proofs and validating data inclusion. For detailed information on the Merkle Tree format, leaf nodes, internal nodes, and the process of validating Merkle proofs, refer to the Merkle Tree Format and Merkle Tree Validation sections.

### Key Characteristics
Binary Tree Structure: Ergo employs a binary structure for its Merkle Trees, where each node has two children. Leaf nodes contain hashes of transaction data or proofs, while internal nodes contain hashes of their child nodes.
Cryptographic Security: The cryptographic hashes ensure that any alteration in the underlying data is reflected in the Merkle Root, making the tree tamper-evident.
Deterministic Byte Representation: The byte representation of transactions in Ergo is deterministic, allowing consistent restoration and verification of Merkle Tree roots, even if transactions are serialized in different formats, such as JSON.
Pregenesis State: Ergo's deterministic pregenesis state, configured at the blockchain's inception, facilitates seamless restoration and verification of state transitions by comparing them with the hashes stored in the block header.

#### Transaction Merkle Tree
The Transaction Merkle Tree is a core component of Ergo, combining all transactions and their corresponding spending proofs into a single Merkle Tree. This structure provides a cryptographic guarantee that the transaction data has not been tampered with, playing a critical role in the Proof-of-Work (PoW) mechanism. The Merkle Root, derived from this tree, is included in the block header, ensuring that any change to a transaction within the block results in a different Merkle Root.
Code Reference: The implementation can be found in the BlockTransactions.scala file.

#### Extension Block Merkle Tree
The Extension Block Merkle Tree secures key-value data like miner votes and protocol parameters. It organizes this data into a binary Merkle Tree, with leaf nodes containing key-value pair hashes and non-leaf nodes containing child node hashes. The root hash is included in the block header, cryptographically committing to the Extension Block data. Merkle proofs allow efficient verification of specific key-value pairs without downloading the entire block. This tree ensures data integrity and enables secure storage of auxiliary blockchain information.
Code Reference: The implementation can be found in the Extension.scala file.

#### Merkle Batch Proofs
Merkle Batch Proofs are an advanced application that allows for efficient verification of multiple data elements within a Merkle Tree, reducing computational overhead. These proofs build on the foundational Merkle Trees used in transactions and the Extension Block.

#### State Proofs
Merkle Trees are also used to create compact proofs of state transitions (related to AD Proofs). These proofs allow for efficient verification of the blockchain state without requiring a full node, which is crucial for lightweight clients to securely participate in the network. An example of how a lite client can check a Merkle-tree-based membership proof is detailed in the Lite Client Checking Merkle Proof documentation.
