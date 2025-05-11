# Guards - ErgoDocs
Source: [https://docs.ergoplatform.com/eco/rosen/rosen-guard/](https://docs.ergoplatform.com/eco/rosen/rosen-guard/)
Generated: 2025-05-11

## Summary
Rosen is an Ergo-centric bridge fortified with multi-layered security protection. In the initial layer, Watchers monitor network activities and report valid bridge-related events to the subsequent layer, Guards. These Guards then carefully process the reported events and execute required actions. In brief, Guards are dedicated to security maintenance and executing responses, while Watchers are focused on the ongoing monitoring of activities and transparent reporting. Guards are a federated group of entities managing the Rosen core.

## Keywords
rosen, ergo, bridge, security, protection, layer, watchers, network, activity, event, guards, guard, action, brief, maintenance, response, watcher, monitoring, reporting, group

## Content
## Rosen Guards#
Rosen is an Ergo-centric bridge fortified with multi-layered security protection. In the initial layer, Watchers monitor network activities and report valid bridge-related events to the subsequent layer, Guards. These Guards then carefully process the reported events and execute required actions. In brief, Guards are dedicated to security maintenance and executing responses, while Watchers are focused on the ongoing monitoring of activities and transparent reporting.
Guards are a federated group of entities managing the Rosen core. Their authority over Rosen is restricted through multisignature contracts and wallets. Failure or collusion of Guards will be tolerated while the majority of Guards are healthy. Each Guard has a reasonable amount of funds locked as collateral and will lose all their funds at once in case of malicious behaviour.
Guards need to lock RSN as collateral. Funds will be emitted to the Guard Set and involved Watchers in case of any successful bridge transfers. However, funds will be slashed/collected in case of malicious behavior. When RSN emission has ended, all bridge fees will be collected in the RSN token. Holding RSN will have special fee benefits for projects.
Who can become a Guard?
Becoming a guard is effort-intensive and permission-based, starting with selected known entities and later admissions by the guard set. Guards buy and lock RSN tokens in a multisig wallet, with stakes lost for misconduct or inactivity.
Who are the current Guards?
The Guard Set can be seen on rosen.tech

### How are transactions submitted to the target blockchain.#
The Rosen Bridge Guard Service facilitates transaction submissions across different blockchains. Here's how transactions are submitted to the target blockchain within this service:
Event Processing:

Scanner & Extractor: The system includes a blockchain scanner and data extractor that monitor the Ergo blockchain and Rosen Bridge for relevant events. These components fetch new blocks, looking for specific transaction patterns or events that need to be acted upon.
Event Processor: Each event detected by the extractor is processed to verify its authenticity and relevance. This process includes checks against predefined rules and conditions specific to the blockchain operations being monitored.



Transaction Agreement and Execution:

TxAgreement: For actions that require consensus or agreement (like cross-chain movements involving significant value), the Guard Service utilizes a multi-guard consensus mechanism. Each guard node (participant in the Rosen Bridge Guard network) independently verifies the transaction details and signals agreement.
Transaction Processor: Once consensus is reached, the Transaction Processor crafts the necessary blockchain transaction. This component is responsible for creating a valid and secure transaction that represents the agreed-upon action (like transferring assets between chains).
MultiSig & TSS (Threshold Signature Scheme): The final transaction is signed using multi-signature and threshold signature schemes to ensure security and trustworthiness. These cryptographic schemes help in securing transactions by requiring multiple signatures or a subset of signatures from a larger set to authorize a transaction.



Blockchain Interaction:

BaseChain and Reward Services: These services handle the actual interaction with the blockchain. They generate and verify payment transactions, interacting directly with the blockchain to submit the signed transactions.
The services are designed to be flexible enough to support various blockchains (like ...
