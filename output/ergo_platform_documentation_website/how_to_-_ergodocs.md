# How To - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/protocol/tx/babel-howto/](https://docs.ergoplatform.com/dev/protocol/tx/babel-howto/)
Generated: 2025-05-11

## Summary
Every blockchain requires a fee to fund transactions, and it is most often a blockchain's respective coin that pays for transactions on the network. In the case of Ergo, every transaction requires a payment in $ERG. For those who are active within a blockchainâs ecosystem, there is often a desire to hold assets other than that blockchainâs coin. You may want to buy NFTs, or you may want other tokens native to the blockchain. Depending on a wallet's holdings, the need to use $ERG to pay for transactions may create some complexities.

## Keywords
blockchain, transaction, coin, network, case, ergo, payment, blockchainâs, ecosystem, desire, asset, token, wallet, holding, need, complexity, user, sort, scenario, person

## Content
### The Problem#
Every blockchain requires a fee to fund transactions, and it is most often a blockchain's respective coin that pays for transactions on the network. In the case of Ergo, every transaction requires a payment in $ERG.
For those who are active within a blockchainâs ecosystem, there is often a desire to hold assets other than that blockchainâs coin. You may want to buy NFTs, or you may want other tokens native to the blockchain. Depending on a wallet's holdings, the need to use $ERG to pay for transactions may create some complexities. What if the wallet does not have enough $ERG to fund a transaction where the user is trying to send a native token? This sort of scenario might discourage a person from using the chain because they cannot fund a transaction with $ERG.
Based on the above scenario, it would be more convenient to pay for transactions in native tokens rather than $ERG. This is now possible with the introduction of Babel fees.

### Babel Fees#
With Babel fees, you no longer need $ERG to pay for a transaction. You can pay for the transaction using fungible, native tokens that have liquidity. Letâs take a look at how this new feature works on Ergo.

### Providing Babel Fee Liquidity#
Before using Babel fees, someone (or many people) must provide liquidity on the blockchain. They agree to buy the native asset for $ERG at some rate. To illustrate:
Go to the Tokenjay site.
Click âOpen Appâ. 
Click âPurchase Tokensâ.
Click âBabel Fee Liquidityâ.
Connect a compatible ErgoPay wallet.
Click âcreate new babel fee boxâ.
Select token from drop-down box or own ID entered below.
Optional: Enter token ID of a fungible token (not an NFT) not on drop-down list.
Enter rate, or number of $ERG per token, often as a decimal, such as 0.0001.
Enter the amount of $ERG you are willing to buy at that rate.
Click âcreate Babel fee boxâ.
Scan QR code.
Check the rates before signing.
Optional: Go back to Step 6 if the rates were not as expected.
Sign transaction in your ErgoPay compatible wallet.
This provides a Babel Fee bank box, which anyone can use to trade the digital asset for $ERG to pay for transactions. Building the transaction is handled within a wallet that supports Babel Fees.

### Using Babel Fee Bank Boxes#
Using Babel Fee Boxes is simple. Nautilus, for example, allows you to pick a token to pay a fee based on what is in your wallet, and it selects the best rate from the Babel Fee bank boxes available on the blockchain. In the case below, the token SigUSD is being used to swap for the necessary amount of $ERG to pay for the transaction. The process of choosing to pay with Babel fees is as simple as selecting the native asset from a pull-down list.

##### Conclusion#
Babel Fees are an innovative solution that make blockchains easier to use. For users, they eliminate the need to keep the blockchain coin in each wallet they own. It basically helps to prevent assets from getting âstuckâ because a wallet does not have the blockchainâs coin (or enough of that coin). The introduction of Babel fees on Ergo offers a significant boost to the versatility of the blockchain. With this newly implemented technology, Ergo becomes much more fluid and flexible by increasing the efficiency of transactions and interactions on the network.
