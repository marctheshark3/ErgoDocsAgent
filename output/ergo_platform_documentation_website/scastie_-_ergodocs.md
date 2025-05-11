# Scastie - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/ergoscript/scastie/](https://docs.ergoplatform.com/dev/scs/ergoscript/scastie/)
Generated: 2025-05-11

## Summary
Scastie is an online compiler for the Scala programming language. It's an ideal environment for developers looking to experiment, share, or learn Scala. In this document, we will discuss how to use Scastie for Ergo blockchain development, allowing developers to write, compile, and experiment with Ergo contracts in a fast and easy-to-use online environment. You can see an example here Before we begin, we need to import the necessary packages to interact with the Ergo Blockchain environment. To do this, enter the following lines at the top of your Scastie workspace: With these imports, you gain access to the ErgoScalaCompiler, which compiles Ergo smart contracts written in ErgoScript, and the Playground package, which provides convenient classes and methods for Ergo blockchain simulation.

## Keywords
scastie, compiler, scala, programming, language, environment, developer, experiment, share, document, ergo, blockchain, development, compile, contract, example, package, line, workspace, import

## Content
### Introduction#
Scastie is an online compiler for the Scala programming language. It's an ideal environment for developers looking to experiment, share, or learn Scala. In this document, we will discuss how to use Scastie for Ergo blockchain development, allowing developers to write, compile, and experiment with Ergo contracts in a fast and easy-to-use online environment.
You can see an example here

### Setup#
Before we begin, we need to import the necessary packages to interact with the Ergo Blockchain environment. To do this, enter the following lines at the top of your Scastie workspace:
import org.ergoplatform.compiler.ErgoScalaCompiler._
import org.ergoplatform.playground._
With these imports, you gain access to the ErgoScalaCompiler, which compiles Ergo smart contracts written in ErgoScript, and the Playground package, which provides convenient classes and methods for Ergo blockchain simulation.

### Creating a Blockchain Simulation#
In order to simulate and test the interactions of your smart contract with the Ergo blockchain, we create a new blockchain simulation instance as follows:
val blockchainSim = newBlockChainSimulation
newBlockChainSimulation creates a simulated Ergo blockchain environment. This allows for testing and debugging contracts without real-world implications.

### Creating a Transaction Builder#
To create transactions within your simulated blockchain, we need a transaction builder. We instantiate one as follows:
val txBuilder = newTransactionBuilder(blockchainSim.ctx)
The newTransactionBuilder method creates a new instance of a transaction builder using the current blockchain context. This allows us to create transactions in our simulation.
The Ergo Scala Playground, combined with Scastie's online environment, is a powerful tool for developing and testing Ergo smart contracts. Remember to always test your contracts thoroughly before deploying them on the real Ergo network. Happy coding!
