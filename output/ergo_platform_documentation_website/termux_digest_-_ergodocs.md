# Termux (Digest) - ErgoDocs
Source: [https://docs.ergoplatform.com/node/install/node-android/termux-digest/](https://docs.ergoplatform.com/node/install/node-android/termux-digest/)
Generated: 2025-05-11

## Summary
This guide details the recommended method for running an Ergo node on Android using Termux directly. This approach is best suited for the resource-efficient stateType="digest" mode. Prerequisites: Steps: Refer back to the main Android guide for general tips, disk space clarification, and troubleshooting.

## Keywords
guide, method, ergo, node, android, termux, approach, resource, mode, prerequisite, step, disk, space, clarification, troubleshooting

## Content
## Android Node: Direct Termux Setup (Digest Mode)#
This guide details the recommended method for running an Ergo node on Android using Termux directly. This approach is best suited for the resource-efficient stateType="digest" mode.
Prerequisites:
Android device meeting the requirements.
Termux installed from F-Droid (see main Android guide).
Steps:
Update Termux Packages:
Open Termux and run:
    pkg update && pkg upgrade -y

Answer default prompts if asked.


Install Dependencies:
Install Java (OpenJDK 17 recommended) and wget:
    pkg install openjdk-17 wget -y



Download Ergo Node JAR:
For stateType="digest", the standard Ergo node JAR (without -rocksdb suffix) is usually sufficient.
Use wget to download the latest release:
    # Get the URL for the latest standard JAR
LATEST_JAR_URL=$(wget -qO- "https://api.github.com/repos/ergoplatform/ergo/releases/latest" | grep -o 'https://github.com/ergoplatform/ergo/releases/download/.*ergo-[0-9.]*\.jar' | head -n 1)

# Download it
echo "Downloading latest Ergo node JAR from: $LATEST_JAR_URL"
wget -q --show-progress "$LATEST_JAR_URL" -O ergo.jar

(Verify the downloaded URL or manually find the correct URL on the Ergo Releases page if the script fails).


Create Configuration File (ergo.conf):
Create the file using nano:
    nano ergo.conf

Paste the following configuration, suitable for mobile digest mode:
    ergo {
  node {
    stateType = "digest"
    blocksToKeep = 1440 // Keep ~1 day of full blocks (~500MB-1GB), adjust if needed
    mining = false

    # Enable faster bootstrapping (both recommended for flexibility)
    nipopow.nipopowBootstrap = true
    utxoBootstrap = true

    # Optional: Adjust NiPoPoW parameters if using nipopowBootstrap
    # nipopow.p2pNipopows = 2
  }
}

scorex {
  restApi {
    # Set your desired API key hash (generate one if needed)
    # Example hash for password "hello":
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
  }
  network {
    # Optional: Add known reliable peers if discovery is slow
    # ...
