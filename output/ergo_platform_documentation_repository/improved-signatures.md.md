# improved-signatures.md
Source: docs/dev/scs/sigma/improved-signatures.md
Generated: 2025-05-11

## Summary
The initial implementation of distributed signatures support in the Ergo node worked well in simple cases, and ZK Treasury was built on top of it. However, in complex scenarios, it exhibited some problems:

*   Hints generated (such as commitments) were not tied to the position of a sub-expression within the overall sigma-expression. For example, for a statement like `atLeast(2, Coll(pkAlice, pkBob, pkCharlie)) && (pkBob || pkDiana)`, the same commitment would be generated for Bob's public key (`pkBob`) in both parts of the expression. This is improper and insecure, as a signature could potentially reveal Bob's secret key because the same randomness would be used twice for different challenges in the Schnorr protocol. *   Similarly, generated hints were not tied to specific transaction inputs.

## Keywords
implementation, signature, support, ergo, node, case, treasury, scenario, problem, hints, commitment, position, expression, sigma, example, statement, atleast(2, coll(pkalice, pkbob, pkcharlie

## Content