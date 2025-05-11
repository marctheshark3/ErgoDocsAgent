# Composing Transactions - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/protocol/tx/composing/](https://docs.ergoplatform.com/dev/protocol/tx/composing/)
Generated: 2025-05-11

## Summary
Each Ergo transaction represents an atomic state transition operation. This operation destroys an existing box from the state and generates new ones. Every transaction executed on Ergo comprises three main components: Data inputs are a unique feature introduced by Ergo and later adopted by Cardano with the Vasil Hardfork. This concept allows multiple transactions to share a data-input box, storing only a single reference to the box in the block. In traditional UTXO-based blockchains, transactions typically require spending and destroying all inputs.

## Keywords
ergo, transaction, state, transition, operation, component, datum, input, feature, cardano, vasil, hardfork, concept, data, reference, block, utxo, blockchain, spending, innovation

## Content
## Composing Transactions#
Each Ergo transaction represents an atomic state transition operation. This operation destroys an existing box from the state and generates new ones.

### Anatomy of a Transaction#
Every transaction executed on Ergo comprises three main components:
One or more Input boxes: These are the sources of your funds for the transaction. These boxes, which must already exist, will be destroyed by the transaction. The guard script in each box is evaluated and must return true for the transaction to be deemed valid.
One or more Output boxes: These are the destinations of your funds. These boxes will be created by the transaction.
Zero or more Data-Input boxes: These are supplementary boxes whose data can be referenced and utilized by the smart contracts of the inputs. The guard script in these boxes is not evaluated.

#### Data Inputs#
Data inputs are a unique feature introduced by Ergo and later adopted by Cardano with the Vasil Hardfork. This concept allows multiple transactions to share a data-input box, storing only a single reference to the box in the block.
In traditional UTXO-based blockchains, transactions typically require spending and destroying all inputs. However, Ergo introduces the concept of data inputs to allow transactions to reference existing UTXOs and read their data without consuming them. This innovation solves the limitations normally associated with eUTXO.
Data inputs enable multiple transactions within a block or slot to read the data from the same UTXO concurrently, as none of them actually spend or destroy the data. This parallel processing of data inputs reduces transaction fees, as smart contract execution is not required, and there is no need to create extra outputs. Additionally, data inputs address various other challenges, making them a valuable design choice for all UTXO-based blockchains.

### Overview#
If the transaction is spending boxes protected by a non-trivial script, its inputs should also contain proof of spending correctness - context extension (user-defined key-value map) and data inputs (links to existing boxes in the state) that can be used during script reduction to crypto, signatures that satisfy the remaining cryptographic protection of the script.
Transactions are not encrypted, which means that transactions included in blocks can be viewed publicly.

### Tools for Composing Transactions#
Transaction builder: This application enables you to manipulate Ergo JSON transactions with a UI and to sign them with a wallet or to prepare the JSON for the Swagger API. It can also load the JSON of an unsigned transaction for editing. GitHub | Video
Refer to this basic tutorial for sending a transaction for an introduction.
Ergo also supports 'Chained transactions' (spending outputs of off-chain transactions).
