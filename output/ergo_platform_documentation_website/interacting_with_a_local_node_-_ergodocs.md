# Interacting with a local Node - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/stack/appkit/appkit-node/](https://docs.ergoplatform.com/dev/stack/appkit/appkit-node/)
Generated: 2025-05-11

## Summary
Among other things, the Appkit library allows us to communicate with Ergo nodes via the REST API. Let's see how we can write ErgoTool - a simple Java console application (similar to ergo-tool utility) which uses Appkit library. ErgoTool allows to create and send a new transaction to any existing Ergo node on the network which. A new node can also be started locally and thus available at http://localhost:9052/. Suppose we set up a full node and started it using the following command.

## Keywords
thing, appkit, library, ergo, node, rest, ergotool, java, console, application, tool, utility, transaction, network, http://localhost:9052/., suppose, command, configuration, parameter, file

## Content
## Interacting with a local node.#
Among other things, the Appkit library allows us to communicate with Ergo nodes via the REST API.
Let's see how we can write ErgoTool - a simple Java console application (similar to ergo-tool utility) which uses Appkit library.
ErgoTool allows to create and send a new transaction to any existing Ergo node on the network which. A new node can also be started locally and thus available at http://localhost:9052/.
Suppose we set up a full node and started it using the following command.
$ java -jar -Xmx4G target/scala-2.12/ergo-4.0.8.jar --testnet -c ergo-testnet.conf
We will need some configuration parameters which can be loaded from ergotool.json file
{
  "node": {
    "nodeApi": {
      "apiUrl": "http://139.59.29.87:9053",
      "apiKey": "82344a18c24adc42b78f52c58facfdf19c8cc38858a5f22e68070959499076e1"
    },
    "wallet": {
      "mnemonic": "slow silly start wash bundle suffer bulb ancient height spin express remind today effort helmet",
      "password": "",
      "mnemonicPassword": ""
    },
    "networkType": "MAINNET"
  },
  "parameters": {
    "newBoxSpendingDelay": "30"
  }
}
Here apiKey is the secret key required for API authentication which can be obtained as described here. And mnemonic is the secret phrase obtained during setup of a new wallet or if you don't want to set up your node using ergo-tool's mnemonic command.
Our example app also reads the amount of NanoErg to put into a new box from command line arguments
public static void main(String[] args) {
    long amountToPay = Long.parseLong(args[0]);
    ErgoToolConfig conf = ErgoToolConfig.load("ergotool.json");
    int newBoxSpendingDelay = Integer.parseInt(conf.getParameters().get("newBoxSpendingDelay"));
    // the rest of the code shown below 
    ...
}
Next, we connect to the running testnet node from our Java application by creating a ErgoClient instance.
ErgoNodeConfig nodeConf = conf.getNode();
ErgoClient ergoClient = RestApiErgoClient.create(nodeConf, null);
Using ErgoClient we can execut...
