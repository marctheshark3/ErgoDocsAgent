# Modifiers Validation - ErgoDocs
Source: [https://docs.ergoplatform.com/node/modifiers-validation/](https://docs.ergoplatform.com/node/modifiers-validation/)
Generated: 2025-05-11

## Summary
This section contains a list of all consensus-critical validation rules that every node in the network should perform; rules that are not listed in this table should not be considered consensus-critical and enforced by the network. Every rule is enumerated and is initially activated. Rules that could not lead to money printing and are not enforced by serialisers may be disabled later by a miner
voting via soft forks, while new rules may also be added at the same time. Transaction validation: Header validation: Block sections validation: Extension validation: Block application to state validation:

## Keywords
section, list, consensus, validation, rule, node, network, table, money, printing, serialiser, miner, voting, fork, time, transaction, header, block, extension, application

## Content
## Ergo Modifiers Validation#
This section contains a list of all consensus-critical validation rules that every node in the network should perform; rules that are not listed in this table should not be considered consensus-critical and enforced by the network.
Every rule is enumerated and is initially activated.
Rules that could not lead to money printing and are not enforced by serialisers may be disabled later by a miner
voting via soft forks, while new rules may also be added at the same time.
Transaction validation:
Id
Validation rule
Soft-forkable
Active
Modifiers




100
A transaction should have at least one input.
x
â
ErgoTransaction


101
A transaction should have at least one output.
x
â
ErgoTransaction


102
A number of transaction inputs should not exceed 32767.
x
â
ErgoTransaction


103
A number transaction data inputs should not exceed 32767.
x
â
ErgoTransaction


104
A number of transaction outputs should not exceed 32767.
x
â
ErgoTransaction


105
Erg amount for a transaction output should not be negative.
x
â
ErgoTransaction


106
Sum of transaction output values should not exceed 9223372036854775807.
x
â
ErgoTransaction


107
There should be no duplicate inputs.
x
â
ErgoTransaction


108
All token amounts of transaction outputs should be positive.
x
â
ErgoTransaction


109
A number of tokens within a box should not exceed 255 and sum of assets of one type should not exceed 9223372036854775807.
x
â
ErgoTransaction


111
Every output of the transaction should contain at least  nanoErgs.
â
â
ErgoTransaction


112
Transaction outputs should have creationHeight not exceeding block height.
x
â
ErgoTransaction


113
Every input of the transaction should be in UTXO.
x
â
ErgoTransaction


114
Every data input of the transaction should be in UTXO.
x
â
ErgoTransaction


115
Sum of transaction inputs should not exceed 9223372036854775807.
x
â
ErgoTransaction


116
Amount of Ergs in inputs should be equal to amount of Erg in outputs.
x
â
ErgoTransaction


...
