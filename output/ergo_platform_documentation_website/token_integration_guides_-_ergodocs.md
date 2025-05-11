# Token Integration Guides - ErgoDocs
Source: [https://docs.ergoplatform.com/tutorials/token_integration/](https://docs.ergoplatform.com/tutorials/token_integration/)
Generated: 2025-05-11

## Summary
This guide outlines the process for integrating and listing tokens that have been bridged between networks using Rosen Bridge. Whether you're bridging from Ergo to Cardano, Cardano to Ethereum, or any other supported network combination, these steps will help ensure your token is properly integrated across ecosystems. Tokens can be bridged between any networks connected via Rosen Bridge. This means: The world's largest independent crypto data aggregator. Generally easier to get listed compared to CoinMarketCap but still requires significant volume and legitimate activity.

## Keywords
guide, process, token, network, rosen, bridge, ergo, cardano, ethereum, combination, step, ecosystem, tokens, world, datum, aggregator, coinmarketcap, volume, activity, option

## Content
## Cross-Chain Token Integration Guide for Rosen Bridge Tokens#
This guide outlines the process for integrating and listing tokens that have been bridged between networks using Rosen Bridge. Whether you're bridging from Ergo to Cardano, Cardano to Ethereum, or any other supported network combination, these steps will help ensure your token is properly integrated across ecosystems.

### Overview of Cross-Chain Possibilities#
Tokens can be bridged between any networks connected via Rosen Bridge. This means:
Ergo tokens can be bridged to Cardano/Ethereum
Cardano tokens can be bridged to Ergo/Ethereum
Future networks will be supported as they're added to Rosen Bridge (BSC, DOGE)

#### Key Considerations for Multi-Chain Presence#
Each bridged version represents the same token on different networks
Liquidity needs to be managed across all chains
Analytics and trading platforms should be integrated per network
Community education needed for cross-chain functionality

##### CoinGecko#
The world's largest independent crypto data aggregator. Generally easier to get listed compared to CoinMarketCap but still requires significant volume and legitimate activity.
Submit via CoinGecko Token Request Form
Follow the CoinGecko Verification Guide
Options:
For tokens with existing listings + decent volume: Potential automatic acceptance
Alternative: $400 for fast-track listing

##### CoinMarketCap#
The most recognized crypto data platform globally. Getting listed here provides significant legitimacy but has stringent requirements. Typically requires higher volume and more established presence than CoinGecko. Essential for serious projects but should be attempted after CoinGecko listing.

##### LiveCoinWatch#
A growing alternative to CMC and CoinGecko. Generally has lower barriers to entry and faster listing times. Good for building initial market presence and tracking metrics while working toward larger platform listings.

##### GeckoTerminal#
Modern DEX analytics platform focusing on real-time trading data and charts. Particularly strong for tracking DEX pairs and providing detailed trading analytics.

##### Dexscreener#
Popular DEX pair analytics platform with strong community adoption. Often the first stop for traders researching new tokens. While token information can be automatically pulled from CoinGecko once listed there, enhanced features are available as a paid option.
Purchase (Optional) Enhanced Token Info for $299
Benefits:
Verified token status
Custom branding
Social links integration

##### Dextools.io#
Industry standard for Ethereum token trading and analysis. Basic listing is available for free, with token information pulled from CoinGecko.
Submit via Dextools Fast Track Form

#### Security and Audit Platforms#
Quick Intel: Focuses on rapid security analysis and risk assessment. Popular among traders for quick verification of token safety.


GoPlus: Comprehensive security API providing real-time contract analysis. Industry standard for contract verification.


Honeypot.is: Specialized in detecting scam tokens and contract malfunction. Essential for proving token tradability.


De.Fi Scanner: Modern security platform focusing on DeFi-specific risks and vulnerabilities. Helps establish token credibility.

##### Verifying The Source Code#
Source code verification is essential for removing "Unverified Contract" warnings that appear on security scanners and DEX aggregators. By publishing your token's source code on Etherscan, you enable public inspection of the contract code and confirm there are no hidden functions.
Verifying The Source Code
You can verify all of wrapped tokens using this code. Use Compiler version 0.8.20, MIT license, and EVM version paris. Leave all other fields at their default values.
// Sources flattened with hardhat v2.22.12 https://hardhat.org

// SPDX-License-Identifier: MIT

// File @openzeppelin/contracts/interfaces/[email protected]

// Original license: SPDX_License_Identifier: MIT
// OpenZeppelin Contracts (last updated v5.0.0) (interfaces/draft-IERC6093.sol)
pragma solidity ^0.8.20;

/**
 * @dev Standard ERC20 Errors
 * Interface of the https://eips.ethereum.org/EIPS/eip-6093[ERC-6093] custom errors for ERC20 tokens.
 */
interface IERC20Errors {
    /**
     * @dev Indicates an error related to the current `balance` of a `sender`. Used in transfers.
     * @param sender Address whose tokens are being transferred.
     * @param balance Current balance for the interacting account.
     * @param needed Minimum amount required to perform a transfer.
     */
    error ERC20InsufficientBalance(address sender, uint256 balance, uint256 needed);

    /**
     * @dev Indicates a failure with the token `sender`. Used in transfers.
     * @param sender Address whose tokens are being transferred.
     */
    error ERC20InvalidSender(address sender);

    /**
     * @dev Indicates a failure with the token `receiver`. Used in transfers.
     * @param receiver Address to which tokens are being transferred.
     */
    error ERC20InvalidReceiver(address receiver);

    /**
     * @dev Indicates a failure with the `spender`âs `allowance`. Used in transfers.
     * @param spender Address that may be allowed to operate on tokens without being their owner.
     * @param allowance Amount of...

#### Ethereum Network#
This section covers the main priorities for Ethereum integration which are those Trading Analytics Platforms mentioned above and Uniswap. Due to Ethereum's massive DeFi ecosystem, there are hundreds of additional DEXes, lending protocols, yield farms, and other DeFi platforms that tokens could potentially integrate with. Track key platforms via DeFiLlama's Ethereum section.

##### Uniswap#
The largest DEX on Ethereum. Essential for any ETH-based token.
Submit to Uniswap Default Token List
Monitor gas fees via ETH Gas Station

##### Coinbase Wallet#
Most popular non-custodial wallet in the US. Listing here provides significant mainstream exposure.

#### Cardano Network#
Track platforms via DeFiLlama's Cardano section

##### Taptools.io#
Premier analytics platform for Cardano assets. Essential for Cardano token visibility.

##### Cardanoscan#
Main block explorer for Cardano. View transactions at Cardanoscan. Crucial for transaction verification and tracking.

##### AdaPulse#
News and analytics platform focusing on Cardano ecosystem projects.

##### DEX Platforms#
Splash: Our recommended DEX for initial liquidity and trading
View all Cardano DEXes ranked by TVL at DeFiLlama's Cardano DEX Rankings

#### DeFi Ecosystem#
Liqwid: Decentralised lending protocol

##### Core Integrations#
Decentralised exchange: ErgoDEX and MewMart
ErgoTipperBot: Social tipping service, helps with community engagement. Tip your rsToken in Telegram, Discord, bsky, Reddit, and more.
To add a token to the list, simply create a PR that adds your token to the list.


SigmaFi PR: Decentralised bonds
Add as a verified token


DuckPools: DAO-governed liquidity platform 
Requires DAO vote


ErgoMixer: Can mix any rsToken by default, but requires a custom PR to have the name of your rsToken in the UI. (TBC)
TradeHouse: Decentralised orderbook for Ergo assets,

#### Monitoring#
Use ETH Gas Station for optimizing Ethereum transactions
Monitor platform performance via DeFiLlama (most comprehensive DeFi TVL tracker)

#### Gas Fee Management#
Track real-time gas prices on ETH Gas Station to:
Optimize transaction timing
Reduce costs for users
Plan liquidity operations
