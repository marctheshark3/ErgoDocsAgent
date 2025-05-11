# Developer's Guide
Source: docs/dev/get-started.md
Generated: 2025-05-11

## Summary
---
tags:
  - Developer Guide
  - Getting Started
  - Overview
---

# Developer's Guide

/// admonition | Welcome to the Ergo Developer's Guide

Welcome to the comprehensive **Ergo Developer's Guide**! Whether you're a seasoned blockchain developer or just starting out, this guide is designed to provide you with an in-depth understanding of the Ergo platform and the resources available to you. Explore the unique features of Ergo, learn how to develop on our platform, and connect with our vibrant community. ///

## Ergo Platform Overview

Ergo is a next-generation **Proof-of-Work (PoW)* * blockchain platform designed for secure, efficient, and decentralized smart contract execution.

## Keywords
developer, guide, start, overview, admonition, welcome, ergo, blockchain, depth, understanding, platform, resource, feature, community, generation, work, contract, execution, foundation, wave

## Content
## Developer's Guide
/// admonition | Welcome to the Ergo Developer's Guide
Welcome to the comprehensive Ergo Developer's Guide! Whether you're a seasoned blockchain developer or just starting out, this guide is designed to provide you with an in-depth understanding of the Ergo platform and the resources available to you. Explore the unique features of Ergo, learn how to develop on our platform, and connect with our vibrant community.
///

### Ergo Platform Overview
Ergo is a next-generation Proof-of-Work (PoW) blockchain platform designed for secure, efficient, and decentralized smart contract execution. It lays the foundation for a new wave of blockchain-based applications, focusing on scalability, security, and privacy. Ergo leverages advanced technologies like the powerful scripting language ErgoScript, flexible Zero-Knowledge Proofs, and the eUTXO model, an evolution of Bitcoin's UTXO model.
Get a concise overview of Ergo, its standout features, and the technology and decisions that power it on the Why Ergo? page.
Find answers to the most common questions about Ergo in our FAQ.

#### Key Features
ErgoScript: A simple high-level language that enables clear descriptions of contractual logic. ErgoScript supports the creation of flexible crypto-contracts based on Σ-protocols (a class of Zero-Knowledge Proofs), allowing for privacy-preserving transactions and complex smart contract functionality.


Extended UTXO Model (eUTXO): The eUTXO model allows each UTXO to carry arbitrary data and be protected by an arbitrary predicate or spending condition. This flexibility enables the representation of various assets, tokens, and smart contract states within the blockchain.


Mining with Autolykos: Ergo utilizes Autolykos, an efficient, ASIC-resistant Proof-of-Work algorithm designed for a fair launch.

Learn about Ergo's Emission schedule.



NiPoPoWs: Short for Non-Interactive Proofs of Proof-of-Work, these are compact data structures that validate blockchain events without needing full network connectivity or downloading all block headers. They enable efficient light clients, log-space mining, and trustless sidechains.


Storage Rent: Also known as demurrage, this mechanism mitigates blockchain bloat and turns it into a profitable venture by charging for on-chain storage.


