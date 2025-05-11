# Ergo Modifiers Validation
Source: docs/node/modifiers-validation.md
Generated: 2025-05-11

## Summary
---
tags:
  - Modifiers
  - Validation
  - Node
  - Technical
  - Consensus
---

# Ergo Modifiers Validation

This section contains a list of all consensus-critical validation rules that every node in the network should perform; rules that are not listed in this table should not be considered consensus-critical and enforced by the network. Every rule is enumerated and is initially activated. Rules that could not lead to money printing and are not enforced by serialisers may be disabled later by a miner
voting via soft forks, while new rules may also be added at the same time. **Transaction validation:**

 **Id** | **Validation rule**                                                                                                        | **Soft-forkable** | **Active** | **Modifiers**   
--------|----------------------------------------------------------------------------------------------------------------------------|-------------------|------------|-----------------
 100    | A transaction should have at least one input. | x            | √     | ErgoTransaction 
 101    |

## Keywords
modifiers, validation, node, consensus, ergo, section, list, rule, network, table, money, printing, serialiser, miner, voting, fork, time, modifier, --------|----------------------------------------------------------------------------------------------------------------------------|-------------------|------------|-----------------, transaction

## Content
## Ergo Modifiers Validation
This section contains a list of all consensus-critical validation rules that every node in the network should perform; rules that are not listed in this table should not be considered consensus-critical and enforced by the network.
Every rule is enumerated and is initially activated.
Rules that could not lead to money printing and are not enforced by serialisers may be disabled later by a miner
voting via soft forks, while new rules may also be added at the same time.
Transaction validation:
Id | Validation rule                                                                                                        | Soft-forkable | Active | Modifiers 
--------|----------------------------------------------------------------------------------------------------------------------------|-------------------|------------|-----------------
 100    | A transaction should have at least one input.                                                                              | x            | √     | ErgoTransaction 
 101    | A transaction should have at least one output.                                                                             | x            | √     | ErgoTransaction 
 102    | A number of transaction inputs should not exceed 32767.                                                                    | x            | √     | ErgoTransaction 
 103    | A number transaction data inputs should not exceed 32767.                                                                  | x            | √     | ErgoTransaction 
 104    | A number of transaction outputs should not exceed 32767.                                                                   | x            | √     | ErgoTransaction 
 105    | Erg amount for a transaction output should not be negative.                                                                | x            | √     | ErgoTransaction 
 106    | Sum of transaction output values should not exceed 9223372036854775807.                         ...
