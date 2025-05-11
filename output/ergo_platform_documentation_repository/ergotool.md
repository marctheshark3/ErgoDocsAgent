# ErgoTool
Source: docs/dev/stack/ergotool.md
Generated: 2025-05-11

## Summary
# ErgoTool


## Introduction

[ErgoTool](https://github.com/aslesarenko/ergo-tool) is a command-line interface (CLI) for [Ergo blockchain](https://ergoplatform.org/). You can use ErgoTool without running your own Ergo node. However, running a node is the most secure way to communicate with the blockchain. In this post, we will walk through simple steps to generate a mnemonic phrase, create a local secret storage and use it to send ERGs between addresses, all with the help of ErgoTool commands. ## Getting Started

First, we need to install ErgoTool on our system from sources by following the [installation instructions](https://github.com/aslesarenko/ergo-tool#installation).

## Keywords
ergotool, introduction, ergo, tool, command, line, interface, blockchain](https://ergoplatform.org/, node, blockchain, post, step, phrase, storage, address, help, system, source, installation, tool#installation

## Content
### Introduction
ErgoTool is a command-line interface (CLI) for Ergo blockchain. You can use ErgoTool without running your own Ergo node. However, running a node is the most secure way to communicate with the blockchain.
In this post, we will walk through simple steps to generate a mnemonic phrase, create a local secret storage and use it to send ERGs between addresses, all with the help of ErgoTool commands.

### Getting Started
First, we need to install ErgoTool on our system from sources by following the installation instructions. In the directory where we cloned ErgoTool, there is the ergo-tool.sh script we will use to run commands. Run the following command to check that ErgoTool is installed correctly.
```bash
$ ./ergo-tool.sh help   
the command name is not specified (run ergo-tool without arguments to list commands)
Command Name: help
Usage Syntax: ergo-tool help 
Description:  prints usage help for a command
Doc page: https://aslesarenko.github.io/ergo-tool/api/org/ergoplatform/appkit/ergotool/HelpCmd.html
```
Let's see what we get here. ErgoTool outputs the error message with the information about the help command. This is a typical output of ErgoTool when one of the known commands is specified but used incorrectly. As we can learn from the message, the help. the command requires us to specify an additional <commandName> argument. Also, each command has an API doc page with all the details about command execution, so its URL is shown here.

### Create a New Mnemonic Phrase
A Mnemonic is a random sequence of characters that is used to generate a master key according to Hierarchical Deterministic Wallets specification. For random convenience sequence of English words is used, but this is not required. Run the following command to generate a new mnemonic phrase:
bash
$ ./ergo-tool.sh mnemonic          
bird harbor wheat innocent business disease busy quick yellow trust time oil enter situate moon
Please write it down on paper and keep it in a safe and secret place. As an additional security measure, you can create a random mnemonic password. In some sense, it can serve as another non-vocabulary word in the mnemonic. A mnemonic password is optional and is used for additional security. If you decide to use a mnemonic password, you should also write it down and keep it a secret, probably different from a mnemonic one.
Important, both mnemonic phrases and mnemonic passwords are required to restore secret keys, if you lose any of them, then you will not be able to regenerate your master key again.
Next, use the generated Mnemonic to create storage with a master secret key.

### Create a New Encrypted Storage
For better security, neither a mnemonic phrase nor password is required by ErgoTool to perform the transaction signing. Instead, the secret key from the encrypted storage is required to sign a spending transaction. We can generate a secret key and store it in encrypted storage using the createStorage command.
```bash
$ ./ergo-tool.sh help createStorage
Command Name: createStorage
Usage Syntax: ergo-tool createStorage [="storage"] [="secret.json"]
Description:  Creates an encrypted storage file for the Mnemonic entered by the user
Doc page:       https://aslesarenko.github.io/ergo-tool/api/org/ergoplatform/appkit/ergotool/CreateStorageCmd.html
$ ./ergo-tool.sh createStorage 
Enter mnemonic phrase> bird harbor wheat innocent business disease busy quick yellow trust time oil enter situate moon
Mnemonic password> 
Repeat mnemonic password> 
Storage password> 
Repeat storage password> 
Storage File: storage/secret.json
```
A master secret key is generated from the (mnemonic phrase, mnemonic password) pair and saved encrypted in the storage/secret.json file. The Mnemonic itself is not stored in the file, and there is no way to restore it from the file, even if you know the passwords.
Please enter the correct mnemonic password, the one you chose and saved before.
Since a mnemonic password is optional, you can leave it empty by pressing enter.
If you forget the storage password (aka encryption password), you will not be able to use that storage file anymore; however, you can always restore your secret keys from (Mnemonic the phrase, mnemonic password) pair and thus create a new storage file with a new password.
Keep your storage file and storage password in secret; anyone who obtains both your storage file and storage password will be able to decipher it and access secret keys.

### Extracting Data From Storage
Secret storage contains a master secret key and can be used to compute both the public key and the pay-to-public-key address corresponding to that secret key. The extractStorage command is doing just that.
```bash
$ ./ergo-tool.sh help extractStorage
Command Name: extractStorage
Usage Syntax: ergo-tool extractStorage  address|masterKey|publicKey|secretKey mainnet|testnet
Description:  Reads the file, unlocks it using a password and extracts the requested property from the given storage file.
Doc page: https://aslesarenko.github.io/ergo-tool/api/org/ergoplatform/appkit/ergotool/ExtractStorageCmd.html
$ ./ergo-tool.sh extractStorage storage/secret.json address mainnet   
Storage password> 
9iHiSAg3ko2ZGxR2vhc1Aem3tShqfzEPDAF7XK5cdtbZ3Ut2CCf
```
Here the command transforms the secret key to the corresponding public key and then creates the pay-to-public-key address on the mainnet.
In the same way, we can obtain the public key, private key and other data from the storage.
```bash
$ ./ergo-tool.sh extractStorage storage/secret.json secretKey mainnet
Storage password> 
55dfde63c9b6b4f47683592e85ee997ba2e93507f38ba3f9c82933bcfbc677ca
$ ./ergo-tool.sh extractStorage storage/secret.json publicKey mainnet
Storage password> 
03f07aecb145a85920bf6e9be80efe5f1cd1a165b45ad3aa8e5c4ca3ba50856bb8
```

### Listing Unspent Boxes
ErgoTool has the special command to list all available (aka unspent) boxes for a given address.
bash
$ ./ergo-tool.sh listAddressBoxes 9f4QF8AD1nQ3nJahQVkMj8hFSVVzVom77b52JU7EW71Zexg6N8v                                                                
BoxId                                                             NanoERGs          
4840cb6facc20b765085db0ad24768ed0c5e7afd413e8e58e597c33a993f8119  4987000000
if we specify the --print-json option, then ErgoTool will output all the boxes in JSON format
bash
$ ./ergo-tool.sh listAddressBoxes --print-json 9f4QF8AD1nQ3nJahQVkMj8hFSVVzVom77b52JU7EW71Zexg6N8v
[{"boxId":"4840cb6facc20b765085db0ad24768ed0c5e7afd413e8e58e597c33a993f8119","value":4987000000,"ergoTree":"0008cd02472963123ce32c057907c7a7268bc09f45d9ca57819d3327b9e7497d7b1cc347","creationHeight":125646,"assets":[],"additionalRegisters":{},"transactionId":"820c688f4b9d709924ba0186ee930a7df374d8852920bc769fc1f1d0b313e5ab","index":2}]

### Transfer Coins
With a secret key stored securely in the encrypted storage file, we can use ErgoTool to
transfer coins from our address to some other recipient address. The command to do that is
send.
```bash
./ergo-tool.sh help send
Command Name: send
Usage Syntax: ergo-tool send   
Description:  send the given  to the given  using 
 the given  to sign transaction (requests storage password)
Doc page: https://aslesarenko.github.io/ergo-tool/api/org/ergoplatform/appkit/ergotool/SendCmd.html
``
The storage file is necessary to access the secret key and generate a signature. The ErgoTool will request a storage password to unlock and decipher the file content. The commandsendsupports the--dry-run` option, which forces ErgoTool to create the signed transaction, but instead of sending it to the blockchain, ErgoTool prints the transaction on the console.
bash
$ ./ergo-tool.sh send --dry-run storage/E1.json 9hHDQb26AjnJUXxcqriqY1mnhpLuUeC81C4pggtK7tupr92Ea1K 5000000
Storage password>
Creating prover... Ok
Loading unspent boxes from at address 9f4QF8AD1nQ3nJahQVkMj8hFSVVzVom77b52JU7EW71Zexg6N8v... Ok
Signing the transaction... Ok
Tx: {
  "id": "2633733a1d81b8fc747d984bdc36fac42cb52118b5057375b081b4c543c62b0e",
  "inputs": [
    {
      "boxId": "4840cb6facc20b765085db0ad24768ed0c5e7afd413e8e58e597c33a993f8119",
      "spendingProof": {
        "proofBytes": "060e7c99c9c9cecf89ec5c3e7b692075e0b3415318f8064c64f7f01401ac29c6637b44535151e51d43d4cd25e05ad459dbe33718a99a22dd",
        "extension": {}
      }
    }
  ],
  "dataInputs": [],
  "outputs": [
    {
      "boxId": "4eaed414ae763158126859bbf912fa9ffb9ea67ac13d81d473b1c81ec65b06fd",
      "value": 5000000,
      "ergoTree": "ErgoTree(0,WrappedArray(),Right(ConstantNode(SigmaProp(ProveDlog(ECPoint(6ba5cf,8ae5ac,...))),SSigmaProp)),80,[B@1117fff48)",
      "creationHeight": 130508,
      "assets": [],
      "additionalRegisters": {},
      "transactionId": "2633733a1d81b8fc747d984bdc36fac42cb52118b5057375b081b4c543c62b0e",
      "index": 0...

### Security Notes
ErgoTool is created with security in mind and tries its best to safeguard the usage of
sensitive information like mnemonic phrases (which are never stored persistently), 
passwords (which are never shown on the screen) etc. In addition, secret keys are never
stored on a local disk unencrypted and surely never sent anywhere.

### Conclusion
ErgoTool is designed to look and feel like a typical CLI utility:
which is easy to use and fast to run from the command line
can be scriptable via shell scripts
has built-in usage help
At the same time, ErgoTool is designed to be easily extensible:
implemented in high-level language Scala
reuses the core libraries which are used in the Ergo network client
open-sourced and fully documented
This last point is especially important as many new commands can be easily added to ErgoTool, thanks to its architecture. If you need a specific feature or a command,  please file an issue or maybe even a PR.

### References
Ergo Site
Ergo Sources
Ergo Appkit
Ergo Tool
