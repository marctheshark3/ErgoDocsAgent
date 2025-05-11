# Ergo Development Roadmap & History
Source: docs/roadmap.md
Generated: 2025-05-11

## Summary
---
tags:
  - Roadmap
---

# Ergo Development Roadmap & History

Ergo is a blockchain platform designed to provide a secure, efficient, and user-friendly environment for the development of decentralized applications and financial tools. This roadmap outlines the key milestones and objectives for the development and growth of the Ergo ecosystem. ## Resources

//// details | Vision & Key Features
    {type: info, open: false}

Ergo is a cutting-edge smart contract platform that provides secure, accessible, and decentralized financial tools to empower ordinary people. Utilizing a sophisticated scripting language and advanced cryptographic features, Ergo builds on fundamental blockchain principles to transform the concept of Contractual Money. Ergo aims to establish itself as a mineable digital asset akin to "Digital Gold 2.0," supporting trustless derivatives and dynamic contracts.

## Keywords
roadmap, ergo, development, history, platform, user, environment, application, tool, milestone, objective, growth, ecosystem, resource, ////, detail, vision, features, type, info

## Content
## Ergo Development Roadmap & History
Ergo is a blockchain platform designed to provide a secure, efficient, and user-friendly environment for the development of decentralized applications and financial tools. This roadmap outlines the key milestones and objectives for the development and growth of the Ergo ecosystem.

### Resources
//// details | Vision & Key Features
    {type: info, open: false}
Ergo is a cutting-edge smart contract platform that provides secure, accessible, and decentralized financial tools to empower ordinary people. Utilizing a sophisticated scripting language and advanced cryptographic features, Ergo builds on fundamental blockchain principles to transform the concept of Contractual Money.
Ergo aims to establish itself as a mineable digital asset akin to "Digital Gold 2.0," supporting trustless derivatives and dynamic contracts. The development of Ergo’s DeFi ecosystem and the integration of sidechains will broaden the decentralized monetary base and derivative money supply, enhancing financial inclusivity and accessibility worldwide.
Ergo’s commitment to decentralization, fairness, and accessibility is evident in its adoption of the Autolykos Proof-of-Work protocol, which facilitates a user-friendly environment where lightweight clients can interact directly with the blockchain, making Ergo a practical and programmable currency ready for use.
[x] eUTXO Model: Allows UTXOs to carry arbitrary data and complex scripts, enabling advanced smart contracts
[x] Autolykos PoW Algorithm: ASIC-resistant and designed for fair mining, promoting decentralization
[x] Emission Schedule: Ensures a stable and predictable supply of ERG tokens
[x] NiPoPoWs (Non-Interactive Proofs of Proof-of-Work): Enables efficient light clients, log-space mining, trustless sidechains, and enhances accessibility and decentralization by allowing mobile SPV clients and lite full nodes
[x] ErgoScript: Supports clear and concise smart contract development with Σ-protocols
[x] Storage Rent: Mitigates blockchain bloat, incentivizes efficient storage usage, and contributes to long-term economic sustainability
[x] Turing-Complete Smart Contracts: Allows for complex on-chain computations and advanced dApp development
[x] Long-Term Economic Sustainability: Ensured through storage rent, transaction fees from DeFi, a...

### Ergo Timeline
/// details | 2019: Genesis Year
    {open: false}
Milestones:
July 1: Ergo mainnet launched during the "crypto winter"
Autumn: Ergo Foundation established


Development:
First tools and libraries emerged
Inaugural crowdfunding using UTXOs and smart contracts
Zero-join paper published
Multi-stage contracts paper by Amitabh released
First smart contract formally verified
///
/// details | 2020: Foundation Building
    {open: false}
Milestones:
January 7: Introduction of the Ergo Foundation as a community-driven entity


Launches:
Ergo Mixer (initially a raw application, later improved by Anon2020)
Late August: Oracle pools
Zero-knowledge treasury by anon_real
Auction House


