# eUTxO - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/protocol/eutxo/](https://docs.ergoplatform.com/dev/protocol/eutxo/)
Generated: 2025-05-11

## Summary
Ergo utilizes the Extended UTXO (eUTXO) model, based on Bitcoin's original UTXO model but with enhanced capabilities that enable more expressive smart contracts. This section explores the advantages and features of eUTXO. The choice to build upon the UTXO model brings several significant advantages to Ergo: By leveraging the advantages of UTXO and extending its capabilities with eUTXO, Ergo provides a powerful and efficient platform for building and executing smart contracts. In the eUTXO model, Ergo allows smart contracts to utilize UTXOs as data inputs without modifying them.

## Keywords
ergo, extended, utxo, model, bitcoin, capability, contract, section, advantage, feature, eutxo, choice, platform, datum, node, transaction, balance, comparison, ethereum, account

## Content
## Extending the Power of the UTXO Model#
Ergo utilizes the Extended UTXO (eUTXO) model, based on Bitcoin's original UTXO model but with enhanced capabilities that enable more expressive smart contracts. This section explores the advantages and features of eUTXO.

### The Benefits of UTXO#
The choice to build upon the UTXO model brings several significant advantages to Ergo:
Privacy: UTXOs being one-time objects allow for formalized privacy measures, enhancing user confidentiality.
Scalability: UTXO's inherent design supports parallel transaction processing, making it simpler to scale the network. Additionally, UTXOs are more compatible with stateless client solutions like NIPoPoWs.
Interoperability: UTXOs are well-suited for off-chain and sidechain protocols, enabling seamless integration with various solutions beyond the main chain.
Transaction Cost Predictability: In Ergo, the on-chain action is primarily focused on validating smart contracts, resulting in significantly lower transaction costs. Moreover, the transaction costs are predictable, eliminating the need for gas-like mechanisms found in other platforms.
By leveraging the advantages of UTXO and extending its capabilities with eUTXO, Ergo provides a powerful and efficient platform for building and executing smart contracts.

### eUTXO and Smart Contracts#
In the eUTXO model, Ergo allows smart contracts to utilize UTXOs as data inputs without modifying them. This means that nodes primarily verify transactions rather than balances. In comparison, Ethereum's Account model requires nodes to check all accounts to validate the system.
By leveraging eUTXO, Ergo enables parallel computation and facilitates non-custodial atomic swaps. This makes it easier to perform complex operations securely and efficiently.
Furthermore, Ergo's Multi-Stage UTXO model, as detailed in this peer-reviewed paper, enables the implementation of Turing-complete smart contracts. (Note: ErgoScript itself is not Turing-complete by design for security, but the model allows for Turing-complete computations via multi-stage protocols).
You can see a comparison between Ergo's eUTXO model and the Account-Based model here.

#### Articles#
Learning Ergo 101 : eUTXO explained for human beings 
Off-chain logic & eUTXO
The UTXO Alliance Announcement

#### Documentation#
The Extended UTXO Model - IOHK Research
Understanding the Extended UTXO model - docs.cardano

#### Video#
Ergo Blockchain Crash Course Part 1: eUTXO Model Review
DeCo EU Layman Class - Basics of eUTxO
Interesting explanation on the eUTXO model and dapps built in it
Blockchain Basics & Transactions, UTXO and Script Code
