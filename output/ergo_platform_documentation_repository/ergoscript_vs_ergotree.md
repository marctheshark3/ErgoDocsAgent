# ErgoScript vs ErgoTree
Source: docs/dev/scs/ergoscriptvergotree.md
Generated: 2025-05-11

## Summary
---
tags:
  - ErgoScript
  - ErgoTree
---

## ErgoScript vs ErgoTree

[ErgoScript](ergoscript.md) is a high-level, developer-friendly language for writing smart contracts that are then compiled to ErgoTree before being written to the blockchain. The [Ergo node](install.md) does not understand ErgoScript. Instead, it uses a low-level language called [**ErgoTree**](https://ergoplatform.org/docs/ErgoTree.pdf), which is a "tree-based" language (somewhat like XML). However, writing code in ErgoTree is *difficult*. - ErgoTree is similar to Bitcoin's Script in some aspects.

## Keywords
ergoscript, ergotree, ergoscript](ergoscript.md, level, developer, language, contract, blockchain, ergo, node](install.md, ergotree**](https://ergoplatform.org, docs, ergotree.pdf, tree, code, bitcoin, script, aspect, program, sequence

## Content
### ErgoScript vs ErgoTree
ErgoScript is a high-level, developer-friendly language for writing smart contracts that are then compiled to ErgoTree before being written to the blockchain.
The Ergo node does not understand ErgoScript. Instead, it uses a low-level language called ErgoTree, which is a "tree-based" language (somewhat like XML).
However, writing code in ErgoTree is difficult.
ErgoTree is similar to Bitcoin's Script in some aspects. 
An ErgoTree program is deterministic and consists of a sequence of boolean predicates joined using AND and OR.
Ergo nodes execute the ErgoTree program contained in a transaction and consider it valid if it evaluates to true.
An example of such an ErgoTree program would be
scala
AND(OR(condition_1, condition_2), condition_3)
which implies that the transaction is valid if condition_3 holds and at least one of condition_1 or condition_2 holds.
The equivalent of the above program in ErgoScript would be
scala
(condition_1 || condition_2) && condition_3