Partnerships: Collaboration with Emurgo for joint research (Oracle Pools, SigmaUSD, headless dApp framework)
Listings: CoinEx, Gate.io
Community: Roadmap released and Discord community initiated
///
/// details | 2021: Expansion and Recognition
    {open: false}
Launches:
Q1: SigmaUSD launched


Ecosystem Growth:
Spectrum DEX and DeFi ecosystem development began
Autolykos v2 hard fork: opened Ergo to mining pools, improved liquidity and brought many new users into the ecosystem


Partnerships and Listings:
Collaboration with Jinse, Chinese community expanded to 10,000+ members
Listed on KuCoin and Changelly


Community Milestones:
UTXO Alliance formed
Inaugural Ergo Summit and two hackathons


Governance and Legal:
EIP-27 discussions initiated
US Legal Opinion obtained on Ergo's security classification
December 19: Ergo Foundation incorporated in Singapore


Team Expansion:
Joseph Armeanio and Mark Glasgow join Ergo Foundation (Mark replacing Martin S.)
November 1: Daniel Friedman (IOHK) appointed Advisor to Ergo Foundation Board


Additional Achievements:
The EF hired wallet developers to alleviate users' lack of usable wallet options
///
/// details | 2022: Technical Advancements
    {open: false}
Protocol Upgrades:
EIP-27 (emission soft-fork) was implemented
EIP-37 (difficulty retargeting hard...

##### Milestones
[x] ErgoHack VIII - Ergo as a Smart Layer
[x] DAO for Ergo core
[x] Ergo achieved #1 in TVL% of market cap for a PoW chain
[x] Ergo listed on MEXC exchange
[x] Ergo Node improvements:
Successful migration from LevelDB to RocksDB
6.0.0-alpha1 release with Global.some/none methods and AVL+ Tree optimizations


[x] Sigma protocol updates:
Sigma 5.0.14 release
Sigma 6.0.0 update with scrypto 3.0.0


[x] Infrastructure improvements:
Sigmaspace blockchain indexer completion (full index <24 hours)
Resolved indexer issues (rollbacks, duplicates, threading)
Sigmaspace explorer API compatibility with ergoplatform.org
Sigmaspace storage rent dashboard launch

##### Sigmanauts Achievements
[x] Sigmanauts Mining Pool launch
[x] Storage rent integration completed for Sigmanauts Mining Pool
[x] First proposal on Paideia passes (January 2024)
[x] Official takeover of Market-Making services management (March 2024)
[x] Substantial EF grant received matching Sigmanauts-raised funds (March 2024)

##### Application Achievements
Wallet Developments
[x] Nautilus Wallet improvements:

Version 0.15.0 release
Abyss v0.13.0-beta.1 with performance improvements
New frontend implementation
Improved Firefox compatibility
Enhanced asset ranking and sorting in Assets and Send tabs
Comprehensive dApp documentation



[x] Minotaur Wallet:

Version 2.0.1 production release



[x] Satergo Wallet:

3x faster transaction history loading
New Ergonnection library version
Simplified Windows installations
Infrastructure & Tools
[x] Sigmaspace development:

Complete blockchain indexer (<24 hours full index)
Storage rent dashboard launch with tracking features
Explorer API compatibility with ergoplatform.org



[x] Lithos progress:

Initial client development completion
Fraud proofs contracts for NISPs (PoW verification, header validation)



[x] Rosen Bridge improvements:

Enhanced decimal handling logic for cross-chain transactions
API and UI revisions
DeFi Applications
[x] SigmaUSD improvements:

Enhanced stability mechanisms
Oracle upgrade exploration



[x] Fleet SDK advancements:

AgeUSD integration completion
Enhanced development toolkit



[x] Celaut platform development

[x] Bene fundraising platform updates

##### Development Focus
Reference Client
[ ] Sub-blocks implementation:

Data types and update procedures
Candidate generation
Block template regeneration integration



[ ] P2P layer optimization and review

[ ] Bootstrapping improvements
[ ] Sidechain implementation modularization
[x] RocksDB integration and optimization
[ ] Enhanced testing for indices, scans, and wallet
Sigma
[ ] Sigma 6.0 implementation and validation context extension research


[x] Progress on Sigma 6.0 features:

SOption[] serialization
Header serialization/deserialization
Header.checkPoW implementation
Global.powHit implementation
Enhanced collections and numeric methods
Improved error messages





[ ] Signature re-checking optimization

[ ] ErgoScript 2.0
[ ] EIP-0046: Atomic Chains
[ ] EIP-0047: Pooled Transaction Inputs
[ ] MerkleTrees
[ ] EIP-44: Arbitrary Data Signing Standard
[ ] Revisiting formal verification implementation
[ ] Bulletproofs
[ ] Exploration of Rust and JavaScript support in addition to ErgoScript
[ ] Consideration of high-level language support (e.g., Lisp)
[ ] Improvements to error-checking and debugging tools
[x] Enhanced stateless validation in Sigma-Rust
SDKs
[x] AppKit

[x] FleetSDK

[x] Integration with AgeUSD stablecoin
[x] sigma-rust
[ ] JIT costing implementation in Sigma-Rust
[ ] 6.0 features implementation in Sigma-Rust
[ ] Sigma-Rust-Mini development
[x] Sigma.js
Libraries & Tooling
[x] ergo-lib-go
[x] escript.online
[x] Blockly Playground Integration


[x] Token metadata standards discussion
[x] Lithos light-client integration progress
Mining Ecosystem
[ ] Lithos decentralized mining pool infrastructure expected launch by end of 2024
[ ] Plans for reintroduction of Fair Initial Mining Offerings (FIMOs)
Wallets
[x] Nautilus

[x] Manifest v3 rework



[ ] Ledger

[x] Available in developer mode



[x] Keystone Integration progress

[ ] EIP-12 / EIP-20
[ ] Metamask integration
[ ] Trustwallet Integration
[ ] Light SPV Clients using NiPoPoWs
Ecosystem Growth
[x] DeFi ecosystem expa...

### DeFi Ecosystem
Every new addition to our growing DeFi ecosystem contributes to the expansion of trustless collateral, the decentralized monetary base, and the supply of derivative assets.

#### Decentralized Exchanges
[x] ErgoDex (AMM + Yield Farming)
[x] ErgoAuctionHouse (peer-to-peer auctions)
[x] Trade House (orderbook-based P2P DEX)



[x] SkyHarbor (NFT Market)

[x] SkyHarbor Raffle for new UI
[x] single-tx-swap (trustless p2p swaps)
[x] TokenJay (p2p escrow)
[x] Crooks Finance (buying, trading, and staking meme cryptocurrency tokens)
[ ] PalmyraComDex (commodities DEX) (Alpha live!)
[ ] Crystal Pool (instant L1 order-based trading)
[ ] Machina Finance (grid DEX)
[x] Mew Finance

#### Stablecoins
[x] SigmaUSD stablecoin (Djed protocol)
[ ] SigmaUSD v2


[x] Gluon (gold stablecoin)
[ ] DexyGold (seigniorage stablecoin)

#### Lending and Borrowing
[x] SigmaFi (peer-to-peer loans via bonds)
[x] Duckpools (lending pools)
[x] optionPools (option markets)


[x] EXLE (uncollateralized lending)

#### Gaming and Metaverse
[x] BlitzTCG (trading card game)

[x] CyberVerse (metaverse gaming platform)

[x] Cyberverse Multiplayer

#### Derivatives and Synthetics
[x] SigmaO (trustless options)
[x] HodlCoin (trustless ERG derivative with non-declining price)
[x] AuctionCoin (emission via auctions)
[x] Hodlbox (long-term locking)
[ ] OptionCoin (decentralized options trading with token emission)
[ ] ChainCash (elastic p2p money creation based on assets and trust)

#### Crowdfunding
[x] ErgoRaffle (decentralized crowdfunding)
[ ] V2 features

#### Interoperability and Bridges
[x] Oracle Pools (federated transparent data providing)
[x] Rosen Bridge (two-layered federated bridge)
[x] ADA Bridge
[x] BTC Bridge
[ ] Runes Integration


[x] EVM Bridge
[ ] R&D for Monero
[ ] RosenFast Service
[ ] Bridge Expansion Kit
[ ] Bridge SDK
[ ] DOGE Bridge
[ ] BCH Bridge
[ ] Hummingbot Integration / Customisation



[ ] Sigma Chains - Revitalizing Proof of Work

[ ] Trustless Relays (Superseding BTC custody solutions with Ergo smart-contracts)
[ ] Implementing sidechains with trustless transfers and various consensus mechanisms (merged mined with ERG, other blockchains, or double merged mined)
[ ] Expanding Ergo's contractual layer to sidechains, incorporating features like Bulletproofs-based sigma protocols and elevating certain contracts to first-class citizens
[ ] Experimenting with scalability solutions like sharding on sidechains
[ ] Utilizing ERG and other tokens on Ergo and sidechains from launch, fostering a rich and diverse DeFi ecosystem
[ ] Launching existing applications on sidechains, contingent on modifications to the contractual layer

#### Privacy and Mixing
[x] ErgoMixer (non-interactive, non-custodial mixer)
[x] Stealth addresses


[ ] SigmaJoin
[ ] Privacy-Preserving Voting

#### DAOs and Governance
[x] Paideia (DAO toolkit)
[ ] Lithos (decentralized mining infrastructure)
[ ] The Field (peer-to-pool pledging protocol)

#### Tooling
[x] Lilium (NFT sale platform)
[x] Moria Finance (fund management)
[x] Trustless Relys
[x] Random Number Generator
[x] TabbyPOS (Point of Sale device)
[x] Crux Finance (Token charts, portfolio viewer and more)
[ ] ErgoNames (decentralized naming system)
[ ] Reputation System (Testnet Live)

##### Miner Tooling
[x] GuapSwap (miner token swapping)
[x] CYTI (Choose Your Token ID)

##### Other Infrastructure
ergexplorer
sigmaspace

### References
//// details | References
    {type: info, open: false}
/// details | Developing Digital Gold 2.0 and its Infrastructure 
    {type: tip, open: false}
The following is adapted from this post on the R&D DAO for Ergo Core thread.
Vision
The Ergo Core Dev DAO envisions Ergo as Digital Gold 2.0, a mineable digital commodity with trustless derivatives and expressive contracts. By building upon Ergo's robust DeFi ecosystem and introducing sidechains, we aim to expand the decentralized monetary base and derivative money supply, creating a more inclusive and accessible financial system for the Ergo community and beyond.
Completed Milestones
The Ergo platform, with the support of the Ergo Foundation and community developers, has already made significant strides in developing its infrastructure and DeFi ecosystem. This includes launching basic infrastructure such as wallets and explorers, as well as a wide range of DeFi tools and trustless derivatives, such as:
[x] SigmaUSD stablecoin (Djed protocol)
[x] Spectrum DEX (AMM-based)
[x] ErgoMixer (non-interactive, non-custodial mixer)
[x] ErgoAuctionHouse (peer-to-peer auctions)
[x] SigmaFi (peer-to-peer loans via bonds)
[x] Duckpools (lending pools)
[x] ErgoRaffle (decentralized crowdfunding)
[x] EXLE (uncollateralized lending)
[x] SigmaO (trustless options)
[x] HodlCoin (trustless ERG derivative with non-declining price)
[x] AuctionCoin (emission via auctions)
[x] Oracle Pools (federated transparent data providing)
[x] Rosen Bridge (two-layered federated bridge)
These tools collectively contribute to the creation of more trustless collateral through various means such as AuctionCoin, OptionCoin, and fair initial mining offerings. As a result, Ergo's decentralized monetary base and derivative money supply continue to grow. It's worth noting that the entire DeFi ecosystem on Ergo is built upon its unique ErgoTree/ErgoScript contractual layer, also known as Sigma, which provides a secure and flexible foundation for the development...
