# ADProofs - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/data-model/block-adproofs/](https://docs.ergoplatform.com/dev/data-model/block-adproofs/)
Generated: 2025-05-11

## Summary
(Back to: Block Overview) ADProofs, short for Authenticated Data Proofs, are a crucial component of Ergo's block structure that allows for efficient and secure validation of transactions without requiring full blockchain download. They are particularly beneficial for "light clients" â wallets or nodes that don't store the entire blockchain. Function: Structure: The ADProofs class in ADProofs.scala defines the structure of ADProofs. It contains the following key elements: Verification Process: Key Concepts: Benefits:

## Keywords
block, overview, adproof, authenticated, data, proofs, component, ergo, structure, validation, transaction, download, client, wallet, node, blockchain, function, adproofs, class, adproofs.scala

## Content
## ADProofs (Authenticated Data Proofs)#
(Back to: Block Overview)
ADProofs, short for Authenticated Data Proofs, are a crucial component of Ergo's block structure that allows for efficient and secure validation of transactions without requiring full blockchain download. They are particularly beneficial for "light clients" â wallets or nodes that don't store the entire blockchain.
Function:
Efficient Transaction Validation: ADProofs enable light clients to verify the validity of transactions within a block by proving they are included in the Merkle tree of the UTXO set. This eliminates the need to download and process the entire UTXO set or the full block.
State Verification: Light clients can use ADProofs to calculate the new state root (a cryptographic summary of the UTXO set) after applying the transactions in a block. This allows them to stay synchronized with the blockchain without storing the complete state.
Security: ADProofs are cryptographically secure, ensuring that any tampering with the transactions or the UTXO set will be detected during validation.
Structure:
The ADProofs class in ADProofs.scala defines the structure of ADProofs. It contains the following key elements:
headerId: The ID of the block header to which these proofs correspond.
proofBytes: The serialized cryptographic proof that allows for verification of the state changes.
Verification Process:
Initialization: A light client receives the block header, the ADProofs, and the list of transactions.
Proof Application: The client uses the ADProofs to construct a BatchAVLVerifier. This verifier utilizes the provided proof to validate the changes made to the UTXO set by the transactions.
State Root Calculation: The verifier calculates the new state root after applying the transactions. This calculated root is then compared against the state root declared in the block header.
Verification Result: If the calculated state root matches the one in the header, the transactions and the state transition are considered valid.
Key Concepts:
Merkl...
