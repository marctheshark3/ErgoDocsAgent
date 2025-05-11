# Accessing Sigmausd As A Developer
Source: docs/uses/sigmausd.md
Generated: 2025-05-11

## Summary
# Accessing Sigmausd As A Developer

SigmaUSD is the first eUTxO-based stablecoin, implementing the [AgeUSD protocol](https://github.com/Emurgo/age-usd). It was co-designed by IOHK, Ergo, and Emurgo, focusing on conservative collateral reserve settings, thus eliminating the need for liquidations. SigmaUSD supports a fully decentralized stablecoin emission setup, offering a stable, simple, and decentralized stablecoin. ## How does SigmaUSD work?

## Keywords
access, sigmausd, developer, eutxo, stablecoin, ageusd, protocol](https://github.com, emurgo, iohk, ergo, collateral, reserve, setting, need, liquidation, emission, setup, provider, dapp, coin

## Content
## Accessing Sigmausd As A Developer
SigmaUSD is the first eUTxO-based stablecoin, implementing the AgeUSD protocol. It was co-designed by IOHK, Ergo, and Emurgo, focusing on conservative collateral reserve settings, thus eliminating the need for liquidations. SigmaUSD supports a fully decentralized stablecoin emission setup, offering a stable, simple, and decentralized stablecoin.

### How does SigmaUSD work?
Reserve providers submit ERGs to the dApp's reserves to mint reserve coins (SigmaRSV), each representing a portion of the underlying ERG reserves. SigmaUSD users also submit ERGs to the dApp reserves to mint SigmaUSD, provided there are sufficient reserves within the dApp. Users can redeem their SigmaUSD for an equivalent amount of ERGs from the reserves at the current exchange rate as provided by the ERG-USD oracle pool.
Reserve Providers can redeem their reserve coins for ERGs if the price of ERGs increases or a significant amount of protocol fees are collected, covering the value of all existing minted SigmaUSD plus an extra margin. This allows Reserve Providers to profit by receiving more underlying reserve cryptocurrency than when they minted their reserve coins.

### Common Questions
/// details | What is a stablecoin?
     {type: question, open: false}
It is a derivate product. This derivative intends to create a way to stabilise volatility.
Price stability is a critical part of finance; without it, it becomes difficult to create long-term financial product modellings. Investment takes a risk; a good business requires modelling and forecasting to estimate profitability, whether on-chain or off.
The crypto space, by nature, is highly volatile. SigmaUSD and SigmaRSV are mechanisms to create stable value, and stable value is the foundation for a prosperous economy.
Derivatives were created to minimise volatility when trading in foreign currencies.
In a globalised economy, the shift in purchasing power of one currency vs another can be a highly destructive force. Instability disrupts trade and destroys business models.
Stability comes at a cost. Instability in price is often added as a premium, sometimes a price premium, and other times an interest premium.
The cost of SigmaUSD is the current USD value of ERG plus a 2.5% fee.
This is a low premium, 2.5%.
What is your current interest rate? What is the rate at which a bank will collateralise an asset you hold and offer a loan?
Very few have access to this low premium in the global economy, and the bank may not offer liquidity with little to no reserve.
SigmaUSD allows anyone who owns ERG to collateralise their ERG and create liquid value. What does this mean?
The long-term goal will be to create use cases for this stablecoin that offers a return beyond this 2.5% fee. 
///
/// details | Why SigmaUSD
     {type: question, open: false}
When Dapps and use/utility are in place that supersedes this 2.5% fee, magic happens.
A user can take their ERG, create SigmaUSD, and then use that to create a return greater than the 2.5% cost of stability. Most business models rely on stability and price/risk prediction rather than asset speculation.
SigmaUSD is not just an opportunity to take a short position on ERG. ...

### Explore
/// details | Accessing SigUSD as a Developer
     {type: info, open: false}
This guide introduces key methods for developers to interact with the SigmaUSD stablecoin on the Ergo blockchain, providing detailed steps, code examples, and references to relevant files. Whether you're building a frontend dApp with Mosaik or managing UTXOs with AppKit, this guide covers the essentials. For a deeper dive, see the full documentation here.
///
/// details | Useful Links
     {type: info, open: false}
- ERG/USD Explorer
- ergo.watch
- Bank Wallet
///
/// details | SigmaUSD Calculators
     {type: info, open: false}
- Spreadsheet
///
/// details | Related Articles
     {type: info, open: false}
- Building Ergo: How the AgeUSD stablecoin works
- AgeUSD Protocol: SigRSV and SigUSD
- SigmaUSD vs the competition.
- SigmaUSD on Ergo - Privacy, Stability and Governance
- Risk and reward mechanism
///
/// details | Explainer Threads
     {type: info, open: false}
- Noob tries to explain SigmaUSD/RSV (an attempt at an ELI5)
- PSA: sigRSV is not a simple long position
///
/// details | SigmaUSD Videos
     {type: info, open: false}
- Ergo Summit 2021 - The IOHK Perspective - Designing the AgeUSD StableCoin
- Overview Video (with diagrams)
- Youtube Playlist
- Buying Guide
- Buying Guide2
///
