# EIP37: Tweaking Difficulty Adjustment Algorithm
Source: docs/mining/standards/eip37.md
Generated: 2025-05-11

## Summary
# EIP37: Tweaking Difficulty Adjustment Algorithm

## Overview

- **Author**: kushti
- **Status**: Implemented
- **Created On**: September 23, 2022
- **Type of Change**: Hard Fork Required

> 📖 [Full Documentation](https://github.com/ergoplatform/eips/blob/ddbca24fef5e91e0c80c6881fc31d8831ae69768/eip-0037.md)

## Why Is This Important? The goal of a difficulty adjustment algorithm is to stabilize the time it takes to produce a new block, based on how fast blocks are being mined. In Ergo, we aim for a 120-second average block time. While Bitcoin's algorithm works well in certain conditions, it has its limitations—especially in fluctuating mining environments.

## Keywords
eip37, tweaking, difficulty, adjustment, algorithm, overview, author, kushti, status, september, type, change, hard, fork, documentation](https://github.com, ergoplatform, blob, ddbca24fef5e91e0c80c6881fc31d8831ae69768, goal, time

## Content
### Overview
Author: kushti
Status: Implemented
Created On: September 23, 2022
Type of Change: Hard Fork Required
📖 Full Documentation

### Why Is This Important?
The goal of a difficulty adjustment algorithm is to stabilize the time it takes to produce a new block, based on how fast blocks are being mined. In Ergo, we aim for a 120-second average block time. While Bitcoin's algorithm works well in certain conditions, it has its limitations—especially in fluctuating mining environments. Ergo's original algorithm performed well but was prone to erratic difficulty changes. This proposal aims to make the algorithm more stable and responsive.

### Background and Comparative Analysis
Bitcoin uses a relatively simple adjustment algorithm, but it can struggle with issues like "coin hopping," where miners switch between coins to maximize profits. Ergo previously used a predictive method to anticipate such behaviors. To improve upon both, this proposal blends features from Bitcoin's "classic" algorithm and Ergo's predictive model.

### Key Proposed Changes
Shorter Epoch Length: Reducing the epoch length to 128 blocks, making the system more responsive.
Dual Calculations: Use both a predictive method based on the last eight epochs and the classic Bitcoin-style method.
Predictive Limits: Cap the changes in predictive difficulty to a maximum of 50% per epoch.
Overall Limits: Finally, take an average of both calculated difficulties and limit changes to a maximum of 50% per epoch.

### Simulation Results
We've simulated various scenarios including price fluctuations, consistent growth, and coin hopping. The proposed changes consistently result in lower errors and delays compared to the existing algorithms. This suggests that the proposed changes will make the algorithm more robust and efficient.

### Activation Criteria
Activation Window: Between block #843,776 and block #851,969.
Vote Requirement: At least 232 votes for activation within the last 256 blocks.
Vote Checking: Voting status will be checked every 128 blocks.

### How To Upgrade
To adopt these changes, please update to the Ergo reference protocol client version 4.0.100 or newer.
