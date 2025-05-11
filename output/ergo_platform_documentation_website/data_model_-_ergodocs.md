# Data Model - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/data-model/data-model/](https://docs.ergoplatform.com/dev/data-model/data-model/)
Generated: 2025-05-11

## Summary
This document provides a comprehensive and in-depth exploration of Ergo's unique data model, based on the UTXO (Unspent Transaction Output) model, enhanced with powerful smart contract capabilities (eUTXO). Ergo represents a significant advancement in blockchain computational models, extending the traditional Unspent Transaction Output (UTXO) paradigm through its enhanced eUTXO (Extended UTXO) model. Unlike conventional blockchain architectures, Ergo's model introduces: A solid understanding of the blockchain structure lays the groundwork for exploring Ergoâs data model. Ergo blocks contain critical metadata, transactions, and proofs. At the core of Ergo's data model is the "Box," which is Ergo's implementation and extension of the UTXO (Unspent Transaction Output) concept.

## Keywords
document, depth, exploration, ergo, data, model, utxo, unspent, transaction, output, contract, capability, eutxo, advancement, paradigm, extended, blockchain, architecture, introduce, understanding

## Content
## The Ergo Data Model#
This document provides a comprehensive and in-depth exploration of Ergo's unique data model, based on the UTXO (Unspent Transaction Output) model, enhanced with powerful smart contract capabilities (eUTXO).

#### 1.1 Computational Model Evolution & UTXO vs. Account Model#
Ergo represents a significant advancement in blockchain computational models, extending the traditional Unspent Transaction Output (UTXO) paradigm through its enhanced eUTXO (Extended UTXO) model. Unlike conventional blockchain architectures, Ergo's model introduces:
Programmable State Transitions: Enabling complex computational logic within transaction outputs. This contrasts with the account-based model used in other blockchains (like Ethereum), where state is globally mutable. See UTXO vs Account Model Comparison for a comparison of Ergo's model in terms of parallelism, privacy, and scalability.
Stateless Verification: Allowing efficient validation without maintaining complete blockchain state, facilitated by technologies like NIPoPoWs.
Deterministic Execution: Ensuring predictable and verifiable transaction outcomes.

#### 1.2 Fundamental Design Principles#
Computational Completeness: Supporting Turing-complete smart contract execution within strict cryptographic constraints via multi-stage contracts.
Cryptographic Composability: Enabling complex cryptographic protocols through Sigma Protocols.
Scalable State Management: Designing a model that supports parallel transaction processing and efficient state verification.

### 2. Blockchain Structure: Components and Function#
A solid understanding of the blockchain structure lays the groundwork for exploring Ergoâs data model. Ergo blocks contain critical metadata, transactions, and proofs.

#### 2.1 Block Components#
Block Overview: Comprehensive introduction to block structure in Ergo, detailing how blocks aggregate transactions, references, and proofs.
Block Header: Detailed examination of block header components, which include references to previous blocks, difficulty, and other crucial metadata.
Block Transactions: Understanding how transactions are organized within a block to form the ledger state.
AD Proofs: Authenticated Data Proofs enable efficient stateless client verification by providing cryptographic proofs of state transitions.
Extension Section: An exploration of Ergoâs flexible data storage section that can hold additional metadata and information beyond basic transactions.

### 3. Boxes: Foundational State Units#
At the core of Ergo's data model is the "Box," which is Ergo's implementation and extension of the UTXO (Unspent Transaction Output) concept. While traditional UTXOs simply track unspent coins, Ergo's Boxes enhance this model with additional programmable capabilities.

#### 3.1 The Box Concept#
A Box is essentially a "smart UTXO" - it serves the same role as a UTXO in tracking unspent value, but extends this with sophisticated computational features. Like a UTXO, a Box is created when value is sent in a transaction and is consumed (spent) when that value is transferred elsewhere. However, Boxes add the following capabilities that go beyond basic UTXOs:
Immutable State: Each box represents an atomic, immutable state unit that cannot be modified after creation. (Lifecycle details might be added later or linked if a dedicated page exists).


Typed Registers: Boxes contain 10 registers (R0-R9) with specific purposes and rich computational potential:

R0: Monetary Value (in nanoERGs)
R1: Protection Script (Smart Contract)
R2: Assets/Tokens
R3: Creation Details
R4-R9: Flexible, Typed Custom Data Storage
Supports multiple data types: Int, Long, BigInt, GroupElement, Coll[Byte]
Can store complex structures and collections
Densely packed with type-safe access





Programmable Spending Conditions: Each box specifies precise conditions under which it can be spent, enabling complex logic through ErgoScript. See Box Modeling and Box Overview for detailed exploration.
By transforming UTXOs from simple value trackers to programmable state containers, Ergo enables more expressive and flexible blockchain interactions while maintaining cryptographic integrity and computational efficiency.

### 4. Transactions: Engines of State Change#
Transactions define how boxes are created, transformed, and consumed, and are central to Ergoâs dynamic state evolution.

#### 4.1 Transaction Foundations#
Transaction Overview: Fundamental principles of how transactions work in Ergo.
Transaction Composition: Detailed guide to constructing complex transactions off-chain before submitting them on-chain.
Transaction Format: Technical specification of transaction structure, ensuring interoperability and standardization.

