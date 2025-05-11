# Overview - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/debugging/](https://docs.ergoplatform.com/dev/scs/debugging/)
Generated: 2025-05-11

## Summary
Debugging smart contracts written in ErgoScript presents unique challenges compared to traditional software development. Since the code executes within the constrained and deterministic environment of the blockchain, standard interactive debuggers or extensive logging are often not available during on-chain execution. This guide provides an overview of debugging strategies, linking to more detailed explanations of specific techniques. Given the limitations of on-chain debugging, a strong emphasis must be placed on off-chain testing and careful design: Thorough Unit & Integration Testing: This is the most crucial aspect. Use testing frameworks provided by SDKs like Appkit (Scala), Fleet SDK (JS/TS), or Sigma-Rust to simulate transaction scenarios off-chain.

## Keywords
contract, ergoscript, challenge, software, development, code, environment, blockchain, debugger, logging, chain, execution, guide, overview, strategy, explanation, technique, limitation, debugging, emphasis

## Content
## Debugging ErgoScript#
Debugging smart contracts written in ErgoScript presents unique challenges compared to traditional software development. Since the code executes within the constrained and deterministic environment of the blockchain, standard interactive debuggers or extensive logging are often not available during on-chain execution.
This guide provides an overview of debugging strategies, linking to more detailed explanations of specific techniques.

### Core Principles & Best Practices#
Given the limitations of on-chain debugging, a strong emphasis must be placed on off-chain testing and careful design:
Thorough Unit & Integration Testing: This is the most crucial aspect. Use testing frameworks provided by SDKs like Appkit (Scala), Fleet SDK (JS/TS), or Sigma-Rust to simulate transaction scenarios off-chain.

Cover expected behavior (happy paths).
Test edge cases and potential failure conditions.
Verify expected outputs, register values, and created boxes.
Test logic under various simulated context states.
Use property-based testing where applicable.



Careful Logic Design:

Prioritize simplicity.
Break down complex logic.
Reason carefully about execution paths and state transitions.
Consider economic exploits.



Code Reviews: Have peers review your contract logic.


Formal Verification (Advanced): Consider for highly critical contracts (tooling is evolving).

### Debugging Techniques Overview#
Explore the following pages for details on specific techniques:
Scala-Based Debugging: Leverage Scala's debugging tools by testing your contract logic within the JVM environment (e.g., using Appkit or sigmastate-interpreter tests). This is often the most effective way to step through logic off-chain.
On-Chain Mechanisms (Limited): Understand the limited tools available for insights during on-chain execution, such as the experimental debug() function and analyzing transaction failure logs.
External Tools & Simulators: Utilize off-chain simulators (like the Spectrum Finance simulator) and other tools (SDK playgrounds, online editors) to test and analyze script behavior in controlled environments.

### Future Directions#
The community desires more advanced debugging tools, potentially including execution traces and enhanced simulators. As the ecosystem evolves, improved tools may emerge.
Rigorous off-chain testing remains the cornerstone of developing reliable ErgoScript contracts.

### Recommended Resources#
SigmaState Interpreter Repository
ErgoScript Language Overview
Ergo Developer Forum
