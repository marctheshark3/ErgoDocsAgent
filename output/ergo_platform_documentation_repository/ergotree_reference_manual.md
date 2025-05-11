# ErgoTree: Reference Manual
Source: docs/dev/scs/ergotree.md
Generated: 2025-05-11

## Summary
---
tags:
  - ErgoTree
  - Reference Manual
---

# ErgoTree: Reference Manual

ErgoTree forms the backbone of Ergo's [smart contracts](contracts.md). It is the typed abstract syntax of the ErgoTree language used for defining logical propositions that protect [boxes](box.md) (coin abstractions) in Ergo. While ErgoTree is fundamental, most users interact with it indirectly, primarily developing contracts using a higher-level language called [ErgoScript](ergoscript.md), which later compiles into ErgoTree. ## Understanding ErgoTree

ErgoTree serves as a specialized language, encapsulating the [*universal language*](https://www.martinfowler.com/bliki/UbiquitousLanguage.html) of the [Ergo blockchain](protocol-overview.md). It directly interacts with key components such as [Boxes](box.md),

## Keywords
ergotree, reference, manual, backbone, ergo, contracts](contracts.md, syntax, language, proposition, boxes](box.md, coin, abstraction, user, contract, level, ergoscript](ergoscript.md, language*](https://www.martinfowler.com, bliki, ubiquitouslanguage.html, blockchain](protocol

## Content
## ErgoTree: Reference Manual
ErgoTree forms the backbone of Ergo's smart contracts. It is the typed abstract syntax of the ErgoTree language used for defining logical propositions that protect boxes (coin abstractions) in Ergo. While ErgoTree is fundamental, most users interact with it indirectly, primarily developing contracts using a higher-level language called ErgoScript, which later compiles into ErgoTree.

### Understanding ErgoTree
ErgoTree serves as a specialized language, encapsulating the universal language of the Ergo blockchain. It directly interacts with key components such as Boxes, Tokens, and Zero-Knowledge Sigma-Propositions. ErgoTree is optimized for efficient storage and rapid execution.
A language intended for writing blockchain contracts must be deterministic to ensure spam-resistance. It also needs to be simple yet expressive enough to function as a solid platform for contractual money. ErgoTree meets these requirements, making it an essential tool for creating, securing, and managing boxes on the Ergo blockchain.
Complementing ErgoTree is a frontend language named ErgoScript. Drawing inspiration from Scala/Kotlin, ErgoScript shares common subsets with Java and C#, making it user-friendly for programmers acquainted with these languages. ErgoScript is designed to attract a broad spectrum of programmers with its intuitive approach.

### Structure, Authentication, and Application
ErgoTree, distinct from low-level languages like stack-based EVM assembly, is structured as a typed abstract syntax tree. In this regard, ErgoTree is a kind of authentication language aka "smart signature" used to validate transactions or actions by verifying specific conditions.
ErgoTree achieves this by combining:
Secret Data Predicates: Conditions verifying confidential information such as digital signatures or secret keys.
Blockchain Context Predicates: Conditions dependent on the transaction's specific context within the blockchain.
By evaluating these predicates, ErgoTree authenticates transactions, ensuring their legitimacy and adherence to set rules. Its ability to validate and secure transactions while adapting to the transaction context makes ErgoTree a versatile tool, extending its applicability to various digital platforms, including other cryptocurrencies and Central Bank Digital Currencies (CBDCs), or even non-monetary digital objects where smart access could be needed. Off-chain applications often need to perform similar validations; see Fleet SDK Recipes for examples using JavaScript/TypeScript.
Additional parties can be authorized
Parties can delegate authorization
AND/OR expressions
Conditions can extend beyond signer identity.

### Key ErgoTree Concepts
ErgoTree is written into UTXO boxes and is subsequently evaluated by the transaction verifier.
The propositions are stored in the blockchain in the ErgoTree serialization format. This format optimizes for compact storage, swift script execution, and efficient transaction validation.
The reference implementation of ErgoTree is in Scala, but alternative implementations can utilize other languages.
ErgoTree's binary format intentionally omits metadata, which might be necessary for various Ergo applications.

### Additional Resources
ErgoTree serialization section available here.
Constant-less lambdas.
ErgoTree as an Authentication Language.
Human representation for ergo tree #812.
ErgoTree pseudo-code: Generates pseudo code for compiled ErgoTrees on a best effort basis.
