# Rust - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/lang/rust/](https://docs.ergoplatform.com/dev/lang/rust/)
Generated: 2025-05-11

## Summary
On-chain contracts are developed in ErgoScript, a simple language designed for writing smart contracts on the Ergo blockchain. ErgoScript is a Turing-complete language that prioritizes security and is well-suited for the UTXO transactional model used by Ergo. For off-chain components, such as interacting with the blockchain, creating transactions, and building applications, developers can use Rust along with frameworks like sigma-rust. Rust provides a powerful and efficient language for building off-chain components, while sigma-rust provides a Rust port of the sigmastate-interpreter, allowing developers to interact with the Ergo blockchain from their Rust applications. Various language bindings for sigma-rust are available for other languages.

## Keywords
chain, contract, ergoscript, language, ergo, blockchain, security, utxo, model, component, transaction, building, application, developer, rust, framework, sigma, port, sigmastate, interpreter

## Content
## Rust#
On-chain contracts are developed in ErgoScript, a simple language designed for writing smart contracts on the Ergo blockchain. ErgoScript is a Turing-complete language that prioritizes security and is well-suited for the UTXO transactional model used by Ergo.
For off-chain components, such as interacting with the blockchain, creating transactions, and building applications, developers can use Rust along with frameworks like sigma-rust. Rust provides a powerful and efficient language for building off-chain components, while sigma-rust provides a Rust port of the sigmastate-interpreter, allowing developers to interact with the Ergo blockchain from their Rust applications. Various language bindings for sigma-rust are available for other languages.
One example of using Rust for off-chain components is the Oracle Pools project, a federated protocol for delivering external data to the Ergo blockchain. The on-chain contracts and descriptions are available in the Ergo Improvement Proposals (EIPs), while the off-chain part is implemented in Rust using the oracle-core repository.
Understanding the UTXO transactional model is crucial when developing off-chain components for Ergo, as it differs from the account-based model used by other blockchains. Developers with experience in parallel computing may find the UTXO model more natural to work with.

### Frameworks#
sigma-rustRust port of the sigmastate-interpreter
HDFHeadless dApp Framework
RustKit(WIP), A SDK for building applications on the Ergo blockchain

### Utilities#
ð Ergo Utilitiessimplify writing off-chain code in Rust.
ð ergo-monitoringDebug service printing out useful for developers and managers information about ergo blockchain state.
ð Rust AVL TreeRust port of AVL tree from scrypto package.
