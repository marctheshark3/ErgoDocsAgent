# Transactions - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/data-model/block-transactions/](https://docs.ergoplatform.com/dev/data-model/block-transactions/)
Generated: 2025-05-11

## Summary
(Back to: Block Overview) The Transactions section of an Ergo block is the heart of the blockchain's state changes. It contains a list of all the transactions that are included and validated within that specific block. These transactions define how tokens and assets are transferred and how the overall state of the Ergo blockchain evolves. This page covers the structure of the transactions section within an Ergo block.

## Keywords
block, overview, transactions, section, ergo, heart, blockchain, state, change, list, transaction, token, asset, evolve, page, structure, information, core, ergotransaction, class

## Content
## Block Transactions#
(Back to: Block Overview)
The Transactions section of an Ergo block is the heart of the blockchain's state changes. It contains a list of all the transactions that are included and validated within that specific block. These transactions define how tokens and assets are transferred and how the overall state of the Ergo blockchain evolves.
In the right place?
This page covers the structure of the transactions section within an Ergo block. For more general information on transactions, see the Transaction Overview page.

### Function#
Value Transfer: Ergo transactions enable users to transfer ERG (Ergo's native token) and other custom tokens/assets to other users on the network.
State Transition: Each transaction consumes existing unspent boxes (which hold tokens and assets) and creates new boxes with potentially modified values and ownership. This process updates the state of the UTXO set.
Smart Contract Execution: Transactions can trigger the execution of scripts within boxes, allowing for complex logic and decentralized applications to be implemented on the Ergo blockchain.

### Structure#
The core structure of an Ergo transaction is defined by the ErgoTransaction class in ErgoTransaction.scala.
Here's a breakdown of its main components:
inputs: A list of Input objects, each referencing an existing box that the transaction will spend. Each input includes a spendingProof (see Transaction Signing) to prove the spender has the right to consume the box.
dataInputs: A list of DataInput objects referencing boxes that the transaction needs to access for its scripts but won't spend. These provide data to the scripts without requiring ownership.
outputCandidates: A list of ErgoBoxCandidate objects representing the new boxes that the transaction will create. These candidates define the values, assets, and scripts of the new boxes.

### Validation#
Ergo transactions undergo rigorous validation to ensure they are legitimate and maintain the integrity of the blockchain:
Stateless Validation: Checks that don't require accessing the blockchain state, including:
Ensuring the transaction has inputs and outputs.
Verifying basic rules (no negative values, unique inputs, etc.).


Stateful Validation: Requires accessing the blockchain state to check:
Whether the inputs refer to valid and unspent boxes.
Whether the spending proofs are correct.
Whether the transaction adheres to rules related to assets, fees, and block size limits.
Whether the scripts in the inputs are satisfied (using the ErgoInterpreter - see ErgoTree Evaluation).

### Key Concepts#
Boxes: The fundamental building blocks of Ergo's UTXO model. They are containers that hold ERG, other tokens, and scripts (smart contracts).
Scripts: Programs written in ErgoScript (a powerful scripting language) that define the conditions for spending boxes.
Spending Proofs: Cryptographic proofs that demonstrate the spender has the right to use the funds in a box, often involving signatures or more complex cryptographic protocols.
Context Extension: A key-value map attached to a spending proof, providing additional data that can be used by scripts during validation. See Blockchain Context.
