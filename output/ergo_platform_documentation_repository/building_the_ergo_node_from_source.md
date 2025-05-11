# Building the Ergo Node from Source
Source: docs/node/install/build-from-source.md
Generated: 2025-05-11

## Summary
---
tags:
  - Node
  - Installation
  - Build
  - Source Code
  - SBT
  - Development
  - Release Candidate
---

# Building the Ergo Node from Source

While downloading the pre-compiled JAR from the [Ergo GitHub releases page](https://github.com/ergoplatform/ergo/releases/) is recommended for most users, you might need to build the node from source if you:

*   Need a specific version not available as a pre-compiled JAR (e.g., a specific development commit or Release Candidate). *   Want to contribute to Ergo node development. *   Prefer compiling the software yourself. ## Prerequisites

*   **Git:** [Install Git](https://git-scm.com/downloads) if you don't have it.

## Keywords
node, installation, build, source, code, development, release, candidate, ergo, github, page](https://github.com, ergoplatform, user, version, commit, prefer, software, prerequisite, install, git](https://git

## Content
## Building the Ergo Node from Source
While downloading the pre-compiled JAR from the Ergo GitHub releases page is recommended for most users, you might need to build the node from source if you:
Need a specific version not available as a pre-compiled JAR (e.g., a specific development commit or Release Candidate).
Want to contribute to Ergo node development.
Prefer compiling the software yourself.

### Prerequisites
Git: Install Git if you don't have it.
Java Development Kit (JDK): A compatible JDK is required (typically JDK 9 or higher). Check the specific version recommendations in the main Ergo repository README. OpenJDK is recommended.
SBT (Scala Build Tool): Install SBT.

### Build Steps
Clone Repository:
bash
    git clone https://github.com/ergoplatform/ergo.git
Navigate to Directory:
bash
    cd ergo
Checkout Specific Version (Optional):
To build the absolute latest development code (potentially unstable), stay on the default branch (master).

To build a specific release or release candidate (RC), check out the corresponding tag using git checkout <tag_name>. Find tags on the releases page.
    ```bash
    # Example for a specific release
    git checkout v5.0.10 
Example for a Release Candidate
git checkout v6.0.0-RC2 
4.  **Handle SNAPSHOT Dependencies (If Applicable):**
    *   Some development versions, especially **Release Candidates**, may depend on unreleased `SNAPSHOT` versions of libraries (like `sigmastate-interpreter`). If the next step fails due to missing SNAPSHOT dependencies, you **must** build and publish these dependencies locally first.
    *   **See the dedicated guide: [Handling SNAPSHOT Dependencies](snapshot-dependencies.md)**
5.  **Compile the JAR:**
    *   Run the SBT `assembly` task. This compiles the code and packages the node and all its dependencies into a single executable JAR file.bash
sbt assembly
``
    *   The resulting JAR file will be located in thetarget/scala-/directory within theergoproject folder (e.g.,target/scala-2.13/ergo-.jar). The exact name will include the version number.
6.  **Locate the JAR:** Find the generatedergo-.jarfile in thetarget/scala-/directory. You can now move this JAR file to your desired node installation folder (e.g., theergo` folder created in the Manual Setup guide).
You can also build and run the node using Docker. See the Docker setup guide for instructions.
After successfully building the JAR, proceed with Setting Up Your Node as described in the main manual installation guide.

## Example for a Release Candidate
git checkout v6.0.0-RC2 
4.  **Handle SNAPSHOT Dependencies (If Applicable):**
    *   Some development versions, especially **Release Candidates**, may depend on unreleased `SNAPSHOT` versions of libraries (like `sigmastate-interpreter`). If the next step fails due to missing SNAPSHOT dependencies, you **must** build and publish these dependencies locally first.
    *   **See the dedicated guide: [Handling SNAPSHOT Dependencies](snapshot-dependencies.md)**
5.  **Compile the JAR:**
    *   Run the SBT `assembly` task. This compiles the code and packages the node and all its dependencies into a single executable JAR file.bash
sbt assembly
``
    *   The resulting JAR file will be located in thetarget/scala-/directory within theergoproject folder (e.g.,target/scala-2.13/ergo-.jar). The exact name will include the version number.
6.  **Locate the JAR:** Find the generatedergo-.jarfile in thetarget/scala-/directory. You can now move this JAR file to your desired node installation folder (e.g., theergo` folder created in the Manual Setup guide).

### Alternative: Docker Build
You can also build and run the node using Docker. See the Docker setup guide for instructions.
After successfully building the JAR, proceed with Setting Up Your Node as described in the main manual installation guide.
