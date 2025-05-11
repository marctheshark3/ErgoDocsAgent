# Introduction - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/ergotree/ergotree-intro/](https://docs.ergoplatform.com/dev/scs/ergotree/ergotree-intro/)
Generated: 2025-05-11

## Summary
This section describes the typed abstract syntax of the ErgoTree language, which is used to define logical propositions protecting boxes in the Ergo blockchain. Serialized ErgoTree expressions are written into UTXO boxes and then evaluated by the transaction verifier. Most Ergo users do not use ErgoTree directly, as they typically develop contracts in a higher-level language, such as ErgoScript, which is then compiled into ErgoTree. The reference implementation of ErgoTree uses Scala; however, alternative implementations can be written in other languages. This documentation provides a language-neutral specification of ErgoTree for developers creating alternative ErgoTree implementations.

## Keywords
section, syntax, ergotree, language, proposition, ergo, blockchain, expression, utxo, transaction, verifier, most, user, contract, level, ergoscript, reference, implementation, scala, documentation

## Content
## ErgoTree Introduction#
This section describes the typed abstract syntax of the ErgoTree language, which is used to define logical propositions protecting boxes in the Ergo blockchain.
Serialized ErgoTree expressions are written into UTXO boxes and then evaluated by the transaction verifier.
Most Ergo users do not use ErgoTree directly, as they typically develop contracts in a higher-level language, such as ErgoScript, which is then compiled into ErgoTree.
The reference implementation of ErgoTree uses Scala; however, alternative implementations can be written in other languages. This documentation provides a language-neutral specification of ErgoTree for developers creating alternative ErgoTree implementations.
The design space of programming languages is very broad, ranging from general-purpose languages like C, Java, and Python to specialized languages like SQL, HTML, CSS, etc.
The language for writing contracts on the blockchain must have several properties to serve as a robust platform for contractual money:
First, the language and the contract execution environment must be deterministic. Once created and stored in the blockchain, a smart contract should always behave predictably and deterministically; it should depend only on a well-defined data context. 
As long as the data context does not change, any execution of the contract should return the same value every time it is executed on any compliant execution platform or language implementation. General-purpose programming languages are typically not deterministic because they provide non-deterministic operations; ErgoTree avoids these.


Second, the language should facilitate spam-resistance, i.e., defending against attacks where malicious contracts could overload network nodes and bring down the blockchain (Ler17). 
To fulfill this goal, the ErgoTree transaction model supports predictable cost estimation and the fast calculation of contract execution costs, ensuring the evaluation cost of any given transaction remains within accepta...
