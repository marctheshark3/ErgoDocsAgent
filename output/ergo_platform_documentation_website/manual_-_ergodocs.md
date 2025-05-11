# Manual - ErgoDocs
Source: [https://docs.ergoplatform.com/node/install/manual/](https://docs.ergoplatform.com/node/install/manual/)
Generated: 2025-05-11

## Summary
This guide covers the manual setup process for running an Ergo full node. For alternative methods, see Docker Setup or Running on Android. Create a Configuration File (ergo.conf): Launch Your Node: Wait for Initialization & Synchronization:

## Keywords
guide, setup, process, ergo, node, method, docker, android, configuration, file, launch, initialization, synchronization

## Content
## Ergo Full Node Installation Guide#
This guide covers the manual setup process for running an Ergo full node. For alternative methods, see Docker Setup or Running on Android.

#### Preparing Your Environment#
Create a Folder: Start by creating a dedicated folder for your Ergo node files (e.g., ergo in your home directory).
Obtain the Ergo Client JAR: You have two main options:
Download (Recommended): Visit the Ergo GitHub releases page and download the latest stable ergo-<version>.jar file. This is the simplest method for most users. Place the downloaded JAR file in your ergo folder.
Build from Source: If you need a specific version (like a Release Candidate) or want to contribute to development, you can compile the JAR yourself. This requires Git, JDK, and SBT.
See the detailed guide: Building the Ergo Node from Source
Note: Building development versions might require handling SNAPSHOT dependencies. Refer to the build guide and the specific SNAPSHOT Dependencies guide if you encounter issues.

#### Setting Up Your Node#
Create a Configuration File (ergo.conf):

In your ergo folder, create a text file named ergo.conf.
This file overrides default node settings. Only add settings you need to change.
Start with a basic configuration (adjust apiKeyHash later if needed):
    ergo {
    node {
        mining = false // Disable mining unless intended
    }
}
scorex {
    restApi {
        // Set a secure API key hash for API access
        // Example hash for password "hello":
        apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf" 
    }
}

For more configuration options, see the Configuration Files documentation.



Launch Your Node:

Open a terminal or command prompt in your ergo folder.
Run the node using the java -jar command, specifying the JAR file, network (--mainnet or --testnet), and configuration file (-c). Allocate sufficient memory using -Xmx.
    # Example for mainnet with 4GB RAM allocated
java -jar -Xmx4G ergo-<version>.jar --mainnet -c ergo.conf 

Adjust -Xmx4G based on your system's available RAM (e.g., -Xmx2G, -Xmx8G). More RAM generally improves performance, especially during sync.
Replace ergo-<version>.jar with the actual name of your downloaded or built JAR file.



Wait for Initialization & Synchronization:

The node will start up and begin synchronizing with the Ergo network. This process downloads and validates the blockchain history.
Synchronization can take a significant amount of time (hours to days) depending on your hardware, network speed, and the chosen Node Mode. Be patient.

### Verifying Node Synchronization#
Monitor via Web Panel: Open http://127.0.0.1:9053/panel (or port 9052 for testnet) in your web browser. During sync, it should show "Active synchronization" and increasing block height.
Check Sync Status: Once synchronization is complete, the panel will indicate "Node is synced." You can also check the /info endpoint (http://127.0.0.1:9053/info) and compare the reported fullHeight with a reliable public explorer like explorer.ergoplatform.com.

### Additional Resources#
Troubleshooting Guide
Node Configuration Files
Node Modes
Node API (Swagger)
Testnet Guide
Node FAQ
