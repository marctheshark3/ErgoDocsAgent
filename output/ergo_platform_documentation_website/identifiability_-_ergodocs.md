# Identifiability - ErgoDocs
Source: [https://docs.ergoplatform.com/eco/ergomixer/identifiability/](https://docs.ergoplatform.com/eco/ergomixer/identifiability/)
Generated: 2025-05-11

## Summary
ErgoUtils now support obfuscating entry points for ErgoMixer. When you withdraw from the mixer to a wallet, it is obvious that that person has received some funds from the mixer, and when he spends those boxes, it is also obvious that those boxes are from the mixer. Those who care about privacy and use ErgoMixer, also probably care about not anyone being able to tell that they are using the mixer easily when they interact with their wallets. This tool is designed to address this issue. Just create an (or more if you wish) obfuscating address with your desired hop number here and use it permanently.

## Keywords
ergoutils, entry, point, ergomixer, mixer, wallet, person, fund, privacy, tool, issue, address, number, output, amount, example, transaction, utility

## Content
## Identifiability#
ErgoUtils now support obfuscating entry points for ErgoMixer.
When you withdraw from the mixer to a wallet, it is obvious that that person has received some funds from the mixer, and when he spends those boxes, it is also obvious that those boxes are from the mixer.
Those who care about privacy and use ErgoMixer, also probably care about not anyone being able to tell that they are using the mixer easily when they interact with their wallets. This tool is designed to address this issue.
Just create an (or more if you wish) obfuscating address with your desired hop number here and use it permanently. To use it, withdraw from the mixer to the address that is created for you; your received funds in that address will automatically go through some random addresses (randomly created outputs, both number of outputs and output amounts) and finally be received in your wallet.
As an example, try to figure out if this transaction is from the mixer or not - a lot harder to figure out.
As always, utilities in ErgoUtils are completely free to use!
ergoutils GitHub
mixerHop.js
