# ErgoScript vs ErgoTree - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/ergoscriptvergotree/](https://docs.ergoplatform.com/dev/scs/ergoscriptvergotree/)
Generated: 2025-05-11

## Summary
ErgoScript is a high-level, developer-friendly language for writing smart contracts that are then compiled to ErgoTree before being written to the blockchain. The Ergo node does not understand ErgoScript. Instead, it uses a low-level language called ErgoTree, which is a "tree-based" language (somewhat like XML). However, writing code in ErgoTree is difficult. An example of such an ErgoTree program would be which implies that the transaction is valid if condition_3 holds and at least one of condition_1 or condition_2 holds.

## Keywords
ergoscript, level, developer, language, contract, ergotree, blockchain, ergo, node, tree, code, example, program, transaction, condition_3, condition_1, condition_2, hold, equivalent

## Content
### ErgoScript vs ErgoTree#
ErgoScript is a high-level, developer-friendly language for writing smart contracts that are then compiled to ErgoTree before being written to the blockchain.
The Ergo node does not understand ErgoScript. Instead, it uses a low-level language called ErgoTree, which is a "tree-based" language (somewhat like XML).
However, writing code in ErgoTree is difficult.
ErgoTree is similar to Bitcoin's Script in some aspects. 
An ErgoTree program is deterministic and consists of a sequence of boolean predicates joined using AND and OR.
Ergo nodes execute the ErgoTree program contained in a transaction and consider it valid if it evaluates to true.
An example of such an ErgoTree program would be
AND(OR(condition_1, condition_2), condition_3)
which implies that the transaction is valid if condition_3 holds and at least one of condition_1 or condition_2 holds.
The equivalent of the above program in ErgoScript would be
(condition_1 || condition_2) && condition_3