Turing-Complete Smart Contracts: Ergo supports Turing-complete smart contracts, enabling complex on-chain computations.
::cards::
[
  {
    "title": "📚 DeCo EU Layman Class - Basics of eUTxO",
    "content": "A great introductory course aimed at the layman from Decentralised Collaboration.",
    "url": "https://www.youtube.com/watch?v=SAWeW6wajEw"
  },
  {
    "title": "🧾 Learning Ergo 101: eUTXO Explained for Human Beings",
    "url": "https://dav009.medium.com/learning-ergo-101-blockchain-paradigm-eutxo-c90b0274cf5e"
  },
  {
    "title": "📹 Learning Blockchains like Cardano and Ergo",
    "content": "Discusses the process of learning blockchain concepts, emphasizing the importance of understanding theoretical aspects and practical interaction through playgrounds and nodes.",
    "url": "https://w...

#### Transactional Model
Ergo adopts a transactional approach similar to Bitcoin's UTXO model. In this model, transactions utilize and produce single-use entities known as 'boxes'. Every transaction in Ergo represents an atomic state transition, consuming boxes from the state and creating new ones in their place. The eUTXO model allows each UTXO to carry arbitrary data and be protected by an arbitrary predicate (or spending condition). The data can represent various tokens or smart contract states.
This image illustrates the structure and process flow of a blockchain transaction on the Ergo platform using its extended UTXO model (eUTXO).

##### Boxes & Their Components
Registers within Boxes: Boxes come equipped with multiple registers capable of holding various assets and complex ErgoScript types.


Assets in Ergo: Dive deeper into the different assets that can be held within these boxes.
Ergo also supports advanced data structures like AVL+ Trees which can be used to store and authenticate large amounts of data on-chain.

##### Tutorials & Guides
Ergo Platform Basic Starter Tutorial


Create & Send a Transaction: A video tutorial on creating and sending a transaction using AppKit.


Sign a Transaction: Learn how to sign a transaction with Sigma Rust.


Sending a Chained Transaction: A guide on sending a chained transaction using Ergpy.


Getting Started with Fleet SDK: A beginner's guide to the Fleet SDK.

##### Tokens & NFTs
Issuing a Token: A step-by-step guide on how to issue a token on Ergo.


Burning a Token: Learn how to burn a token, effectively removing it from circulation.


Minting an NFT: A comprehensive guide on creating a Non-Fungible Token (NFT) on Ergo.


Minting an On-Chain NFT: Don't want to rely on third-party storage? You can squeeze an NFT directly into the registers!

### ErgoScript
ErgoScript is a super-simple subset of Scala, enabling clear descriptions of contractual logic that can be Turing-complete. It is flexible enough to allow for ring signatures, multi-signatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation.
The Account model of Ethereum is imperative, meaning that sending coins from Alice to Bob requires changing balances in storage through a series of operations. In contrast, Ergo's UTXO-based programming model is declarative. ErgoScript contracts specify conditions for a transaction to be accepted by the blockchain, not changes to be made in the storage state as a result of the contract execution.

#### Introduction
Quick Primer
Core Concepts of ErgoScript
Sigma Language
Creating a Simple Pay-to-Script App

#### Experimenting
escript.online


PlutoMonkey: Compile any ErgoScript contract into a P2S. Check out these simple examples.


Scastie: An online compiler tailored for Scala, perfect for developers eager to experiment, share, or learn Scala.


Kiosk: A web-based UI to explore ErgoScript. (Corrected path)


Ergo-Puppet: An advanced tool built on the Ergo Playground, designed for off-chain experimentation and unit testing of Ergo contracts.

#### Tooling
Ergo Development Generics Elements


VSCode ErgoScript Language Support


ErgoScala: A compiler for Ergo smart contracts written in ErgoScala (a subset of Scala).


CLI Compiler: A Command Line Interface tool to compile ErgoScript code into an Ergo address.


FlowCards: A declarative framework for developing Ergo dApps.


ergo-playgrounds: Run contracts and off-chain code in the browser.


ergo-script-re: Libraries for Ergo Script reverse engineering and analysis.

#### Courses
If you're interested in deepening your understanding of ErgoScript and the Ergo ecosystem, consider taking one of the following courses:
DeCo Education: Into the Woods: This course provides a comprehensive introduction to the Ergo ecosystem.


ErgoScript 101 Crash Course (Slides): A crash course covering the basics of ErgoScript, perfect for beginners.


Learn ErgoScript By Example Via The Ergo Playground with Robert Kornacki (Video): This video tutorial offers practical examples of how to use ErgoScript in the Ergo Playground.


DeCo-Education/ErgoScript-Developer-Course: A more advanced course for developers looking to build on their ErgoScript knowledge.

#### Tutorials
ErgoScript by Example Repository


Testing Ergo Contracts Off-chain


Debugging ErgoScript


ergo-playground: A collection of miscellaneous scenarios implemented on the Ergo blockchain.

#### Boilerplate
scala-play-next-ergo


ergo-scala-skeleton-app


The Ergo Web Template: An introductory guide for individuals new to Ergo, offering a hands-on experience with essential Ergo functionalities.

ergo-play-boilerplate: Barebone code to jump into Ergo development quickly.

#### Advanced Tutorials
ErgoScript Tutorial


Advanced ErgoScript Tutorial

#### Interpreters
ErgoScript has two compiler and ErgoTree interpreter implementations for the Sigma Language:
Sigmastate-interpreter: For JVM languages, utilized by AppKit.


Sigma-Rust: A simpler alternative for the ErgoTree interpreter and transaction tools.

### Cryptography
Ergo has generic support for ring and threshold signatures, as well as a variety of cryptographic protocols via composable sigma-protocols built into the core.
Sigma Protocols (Σ-Protocols) are the foundation of Ergo’s smart contracts. Their advantage is that they are composable using simple AND/OR logic. When combined with a blockchain, these composable proofs enable very powerful use cases, allowing for the implementation of sophisticated tasks that would otherwise be impossible, risky, or expensive on other platforms.

#### Crypto Primitives
Hash Functions:

Sha256: Secure Hash Algorithm 256-bit.
Blake2b256: A cryptographic hash function faster than MD5 and SHA-256, providing security similar to the strongest hash functions available.



Encoding:

Base58: A binary-to-text encoding scheme used for encoding Bitcoin addresses and other text-based data.



Signing Algorithms:

ECDSA (secp256k1): Elliptic Curve Digital Signature Algorithm over the secp256k1 curve, widely used in Bitcoin and other cryptocurrencies.
Schnorr: A digital signature scheme that is simple, provably secure in the random oracle model, and allows for the aggregation of multiple signatures into a single signature, enhancing efficiency and privacy.



Primitive Secrets:

Schnorr Signature: A proof of knowledge of a discrete logarithm with respect to a fixed group generator.
Diffie-Hellman Tuple: A proof of equality of discrete logarithms, enabling secure exchange of cryptographic keys over a public channel.



Non-Interactive Proofs:

The proofs of sigma-statements are made non-interactive with the Fiat-Shamir transformation, which converts an interactive proof of knowledge into a non-interactive one by using a cryptographic hash function.



Additional Cryptographic Standards:

EIP-0003: Deterministic Wallet Standard: A standard defining the structure and operation of deterministic wallets in the Ergo platform.
See this page for a description of the global cryptographic functions available in ErgoScript. (Corrected path and anchor)

#### Tutorials
Creating a 3-out-of-5 Threshold Signature


Message Signing and User Authentication


Verifying Schnorr Signatures in ErgoScript


Updateable Multisig Pattern


Making and Implementing a Signature, Elliptic Curves, and Extended Keys: Ergo with C#

#### Tools
Scrypto: A comprehensive open-source cryptographic toolkit, specifically engineered to simplify and safeguard the process of integrating cryptography into your applications. Supports AVL+ Trees and Batch Merkle Proof Serialization and Deserialization.

#### Merkle Trees
Merkle Trees are a fundamental data structure in the Ergo blockchain, ensuring the integrity and authenticity of data. They play a crucial role in various blockchain operations, from verifying transactions within blocks to securing additional metadata in the Extension Block. Ergo extends the concept of Merkle Trees by combining transactions and their corresponding spending proofs into a single Merkle Tree.
Developers should familiarize themselves with Merkle Trees and their associated code implementations to effectively leverage them in their Ergo projects.

#### AVL Trees (Plasma)
AVL trees are highly efficient authenticated data structures natively supported in Ergo. These trees offer several benefits, including the ability to authenticate data properties without accessing the entire dataset. Developers can seamlessly integrate AVL trees into their Ergo applications using one of the Plasma libraries.

#### Multi-Stage Protocols
Multi-Stage Contracts is a technique where, using transaction trees, we can emulate persistent storage in UTXO-based systems by linking several UTXOs containing small pieces of code to form a large multi-stage protocol. This enables on-chain computations, making it possible to process parallelized actions on top of smart contracts and construct Turing-complete applications.

### App Development
Developers have a plethora of tools, libraries, SDKs, frameworks, and utilities at their disposal to seamlessly interact with the blockchain, craft applications, and present them to users. Navigate through the Developer Section to use grid buttons that help refine your technical stack requirements and pinpoint the ideal tooling.
If you're aiming to develop a comprehensive decentralized application on Ergo, consider the following SDKs and frameworks tailored to your specific needs:
/// admonition | As a spreadsheet!
    type: info
Most repositories are also categories on Grist. This is a great place to start if you're looking for a specific repository or want to see what's currently being worked on.
///

#### Primary SDKs
AppKit: The go-to SDK for JVM developers, supporting Java, Scala, Kotlin, and Mobile platforms.

General Example
Using AppKit with Python
AppKit by Example



Fleet SDK: A pure JS library designed for effortless Ergo transaction creation.

Getting Started with Fleet SDK
The Ergo Web Template: An introductory guide for individuals new to Ergo, offering a hands-on experience with essential Ergo functionalities.



SigmaRust: An ErgoTree interpreter with transaction tools and bindings for JS/TS/Swift/Java/C/Ruby.

Address Generation Demo
Create Transaction Demo

#### Alternative SDKs
Ergpy: A Python-JVM wrapper facilitating interactions with the Ergo blockchain.


Mosaik: A dedicated UI system crafted for Ergo dApps.


JSON dApp Environment


Headless dApp Framework: A Rust-based framework for creating Ergo Headless dApps, marking the debut of a portable UTXO-centric headless dApp development framework on any blockchain.


RustKit (In Development): An upcoming toolkit aiming to align the Rust development experience with the JVM.

#### Payments
ErgoPay: Ergo's dApp connector for non-web wallets.


dApp Connector: For connecting dApps to web-based wallets like Nautilus and SAFEW.


Proxy Contracts: A smart contract design used in blockchain ecosystems to enable secure and controlled interaction between users and decentralized applications.

#### Libraries
ergo-lib-go: Go wrapper around C bindings for ErgoLib from sigma-rust.


ergo-lib-wasm: Ergo-lib bindings for JS/TS.


ergo_client: Rust library containing HTTP clients for various Ergo applications.


sigma-builders: Easy-to-use library for creating protocol abstractions interacting with the Ergo blockchain.

#### Templates
::cards::
[
  {
    "title": "📕 Side Tooling for Building dApps on Ergo",
    "url": "https://dav009.medium.com/ergo-101-side-tooling-for-building-dapps-on-ergo-c71889d60826",
    "content": "Building functional dApps on Ergo requires more than just smart contracts and transactions."
  },
  {
    "title": "📕 DeCo Education: DApp Components - Backend",
    "url": "https://deco-education.github.io/deco-docs/docs/into-the-woods/trail2-ergo-coding/dapp-components"
  },
  {
    "title": "📕 DeCo Intro Lessons: Build a Mobile App on Android or iOS",
    "url": "https://www.youtube.com/watch?v=qR0_k7VH6KI&list=PLopsKGshj0B4BpMoSMh5hQk8gVfWk-si6"
  }
]
::/cards::

#### Ergo Node & Network
Ergo Node: The Ergo Node forms the core of Ergo's P2P network, maintaining and synchronizing the entire blockchain.
Bootstrap from UTXO Snapshot: Expedite the setup of a pruned full node on the testnet by bootstrapping from a UTXO snapshot.
Fork Your Own Chain: Learn how to customize and create your own chain with specific parameters.

#### API & Programmatic Access
Node API: Gain a comprehensive overview of the Ergo node API functionalities.
Public APIs: If you prefer not to run your own node, you can utilize these public APIs for a variety of functionalities.

#### Explorers
Public Explorers can be accessed at explorer.ergoplatform.com and testnet.ergoplatform.com.


Delve deeper into blockchain data with GraphQL.


Explorer & Node Bundles: Install both locally for a comprehensive blockchain experience.

uExplorer: A lightweight Ergo explorer backed by CassandraDB.
Blockchain Explorer with Raspberry Pi: Learn how to set up an explorer using Raspberry Pi.

#### Toolkits
danaides: A high-performance blockchain toolkit.

#### Off-chain
Bootstrap an Oracle Pool on Testnet


Running Off-chain Bots

### Documentation & Reports
Foundational Papers: Explore the academic and technical papers that laid the groundwork for Ergo.


EF Transparency Report: Gain insights into the Ergo Foundation's operations and transparency initiatives.


Ergo's Social Contract: Delve into the principles and commitments that guide Ergo's community and development.

Howey Test Analysis: Understand how Ergo measures up against the Howey Test for securities.

#### Further Resources
Completeness of Ergo | Kushti | Ergoversary Summit 2023: Video discussing the completeness aspects of the Ergo platform.

### Introductory Resources
::cards::
[
  {
    "title": "📚 DeCo Intro Lessons",
    "content": "Programming basics for the layman from Decentralised Collaboration (DeCo).",
    "url": "https://www.youtube.com/watch?v=qR0_k7VH6KI&list=PLopsKGshj0B4BpMoSMh5hQk8gVfWk-si6"
  },
  {
    "title": "📚 DeCo Education Docs",
    "content": "DeCo steps you through eUTXO & NFTs, dApp Development, and Multi-Stage Transactions & Smart Contracts.",
    "url": "https://deco-education.github.io/deco-docs/docs/category/into-the-woods"
  },
  {
    "title": "📹 Ergo Blockchain Crash Course",
    "content": "Ergo crash course presented by developer Luca (lgd), covering the eUTXO model, anatomy of Ergo, and more.",
    "url": "https://www.youtube.com/playlist?list=PL8-KVrs6vXLTVXGwmYXjOBRx3VymB4Vm2"
  }
]
::/cards::

### Connect with Our Community
If you encounter any issues or have questions, feel free to connect with us on any of the following platforms. All our chat platforms are bridged, ensuring seamless communication:
::cards::
[
  {
    "title": "Come Chat!",
    "content": "Join the action on Discord",
    "image": "../assets/img/dev-grid/discord.png", # Corrected image path
    "url": "https://discord.gg/ergo-platform-668903786361651200"
  },
  {
    "title": "ERGOHACK",
    "content": "We host regular hackathons which are a great opportunity to get involved.",
    "image": "../assets/img/grid/05.png", # Corrected image path
    "url": "../events/ergohack.md" # Corrected link path
  },
  {
    "title": "Contribute",
    "content": "See the Contributing Guidelines for information on bounties and grants.",
    "image": "../assets/img/grid/05.png", # Corrected image path
    "url": "../contribute/standards/guidelines.md" # Corrected link path to likely target
  }
]
::/cards::
/// admonition | Chatbots!
    type: info
To further explore and understand Ergo's concepts, you can interact with the following chatbots:
General Chatbot


ErgoScript Chatbot
///

#### Analytics & Insights
Ergo Watch: Dive into on-chain analytics and data.

#### Community Knowledge Base
Ergonaut Space: Discover Ergo's community-driven wiki, filled with insights and information.

#### Explore the Ecosystem!
Sigmaverse.io: Explore a diverse range of dApps built on Ergo.


ErgCube: Another platform to discover and interact with Ergo dApps.


The Ecosystem section on this site acts as a directory for projects building on Ergo and potential future ideas.
