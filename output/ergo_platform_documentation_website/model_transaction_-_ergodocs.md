# Model Transaction - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/protocol/tx/model-tx/](https://docs.ergoplatform.com/dev/protocol/tx/model-tx/)
Generated: 2025-05-11

## Summary
The UTXO (Unspent Transaction Output) model, which we use, can be a bit confusing if you're used to the Account model. Here's a simple way to understand it: In the Account model, you have a single account where you receive your coins. In the UTXO model, every transaction creates a new "box", and your balance is the sum of all the boxes linked to your addresses. In other words, your Yoroi private key can consist of multiple boxes within a single address to hold your coins. When you generate a new address, a secondary box is created to hold your coins.

## Keywords
utxo, unspent, transaction, output, model, account, coin, balance, address, word, yoroi, fund, number, spending, action, feature, misconception, network, token, thing

## Content
## Understanding Model Transaction#
The UTXO (Unspent Transaction Output) model, which we use, can be a bit confusing if you're used to the Account model. Here's a simple way to understand it: In the Account model, you have a single account where you receive your coins. In the UTXO model, every transaction creates a new "box", and your balance is the sum of all the boxes linked to your addresses.
In other words, your Yoroi private key can consist of multiple boxes within a single address to hold your coins.
When you generate a new address, a secondary box is created to hold your coins. Once created, you can send funds to this new address. These funds will be linked with your private key. You can create an unlimited number of new boxes to hold your coins. Therefore, every receiving and spending action will also create an additional unique box.
This feature can initially create misconceptions. When you make a transaction, the network scans your "boxes" to verify if you have your tokens and then initiates the transaction.
Things get complex after this point because you can not predict which boxes are going to be spent. Let's say you have three different receiving addresses. You received a couple of coins in each of them, and you want to spend some of your coins. In a Yoroi wallet, you can hold any Ergo native coins such as SigRSV or SigUSD. When you initiate a transaction that accesses the boxes of these coins, you will see that they are taken away and then redeposited. Recently, an Ergonaut raised the following question:
"I just created a Yoroi Nightly wallet. I transferred 31 Erg from my main Yoroi wallet to the Yoroi Nightly wallet. The transaction shows 31 Erg plus a small fee, 0.0011. But it also says +92,000 SigRSV. My balance shows no change in SigRSV. What is the meaning of the +92,000 SigRSV in the transaction?"
Let's break down this particular transaction:
To make a transaction of '31 ERG`,  the wallet selected three of the boxes with ERG:
A box containing 0.029595 ERG that was received on 07/1...

### Summary#
The Account model contains a single box, and this box is not spent. It remains the same so that non-related coins will remain unaffected.
The UTXO model, on the other hand, contains a set of boxes that represents the total amount of the user's balance and the unspent transaction output has to change with each spending transaction.
You may see a long list of tokens when swapping just 5 SigRSV as below:
This is how UTXO model Transaction works - its storage is different from the Accounts model. In the UTXO model, coins will be stored in one-use UTXO boxes and not in long-living accounts.
