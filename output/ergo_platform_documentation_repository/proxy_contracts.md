# Proxy contracts
Source: docs/dev/wallet/payments/standards/eip17.md
Generated: 2025-05-11

## Summary
---
tags:
  - EIP
---
# Proxy contracts

> 🔗 From [EIP-0017](https://raw.githubusercontent.com/ergoplatform/eips/master/eip-0017.md) * Author: anon_real
* Status: Proposed
* Created: 05-May-2021
* License: CC0
* Forking: not needed 



## Motivation 

Outsourcing transaction generation to an external service/dApp can be useful or even needed in various circumstances. For example, avoiding wallet limitations to generate any transaction on behalf of the user - [Ergo Assembler](https://github.com/anon-real/ergo-assembler) is designed for this purpose. Another example is to scale dApps to be able to fulfill many requests without double-spending or data invalidation - SigmaUSD dApp can use proxy contracts to avoid bank double-spending and ERG/USD oracle data invalidation. ## Background
The idea of proxy contracts came to life with the [Ergo Assembler](https://github.com/anon-real/ergo-assembler) which helped dApp developments like [Ergo Auction House](https://ergoauctions.org/), [ErgoUtils](https://ergoutils.org/), and [SigmaUSD web interface](https://sigmausd.io/#/) despite not having a wallet-bridge like MetaMask (Ethereum wallet) in the ecosystem.

## Keywords
proxy, contract, eip-0017](https://raw.githubusercontent.com, ergoplatform, master, eip-0017.md, author, status, may-2021, license, forking, motivation, outsourcing, transaction, generation, service, dapp, circumstance, example, wallet

## Content
## Proxy contracts
🔗 From EIP-0017
Author: anon_real
Status: Proposed
Created: 05-May-2021
License: CC0
Forking: not needed

### Motivation
Outsourcing transaction generation to an external service/dApp can be useful or even needed in various circumstances. For example, avoiding wallet limitations to generate any transaction on behalf of the user - Ergo Assembler is designed for this purpose. Another example is to scale dApps to be able to fulfill many requests without double-spending or data invalidation - SigmaUSD dApp can use proxy contracts to avoid bank double-spending and ERG/USD oracle data invalidation.

### Background
The idea of proxy contracts came to life with the Ergo Assembler which helped dApp developments like Ergo Auction House, ErgoUtils, and SigmaUSD web interface despite not having a wallet-bridge like MetaMask (Ethereum wallet) in the ecosystem.
During this time, the structure of proxy contracts evolved as some malicious users tried to take advantage of some minor vulnerabilities, mostly in the SigmaUSD dApp.

### The structure
In the beginning, the sole purpose of proxy contracts was to protect users from losing their funds (not to be cheated) when they outsource their assets to engage with some dApp. While the initial structure succeeded to achieve this, it proved to be not sufficient for the whole dApp infrastructure to work without malicious activities. Some examples of dApp infrastructure violations are as follows:
A malicious whale tried to take advantage of this simple structure by stealing UI fees from SigmaUSD web interface developers for some period of time. This happened because the proxy contracts were simply only trying to protect users from malicious activities, not the dApp infrastructure.


The same whale tried to prevent user's requests (minting/redeeming) from being executed by the assembler service by retuning their funds as soon as funds were broadcasted in the network. This happened also because of the same reasons.


Moreover, the whale tried to sell SigUSD/SigRSV tokens to users by imitating the bank box. He succeeded to do that and take 2.25% fee for each request which was supposed to go to the SigRSV holders (2%) and UI devs (0.25%).
The above attacks were possible because proxy contracts were not designed to preserve the integrity of the whole dApp infrastructure but only the user's funds.
Generally, proxy contracts should be designed to:
prevent dApp developers or any other attacker from taking advantage of user's funds in any manner
preserve the integrity of the dApp by preventing attacks like the ones explained in the above examples.
To achieve all of the above, the below contract structure is proposed as an example:
```scala
{
  // dApp-specific part ensuring that user will receive what he is paying for
  val properFundUsage = {
    val userOut = OUTPUTS(1)
    userOut.propositionBytes == fromBase64("$userAddress") && // user must be the recipient
      userOut.tokens(0)._1 == fromBase64("$scTokenId") && // user must receive SigmaUSD
      userOut.tokens(0)._2...
