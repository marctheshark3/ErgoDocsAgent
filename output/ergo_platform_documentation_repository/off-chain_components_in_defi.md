# Off-Chain Components in DeFi
Source: docs/archive/off-chain.md
Generated: 2025-05-11

## Summary
---
tags:
  - Off-Chain Bots
  - Off-Chain Components
  - Automation Bots
---

# Off-Chain Components in DeFi

Within the dynamic realm of Ergo's decentralized finance (DeFi), off-chain components are essential for augmenting the capabilities of on-chain processes. This guide explores the implementation of off-chain elements like watchers, oracles, and bots, which are pivotal for reinforcing the robustness of the ecosystem and opening up opportunities for passive income generation. ## On-chain vs. Off-chain

On-chain elements pertain to the aspects of a decentralized application (dApp) that are directly integrated into the blockchain. These include smart contracts associated with boxes and the data within the registers of those boxes. The typical development flow of a dApp begins with the creation of transactions, followed by crafting smart contracts to facilitate the dApp's decentralized functionality on the blockchain.

## Keywords
chain, bots, components, automation, defi, realm, ergo, finance, component, capability, process, guide, implementation, element, watcher, oracle, robustness, ecosystem, opening, opportunity

## Content
## Off-Chain Components in DeFi
Within the dynamic realm of Ergo's decentralized finance (DeFi), off-chain components are essential for augmenting the capabilities of on-chain processes. This guide explores the implementation of off-chain elements like watchers, oracles, and bots, which are pivotal for reinforcing the robustness of the ecosystem and opening up opportunities for passive income generation.

### On-chain vs. Off-chain
On-chain elements pertain to the aspects of a decentralized application (dApp) that are directly integrated into the blockchain. These include smart contracts associated with boxes and the data within the registers of those boxes. The typical development flow of a dApp begins with the creation of transactions, followed by crafting smart contracts to facilitate the dApp's decentralized functionality on the blockchain.
In contrast, off-chain elements refer to the components of a dApp that operate outside the blockchain. Systems are needed to process Unspent Transaction Outputs (UTxOs) and advance them through the stages of a dApp's lifecycle. Off-chain systems often encompass REST endpoints and bots that execute several vital tasks, such as:
Retrieving data from the blockchain
Composing transactions for user signatures
Processing transactions poised for the next phase in the dApp's workflow

#### Case Study: Transaction Bot
A transaction bot exemplifies an off-chain system designed to streamline the composition and processing of transactions. The Exle Tx Bot is an exemplary model of such a system. Detailed information about the Exle Tx Bot and its architecture can be found in their documentation: Exle Tx Bot.
A thorough grasp of the distinctions between on-chain and off-chain components, along with their respective roles, empowers developers to create more sophisticated and efficient dApps within the Ergo Blockchain ecosystem.

### ErgoDex Off-Chain Services
For a comprehensive understanding of the off-chain services that support the functionality of ErgoDex, refer to the detailed documentation provided in ErgoDEX off-chain services.

### Watchers on Rosen Bridge
Watchers, functioning as cross-chain oracles, are vital to the Rosen Bridge's operations. They diligently monitor and relay deposit events from their respective networks to Ergo, bolstering the network's security and reach.

#### How to Become a Watcher:
Technical Setup: To operate a watcher node, ensure a stable internet connection and a system that aligns with the technical requirements outlined in Ergo's documentation.
Provide Collateral: A collateral of 800 ERG and 30,000 RSN is mandated for each instance, with the flexibility of redemption and adjustment.
Monitor Transactions: Vigilant monitoring of cross-chain transactions is imperative for watchers to validate them in adherence to the protocol's guidelines.
Earn Rewards: Watchers are remunerated in ERG for their pivotal role, with the distribution reflecting their contribution to network security and functionality.

#### Estimated Rewards
The reward distribution for a watcher on the Rosen network from January 22, 2024, to February 3, 2024, is exemplified below. Note that rewards are contingent on bridge traffic and may fluctuate.
ERG Watcher Rewards:  100.217 ERG
ADA Watcher Rewards:  25.37 ADA
Total Rewards (ERG + ADA):  125.59
These figures are indicative and subject to variation based on actual bridge usage. Increased traffic correlates with higher potential rewards for watchers.

### Oracles: Empowering Ergo's dApps
Oracles are the linchpin in DeFi, supplying smart contracts with indispensable external data, such as price feeds. Ergo's ecosystem leverages oracles for an array of applications, including stablecoins and sophisticated financial instruments.
To participate in the Gold oracle pool, acquire a Gold Pool Oracle Token through auctions, ensuring a transparent entry process for aspirants.
{.is-warning}

##### Becoming an Oracle Provider:
Data Source Integration: Oracle providers must integrate dependable data sources with the Ergo blockchain to deliver precise and current information.
Deploy Oracle Contracts: Implement smart contracts on Ergo to act as conduits for your data streams.
Maintain Reliability: Consistent monitoring and upkeep are essential to sustain the credibility and reliability of your oracle service.
Compensation: Oracle providers typically receive compensation from the users or contracts utilizing their data, often via transaction fees or subscription models. Operating a Gold oracle yields an estimated 24 GORT (Gold Oracle Reward Tokens) daily.

### Bots for Automated Trading and Order Matching
The Ergo blockchain embraces the potent concept of decentralized grid trading, enabling automated trading orders while retaining user control over funds. Prominent examples include the Off the Grid and Machina Finance projects.
Discover more about grid trading on Investopedia.

#### Off the Grid
Off the Grid, a dApp, capitalizes on the grid trading contract proposed by kushti. It incorporates an execution bot/batcher to facilitate automated order matching.
Explore the project here
Key features of Off the Grid:
A contract that authorizes spending solely for correctly filled orders or with the order owner's consent, capable of managing multiple orders concurrently.
Off-chain bots/batchers that scrutinize grid orders and pair them with other liquidity sources, such as Spectrum AMMs, with potential extensions to other sources like the SigUSD bank.
Support for ERG trading against any token, accruing profits in ERG.
Grid orders benefit from the repeated execution of identical orders, while bot operators gain from arbitraging price discrepancies between liquidity sources and grid orders.
The concept was introduced by @kushti on ergoforum.
"Decentralized grid trading on Ergo is inherently compatible with existing DEXes, such as Spectrum LP pools and babel fees. It's an effective strategy to capitalize on market volatility, akin to offerings on many centralized exchanges (CEXes)."
View the inaugural decentralized grid order transaction on Ergo.

#### Machina Finance
Machina Finance is an Ergo-based initiative exploring grid trading and developing a DEX that harnesses grid order contracts.
Explore the project here

#### Other bots
HummingBot: Deploying and Backtesting Strategies via Dashboard
KuPyBot: A Python-based bot for Kucoin's platform, designed to execute a simple buy low, sell high strategy.

### Best Practices for Off-Chain Earnings
Stay Informed: Remain abreast of the latest Ergo ecosystem developments, including protocol updates and emerging off-chain earning opportunities.
Security: Prioritize the security of your setup, particularly when managing private keys or substantial ERG quantities.
Community Engagement: Engage with Ergo's community forums and channels to share insights and collaborate, thereby enhancing your strategies and influence.
Compliance: Adhere to all relevant legal and regulatory requirements associated with your financial data or asset-related activities.

### Conclusion
Ergo's ecosystem presents a plethora of off-chain earning prospects through roles such as watchers, oracles, and automated bots. These roles not only offer passive income streams but also significantly contribute to the Ergo blockchain's functionality and security. By participating in these opportunities, users can bolster the decentralized ecosystem and reap the benefits of its progression and success.
