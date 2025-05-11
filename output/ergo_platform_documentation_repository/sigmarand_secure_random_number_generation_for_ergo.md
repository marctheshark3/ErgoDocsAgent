# SigmaRand: Secure Random Number Generation for Ergo
Source: docs/eco/sigmarand.md
Generated: 2025-05-11

## Summary
---
tags:
  - SigmaRand
  - Random Number Generation
  - RNG
  - Commit-Reveal
  - dApp
---

# SigmaRand: Secure Random Number Generation for Ergo

## Background

Generating randomness on any blockchain is challenging because every node must come to the same conclusion on the state of the blockchain. Naive approaches to generate randomness can be manipulated by miners or observant attackers. Insecure randomness can be exploited by attackers to gain an unfair advantage in games, lotteries, or any other contracts that rely on random number generation. ## Problem Statement

We need a secure random number generation service for Ergo with the following properties:

- The scheme should be secure.

## Keywords
sigmarand, random, number, generation, commit, reveal, dapp, secure, ergo, background, generating, randomness, blockchain, node, conclusion, state, approach, miner, attacker, insecure

## Content
### Background
Generating randomness on any blockchain is challenging because every node must come to the same conclusion on the state of the blockchain. Naive approaches to generate randomness can be manipulated by miners or observant attackers. Insecure randomness can be exploited by attackers to gain an unfair advantage in games, lotteries, or any other contracts that rely on random number generation.

### Problem Statement
We need a secure random number generation service for Ergo with the following properties:
The scheme should be secure.
The number generated should be equally unpredictable for all participants, i.e., no participant should have an "upper hand".
All participants must agree on the same random number generated.

### Scope
This document describes how the "Commit-Reveal" scheme can be used to solve the problem described above and dives deep into how to implement the protocol for Ergo.

### The Commit-Reveal Protocol
The Commit-Reveal protocol is a multi-party scheme for generating random numbers. It consists of two phases: commit and reveal. The protocol is described in detail on the ergo-randgen GitHub repository.
Commit Phase: In this phase, each participant generates a random seed and calculates its corresponding hash value. They then submit a commitment that contains the hash of their answer and the random seed value. The smart contract stores these commitments on the blockchain.


Reveal Phase: In this phase, participants reveal their answer and the seed value.
Here's how the protocol works:
Party A generates a random number, randomA.
Party A sends a message with the hash of randomA, hash(randomA). This commits Party A to the value randomA, as while no one can guess the value of randomA, once Party A provides it, everyone can verify its correctness.
Party B sends a message with another random number, randomB.
Party A reveals the value of randomA in a third message.
Both parties accept the random number as randomA ^ randomB, the exclusive OR (XOR) of the two values.
The advantage of using XOR is that the final random number is determined equally by both parties, ensuring that neither party can choose an advantageous "random" value.
The ergo-randgen GitHub repository provides a detailed implementation of the Commit-Reveal protocol for Ergo, including example transactions and workflows.
