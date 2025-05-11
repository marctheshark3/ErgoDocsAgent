# Rosen Bridge - ErgoDocs
Source: [https://docs.ergoplatform.com/eco/rosen/](https://docs.ergoplatform.com/eco/rosen/)
Generated: 2025-05-11

## Summary
Rosen Bridge, an open-source protocol, is pioneering the future of cross-chain asset transfers. It's currently in beta, testing its first bridge to Cardano. Rosen Bridge leverages Ergo's capabilities to facilitate secure and efficient coin and token transfers between Ergo and other blockchains. Rosen Bridge is expected to launch imminently, join the Rosen Telegram chat to keep up to date. Rosen Bridge is an open-source protocol, primarily focused on Ergo, that allows users to seamlessly transfer coins and tokens between Ergo and any other compatible blockchain.

## Keywords
rosen, bridge, source, protocol, future, asset, transfer, beta, cardano, ergo, capability, coin, blockchain, telegram, date, user, token, compatibility, chainx, support

## Content
## Rosen Bridge: The Future of Cross-Chain Asset Transfers#
Rosen Bridge, an open-source protocol, is pioneering the future of cross-chain asset transfers. It's currently in beta, testing its first bridge to Cardano. Rosen Bridge leverages Ergo's capabilities to facilitate secure and efficient coin and token transfers between Ergo and other blockchains.
Latest Developments
Rosen Bridge is expected to launch imminently, join the Rosen Telegram chat to keep up to date.

### Key Features#
Rosen Bridge is an open-source protocol, primarily focused on Ergo, that allows users to seamlessly transfer coins and tokens between Ergo and any other compatible blockchain. The compatibility of the other blockchain, referred to as chainX, is determined by its support for multi-signature transactions or threshold signatures.
One of the unique aspects of this bridge is that it eliminates the need for deploying and using smart contracts on the other chains. This is because consensus on any action is achieved on the Ergo platform by a group of entities known as Guards. These Guards generate a signed transaction (either for Ergo or chainX) which can then be broadcasted to the other chain by any party, including the Guards themselves.
Architecture: The architecture of the bridge comprises of Watchers and Guards. Watchers are responsible for monitoring blockchain activities and reporting them to Guards. The Guards process these events and execute actions, thereby ensuring a high level of security and functionality.
Smart Contract Reduction: The Ergo-centric logic of Rosen Bridge significantly reduces the need for smart contracts on the chains it bridges.
RSN Token: The Rosen Token (RSN) plays a crucial role in the operation of the bridge. It serves as a mechanism for sybil resistance, a system for fee distribution, and a means to access the services of the bridge. (See the Tokenomics section)
Scalability and User Safety: The design of Rosen Bridge allows for the addition of new chains through independent modules. It also prioritizes the success of user transactions by waiting for a sufficient number of confirmations.

### Rosen Bridge Operations and Features#
What is the bridge fee structure?
Initially, it's the greater of $10 or 0.5% of the transaction value, plus network fees, adjustable by the guard set. The fee is collected in the transferred token on Ergo. Network fees vary: static for Ergo and Cardano, dynamic for EVM-based networks.
Why is the fee so high?
Each event has to be reported on by 60%+1 of Watchers, and they need to be incentivised to do so. It also prevents all their permits being exhausted by low-value transactions.
Is there a maximum amount for a single transaction on Rosen Bridge?
No fixed maximum, but large transfers may take longer, from hours to 1-2 days, due to manual guard intervention for fund transfers from cold to hot wallets.
How is ADA managed within the system for transactions to Cardano?
Network fees in the transaction token on Ergo are sent to a dedicated address for covering network fees on different chains. Currently, the Rosen team manually manages this, with plans for future automation.
How can a project add new token options to the bridge?
Projects pay a listing fee to the Rosen Fund, with potential discounts for open-source projects. This involves minting wrapped tokens and updating the token map. Fees are distributed to watchers and guards.
What are the next chains to be added following ADA?
The roadmap includes BTC, BSC (EVM-chains), and Dogecoin in the midterm. Code refactoring aims to facilitate adding new chains, with initial chains being the most challenging.
What is the size and composition of the team?
The team includes 8 developers, with some frontend and UI tasks outsourced. Additionally, 2-3 developers have worked part-time over the past year, supported by several advisors.
For more information, please see the Team section.
