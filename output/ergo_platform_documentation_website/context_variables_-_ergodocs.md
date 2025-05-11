# Context Variables - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/ergoscript/context-variables/](https://docs.ergoplatform.com/dev/scs/ergoscript/context-variables/)
Generated: 2025-05-11

## Summary
ErgoScript provides the capability to create intricate programs with predicates that are context-dependent. Let's take a look at an example: This script uses the context variable HEIGHT, which signifies the height of the block in which the transaction is mined. If the blockchain height is less than 4,000,000, the box associated with this address becomes "anyone-can-spend". Conversely, if the blockchain height equals or exceeds 4,000,000, the box becomes "no-one-can-spend". Apart from HEIGHT, ErgoScript supports other context variables such as OUTPUTS, INPUTS, and minerPubKey.

## Keywords
ergoscript, capability, program, predicate, context, look, example, script, variable, height, block, transaction, address, outputs, inputs, minerpubkey, tool, detail, usage, language

## Content
## Leveraging Context Variables in ErgoScript#
ErgoScript provides the capability to create intricate programs with predicates that are context-dependent. Let's take a look at an example:
HEIGHT < 4000000            // address 2fp75qcgMrTNR2vuLhiJYQt
This script uses the context variable HEIGHT, which signifies the height of the block in which the transaction is mined. If the blockchain height is less than 4,000,000, the box associated with this address becomes "anyone-can-spend". Conversely, if the blockchain height equals or exceeds 4,000,000, the box becomes "no-one-can-spend".
Apart from HEIGHT, ErgoScript supports other context variables such as OUTPUTS, INPUTS, and minerPubKey. These variables offer additional tools for writing more specific and flexible scripts. For more details on context variables and their usage, please refer to the ErgoScript language specification.