#### 4.2 Advanced Transaction Mechanisms#
Chained Transactions: Explore how sequentially dependent transactions can be composed.
Merkle Tree in Transactions: Understanding how Merkle trees provide data integrity and facilitate efficient proofs.
Transaction Signing and Backend Signing: Cryptographic principles and implementations for authenticating transactions.
Transaction Validation: Comprehensive overview of on-chain verification processes that ensure correctness and adherence to protocol rules.

#### 4.3 Specialized Transaction Features#
Data Inputs (Read-Only Inputs): Access additional data in transactions without spending boxes.
Transaction Fees: Understanding fee structures, ensuring that miners are incentivized.
Babel Fees and Babel Fees Plugin: Innovative mechanisms allowing fees to be paid in alternative tokens.

### 5. Assets and Tokens: Powering a Diverse Economy#
Ergo supports a rich ecosystem of assets, from fungible tokens to NFTs, enabling complex economic models.

#### 5.1 Fungible Tokens#
Token Basics: Introduction to tokens within the Ergo ecosystem and their fundamental characteristics.
Asset Standard (EIP-4): Standard for creating and managing tokens in Ergo.
Token Verification (EIP-21): Ensuring token authenticity and integrity.

#### 5.2 Non-Fungible Tokens (NFTs)#
NFT Overview: Comprehensive introduction to NFTs on Ergo.
NFT Creation: Guide to minting NFTs.
NFT Versions (V1 vs V2): Comparison of different NFT implementation standards.
On-Chain NFTs: Storing NFT data directly on the blockchain.
NFT Royalties: Mechanisms for continuous compensation to creators.

#### 5.3 Special Token Concepts#
Perpetual Tokens: Tokens designed to exist indefinitely.
Token Burning: Permanently removing tokens from circulation.
Singletons: Unique tokens with special properties.
Auction Contract (EIP-22): Standard auction contract implementation details.
Artwork Contract (EIP-24): Specialized standard for managing digital artwork tokens.

### 6. Addressing and Identity#
Ergo uses an address system that ensures security, privacy, and flexibility.
Address Basics: Fundamental concepts of Ergo addresses, including encoding, format, and usage.
Address Types: Detailed overview of Pay-to-Public-Key (P2PK), Pay-to-Script-Hash (P2SH), and Pay-to-Script (P2S) address types.
Address Validation: Methods and best practices for validating Ergo addresses, including checksum verification and format validation.

### 7. Payment Standards and Protocols#
Ergo defines protocols to streamline user interactions with wallets and applications.
ErgoPay Protocol (EIP-20): Interaction protocol for mobile wallets and dApps.
Payment Request URI (EIP-25): Standard format for payment requests.
Proxy Contracts (EIP-17): Mechanisms to manage funds and logic via intermediary contracts.

### 8. Cryptographic Foundations#
Ergoâs cryptographic design ensures robust security, privacy, and flexibility.

#### 8.1 Sigma Protocols#
Non-interactive Zero-Knowledge Proofs: Private transaction verification without revealing sensitive data.
Flexible Signature Schemes: Supporting multiple signature types via Sigma Protocols.
Privacy-Preserving Mechanisms: Advanced features to protect user privacy.

#### 8.2 Cryptographic Primitives#
Discrete Logarithm Proofs: Foundational to signature verification (Schnorr).
Ring Signatures: Enhanced privacy through signer ambiguity.
Threshold Signatures: Enabling multi-party computational scenarios.

#### 9.1 Transaction Validation and Script Execution#
Ergo employs a robust, stateless transaction validation approach:
Transaction Construction & Signing: See Transaction Composition, Transaction Format, and Signing.
On-Chain Verification: Transaction Validation and Merkle Proofs.
Script Validation: Detailed in ErgoTree Script Validation and the ErgoScript Language Specification.
Execution Environment: Access blockchain state via Context Variables, ensure deterministic evaluation, and apply [cost constraints]](jitc.md).

#### 9.2 Consensus Algorithm & Storage Rent#
Difficulty Adjustment: A dynamic mechanism that adjusts mining difficulty every epoch to maintain a target block time of approximately 2 minutes, ensuring network stability and predictable block creation despite fluctuations in mining power.
Storage Rent Mechanism: A novel approach that prevents blockchain bloat and ensures long-term sustainability by requiring users to pay rent for storing data on-chain. See the linked page and the detailed guide for implementation, fees, and economic incentives.

### 10. Data Structures and Performance#
General Data Structures
Proof of Proof-of-Work (PoPow): Consensus mechanism enhancement for light clients, related to NIPoPoWs.

#### 10.1 Authenticated Data Structures#
Merkle Trees for efficient state commitment.
Merkle Batch Proof
Merkle Extension
Merkle Light Proof


AVL+ Trees for authenticated key-value storage.
Interlink Vectors: Lightweight blockchain verification.
AD Proofs: Supporting stateless clients.

#### 10.2 Scalability and Efficiency#
Parallel transaction validation inherent in the eUTXO model.
Stateless validation reduces computational and storage overhead.
[Just-in-time costing]](jitc.md) ensures resource use is always checked.
For more information see the scaling section.

#### 11.1 Multi-Stage Transactions#
Multi-Stage Transactions: Understanding how to design and implement complex, multi-step transaction flows using the eUTXO model.
