# Anyone Can Spend - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/ergoscript/anyone-can-spend/](https://docs.ergoplatform.com/dev/scs/ergoscript/anyone-can-spend/)
Generated: 2025-05-11

## Summary
The simplest form of ErgoScript is a single boolean predicate. For example, true corresponds to the address 4MQyML64GnzMxZgm 4MQyML64GnzMxZgm. Any funds sent to this address can be spent by anyone, as the script always evaluates to true. Scripts that consistently evaluate to true, and their corresponding boxes, are referred to as anyone-can-spend scripts.

## Keywords
form, ergoscript, predicate, example, correspond, address, fund, script

## Content
## Anyone-Can-Spend Scripts#
The simplest form of ErgoScript is a single boolean predicate. For example, true corresponds to the address 4MQyML64GnzMxZgm 4MQyML64GnzMxZgm.
Any funds sent to this address can be spent by anyone, as the script always evaluates to true.
Scripts that consistently evaluate to true, and their corresponding boxes, are referred to as anyone-can-spend scripts.
true && (false || true)     // address NwAyzZpF2KcXAGBJvPrAH
