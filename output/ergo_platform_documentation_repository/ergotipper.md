# Ergotipper
Source: docs/contribute/standards/tipbot.md
Generated: 2025-05-11

## Summary
# Ergotipper

This page describes how to set up the **ErgoTipperBot** on each platform. This bot allows you to tip other members erg, or any of the supported native tokens. Simply set up your wallet, fund it, and start tipping! If you tip someone without a wallet, one will automatically be generated for them. You can restore using the same seed phrase, and use the same tip wallet across all platforms.

## Keywords
ergotipper, page, ergotipperbot, platform, member, token, wallet, seed, phrase, coin, luivatra, list, pull, request, github](https://github.com, name, whitespace, clutter, reddit](https://www.reddit.com, message

## Content
## Ergotipper
This page describes how to set up the ErgoTipperBot on each platform. This bot allows you to tip other members erg, or any of the supported native tokens. Simply set up your wallet, fund it, and start tipping! If you tip someone without a wallet, one will automatically be generated for them.
You can restore using the same seed phrase, and use the same tip wallet across all platforms.
Supported coins/tokens

### Adding a token
To add a token to the list, simply create a pull request on Github that adds your token to the list. A token name should not contain whitespace, so if your token does have whitespace in the name make sure to replace/remove it. To avoid clutter in the token list add NFT's to the separate list below.

### Supported Platforms
Reddit 
Discord (Ergo Tipper Bot[BETA]#0902)
Telegram
Twitter
This is a bot that runs on a server managed by u/Luivatra. It is not unhackable (nothing is). Do not use this as a main wallet!
To have your token added to the bot, please start a poll in one of the community spaces.

#### Reddit
Send a private message (not chat!) to u/ErgoTipperBot with the text: !start
Once the wallet is created, send a pm with !address to show your tip address.
Copy your tip address and open your Yoroi wallet.
Click the send tab and transfer some ERG's to the tip wallet address. (Any transaction requires at least 0.001 erg in fees, on top of that funds in utxo are stored in a box. Each box needs to have a small amount of erg in them. So on the tip bot a token tip will require 0.00115 erg)
If you want to tip a token like Kushti for example, transfer the token to the same tip wallet address. 
Once the transactions are sent (~ 2 minutes), send a PM to u/ErgoTipperBot: !balance
Your balance should look like this:
| token  | amount |
|--------|:-------|
| Erg    | 0.1    |
| Kushti | 100    |
You are good to go! In one of the subreddits where u/ErgoTipperBot is activated write a comment to the person you want to tip with the following command (without the brackets):
!tip <amount> <token> <any remaining text will be stored in the transaction database so you can both view it later>

#### Commands
In comments:
!tiphelp: Show this message
!tip <amount> <token> <any remaining text will be stored in the transaction database so you can both view it later>: tip the person you reply to


In PM:
!start: Initialize a tip wallet
!changepw  : Change tip wallet pw
!address: Show tip wallet address
!seed : Show tip wallet seed phrase
!balance: Show tip wallet balance
!restore  : Restore an existing wallet to be used as your tip wallet (use this to use the same wallet across Discord & Reddit)

##### Commands
In comments:
/t <amount> <token> <any remaining text will be stored in the transaction database so you can both view it later>: tip the person you reply to, make sure to tag @ErgoTipperBot


In DM with @ErgoTipperBot:
/start: Initialize a tip wallet
/changepw currentPassword newPassword: Change tip wallet pw
/address: Show tip wallet address
/seed password: Show tip wallet seed phrase (Note that the password you need to retrieve your seed phrase is the one given to you by the tipbot in it's first message.)
/balance: Show tip wallet balance
/restore password seedphrase: Restore an existing wallet to be used as your tip wallet (use this to use the same wallet across Discord, Reddit, Twitter & Telegram)

#### Restoring
You can restore the generated wallet in any supported Ergo wallet by using the retrieved seed.

#### Discord
Simply DM the bot Ergo Tipper Bot[BETA]#0902 on Discord and a menu will appear when you type /

#### Twitter
Please note the bot on Twitter has a ~10min delay in responding.
Send a direct message to ErgoTipperBot with !start
