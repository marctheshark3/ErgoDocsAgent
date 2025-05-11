# Script Validation - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/ergotree/script-validation/](https://docs.ergoplatform.com/dev/scs/ergotree/script-validation/)
Generated: 2025-05-11

## Summary
For a transaction that has an INPUTS collection of boxes to spend, each input box can have a script (termed as the propositionBytes property) that protects it. This script needs to be executed within the context of the current transaction. To maintain steady block validation of 1000 transactions per second, a simple transaction with a single input box requires validation of 1000 scripts per second. To increase the probability of successful mining, the block validation time should be minimized. This allows a miner to start solving the PoW puzzle as soon as possible.

## Keywords
transaction, collection, input, script, propositionbytes, property, context, block, validation, second, probability, mining, time, miner, puzzle, step

## Content
## Efficient Script Validation#
For a transaction that has an INPUTS collection of boxes to spend, each input box can have a script (termed as the propositionBytes property) that protects it. This script needs to be executed within the context of the current transaction. To maintain steady block validation of 1000 transactions per second, a simple transaction with a single input box requires validation of 1000 scripts per second.
To increase the probability of successful mining, the block validation time should be minimized. This allows a miner to start solving the PoW puzzle as soon as possible.
To validate every script (of an input box), the following steps are performed:
A Context object is created with SELF = box.
ErgoTree is traversed to build a cost graph for cost estimation.
The cost estimation is computed by evaluating the cost graph with the current context.
If the cost is within the limit, the ErgoTree is evaluated using the context to obtain a sigma proposition (see SigmaProp).
The Sigma protocol verification procedure is executed.
