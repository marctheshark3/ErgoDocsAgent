# Whitepaper - ErgoDocs
Source: [https://docs.ergoplatform.com/doc/whitepaper/](https://docs.ergoplatform.com/doc/whitepaper/)
Generated: 2025-05-11

## Summary
Authors: Ergo Developers
Date: May 14, 2019
Version: v1.0 We present Ergo, a new flexible blockchain protocol. Ergo is designed for developing decentralized applications with the main focus of providing an efficient, secure and easy way to implement financial contracts. To achieve this goal, Ergo includes various technical and economic improvements to existing blockchain solutions. Every coin in Ergo is protected by a program in ErgoScript, which is a powerful and protocol-friendly scripting language based on \(\Sigma\)-protocols. Using ErgoScript, we can encode the conditions under which coins may be used: who can spend them, when, under what external conditions, to whom, and so on.

## Keywords
author, ergo, developers, date, version, v1.0, blockchain, protocol, application, focus, contract, goal, improvement, solution, coin, program, ergoscript, scripting, language, \(\sigma\)-protocol

## Content
## Ergo: A Resilient Platform For Contractual Money#
Authors: Ergo Developers
Date: May 14, 2019
Version: v1.0

### Abstract#
We present Ergo, a new flexible blockchain protocol.
Ergo is designed for developing decentralized applications with the main focus of providing an efficient, secure and easy way to implement financial contracts.
To achieve this goal, Ergo includes various technical and economic improvements to existing blockchain solutions. Every coin in Ergo is protected by a program in ErgoScript, which is a powerful and protocol-friendly scripting language based on \(\Sigma\)-protocols. Using ErgoScript, we can encode the conditions under which coins may be used: who can spend them, when, under what external conditions, to whom, and so on.
Extended support for light nodes makes Ergo friendly for end users because it allows running contracts on untrusted commodity hardware. To be usable in the long-term, Ergo follows a survivability approach -- it uses widely-researched solutions that don't result in security issues in the future, while also preventing performance degradation over time with a new economic model. Finally, Ergo has a self-amendable protocol that allows it to absorb new ideas and improve itself in the future.

### Introduction#
Beginning more than ten years ago with Bitcoin[@nakamoto2008bitcoin], blockchain technology has so far proved to be a secure way of maintaining a public transaction ledger and disintermediating trusted third parties such as traditional financial institutions to some degree. Even after achieving a market capitalization over $300bn in \(2017\)[@btcPrice], no severe attacks were performed on the Bitcoin network despite the high potential yield. This resilience of cryptocurrencies and the financial empowerment and self-sovereignty they promise to bring is achieved by a combination of modern cryptographic algorithms and decentralized architecture.
However, this resilience comes at a cost and has not yet been proven for existing systems in the long-run at economy-wide scale. To use a blockchain without any trust, its participants should check each other by downloading and processing all the transactions in the network, utilizing network resources. Besides network utilization, transaction processing also utilizes computational resources, especially if the transactional language is sufficiently flexible. Finally, blockchain participants have to keep a significant amount of data in their local storages and the storage requirements are growing fast. Of this, certain data must be maintained in memory. Thus, transaction processing utilizes various resources of hundreds of thousands of computers all over the world and consumption of these resources is paid for by regular users in the form of transaction fees[@chepurnoy2018systematic]. Despite the generous block reward subsidy in some existing systems, their fees can still be very high at times[@bitcoinFees]. Due to this, even after being around for more than ten years, blockchain technology is still primarily being used in financial applications, where the advantage of high security outweighs the disadvantage of high transaction costs.
Besides the vanilla currency example, the other use of blockchains is to build decentralized a...

### Ergo Vision#
The \(Ergo\) protocol is very flexible and may be changed in the future by the community. In this section, we define the main principles that should be followed in \(Ergo\) which might be referred to as "Ergo's Social Contract." In case of intentional violation of any of these principles, the resulting protocol should not be called \(Ergo\).
Decentralization First. \(Ergo\) should be as decentralized as possible: any parties (social leaders, software developers, hardware manufacturers, miners, funds and so on) whose absence or malicious behavior may affect the security of the network should be avoided. If any of these parties do appear during \(Ergo\)'s lifetime, the community should consider ways to decrease their impact level.
Created for Regular People. \(Ergo\) is a platform for ordinary people, and their interests should not be infringed upon in favor of big parties. In particular, this means that centralization of mining should be prevented and regular people should be able to participate in the protocol by running a full node and mining blocks (albeit with a small probability).
Platform for Contractual Money. \(Ergo\) is the base layer to applications that will be built on top of it. It is suitable for several applications but its main focus is to provide an efficient, secure and easy way to implement financial contracts.
Long-term Focus. All aspects of \(Ergo\) development should be focused on a long term perspective. At any point of time, \(Ergo\) should be able to survive for centuries without expected hard forks, software or hardware improvements or some other unpredictable changes. Since \(Ergo\) is designed as a platform, applications built on top of \(Ergo\) should also be able to survive in the long term. This resiliency and long term survivability may also enable \(Ergo\) to be a good store of value.
Permissionless and Open. \(Ergo\) protocol does not restrict or limit any categories of usage. It should allow anyone to join the network and participat...

### Autolykos Consensus Protocol#
The core component of any blockchain system is its consensus protocol and Ergo utilizes a self-developed unique Proof of Work (PoW) consensus protocol called Autolykos, which is described below. Despite extensive research on possible alternatives, the original PoW protocol with the longest chain rule is still in demand due to its simplicity, high-security guarantees, and friendliness to light clients. However, a decade of extensive testing has revealed several problems with the original one-CPU-one-vote idea.
The first known problem of a PoW system is the development of specialized hardware (ASICs), which allows a small group of ASIC-equipped miners to solve PoW puzzles orders of magnitude faster and more efficiently than everyone else. This problem can be solved with the help of memory-hard PoW schemes that reduce the disparity between ASICs and commodity hardware. The most promising approach here is to use asymmetric memory-hard PoW schemes that require significantly less memory to verify a solution than to find it[@biryukov2017equihash,ethHash].
The second known threat to a PoW network decentralization is that even big miners tend to unite in mining pools, leading to a situation when just a few pool operators (5 in Bitcoin, 2 in Ethereum at the time of writing) control more than 51% of computational power. Although the problem has already been discussed in the community, no practical solutions have been implemented before Ergo.
Ergo's PoW protocol, Autolykos[@Ergopow], is the first consensus protocol that is both memory-hard and pool-resistant. Autolykos is based on the one list \(k\)-sum problem: a miner has to find \(k=32\) elements from a pre-defined list \(R\) of size \(N=2^{26}\) (which has a size of 2 Gb), such that:
\[
\sum_{j \in J} r_{j} - sk = d \text{ in the interval } \{-b,\dots,0,\dots,b\mod q\}.
\]
Elements of list \(R\) are obtained as a result of one-way computation from index \(i\), two miner public keys \(pk, w\) and hash of block header \(m\) a...

#### Algorithm: Block Mining#
\[
\begin{aligned}
    &\textbf{Input:} \text{ upcoming block header hash } m, \text{ key pair } pk = g^{sk} \\
    &\text{Generate randomly a new key pair } w = g^x \\
    &r_{i \in [0,N)} = H(i||M||pk||m||w) \\
    &\textbf{While true:} \\
    &\quad \text{Let nonce } \gets \mathsf{rand} \\
    &\quad \text{Let } J \gets \text{genIndexes}(m||\text{nonce}) \\
    &\quad \text{Let } d = \sum_{j \in J} r_j \cdot x - sk \mod q \\
    &\quad \textbf{if } d < b: \\
    &\quad\quad \textbf{return } (m, pk, w, \text{nonce}, d)
\end{aligned}
\]
Note that although the mining process utilizes private keys, the solution itself only contains public keys. Solution verification is done by the following algorithm.

##### Algorithm: Solution Verification#
\[
\begin{aligned}
    &\textbf{Input: } m, pk, w, \text{nonce}, d \\
    &\text{require } d < b \\
    &\text{require } pk, w \in \mathbb{G} \text{ and } pk, w \neq e \\
    &\text{Let } J \gets \text{genIndexes}(m||\text{nonce}) \\
    &\text{Let } f = \sum_{j \in J} H(j||M||pk||m||w) \\
    &\text{require } w^f = g^d \cdot pk
\end{aligned}
\]
This approach prevents mining pool formation because the secret key \(sk\) is needed for mining: once any pool miner finds a correct solution, they can use this secret to steal the block reward. On the other hand, it is secure to reveal a single solution, as it only contains public keys and reveals a single linear relation between the two secrets \(sk, w\).
Memory-hardness follows from the fact that the block mining algorithm requires keeping the whole list \(R\) for the main loop execution. Every list element takes 32 bytes, so the whole list of \(N\) elements takes \(N \cdot 32 = 2 \text{ Gb}\) of memory for \(N = 2^{26}\). A miner can try to reduce memory requirements by calculating these elements "on the fly" without keeping them in memory; however, they will need to calculate the same hash \(H\) multiple times (about \(10^4\) times for modern GPUs), thereby reducing efficiency and profit.
Calculating the list \(R\) is also a computationally heavy task: our initial implementation[@ergoMiner] consumes ~25 seconds on Nvidia GTX 1070 to fill all the \(2^{26}\) elements of the list. This part, however, may be optimized if a miner also stores a list of unfinalized hashes \(u_{i \in [0,N)}=H(i||M||pk)\) in memory, consuming 5 more Gigabytes of it. In such a case, work to calculate unfinalized hashes should be done only once during mining initialization, while finalizing them and filling the list \(R\) for the new header only consumes a few milliseconds (~50 ms on Nvidia GTX 1070).
The target parameter \(b\) is built-in into the puzzle itself and is adjusted to the current network hash rate via a difficulty adjustment algorithm...

### Ergo State#
To check a new transaction, a cryptocurrency client does not use the ledger with all the transactions that happened before this one. Instead, it uses a ledger state snapshot from its history. In the Bitcoin Core reference implementation, this snapshot is the active one-time coins (i.e., UTXOs), and a transaction destroys some coins and also creates new ones. In Ethereum, this snapshot is of long-lived accounts and a transaction modifies monetary balance and internal storage of some accounts. Also, in Ethereum (unlike Bitcoin), the representation of the snapshot is fixed within the protocol because an authenticating digest of the snapshot is written into the block header.
Ergo follows Bitcoin's UTXO design and represents the snapshots using one-time coins. The difference from Bitcoin is that in addition to monetary value and protecting script, an Ergo one-time coin, called a box, also contains user-defined data. Similar to Ethereum, an Ergo block also stores an authenticating digest, called the stateRoot, of the global state after applying the block.
An Ergo box is made of registers (and nothing but registers). Such a box can have 10 registers labeled \(R_0, R_1, \ldots, R_9\), of which the first four are filled with mandatory values and the rest may contain arbitrary data or be empty.
\(R_0\) (monetary value): Amount of \(Erg\) locked in this box.
\(R_1\) (guard script): Serialized script protecting this box.
\(R_2\) (tokens): A box can carry multiple tokens. This register contains an array of \((\text{token\_identifier} \to \text{amount})\) pairs locked in this box.
\(R_3\) (transaction info): Contains (1) declared creation height (should be no more than the actual height of a block which contains the transaction), (2) a unique identifier of the transaction that created this box, and (3) the index of this box in that transaction's output boxes.
\(R_4 - R_9\) (additional data): Contains arbitrary user-defined data.
One-time immutable objects (as in Bitcoin's UTXO mo...

### Resiliency and Survivability#
Being a platform for contractual money, Ergo should also support long-term contracts for a period of at least an average person's lifetime. However, even young existing smart contract platforms are experiencing issues with performance degradation and adaptability to external conditions. This leads to a situation where the cryptocurrency depends on a small group of developers to provide a fixing hard fork, or the cryptocurrency won't survive. For example, the Ethereum network was started with a Proof-of-Work consensus algorithm with a plan to switch to Proof-of-Stake in the near future. However, delays in the Proof-of-Stake development have led to several fixing hard forks[@ethDifficultyBomb] and the community is still forced to rely on core developers promising to implement the next hard fork.
The first common survivability issue is that in pursuit of popularity, developers tend to implement ad-hoc solutions without proper preliminary research and testing. Such solutions inevitably lead to bugs, which then lead to hasty bug fixes, then to fixes of those bug fixes, and so on, making the network unreliable and even less secure. A notable example is the IOTA cryptocurrency, which implemented various scaling solutions, including its own hash function and DAG structure, that allowed it to achieve high popularity and market capitalization. However, a detailed analysis of these solutions revealed multiple serious problems, including practical attacks that enabled token theft[@heilmancryptanalysis, de2018break]. A subsequent hard fork[@IOTAReport] then fixed these problems by switching to the well-known SHA3 hash function, thereby confirming the uselessness of such kinds of innovations. Ergo's approach here is to use stable well-tested solutions, even if they lead to slower short-term innovations. Most of the solutions used in Ergo are formalized in papers presented at peer-reviewed conferences[@reyzin2017improving,meshkov2017short,chepurnoy2018systematic,chepurnoy2018self,...

### Ergo's Native Token#
Ergo platform has its native token, which is called \(Erg\) and is divisible to up to \(10^9\) smallest units, \(nanoErg\)s (a \(nanoErg\) is one billionth of an \(Erg\)). \(Erg\)s are important for Ergo platform stability and security for several reasons discussed below.
During the initial phase of Ergo's life, miners will receive the reward in \(Erg\)s according to a predefined and hard-coded token emission schedule (see Emission for more details). These coins will incentivize miners to participate in the Ergo network, securing it from hashrate-based attacks like the known 51% attack[@reorgAttack].
\(Erg\) emission will be finished within just eight years, and after that miners will only receive \(Erg\)s from fees. Although adjustable over time through miner on-chain voting, Ergo block size and maximum block computational cost at any given point in time will be limited, and thus miners are forced to choose only a subset of transactions from the mempool during times of high load. Fees will help miners to sort the transactions, preventing spam attacks while allowing miners to include transactions from honest users in blocks.
Besides network and computation resources, a transaction utilizes storage by increasing state size. In existing cryptocurrencies, an element of the state (a UTXO in UTXO-based blockchains, called a box in Ergo) once created lives possibly forever without any compensation to miners and some users who must keep this state in high-cost random-access memory. This leads to a misalignment of incentives and continuously increasing state size. In contrast, Ergo has a storage rent component that periodically charges users \(Erg\) for every byte included in the state. This storage rent makes the system more stable by limiting state size or ensuring proper compensation for larger state size, returning lost coins into circulation, and providing an additional stable and predictable reward to miners.
Thus, being a platform for contractual money, Ergo is suita...

#### Emission#
All \(Erg\) tokens that will ever circulate in the system are presented in the initial state, which consists of three boxes:
No Premine Proof. This box contains exactly one \(Erg\) and is protected by a script that prevents it from being spent by anyone. Thus, it is a long-lived box that will stay in the system until the storage-rent component destroys it. Its main purpose is to prove that \(Ergo\) mining was not started privately by anyone before the declared launch date. To achieve this, additional registers of this box contain the latest headlines from the media (The Guardian, Vedomosti, Xinhua), as well as the latest block identifiers from Bitcoin and Ethereum. Thus, \(Ergo\) mining could not have started before certain events in the real world and the cryptocurrency space.


Treasury. This box contains 4,330,791.5 \(Erg\)s that will be used to fund \(Ergo\) development. Its protecting script[@scriptTreasury] consists of two parts:


First, it ensures that only a predefined portion of the box value is unlocked. During blocks 1â525,599 (2 years) 7.5 \(Erg\)s will be released every block. Then during blocks 525,600â590,399 (3 months) 4.5 \(Erg\)s will be released every block. Finally, during blocks 590,400â655,199 (3 months) 1.5 \(Erg\)s will be released every block. This rule ensures the presence of funds for \(Ergo\) development for 2.5 years and, at any moment in time, rewards do not exceed 10% of the total number of coins in circulation.


Second, it has custom protection from unexpected spending. Initially, it requires the spending transaction to be signed by at least 2 of 3 secret keys that are under control of the initial team members. When they spend the box, they are free to change this part of the script as they wish, for example by adding new members to protect foundation funds. During the first year, these funds will be used to cover the pre-issued EFYT token. After that, they will be distributed in a decentralized manner via a community voting s...

#### Emission Curve#
All of these rules result in the following curve denoting the number of coins in circulation with time:

### Contractual Money#
In our opinion, the overwhelming majority of use-cases for public blockchains (even those that claim to provide a general-purpose decentralized world computer) are for financial applications, which do not require Turing-completeness. For instance, if an oracle writes down non-financial data into the blockchain (such as temperature), this data is usually used further in a financial contract. Another trivial observation we make is that many applications use digital tokens with mechanics different from the native token.
For an application developer, the Ergo Platform offers custom tokens (which are first-class citizens) and a domain-specific language for writing box protecting conditions in order to implement flexible and secure financial applications. Ergo applications are defined in terms of protecting scripts built into boxes, which may also contain data involved in the execution. We use the term contractual money to define \(Erg\)s (and secondary tokens) whose usage is bounded by a contract. This applies to all tokens on the platform in existence because any box with its contents (\(Erg\)s, tokens, data) is bounded by a contract.
However, we can distinguish between two types of contractual \(Erg\)s. The first, called free \(Erg\)s, are the ones that could change their contracts easily and have no restrictions on the outputs or the other inputs of a spending transaction. The second type is bounded \(Erg\)s, whose contracts require the spending transaction to have input and output boxes with specific properties.
For example, if a box \(A\) is protected by just a public key (so providing a signature against a spending transaction is enough in order to destroy the box), the public key owner can spend \(A\) and transfer the \(Erg\)s to any arbitrary output box. Thus, the \(Erg\)s within \(A\) are free. In contrast, imagine a box \(B\) protected by a combination of a public key and a condition that demands the spending transaction to create an output box with the same am...

#### Preliminaries For Ergo Contracts#
While in Bitcoin, a transaction output is protected by a program in a stack-based language named Script, in Ergo a box is protected by a logic formula which combines predicates over a context with cryptographic statements provable via zero-knowledge protocols using AND, OR, and \(k\)-out-of-\(n\) connectives. The formula is represented as a typed direct acyclic graph, whose serialized form is written in a box. To destroy a box, a spending transaction needs to provide arguments (which include zero-knowledge proofs) satisfying the formula.
However, in most cases, a developer is unlikely to develop contracts in terms of graphs. Instead, they would like to use a high-level language such as ErgoScript, which is provided with the reference client.
Writing scripts in ErgoScript is easy. For example, for a one-out-of-two signature, the protecting script would be $pk_1 \lor pk_2$, which means "prove knowledge of a secret key corresponding to the public key \(pk_1\) or knowledge of a secret key corresponding to public key \(pk_2\)." Two separate documents are available for help in developing contracts with ErgoScript: the ErgoScript Tutorial[@ergoTutorial] and the Advanced ErgoScript Tutorial[@ergoAdvTutorial]. Thus, we do not get into the details of developing contracts with ErgoScript. Instead, we provide a couple of motivating examples in the following sections.
Two more features of Ergo shaping contracting possibilities are:
Data Inputs: To be used in a transaction, a box need not be destroyed but can instead be read-only. In the latter case, we refer to the box as being part of the data input of the transaction. Thus, a transaction gets two box sets as its arguments, the inputs and data inputs, and produces one box set named outputs. Data inputs are useful for oracle applications and interacting contracts.
Custom Tokens: A transaction can carry many tokens as long as the estimated complexity for processing them does not exceed a limit, a parameter that is set by miner vo...

#### Contract Examples#
In this section, we provide some examples which demonstrate the superiority of Ergo contracts compared to Bitcoin's. The examples include betting on oracle-provided data, non-interactive mixing, atomic swaps, complementary currency, and an initial coin offering implemented on top of the Ergo blockchain.

##### An Oracle Example#
Equipped with custom tokens and data inputs, we can develop a simple oracle example which also shows some design patterns that we discovered while playing with Ergo contracts. Assume that Alice and Bob want to bet on tomorrow's weather by putting money into a box that becomes spendable by Alice if tomorrow's temperature is more than 15 degrees, and spendable by Bob otherwise. To deliver the temperature into the blockchain, a trusted oracle is needed.
In contrast to Ethereum with its long-lived accounts, where a trusted oracle's identifier is usually known in advance, delivering data with one-time boxes is more tricky. For starters, a box protected by the oracle's key cannot be trusted, as anyone can create such a box. It is possible to include signed data into a box and check the oracle's signature in the contract, but this is quite involved. Instead, a solution with custom tokens is very simple.
Firstly, a token identifying the oracle should be issued. In the simplest case, the amount of this token could be one. We call such a token a singleton token. The oracle creates a box containing this token along with its data (i.e., the temperature) in register \(R_4\) and the UNIX epoch time in register \(R_5\). In order to update the temperature, the oracle destroys this box and creates a new one with the updated temperature.
Assume that Alice and Bob know the oracle's token identifier in advance. With this knowledge, they can jointly create a box with a contract that requires first (read-only) data input to contain the oracle's token. The contract extracts the temperature and time from the data input and decides who gets the payout.

##### A Mixing Example#
Privacy is important for a digital currency but implementing it can be costly or require a trusted setup. Thus, it is desirable to find a cheaper way for coin mixing. As a first step towards that, we offer a non-interactive mixing protocol between two users, Alice and Bob, that works as follows:
Alice creates a box which demands the spending transaction to satisfy certain conditions. After that, Alice only listens to the blockchain; no interaction with Bob is needed.
Bob creates a transaction spending Alice's box along with one of his own to generate two outputs having identical scripts but different data. Each of Alice and Bob may spend only one of the two outputs, but an observer cannot decide which output belongs to whom because they look indistinguishable.
We refer to the Advanced ErgoScript Tutorial[@ergoAdvTutorial] for more details and examples.

##### More Examples#
Additional examples include atomic swaps, crowdfunding, local exchange trading systems, and initial coin offerings (ICOs). For a complete list of examples and tutorials, refer to[@ergoTutorial, @ergoAdvTutorial].
\bibliography
