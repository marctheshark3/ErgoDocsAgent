# Ergo Platform Blockchain Integration Guide
Source: dev/Integration/guide.md
Generated: 2025-05-11

## Summary
---
tags:
  - Tutorial
  - Integration
---
# Ergo Platform Blockchain Integration Guide

This guide provides developers with the necessary information to integrate with the Ergo Blockchain Platform. For suggestions to improve this guide, please reach out to us at team@ergoplatform.org or join our [`#development` channel on Discord](https://discord.gg/kj7s7nb). ## Key Features

- Ergo's transactions consist of multiple *inputs* and *outputs*, similar to Bitcoin. Unspent outputs, known as **single-use entities**, are used once. Although built from the ground up, Ergo's scripts and transaction formats differ from Bitcoin's.

## Keywords
tutorial, integration, ergo, platform, blockchain, guide, developer, information, suggestion, team@ergoplatform.org, development, channel, discord](https://discord.gg, kj7s7nb, features, transaction, input, output, bitcoin, unspent

## Content
## Ergo Platform Blockchain Integration Guide
This guide provides developers with the necessary information to integrate with the Ergo Blockchain Platform. For suggestions to improve this guide, please reach out to us at team@ergoplatform.org or join our #development channel on Discord.

### Key Features
Ergo's transactions consist of multiple inputs and outputs, similar to Bitcoin. Unspent outputs, known as single-use entities, are used once. Although built from the ground up, Ergo's scripts and transaction formats differ from Bitcoin's. For an in-depth understanding, refer to the Ergo 'Box' model.
Ergo incorporates standard scripts, associated with P2PK addresses, much like Bitcoin. Explore more about the address scheme here.
An Ergo UTXO box utilizes registers to store arbitrary values, such as native tokens, rather than a single amount (like BTC). Each box holds an ERG amount and may include {tokenid, token amount} pairs, adhering to the UTXO model.
Ergo's built-in wallet API caters to most use cases. The API employs a Swagger interface and operates on 127.0.0.1:9053 by default in the mainnet (9052 on the testnet).
The precision of each transaction on the Ergo platform is up to $10^{-9}$ ERG. This means that transactions can be made with a precision of up to 0.000000001 ERG.
The average interval time of each block on the Ergo blockchain is approximately 2 minutes.

#### Node
For the best performance, we advise you to run your own node. If that's not feasible, you can use a public node available at 213.239.193.208:9053. For backup options, feel free to reach out to us at team@ergoplatform.org or join our group chat. You can also find a dynamic list of public nodes at api.tokenjay.app/peers/list.
If you choose to run a public node, you can access the web interface at 127.0.0.1:9053/panel. Please note that the port switches to 9052 on the testnet. For guidance on getting started with the testnet, please refer to this page.
Running an Ergo node requires a certain amount of disk space, which depends on factors like the size of the blockchain and the number of transactions. We recommend having at least 100 GB of disk space to ensure seamless operation.
For a more efficient setup, you can bootstrap a pruned node using a verified UTXO set snapshot and NiPoPoWs.

##### Exchange Specific Node Settings
For exchange nodes, consider implementing the following non-default wallet settings:
Set ergo.wallet.dustLimit = 1000000 to disregard incoming payments (e.g., airdrops) of 0.001 ERG or less. Adjust as needed. The default null accounts for all incoming payments.
Set ergo.wallet.profile to exchange to enable larger Bloom filters for more efficient scanning with many addresses.
Set ergo.wallet.tokensWhitelist to a non-null value to automatically burn airdrop tokens and similar.
Combine these settings in your configuration:
```
  ergo {
    ...
    wallet {
      ...
# boxes with value smaller than dustLimit are disregarded in wallet scan logic
  dustLimit = 1000000

  # Whitelisted tokens, if non-null, the wallet will automatically burn non-whitelisted tokens from
  # inputs when doing transactions.
  # If tokensWhitelist = [], all the tokens will be burnt,
  # tokensWhitelist = ["example"] means that all the tokens except of "example" will be burnt
  # tokensWhitelist = null means no tokens burnt automatically
  tokensWhitelist = [
    # SigUSD
    "03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04",
    # SigRSV
    "003bd19d0187117f130b62e1bcab0939929ff5c7709f843c5c4dd158949285d0"
  ]


  # Wallet profile allows to say wallet what kind of load it should expect,
  # and so spend memory on caches and Bloom filters accordingly.
  # There are three options: user, exchange, appServer
  # User profile is about ordinary planned usage.
  # Exchange consumes ~20 MB of RAM for high-load ready Bloom filters
  # AppServer is in between
  profile = "exchange"
}
}  
```

##### Node Wallet
/// admonition | Swagger
    type: tip
Ergo node offers a REST API accessible via HTTP. The complete API specification, in OpenAPI format, can be found here. When the node is operational, access the user-friendly Swagger UI at 127.0.0.1:9053/swagger or experiment with it here. An optional indexed node API is also available.
///
Major wallet functionalities include:
Wallet creation (/wallet/init) and mnemonic generation
Wallet restoration (/wallet/restore) from mnemonic
Wallet unlock (/wallet/unlock) for transaction signing
Wallet lock (/wallet/lock)
Sending a simple payment (/wallet/payment/send)
Checking wallet status (/wallet/status)
Deriving a new key according to EIP-3 (BIP 44 implementation for Ergo) (/wallet/deriveNextKey)
Checking wallet balance (/wallet/balances) for all addresses
Retrieving wallet transactions (/wallet/transactions) for all addresses

###### RPC Documentation
Overview
API Spec
Indexed Node

#### Explorer
The public explorer is available at explorer.ergoplatform.com. Community-hosted alternatives include ergexplorer.com and sigmaspace.io.
For more information, including additional details, toolkits, mirrors, and more, please visit the dedicated Explorer section.

#### GQL
GraphQL queries provide flexible data fetching, minimizing over-fetching and under-fetching. The GraphQL server, built on the Ergo Platform's explorer database schema, is accessible at gql.ergoplatform.com.
The most reliable instance is currently explore.sigmaspace.io/api/graphql.

### Creating an External Wallet
Develop your wallet logic externally using one of the available libraries and the block explorer.
Consider mempool transactions to avoid double-spending.
Available libraries:
ergo-appkit: A complete Java SDK.
ergo-wallet: Developed in Java, source code available in the Ergo node repository.
sigma-rust: A Rust library with WASM bindings for JavaScript/TypeScript.
ergo-golang: An early-stage Go library.
ergo-lib-go: A Go library for Ergo.
Ergo's transactions, akin to Bitcoin, consist of multiple inputs and outputs. Unspent outputs, known as single-use entities, are used once. Although Ergo is built from the ground up, its scripts and transaction formats are distinct from Bitcoin's. For an in-depth understanding, refer to the Ergo 'Box' model.
Ergo incorporates standard scripts, associated with P2PK addresses, much like Bitcoin. An Ergo UTXO box utilizes registers to store arbitrary values, such as its native tokens, rather than a single amount (like BTC). Consequently, each box holds an ERG amount and may also include {tokenid, token amount} pairs, adhering to the UTXO model.

#### Offline Signing
Demo for transaction assembly and offline signing using ergo-wallet and Java: AdressGenerationDemo.java
Transaction assembly and signing in Rust: tx_builder.rs and signing.rs
Transaction assembly and signing in JavaScript

#### Address Generation
Demo for secret seed and derived addresses generation using ergo-wallet and Java: AdressGenerationDemo.java
Use the /wallet/deriveNextKey API to generate new addresses in the same wallet:
bash
curl -X GET "http://localhost:9053/wallet/deriveNextKey" -H  "accept: application/json" -H  "api_key: hello"
The output would be:
json
{
  "derivationPath": "m/44'/429'/0'/0/1",
  "address": "9gF9QP33MoPc8uekF95VHdosL4KzgSz7Ec7MLEtuhx4uPAd3eZs"
}
Derivation is done according to BIP-32.

#### Address Validation
For exchanges, restrict withdrawals to P2PK addresses and invalidate other types. Supporting other types is not recommended. See address types for more information.
ergo-simple-addresses contains Java-friendly utils for working with addresses.

#### Composing Transactions Outside the Node
Get unspent UTXOs for an address using the transactions/boxes/byAddress/unspent Explorer API method:
bash
https://api.ergoplatform.com/transactions/boxes/byAddress/unspent/9gAE5e454UT5s3NB1625u1LynQYPS2XzzBEK4xumvSZdqnXT35M
When selecting UTXOs manually, be sure to use the binary-encoded version of the inputs. You can retrieve the binary data for a UTXO by making a call to /utxo/byIdBinary/{boxId}.
For example:
bash
curl -X 'GET' \
  'http://127.0.0.1:9053/utxo/byIdBinary/{boxId}' \
  -H 'accept: application/json'
Use the returned bytes field in your inputsRaw field of the transaction request.

##### Handling Unconfirmed UTXOs
To avoid double-spending, it's important to handle unconfirmed UTXOs properly. There are two main approaches:
Fetch unconfirmed transactions using the /transactions/unconfirmed/byErgoTree endpoint and exclude inputs from these transactions. You can convert an address to ergoTree using the ErgoAddress class in fleetSDK:
java
   ErgoAddress.fromPublicKey(hex.decode(publicKey), Network.Mainnet).ergoTree;
Download the whole mempool using the /transactions/unconfirmed endpoint and exclude unconfirmed UTXOs from your inputs.
Here's an example of fetching unconfirmed transactions by ergoTree:
bash
curl -X POST "https://api.ergoplatform.com/transactions/unconfirmed/byErgoTree" -H "Content-Type: application/json" -d "\"00020006f03234fca83e0f00e7fe45e4bdb9db03008f279f599273b471bd85e22d8f1ef01\""
If the result is an empty array, there are no unconfirmed transactions for the given ergoTree.

##### Batch Withdrawals
Processing user withdrawals in batches by gathering them in a script and pushing all outputs in one transaction can be beneficial. Here's a high-level overview of the process:
When a user initiates a withdrawal, store the transaction details in your system.
Every X minutes (e.g., 5-10 minutes), collect all pending withdrawals.
Build a new transaction with multiple inputs (from your exchange's wallet) and outputs (to the users' withdrawal addresses).
Sign and broadcast the batch transaction.
This approach can help optimize transaction processing and reduce overall fees. However, it may require adjustments to your existing code framework.

##### Example Batch Transaction Request
When manually creating transactions, make sure the inputsRaw field contains binary-encoded UTXOs retrieved as described earlier. An example transaction might look like this:
json
{
    "requests": [
        {
            "address": "9ek75mvKwhM5uTT39L9mEdsPGWtMkc7wKRUToVNYT5FSAHJazWc",
            "value": 4664620000
        },
        {
            "address": "9fF8dd6XcbAx6n475CZqu7JsxSXTLRJm2ov22GiV6kaxrugX1x6",
            "value": 1000000000
        }
    ],
    "fee": 1000000,
    "inputsRaw": ["8089938d150008cd021d9e5e6e45f12c5dc22f7edbb78391c51483aef82300f0a4a3eaf2c6c66dfb0ffba5500000f97ba6d3d40d54cd2cabb69baf9fea0e2e23e263b9e0c17c360fc935167aa5fa01"],
    "dataInputsRaw": []
}
Submit this transaction via a POST request as described below.

#### Broadcasting Transactions
To broadcast a transaction made outside the node, serialize it into JSON. In Java:
java
Json json = JsonCodecsWrapper.ergoLikeTransactionEncoder().apply(tx);
System.out.println(json.toString());
Send this JSON via a POST request to the public Explorer:
bash
curl -X POST "https://api.ergoplatform.com/api/v0/transactions/send" \
-H "Content-Type: application/json" \
-d '{...}'
Or to your private Explorer or a node with open API (POST to http://{node_ip}:9053/transactions):
bash
curl -X POST "http://{node_ip}:9053/transactions" \
-H "Content-Type: application/json" \
-d '{...}'
This ensures that the transaction is properly submitted to the Ergo network for confirmation.

#### Determining Failed Transactions in UTXO Mode:
Malformed transactions:
Simple transactions should produce an explicit error when signing and/or broadcasting such as:
Failed to sign boxes due to Estimated execution cost 1001580 exceeds the limit 1000000: Vector(ErgoBox(0275eb3a125bc02fe997cb98c0de8131bd9b2e4617110d
This error can occur due to too many inputs collected in a transaction for dusty wallets.
Valid RBF transactions:
Dropped transactions will be removed from the mempool, this can be checked with the /transactions/unconfirmed/{txId} endpoint

#### Dust Collection
Collect dust from miners' deposits periodically to prevent small UTXOs from accumulating.
Ergo's extended-UTXO model can lead to dust - fractional ERG values usually below the protocol fee. Miner wallets are prone to becoming dusty due to the stream of rewards. Excess UTXOs can slow down and impact node functionality. This is important for exchanges receiving mining traffic. Collect dust aggressively, as new dust arrives constantly for miners.
Node-specific settings to address this:
Get UTXOs from /wallet/boxes/unspent with min confirmations
Get their ids and total sum
Get binary representations of UTXOs via /utxo/byIdBinary/{boxId}
Construct the payment transaction:
JSON
{
  "requests": [
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "value": 10000000000
    }
  ],
  "fee": 1000000,
  "inputsRaw": [
    "utxo1", "utxo2"
  ],
  "dataInputsRaw": [
  ]
}
Post to /wallet/transaction/send.
Set value and fee such that value + fee = total sum of UTXOs.
Query with specific parameters:
bash
curl -X GET "http://127.0.0.1:9053/wallet/boxes/unspent?minConfirmations=10&minInclusionHeight=0" -H  "accept: application/json" -H  "api_key: hello"
Another simple way to collect dust is to set:
conf
ergo {
 wallet {
   maxInputs = 300 
   optimalInputs = 100
 }
}
And send 1 ERG to the change address. The node will attach 100 dust inputs (send any large change amounts to the change address as well).

##### Failed to sign boxes
This error can occur due to too many inputs collected in a transaction for dusty wallets:
bash
Failed to sign boxes due to Estimated execution cost 1001580 exceeds the limit 1000000: Vector(ErgoBox(0275eb3a125bc02fe997cb98c0de8131bd9b2e4617110d

#### Native Assets
For large airdrops, users may mistakenly put exchange addresses to receive native assets. An auto-burn method will be in future node versions to reduce manual effort. See this Issue for more information.
Send this request via /wallet/payment/send, replacing tokenId with the IDs of the spamming tokens:
JSON
[
  {
    "address": "4MQyMKvMbnCJG3aJ",
    "value": 100000000,
    "assets": [
      {"tokenId":"e55adbda4e42f2bd21b1cb9498c105ff3bc1069012942d6158412f55759369c3","amount":1},
      {"tokenId":"6dd3e0ac4edd9702094aa4e3cad7c0c73d5437292c11805adf5d5068312748b4","amount":1}
    ]
  }
]
There is no central token registry. Use community resources like supported tokens in the ergotipper bot and spectrum-finance/ergo-token-list.

#### Frequently Asked Questions
Can P2S and P2SH be two address formats for the same script?
Yes. For P2S, the script is serialized directly into the address. For P2SH, the address contains only a hash of the serialized script.
Are there issues with supporting address types other than P2PK?
Supporting other types isn't a problem if the user is aware of what they're doing, but this is often not the case and can introduce complexity. P2S addresses can't validate input size in forms.
How are ergoTree and address related for conversions?
In appkit, Address.create() accepts an address string and returns an object from which you can obtain the ergoTree.
Transaction Fees
Ergo's transaction fee system is designed to be flexible and explicit. Although the protocol does not enforce a specific minimum transaction fee, it employs a spam-prevention strategy that requires each box to contain a minimum amount of ERG based on its size. This minimum value is determined by a parameter voted on by miners.
As a guideline, it is suggested to allocate 0.001 ERG (1,000,000 NanoErg) for each box involved in the transaction. Including a fee incentivizes miners to process your transaction more quickly.
Miners prioritize transactions based on either the fee per byte or the validation cost unit, which are adjustable via a voting mechanism among miners. Transaction fees are collected in a specific contract that can only be spent through a miner's script.
To determine the appropriate transaction fee, consider the protocol's minimum requirements based on the box size and the network's current hashrate. Higher hashrates reduce the risk of double-spend attacks, thus requiring fewer confirmations.
For more detailed information on transaction fees, including minimum values, miner prioritization, fee collection, and related topics, please refer to the dedicated Transaction Fees page.
What algorithm generates a boxid?
The boxid is generated by hashing the box contents.
See the code in AppKit for details
A box's bytes are unique becau...

#### Frequently Asked Questions
What is the difference between the value field and assets array in a box?
Each box always has an ERG value in the value field. Assets are optional and are represented in the assets array. A box can contain a combination of ERG and tokens.
What is the difference between inclusionHeight and creationHeight?
Creation height is when the transaction was built, but it's not reliable since the person building the transaction can input a number <= current block height. Inclusion height is the block number where the transaction was first included (first confirmation).
How can I get the block number of the first transaction confirmation?
Call /blocks/{blockId}/header to get the block height. The height in the header defines the block number in which the transactions from that block received their first confirmation.
Is the numConfirmations value returned by /blockchain/transaction/byId/{txId} the number of transaction confirmations?
Yes, it is.
What is considered a safe number of confirmations?
A common practice is to use 10 confirmations for deposits, which takes about 20 minutes. Ergo doesn't have many forking events due to the relatively long block time.
What's the difference between /wallet/balances and /wallet/balances/withUnconfirmed endpoints?
/balances returns the balance excluding current unconfirmed transactions in the mempool. /balances/withUnconfirmed accounts for transactions in the mempool, returning the confirmed balance plus (or minus) unconfirmed transactions.
Which endpoint should be used to get the balance before sending a transaction?
When working with chained transactions, it's better to use /balances/withUnconfirmed to get the balance before sending a transaction, as it reflects the "new wallet balance" after sending the previous transaction.
