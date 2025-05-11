# Oracles - ErgoDocs
Source: [https://docs.ergoplatform.com/uses/oracles/](https://docs.ergoplatform.com/uses/oracles/)
Generated: 2025-05-11

## Summary
Oracles form the critical infrastructure in a decentralized financial system, connecting off-chain data with on-chain transactions. They provide essential data feeds for various operations, from atomic swaps to more complex interactions like lending/borrowing and dynamic market-making. Yet, DeFi ecosystems are vulnerable to Flash Loan attacks due to centralized price oracle misinformation. Ergo has pioneered Oracle Pools to sustain a resilient DeFi ecosystem. Utilizing the Extended UTXO (eUTXO) model and the powerful ErgoScript programming language, Ergo facilitates highly decentralized oracle networks.

## Keywords
oracle, infrastructure, system, chain, datum, transaction, feed, operation, swap, interaction, lending, borrowing, market, making, defi, ecosystem, flash, loan, attack, price

## Content
## Oracles on Ergo#
Oracles form the critical infrastructure in a decentralized financial system, connecting off-chain data with on-chain transactions. They provide essential data feeds for various operations, from atomic swaps to more complex interactions like lending/borrowing and dynamic market-making. Yet, DeFi ecosystems are vulnerable to Flash Loan attacks due to centralized price oracle misinformation.

### Oracle Pools on Ergo#
Ergo has pioneered Oracle Pools to sustain a resilient DeFi ecosystem. Utilizing the Extended UTXO (eUTXO) model and the powerful ErgoScript programming language, Ergo facilitates highly decentralized oracle networks. Oracle Pools serve as an abstraction layer over the Oracle data, allowing scalable benefits while managing trade-offs between cost and speed. An example of this is the operational ERG/USD oracle pool on the Ergo Blockchain.
External oracle data, when posted on-chain, must be precisely encoded within a transaction. Oracle pools, which consist of various interconnected components, require specific transactions to transition through the pool protocol's different stages. Oracle Core handles these complex transactions, which include data posting and executing the on-chain oracle pool protocol (like data point averaging). It is packaged with the Oracle Pool Bootstrap and a Connector Library. You can refer to the ada-usd-oracle source for an illustration. For a comprehensive perspective, see this overview by Robert Kornacki.

#### Introduction to Oracle Pools V2#
The following section delves into the Oracle Pools V2, an innovative upgrade to the existing Oracle Pool v1.0, as documented in EIP16. This proposed update is designed to resolve various drawbacks associated with the first version such as the generation of extensive dust, low rewards, complexity due to two types of pool boxes, and issues related to the non-transferability of oracle and ballot tokens.
Oracle Pools V2 offers a range of new features and improvements including a single pool address, an epoch counter, a compact pool box, a refresh box, token-based rewards, no separate funding process, reward accumulation, and transferability of oracle and ballot tokens.
For detailed steps on how to bootstrap an ERG/XAU pool on testnet with this new version, follow the guide here.
To gain a deeper understanding of these changes and how they enhance the overall performance of Oracle Pools, refer to the comprehensive EIP-0023 Oracle pool 2.0. The document provides an exhaustive comparison between versions v1.0 and v2.0, highlighting the significant advancements in the latter.
For further details, refer to Oracles-V2.
For an easy docker setup see easy-ergo-oracle

#### Forum Posts#
Trustless Oracle Contracts
Shrimpcoin - The first shrimp-pinned stablecoin on Ergo (Inactive)

#### GitHub#
eth/usd connector
Ergo oracles | A command-line tool to launch oracles, with implementations for USD/ERG, EUR/ERG, BTC/ERG, AUG/ERG prices. Forum topic with example.

#### Articles#
Chainlink Oracles vs. Ergo Oracle Pools
Oracle Pools - A New Oracle Model
Interoperability with Cardano Oracles
Ergo Blockchain: Oracle Pool Governance Update
The Role of Ergo Oracles

#### The Delphi Project (Inactive)#
The Delphi Project aimed to facilitate exploration, operation, and launching of decentralized oracles on the Ergo blockchain.
Website
Final Report
