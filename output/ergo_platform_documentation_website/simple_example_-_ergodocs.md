# Simple Example - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/tokens/nfts/nft-examples/](https://docs.ergoplatform.com/dev/tokens/nfts/nft-examples/)
Generated: 2025-05-11

## Summary
minting-for-dummies is a basic tool for NFT minting quickly in Scala. You can see the mint() logic here To mint an NFT using the Ergo Python Appkit, you can utilize the mintToken method provided by the ErgoAppKit class. First, you need to initialize the ErgoAppKit instance with the appropriate parameters such as nodeUrl, networkType, explorerUrl, and nodeApiKey. Then, you can call the mintToken method with the required parameters, including the value, tokenId, tokenName, tokenDesc, mintAmount, decimals, and contract. Here's an example of how to mint an NFT using the ergo-python-appkit: After minting the NFT, you can use other methods provided by the ErgoAppKit class to interact with the NFT, such as transferring it to another address or querying its properties.

## Keywords
dummies, tool, scala, mint, logic, ergo, python, appkit, method, class, instance, parameter, nodeurl, explorerurl, nodeapikey, value, tokenid, mintamount, decimal, contract

## Content
### Using Scala#
minting-for-dummies is a basic tool for NFT minting quickly in Scala.
You can see the mint() logic here

### Using Ergo Python Appkit#
To mint an NFT using the Ergo Python Appkit, you can utilize the mintToken method provided by the ErgoAppKit class. First, you need to initialize the ErgoAppKit instance with the appropriate parameters such as nodeUrl, networkType, explorerUrl, and nodeApiKey. Then, you can call the mintToken method with the required parameters, including the value, tokenId, tokenName, tokenDesc, mintAmount, decimals, and contract.
Here's an example of how to mint an NFT using the ergo-python-appkit:
from ergo_python_appkit import ErgoAppKit
from org.ergoplatform.appkit import ErgoContract

# Initialize ErgoAppKit instance
appKit = ErgoAppKit(nodeUrl="https://ergo-node-url", networkType="mainnet", explorerUrl="https://ergo-explorer-url", nodeApiKey="your-node-api-key")

# Define the NFT parameters
value = 1000000
tokenId = "your-token-id"
tokenName = "Your Token Name"
tokenDesc = "Your Token Description"
mintAmount = 1
decimals = 0

# Compile the contract
contract = ErgoContract.compile("sigmaProp(true)")

# Mint the NFT
appKit.mintToken(value, tokenId, tokenName, tokenDesc, mintAmount, decimals, contract)
After minting the NFT, you can use other methods provided by the ErgoAppKit class to interact with the NFT, such as transferring it to another address or querying its properties.
Reference links:
ErgoBox
ErgoAppKit
ErgoTransaction
ergo-python-appkit module
Building transaction and minting a token using AppKit from Python.

### More Examples#
Bulk Mint with Royalties using v1 design in Python
On-Chain NFTs

### References#
Eip4TokenBuilder on GitHub
Eip4Token on GitHub
