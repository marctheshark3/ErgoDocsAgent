# Babel Fees - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/protocol/tx/babel-fees/](https://docs.ergoplatform.com/dev/protocol/tx/babel-fees/)
Generated: 2025-05-11

## Summary
Babel fees (introduced via EIP-0031) allow users to pay transaction fees in tokens other than the platform's primary token (ERG). This system is particularly helpful for users primarily interested in transferring tokens without needing to obtain ERG. On Ergo, Babel fee payments are facilitated through pre-defined Babel Fee pools, offering a predictable and transparent fee payment process. This system differs from Cardano's approach, where users broadcast incomplete transactions and wait for a third party to pay fees in ADA in exchange for the offered tokens. Here's how Babel fees work: EIP-31 Supporters Provide Liquidity:

## Keywords
babel, eip-0031, user, transaction, token, platform, system, ergo, payment, pool, process, cardano, approach, party, exchange, eip-31, supporters, liquidity, users, amount

## Content
## Babel Fees#
Babel fees (introduced via EIP-0031) allow users to pay transaction fees in tokens other than the platform's primary token (ERG). This system is particularly helpful for users primarily interested in transferring tokens without needing to obtain ERG.
How Babel Fees Work on Ergo
On Ergo, Babel fee payments are facilitated through pre-defined Babel Fee pools, offering a predictable and transparent fee payment process. This system differs from Cardano's approach, where users broadcast incomplete transactions and wait for a third party to pay fees in ADA in exchange for the offered tokens.
Here's how Babel fees work:


EIP-31 Supporters Provide Liquidity:

Users (referred to as "EIP-31 supporters") create Unspent Transaction Outputs (UTXOs) containing ERG locked in a smart contract
These UTXOs have a price attribute specifying the amount of ERG the supporter is willing to pay for one unit of a specific "babel token"
Smart contracts secure these UTXOs



Users Select a Babel Fee Box:

Users locate UTXOs for their desired token
Verify sufficient ERG for transaction fees
Evaluate exchange rates
Choose the most favorable rate



Babel Fee Box is Spent and Recreated:

User spends the selected UTXO
Recreates UTXO with identical parameters (creator's public key and price)
Deposits required token amount
Smart contract ensures the difference in ERG is less than or equal to the amount of inserted babel tokens multiplied by the price




On Cardano, you will send an "incomplete" transaction, offering to pay the fee using x amount of tokens and wait until a third party accepts your tokens in exchange for ADA to pay the fees.
On Ergo, we have pre-defined Babel Fee pools, so there is no waiting, and we can know in advance what tokens we can use to pay fees and the best price available.

For more information about the origin of the term and concepts behind "babel fees", please see the following articles:

Babel fees - denominating transaction costs in native tokens
Paying fee in ErgoM...

### Providing Babel Fee Liquidity#
Providing liquidity for Babel fees is a way to earn passive income while helping new users onboard to Ergo. As a liquidity provider, you lock up ERG in a smart contract and specify a rate at which you're willing to buy tokens. When users pay transaction fees with those tokens, you automatically receive them in exchange for your ERG. This creates a win-win situation - users can transact without needing ERG, and you accumulate tokens at your desired rate.
To provide Babel fee liquidity:
{type: question, open: true}


Go to the Tokenjay site
Click "Open App"
Click "Purchase Tokens"
Click "Babel Fee Liquidity"
Connect a compatible ErgoPay wallet
Click "create new babel fee box"
Select token from drop-down box or own ID entered below
Optional: Enter token ID of a fungible token (not an NFT) not on drop-down list
Enter rate, or number of $ERG per token, often as a decimal, such as 0.0001
Enter the amount of $ERG you are willing to buy at that rate
Click "create Babel fee box"
Scan QR code
Check the rates before signing
Optional: Go back to Step 6 if the rates were not as expected
Sign transaction in your ErgoPay compatible wallet

### Developers#
By implementing babel fees in your application, you can enable new users to start transacting immediately using tokens instead of ERG. The Fleet SDK makes this easy with its babel-fees plugin, which handles all the complexities of token-to-ERG conversions and contract interactions.
You can see the full documentation here.
