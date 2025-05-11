# Data Inputs - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/protocol/tx/read-only-inputs/](https://docs.ergoplatform.com/dev/protocol/tx/read-only-inputs/)
Generated: 2025-05-11

## Summary
ErgoScript's data inputs are a novel feature that enhances the traditional UTXO-based blockchain's functionality. This section delves into the concept of data inputs, their advantages, and their application within Ergo transactions. Traditional UTXO-based blockchains involve the consumption and subsequent destruction of inputs during transactions. Ergo innovates on this model with data inputs, which permit transactions to reference and read from existing UTXOs without the need to consume them. This breakthrough overcomes several limitations of the classic UTXO model, adding a layer of flexibility and efficiency to Ergo's extended UTXO (eUTXO) model.

## Keywords
ergoscript, data, input, feature, utxo, blockchain, functionality, section, concept, datum, advantage, application, ergo, transaction, consumption, destruction, model, reference, need, breakthrough

## Content
## Data Inputs in ErgoScript#
ErgoScript's data inputs are a novel feature that enhances the traditional UTXO-based blockchain's functionality. This section delves into the concept of data inputs, their advantages, and their application within Ergo transactions.

### Understanding Data Inputs#
Traditional UTXO-based blockchains involve the consumption and subsequent destruction of inputs during transactions. Ergo innovates on this model with data inputs, which permit transactions to reference and read from existing UTXOs without the need to consume them. This breakthrough overcomes several limitations of the classic UTXO model, adding a layer of flexibility and efficiency to Ergo's extended UTXO (eUTXO) model.

#### Key Features of Data Inputs#
Non-Destructive Access: Data inputs grant transactions the ability to tap into UTXO contents without the need to spend or consume them, preserving the UTXOs for future transactions.
Concurrent Data Access: Data inputs allow for the simultaneous referencing and reading of a UTXO's data by multiple transactions within a single block, without any of them spending the UTXO. This feature facilitates parallel processing and alleviates transaction execution bottlenecks.

### Benefits of Data Inputs#
The integration of data inputs into ErgoScript offers several notable benefits:
Reduced Transaction Fees: Since data inputs do not necessitate script execution or the generation of new outputs, they contribute to lower transaction fees, making them an economical choice for intricate transactions.


Enhanced DeFi Applications: Data inputs prove invaluable for decentralized finance (DeFi) applications, such as decentralized exchanges (DEXs) or order-book systems. They enable contracts to reference external data, like oracle data or order book states, without the need to consume the data boxes, facilitating concurrent interactions with the same state by multiple parties.


Improved Scalability and Efficiency: Data inputs contribute to network scalability and efficiency by allowing several transactions to concurrently read from the same data input, reducing the necessity for extra outputs and lessening the likelihood of transaction conflicts.

### Working with Data Inputs#
Ergo's data inputs are a distinctive feature not found in other eUTXO-based systems. When employing data inputs in ErgoScript, it's crucial to grasp their operation and how to leverage them effectively in smart contracts.

#### Usage in Transactions#
In ErgoScript, data inputs are "read-only" boxes that supply vital information for contract validation without being spent in the transaction. For instance, a DeFi contract might utilize a data input to verify an asset's current price from an oracle box, ensuring the transaction complies with specific conditions without modifying the oracle box.

#### Example Use Case#
Imagine a transaction that references a box with the ID d2b9b6536287b242f436436ce5a1e4a117d7b4843a13ce3abe3168bff99924a1 as both an input and a data input. This illustrates the versatility of data inputs, enabling a transaction to read and potentially update a box's state in one operation, assuming the box pre-existed the transaction.
In ErgoScript, you can refer to other boxes in the transaction using constructs like:
INPUTS(0).value > 10000 && OUTPUTS(1).value > 20000
This script enforces conditions based on the values of the first input and the second output boxes, showcasing how data inputs can be used to influence the logic of a transaction without consuming the referenced boxes.

#### Comparison with Traditional Models#
Data inputs in ErgoScript provide a significant advancement over traditional UTXO models, particularly in how they facilitate more complex and interactive smart contracts. For a more detailed comparison between eUTXO and account-based models, refer to the Off Chain Logic & eUTXO article.

### Best Practices and Considerations#
Selective Use: Only include data inputs that are necessary for your contract logic to minimize transaction size and fees.
Reliable Sources: Ensure that the data accessed through data inputs is reliable and comes from trusted sources, especially when using oracles or external data providers.
Validation Checks: Always validate the data within data inputs to ensure it is in the expected format and state, reducing the risk of transaction failures.

### Additional Resources#
For further reading and deeper understanding of the UTXO model and its implementation in Ergo, consider the following resources:
Unlocking The Potential Of The UTXO Model
Building A Portable And Reusable (PaR) UTXO dApp Standard
Data Inputs Semantics
Model Transaction Example

#### Conclusion#
Data inputs are a powerful feature in ErgoScript that significantly enhance the flexibility, efficiency, and scalability of smart contracts. By allowing read-only access to UTXOs, data inputs enable more sophisticated interactions within the Ergo blockchain, making them an essential tool for developers building complex dApps and DeFi solutions.
