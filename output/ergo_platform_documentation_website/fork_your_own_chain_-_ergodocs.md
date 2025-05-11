# Fork your own chain - ErgoDocs
Source: [https://docs.ergoplatform.com/node/testnet/mine-your-own-chain/](https://docs.ergoplatform.com/node/testnet/mine-your-own-chain/)
Generated: 2025-05-11

## Summary
To start your custom Ergo chain, you need to modify the configuration to ensure it doesn't clash with the Ergo mainnet or public testnet. The key changes involve setting a unique addressPrefix and custom magicBytes. Hereâs an updated configuration for your testnet.conf file: Set Up the Configuration: Compile the Node: Run the Node: Initialize and Unlock the Wallet: For deeper modifications or any questions, you can join the community on: This setup ensures your custom chain runs independently and avoids conflicts with existing networks.

## Keywords
custom, ergo, chain, configuration, mainnet, testnet, change, addressprefix, magicbytes, file, compile, node, initialize, unlock, wallet, modification, question, community, setup, conflict

## Content
#### Configuration#
To start your custom Ergo chain, you need to modify the configuration to ensure it doesn't clash with the Ergo mainnet or public testnet. The key changes involve setting a unique addressPrefix and custom magicBytes.
Hereâs an updated configuration for your testnet.conf file:
ergo {
  networkType = "testnet"

  node {
    mining = true
    offlineGeneration = true
    useExternalMiner = false
  }

  chain {
    addressPrefix = 32 #  to avoid address clashing with Ergo mainnet and public testnet
  }
}

scorex {
  network {
    magicBytes = [2, 0, 4, 8] # custom value to avoid connections with other networks
    bindAddress = "0.0.0.0:9022"
    nodeName = "ergo-testnet-5"
    #knownPeers = []
  }

  restApi {
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
  }
}

#### Steps to Run the Node#
Set Up the Configuration:

Make sure your testnet.conf file is configured as shown above. This will help prevent address clashes with the mainnet and public testnet by using a custom addressPrefix and magicBytes.



Compile the Node:

Use the following command to compile the Ergo node:
  sbt assembly

This will generate an ergo.jar file at /target/scala*/ergo-*.jar.



Run the Node:

Start the node using the command:
  java -jar -Xmx4G ergo-*.jar --testnet -c testnet.conf




Initialize and Unlock the Wallet:

Access the panel at 127.0.0.1:9052/panel to initialize and unlock your wallet. This is necessary as the first blocks will be generated using Autolykos v1.

#### Additional Support#
For deeper modifications or any questions, you can join the community on:
Telegram: Ergo Developers Chat
Discord: Ergo Platform Developers Channel
This setup ensures your custom chain runs independently and avoids conflicts with existing networks.
