# Block - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/data-model/block/](https://docs.ergoplatform.com/dev/data-model/block/)
Generated: 2025-05-11

## Summary
(Back to: Data Model Overview) In blockchain technology, a block is a fundamental unit of data that groups together a set of transactions. These blocks are linked together chronologically to form a "blockchain," serving as a secure and transparent record of all transactions. Proof-of-Work (PoW) is a consensus mechanism that requires miners to solve complex mathematical problems to add new blocks to the blockchain. This process, known as "mining," involves significant computational effort, ensuring the security and immutability of the blockchain.

## Keywords
data, model, overview, technology, block, unit, datum, transaction, blockchain, record, work, consensus, mechanism, miner, problem, process, mining, effort, security, immutability

## Content
## Understanding Blocks in Ergo#
(Back to: Data Model Overview)
In blockchain technology, a block is a fundamental unit of data that groups together a set of transactions. These blocks are linked together chronologically to form a "blockchain," serving as a secure and transparent record of all transactions.
Proof-of-Work (PoW) is a consensus mechanism that requires miners to solve complex mathematical problems to add new blocks to the blockchain. This process, known as "mining," involves significant computational effort, ensuring the security and immutability of the blockchain.
Ergo, like other Proof-of-Work (PoW) blockchains such as Bitcoin, uses blocks to record transactions and ensure the integrity of the network. However, Ergo's block structure is more sophisticated, offering enhanced functionality and efficiency.
In Ergo, a new block is created approximately every two minutes. Initially, each block rewarded miners with 75 ERG, which were distributed among them and the Ergo Foundation Treasury. This emission schedule applied for the first two years of the network's operation. You can find more details in the emission section.

### Ergo Block Structure#
Ergo's blocks are divided into distinct sections to optimize organization and functionality:
Header: The header acts as a summary of the block's content. It includes metadata (block version, timestamp, etc.), hashes linking to other block sections, and the Proof-of-Work solution.


Block Transactions: This section contains the core data of the block â a list of all transactions included within it. These transactions define how tokens and assets are transferred on the Ergo blockchain.


ADProofs: These cryptographic proofs, short for Authenticated Data Proofs, allow light clients (nodes with limited storage) to verify transactions without downloading the entire block or the full UTXO set.


Extension: This section provides a flexible space to store additional data that doesn't fit into the other sections. It includes interlinks for NiPoPoWs (efficient proof-of-work verification) and system parameters (e.g., block size).
This structured approach enhances efficiency and allows for greater flexibility in incorporating new features and upgrades into the Ergo blockchain.

### Related Concepts#
Ergo Modifiers: In Ergo's peer-to-peer network protocol, blocks and transactions are referred to as "modifiers." These modifiers are exchanged between nodes to keep the network synchronized. More details
Superblock Clients: Ergo supports "superblock clients," which provide an additional layer of efficiency and flexibility for specific use cases, related to logarithmic space mining. More details.
