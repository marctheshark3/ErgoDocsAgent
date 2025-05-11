# Burning a token
Source: docs/dev/tokens/burn.md
Generated: 2025-05-11

## Summary
# Burning a token

There are sometimes occasions when you want to delete a token from your wallet. - Your address was airdropped a token you no longer want
- You created an NFT but something about it is not right. - A project sent you voting or other tokens that you no longer need

To get rid of those tokens, you have a few options. - **Mobile Wallet:** [TokenJay](https://www.tokenjay.app/app/#burntoken) (This requires an Ergopay compatible wallet like Ergo Mobile Wallet)
- **Nautilus:**

## Keywords
token, occasion, wallet, address, project, voting, option, mobile, tokenjay](https://www.tokenjay.app, ergopay, ergo, nautilus, minter, burner](https://github.com, thierrym1212, safew, script)](p2s.md, representation, condition, --todo

## Content
## Burning a token
There are sometimes occasions when you want to delete a token from your wallet.
Your address was airdropped a token you no longer want
You created an NFT but something about it is not right. 
A project sent you voting or other tokens that you no longer need
To get rid of those tokens, you have a few options.
Mobile Wallet: TokenJay (This requires an Ergopay compatible wallet like Ergo Mobile Wallet)
Nautilus: Ergo Token Minter / Burner
SAFEW supports token burning natively.
Send to 4MQyMKvMbnCJG3aJ, a P2S (Pay-to-Script) representation of a “false” condition, i.e. the box is unspendable.

### Programmatically
To burn tokens programmatically, simply spend an Unspent Transaction Output (UTXO) containing the tokens you wish to eliminate. Ensure not to include these tokens in the output of the transaction.

#### Using AppKit
If you're working with AppKit, the transaction builder conveniently offers a burntoken method tailored for this purpose.

#### Ergo Token Minter Integration
The burn token functionality integrated by ThierryM1212 can be observed here. The crucial steps involved are as follows:
Identify and select the input boxes holding the tokens to be burnt, along with a small ERG amount.
Construct the output boxes, excluding consideration of the tokens. The transaction builder automatically appends an additional output change box encompassing all tokens.
Retrieve the transaction JSON representation.
Edit the output change box details to eliminate the tokens intended for burning.
Dispatch the modified transaction (JSON) to the network.
This streamlined approach simplifies the process of burning tokens while maintaining transaction integrity.
