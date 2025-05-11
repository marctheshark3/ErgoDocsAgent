# Handling SNAPSHOT Dependencies When Building Ergo Node
Source: docs/node/install/snapshot-dependencies.md
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
  - SNAPSHOT
  - Dependencies
  - Troubleshooting
---

# Handling SNAPSHOT Dependencies When Building Ergo Node

When [building the Ergo node from source](build-from-source.md), especially when working with development branches or Release Candidates (RCs), you might encounter build failures related to `SNAPSHOT` dependencies. ## The Problem

* **What are SNAPSHOTs?* * SNAPSHOT versions represent unstable, work-in-progress builds of libraries (like `sigmastate-interpreter`, `scorex-util`, etc.)

## Keywords
node, installation, build, source, code, development, release, candidate, snapshot, dependencies, troubleshooting, handle, dependency, building, ergo, branch, candidates, failure, problem, version

## Content
## Handling SNAPSHOT Dependencies When Building Ergo Node
When building the Ergo node from source, especially when working with development branches or Release Candidates (RCs), you might encounter build failures related to SNAPSHOT dependencies.

### The Problem
What are SNAPSHOTs? SNAPSHOT versions represent unstable, work-in-progress builds of libraries (like sigmastate-interpreter, scorex-util, etc.) that are not yet officially released.
Why they cause issues: The standard build process (sbt assembly) tries to download dependencies from remote repositories (like Maven Central). SNAPSHOT versions are typically not published to these public repositories.
Error Message: If the Ergo node version you are trying to build depends on a SNAPSHOT version (e.g., 6.0.0-RC2-SNAPSHOT) that isn't available remotely or locally, the build will fail with errors indicating unresolved dependencies or artifacts not found.

### The Solution: sbt publishLocal
To resolve this, you need to manually build the required SNAPSHOT dependency yourself and publish it to your local SBT repository (usually located at ~/.ivy2/local on Linux/macOS or %USERPROFILE%\.ivy2\local on Windows). The Ergo node build process can then find the dependency locally.

### Steps
Identify the Required SNAPSHOT Dependency:

Check the build.sbt file in the root of the Ergo node source code (for the specific tag or branch you checked out, e.g., v6.0.0-RC2).
Look for lines defining versions for core libraries, like:
    scala
    val sigmastateVersion = "6.0.0-RC2-SNAPSHOT" 
    // or similar for scorexVersion, etc.
Note the exact SNAPSHOT version string (e.g., "6.0.0-RC2-SNAPSHOT") and the corresponding library's repository URL (usually found nearby in build.sbt or in the project's main README/documentation). For sigmastate-interpreter, it's typically https://github.com/ergoplatform/sigmastate-interpreter.git.
Important: Sometimes, specific Release Notes or developer announcements for an RC will specify the exact commit hash within the dependency's repository that corresponds to the required SNAPSHOT. Using the correct commit hash is crucial for compatibility. If unsure, check release notes or ask in developer channels.



Clone the Dependency Repository:

Clone the repository of the required library:
    bash
    # Example for sigmastate-interpreter
    git clone https://github.com/ergoplatform/sigmastate-interpreter.git



Navigate and Checkout the Correct Commit/Branch:

Change into the cloned dependency's directory:
    bash
    cd sigmastate-interpreter

Check out the specific commit hash or branch corresponding to the required SNAPSHOT version identified in Step 1.
    ```bash
    # Example using a specific commit hash
    git checkout  
Or, if a specific branch is indicated (less common for SNAPSHOTs)
git checkout 
```




Publish Locally:

Run the sbt publishLocal command within the dependency's directory. This compiles the library and installs the SNAPSHOT version into your local Ivy repository.
    bash
    sbt publishLocal
Wait for the process to complete successfully.



Return and Build Ergo Node:

Navigate back to the main Ergo node source directory:
    bash
    cd ../ergo
Now, run the Ergo node build command again:
    bash
    ...

## git checkout
```
