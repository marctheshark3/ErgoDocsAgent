# sigmastate-interpreter - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/sigmastate-interpreter/](https://docs.ergoplatform.com/dev/scs/sigmastate-interpreter/)
Generated: 2025-05-11

## Summary
The sigmastate-interpreter repository contains the core implementations of the ErgoScript compiler and ErgoTree Interpreter. These tools are part of a broader framework that supports a family of Sigma-protocol based authentication languages, collectively known as the Sigma Language. This library is integral to the operation of the Ergo Node and the ergo-wallet. It serves as the backbone for processing and validating ErgoScript contracts, ensuring that transactions comply with the defined cryptographic conditions. For an alternative and potentially more detailed documentation source generated from the repository, explore the Sigmastate Interpreter on DeepWiki In Bitcoin, each coin is secured by a script written in a stack-based language, which is evaluated by the Bitcoin Script interpreter.

## Keywords
sigmastate, interpreter, repository, core, implementation, ergoscript, compiler, ergotree, tool, part, framework, family, sigma, protocol, authentication, language, library, operation, ergo, node

## Content
## Sigmastate Interpreter#
The sigmastate-interpreter repository contains the core implementations of the ErgoScript compiler and ErgoTree Interpreter. These tools are part of a broader framework that supports a family of Sigma-protocol based authentication languages, collectively known as the Sigma Language.
This library is integral to the operation of the Ergo Node and the ergo-wallet. It serves as the backbone for processing and validating ErgoScript contracts, ensuring that transactions comply with the defined cryptographic conditions.
DeepWiki Documentation
For an alternative and potentially more detailed documentation source generated from the repository, explore the Sigmastate Interpreter on DeepWiki

#### Key Components#
ErgoScript Compiler:
The ErgoScript Compiler translates high-level ErgoScript code into low-level ErgoTree bytecode. This bytecode can then be stored in UTXO coins to define spending conditions, akin to how scripts function in Bitcoin but with enhanced flexibility and capabilities.


ErgoTree Interpreter:
The ErgoTree Interpreter executes the ErgoTree bytecode within a specific blockchain context. It evaluates the scripts against the current state of the blockchain and the spending transaction, ultimately producing a boolean outcome that determines the validity of the transaction.

#### Sigma Language Background#
In Bitcoin, each coin is secured by a script written in a stack-based language, which is evaluated by the Bitcoin Script interpreter. ErgoScript and the ErgoTree interpreter generalize this concept into an "authentication language" that can express complex spending conditions using Sigma protocols. These protocols allow for sophisticated cryptographic proofs, enabling the creation of contracts that can require multiple signatures, threshold signatures, or even conditions based on external data.

#### Prover and Verifier Workflow#
The Sigmastate Interpreter involves two primary components in transaction processing:
Prover:
The Prover uses the ErgoTree interpreter to reduce a high-level spending condition (ErgoTree) into a Sigma protocol proposition (SigmaBoolean). This proposition is then converted into a cryptographic proof using the Fiat-Shamir transformation, ensuring that the transaction can only be signed by parties possessing the necessary secrets.


Verifier:
The Verifier also uses the ErgoTree interpreter to independently reduce the ErgoTree into a SigmaBoolean. It then checks the provided proof against this proposition. This process ensures that the transaction is valid and the necessary conditions for spending are met.

#### Integration and Usage#
While the sigmastate-interpreter library provides the low-level primitives necessary for processing ErgoScript contracts, developers typically interact with these components through higher-level tools.
AppKit:
A more accessible alternative for JVM-based development (Java/Scala/Kotlin) is AppKit, a thin wrapper around the core components provided by the ErgoScript interpreter and Ergo protocol implementations.


SigmaJS:
The library is cross-compiled to JavaScript using Scala.js, allowing developers to use these components directly in web applications via the SigmaJS NPM package.

#### Getting Started#
To start using the sigmastate-interpreter in your Scala project, add the following dependency to your SBT configuration:
libraryDependencies += "org.scorexfoundation" %% "sigma-state" % "5.0.14"
For more advanced usage and direct interaction with the ErgoTree and Sigma protocols, refer to the detailed Sigma Language documentation.
