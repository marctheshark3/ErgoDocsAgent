# Build from Source - ErgoDocs
Source: [https://docs.ergoplatform.com/node/install/build-from-source/](https://docs.ergoplatform.com/node/install/build-from-source/)
Generated: 2025-05-11

## Summary
While downloading the pre-compiled JAR from the Ergo GitHub releases page is recommended for most users, you might need to build the node from source if you: You can also build and run the node using Docker. See the Docker setup guide for instructions. After successfully building the JAR, proceed with Setting Up Your Node as described in the main manual installation guide.

## Keywords
ergo, github, release, page, user, node, source, docker, setup, guide, instruction, installation

## Content
## Building the Ergo Node from Source#
While downloading the pre-compiled JAR from the Ergo GitHub releases page is recommended for most users, you might need to build the node from source if you:
Need a specific version not available as a pre-compiled JAR (e.g., a specific development commit or Release Candidate).
Want to contribute to Ergo node development.
Prefer compiling the software yourself.

### Prerequisites#
Git: Install Git if you don't have it.
Java Development Kit (JDK): A compatible JDK is required (typically JDK 9 or higher). Check the specific version recommendations in the main Ergo repository README. OpenJDK is recommended.
SBT (Scala Build Tool): Install SBT.

### Build Steps#
Clone Repository:
git clone https://github.com/ergoplatform/ergo.git

Navigate to Directory:
cd ergo

Checkout Specific Version (Optional):
To build the absolute latest development code (potentially unstable), stay on the default branch (master).
To build a specific release or release candidate (RC), check out the corresponding tag using git checkout <tag_name>. Find tags on the releases page.
    # Example for a specific release
git checkout v5.0.10 

# Example for a Release Candidate
git checkout v6.0.0-RC2 



Handle SNAPSHOT Dependencies (If Applicable):
Some development versions, especially Release Candidates, may depend on unreleased SNAPSHOT versions of libraries (like sigmastate-interpreter). If the next step fails due to missing SNAPSHOT dependencies, you must build and publish these dependencies locally first.
See the dedicated guide: Handling SNAPSHOT Dependencies


Compile the JAR:
Run the SBT assembly task. This compiles the code and packages the node and all its dependencies into a single executable JAR file.
    sbt assembly

The resulting JAR file will be located in the target/scala-*/ directory within the ergo project folder (e.g., target/scala-2.13/ergo-*.jar). The exact name will include the version number.


Locate the JAR: Find the generated ergo-*.jar file in the target/scala-*/ directory. You can now move this JAR file to your desired node installation folder (e.g., the ergo folder created in the Manual Setup guide).

### Alternative: Docker Build#
You can also build and run the node using Docker. See the Docker setup guide for instructions.
After successfully building the JAR, proceed with Setting Up Your Node as described in the main manual installation guide.
