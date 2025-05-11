# Improved Signatures - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/sigma/improved-signatures/](https://docs.ergoplatform.com/dev/scs/sigma/improved-signatures/)
Generated: 2025-05-11

## Summary
The initial implementation of distributed signatures support in the Ergo node worked well in simple cases, and ZK Treasury was built on top of it. However, in complex scenarios, it exhibited some problems: These issues have been fixed with a new API introduced in the distributed-sigs branch. Now, all hints are tied to both input indexes and positions within the sigma tree after the script reduction phase (which considers the current context). Additionally, the API is now simpler to use. Let's walk through a new tutorial on collective signing using this improved API.

## Keywords
implementation, signature, support, ergo, node, case, treasury, scenario, problem, issue, branch, hint, input, index, position, sigma, tree, script, reduction, phase

## Content
## Improved Signatures
The initial implementation of distributed signatures support in the Ergo node worked well in simple cases, and ZK Treasury was built on top of it. However, in complex scenarios, it exhibited some problems:
Hints generated (such as commitments) were not tied to the position of a sub-expression within the overall sigma-expression. For example, for a statement like atLeast(2, Coll(pkAlice, pkBob, pkCharlie)) && (pkBob || pkDiana), the same commitment would be generated for Bob's public key (pkBob) in both parts of the expression. This is improper and insecure, as a signature could potentially reveal Bob's secret key because the same randomness would be used twice for different challenges in the Schnorr protocol.
Similarly, generated hints were not tied to specific transaction inputs.
These issues have been fixed with a new API introduced in the distributed-sigs branch. Now, all hints are tied to both input indexes and positions within the sigma tree after the script reduction phase (which considers the current context). Additionally, the API is now simpler to use.
Let's walk through a new tutorial on collective signing using this improved API. Similar to the previous tutorial, we first pay to a 2-out-of-3 spending script where the public keys are stored in registers:
{
  // Retrieve GroupElement pkA, pkB, and pkC from the register R4, R5, and R6 respectively.
  val pkA  = SELF.R4[GroupElement].get
  val pkB  = SELF.R5[GroupElement].get
  val pkC  = SELF.R6[GroupElement].get

  // Require at least two of the three provided public keys to be included in the spending transaction.
  atLeast(2, Coll(proveDlog(pkA), proveDlog(pkB), proveDlog(pkC)))
}
This code defines a script requiring signatures corresponding to at least two out of the three specified public keys (pkA, pkB, pkC) to spend the box. The public keys (as GroupElement values) are retrieved from registers R4, R5, and R6 of the box being spent (SELF). These are then converted into SigmaProp objects using proveDlog...
