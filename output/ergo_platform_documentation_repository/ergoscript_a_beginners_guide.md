# ErgoScript: A Beginner's Guide
Source: docs/archive/dev/scs/ergoscript-primer.md
Generated: 2025-05-11

## Summary
---
tags:
  - ErgoScript
  - Beginner Guide
---

# ErgoScript: A Beginner's Guide

## What is ErgoScript?

ErgoScript is a powerful, developer-friendly programming language designed specifically for writing [smart contracts](contracts.md) on the [Ergo blockchain](protocol-overview.md). Think of it as a specialized language that allows you to create complex [financial contracts](contracts.md) and applications with unprecedented flexibility and [security](security.md). ## Key Characteristics

### 1. UTXO-Based Model
Unlike [account-based blockchains](accountveutxo.md), ErgoScript uses the [UTXO (Unspent Transaction Output) model](eutxo.md). This means:

- Contracts define conditions for spending coins
- [Transactions](transactions.md) are immutable and more secure
- Improved

## Keywords
ergoscript, beginner, guide, developer, programming, language, contracts](contracts.md, ergo, blockchain](protocol, application, flexibility, characteristics, utxo, based, model, unlike, account, blockchains](accountveutxo.md, unspent, transaction

## Content
### What is ErgoScript?
ErgoScript is a powerful, developer-friendly programming language designed specifically for writing smart contracts on the Ergo blockchain. Think of it as a specialized language that allows you to create complex financial contracts and applications with unprecedented flexibility and security.

#### 1. UTXO-Based Model
Unlike account-based blockchains, ErgoScript uses the UTXO (Unspent Transaction Output) model. This means:
Contracts define conditions for spending coins
Transactions are immutable and more secure
Improved scalability and parallel processing

#### 2. Declarative Programming
ErgoScript is declarative, which means you specify what should happen, not how it happens. For example:
scala
// A simple contract that allows spending only after a specific block height
if (HEIGHT > 100000) signerPubKey else fail()
This contract says: "Allow spending only if the current blockchain height is greater than 100,000, otherwise fail."

#### 3. Sigma Protocols
ErgoScript leverages advanced cryptographic techniques called Sigma Protocols, enabling:
Complex signature schemes
Ring signatures
Threshold signatures
Advanced privacy features

#### Basic Syntax
ErgoScript is a subset of Scala, so if you're familiar with functional programming, you'll feel right at home. Here's a simple example:
```scala
// A contract that requires two of three signatures to spend
val pubKey1 = ...
val pubKey2 = ...
val pubKey3 = ...
sigmaProp(pubKey1 && pubKey2 || pubKey1 && pubKey3 || pubKey2 && pubKey3)
```

#### Development Tools
ErgoScript P2S Playground: Experiment and generate Ergo addresses
Ergo AppKit: Development framework for building Ergo applications

### Common Use Cases
Multi-Signature Wallets
   Create wallets requiring multiple parties to approve transactions


Time-Locked Contracts
   Define contracts that can only be executed after a specific time or block height


Conditional Spending
   Set complex conditions for spending funds based on various parameters

#### Beginner
ErgoScript Overview
UTXO Model Explained

#### Intermediate
Sigma Protocols
Advanced Contract Patterns

#### Advanced
ErgoTree Compilation
Cryptographic Protocols

### Best Practices
Keep contracts simple and readable
Use built-in cryptographic primitives
Always consider transaction validation overhead
Test contracts thoroughly in the playground

### Common Pitfalls to Avoid
Overcomplicating contract logic
Ignoring performance implications
Neglecting error handling
Not understanding UTXO model nuances

### Community and Support
Ergo Developer Forum
Ergo GitHub Discussions
Ergo Developer Telegram

### Next Steps
Experiment with the P2S Playground
Study example contracts
Join community discussions
Start building your first dApp!

### Recommended Reading
Ergo Whitepaper
ErgoScript Technical Documentation
