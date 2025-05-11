# Ergo Headless dApp Framework (HDF)
Source: docs/dev/stack/headless.md
Generated: 2025-05-11

## Summary
---
title: Ergo Headless dApp Framework (HDF)
description: Learn about the Ergo Headless dApp Framework (HDF), a Rust framework for building portable and reusable off-chain logic for Ergo dApps. tags:
  - Headless dApp
  - Framework
  - Rust
  - dApp Development
  - Off-chain Logic
  - EIP-6
---

# Ergo Headless dApp Framework (HDF) The [Ergo Headless dApp Framework (HDF)](https://github.com/ergoplatform/ergo-headless-dapp-framework) is a powerful **Rust framework** designed for developing portable and reusable off-chain logic for Ergo dApps, often referred to as "Headless dApps". It provides developers with the first portable [UTXO](eutxo.md)-based headless dApp development framework on any blockchain.

!!! warning "Testnet Address Limitation"
    Please be aware that the current version of the Headless dApp Framework [does not support testnet addresses](https://github.com/ergoplatform/ergo-headless-dapp-framework/blob/main/src/encoding.rs#L104).

## Keywords
title, ergo, headless, dapp, framework, description, rust, chain, logic, dapps, development, eip-6, hdf)](https://github.com, ergoplatform, developer, portable, utxo](eutxo.md)-based, blockchain, testnet, address

## Content
## Ergo Headless dApp Framework (HDF)
The Ergo Headless dApp Framework (HDF) is a powerful Rust framework designed for developing portable and reusable off-chain logic for Ergo dApps, often referred to as "Headless dApps". It provides developers with the first portable UTXO-based headless dApp development framework on any blockchain.
!!! warning "Testnet Address Limitation"
    Please be aware that the current version of the Headless dApp Framework does not support testnet addresses. Development and testing should target mainnet address formats.

### What Are Headless dApps?
Headless dApps represent a novel approach to dApp development, focusing on creating pure, portable, self-contained logic for interacting with on-chain smart contract protocols.
Key characteristics and benefits include:
Separation of Concerns: They separate the core dApp logic (reading blockchain state, constructing transactions) from the user interface (frontend). The HDF is the "backend" logic, but without a built-in frontend (hence "headless").
Portability: Because they are self-contained logic (often compiled to WebAssembly or native libraries), headless dApps built with the HDF can run anywhere – desktop OS, mobile OS, browsers, servers, bots, etc.
Reusability & Composability: They expose a streamlined interface, allowing various frontends (websites, mobile apps, CLI tools) and automated systems (scripts, arbitrage bots) to easily integrate and interact with the underlying protocol without needing deep knowledge of its internal workings. Multiple headless dApps can be composed together within a single application.
Decentralized Ecosystem: This model encourages a diverse ecosystem of frontends built by different developers or companies, all leveraging the same core headless dApp logic. This contrasts with the traditional model where the protocol creators often also control the single, primary frontend.
New Business Models: It creates opportunities for frontend developers to build value and potentially generate revenue by creating user interfaces for existing headless dApps.
In essence, headless dApps provide the standardized "engine" for interacting with a smart contract protocol, allowing anyone to build the "car" (the user interface or application) around it.

### The Ergo HDF: Goals & Concepts
The Ergo HDF aims to:
Write Once, Run Anywhere: Enable developers to write off-chain logic once in Rust and target all platforms.
Simplified Development: Provide a clearer path from Ergo dApp Specifications (like EIP-6) to a working implementation.
Standardized Interface: Offer easy-to-use methods for frontend implementors to access dApp state and perform actions.
Input Abstraction: Abstract the complexity of finding and selecting input UTXOs using BoxSpec definitions.
Composability: Facilitate building scripts, bots, and complex applications on top of multiple HDF-based dApps.

#### Core Concepts (Based on EIP-6)
The HDF's design aligns with EIP-6: Ergo Smart Contract Protocol Specification Format:
Protocol: Your dApp is defined as a smart contract protocol.
Stage: Represents a specific state within the protocol where a UTXO (box) resides at a point in time. Protocols can be single-stage or multi-stage.
Action: Defines the logic for state transitions – how UTXOs move between stages, enter the protocol, or exit the protocol. Actions involve:
Acquiring Inputs: Gathering necessary UTXOs, user inputs, or external data.
Creating Outputs: Constructing the output UTXOs that represent the new state after the action, embedded within an UnsignedTx.
The HDF provides Rust structs, traits, and utilities to define these stages, actions, input specifications (BoxSpec), and transaction-building logic.

### Getting Started with the HDF
Prerequisites:
Install the Rust toolchain.
Basic understanding of Rust programming.
Familiarity with Ergo's eUTXO model and ErgoScript concepts.


Clone the Repository:
bash
    git clone https://github.com/ergoplatform/ergo-headless-dapp-framework.git
    cd ergo-headless-dapp-framework
Explore Examples: Review the example projects within the repository to understand usage patterns.
Follow Tutorials: Work through the official tutorials (linked below) to build your first headless dApp.
Consult Documentation: Refer to the framework's Rust documentation (often generated via cargo doc --open) and the EIP-6 specification.

### Resources
GitHub Repository: ergoplatform/ergo-headless-dapp-framework (Primary source code, examples, and tutorials)
Video Introduction: Robert Kornacki explains Headless dApps (Covers technical, business, and ecosystem aspects).

#### Tutorials (Located in HDF GitHub Repo)
Math Bounty Headless dApp Series: A step-by-step guide to building a complete headless dApp with a CLI frontend.
Part 1: Getting Started Writing Your First Action
Part 2: Finishing The Headless dApp
Part 3: Writing A CLI Frontend


(Note: The JDE links in the original document refer to a different, potentially related or deprecated project, Ergo-JDE. The HDF tutorials above are the primary resource for this framework.)

#### References
EIP-6: Ergo Smart Contract Protocol Specification Format (Underlying design philosophy).
