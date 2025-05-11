# Initialize Wallet
Source: docs/node/wallet.md
Generated: 2025-05-11

## Summary
---
tags:
  - Wallet
  - Node
  - API
  - Setup
  - Initialize
  - Restore
  - Unlock
  - Lock
  - Keys
  - BIP39
  - BIP32
---

## Initialize Wallet

To initialize the wallet, restart the node and navigate to the [panel](http://127.0.0.1:9053/panel) (Swagger UI). Set the API key using the secret phrase you configured previously. Remember to use the **plain text secret phrase**, not the hash stored in the configuration file. In our example, this is the string `hello`. 

!

## Keywords
wallet, node, setup, initialize, restore, unlock, lock, keys, bip39, bip32, panel](http://127.0.0.1:9053, panel, swagger, phrase, text, hash, configuration, file, example, string

## Content
### Initialize Wallet
To initialize the wallet, restart the node and navigate to the panel (Swagger UI). Set the API key using the secret phrase you configured previously. Remember to use the plain text secret phrase, not the hash stored in the configuration file. In our example, this is the string hello.
Click on Initialize wallet (or execute the /wallet/init or /wallet/restore endpoint). A pop-up or response will appear depending on the method used. You have two main options:
Initialize a new wallet: If this is your first time running the node, choose this option to generate a new mnemonic sentence.
Restore an existing wallet: If you have an existing wallet (e.g., from a previous installation or another wallet software) and want to access its funds, choose this option and provide your previously saved mnemonic sentence.
Choose the option that suits your situation.

#### Initialize Wallet from Scratch
In the pop-up form (or API request body for /wallet/init), enter a secure password for encrypting your wallet file. The 'Mnemonic password' (BIP-39 passphrase) field is optional but adds extra security. After clicking 'Send' (or executing the request), the API response will contain the generated mnemonic sentence.
Make sure to copy this sentence accurately and store it securely offline. You will need this exact sentence (and the optional passphrase, if used) to restore your wallet later or on a different device.

#### Restore Wallet from Earlier
To restore an existing wallet, paste your previously saved mnemonic sentence into the 'Mnemonic' field in the Restore-wallet form (or the mnemonic field in the /wallet/restore API request). Enter a secure password to encrypt the restored wallet file. Leave the 'Mnemonic password' field empty unless your original mnemonic was created with a BIP-39 passphrase; in that case, enter the passphrase here.
After successfully restoring the wallet from the mnemonic sentence, you will see a confirmation message.

#### Get Wallet Addresses
To verify the wallet is initialized or restored correctly, you can retrieve its addresses. Using the Swagger UI panel, navigate to the Wallet section and execute the /wallet/addresses endpoint. The response should list at least one derived address if the wallet setup was successful.

#### Check Wallet Balance
Once the node is fully synchronized with the blockchain, you can check your wallet balance using the /wallet/balances endpoint in the Swagger UI.

#### Sending Funds
If your wallet has a non-zero balance, you can initiate transactions (e.g., sending ERG) using endpoints like /wallet/payment/send via the Swagger UI or other API clients.
