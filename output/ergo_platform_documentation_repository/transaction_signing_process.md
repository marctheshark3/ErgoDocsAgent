# Transaction Signing Process
Source: docs/dev/protocol/tx/signing.md
Generated: 2025-05-11

## Summary
# Transaction Signing Process

To initiate a transaction, a spending transaction $tx$ is required as an input. This can be achieved by using $bytesToSign(tx)$. It's important to note that multiple inputs can be signed simultaneously, but the coins to be spent must be specified prior to signing. The current state of the blockchain, or $context$, is also required. The signer has the ability to extend the context by adding values. With this data, the signer (or prover) of an input begins by reducing the guarding proposition for the input box.

## Keywords
transaction, signing, process, spending, input, bytestosign(tx)$., coin, state, blockchain, context$, signer, ability, context, value, datum, prover, proposition, outcome, reduction, evaluation

## Content
## Transaction Signing Process
To initiate a transaction, a spending transaction $tx$ is required as an input. This can be achieved by using $bytesToSign(tx)$. It's important to note that multiple inputs can be signed simultaneously, but the coins to be spent must be specified prior to signing. The current state of the blockchain, or $context$, is also required. The signer has the ability to extend the context by adding values.
With this data, the signer (or prover) of an input begins by reducing the guarding proposition for the input box. This is done by evaluating it using the context. The possible outcomes of this reduction are as follows:
The process is aborted if the estimated upper-bound evaluation cost (and verification) is too high.
If the result is true, it means that the box can be spent by anyone.
If the result is false, it means that the box cannot be spent at all (according to the current context).
If the expression still contains predicates over the context, it means more than context is needed to evaluate some predicates over it. The prover can look into its own not yet revealed secrets to extend context. If the secrets are found, the prover evaluates the expression further and proceeds to the next step if there is nothing more to evaluate. Otherwise, the prover aborts.
If the expression contains only expressions over secret information provable via $\Sigma$-protocols, this is the most common case, and we will explain it further.
Complex expressions, such as $dlog(x_1) \lor (dlog(x2) /\ dlog(x3))$, where $dlog(x)$ means "prove me knowledge of a secret $w$, such as for a known group with generator $g$, $g^w = x$, via a non-interactive form of the Schnorr protocol", may be encountered. Internally, this expression is represented as a tree (TODO). This proof is to be proven and then serialized into a binary spending proof (which could be included in a transaction) as follows:
Steps for Proving a Tree:
Bottom-up: Each node, whether real or simulated, is marked according to the following...
