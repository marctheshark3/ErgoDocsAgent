# Sigma Language - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/sigma-lang/](https://docs.ergoplatform.com/dev/scs/sigma-lang/)
Generated: 2025-05-11

## Summary
The sigmastate-interpreter repository contains implementations of ErgoScript compiler and ErgoTree Interpreter for a family of Sigma-protocol based authentication languages (or simply Sigma language). Every coin in Bitcoin is protected by a program in the stack-based Script language. An interpreter for the language evaluates the program against a context (a few variables containing information about a spending transaction and the blockchain), producing a single boolean value. While Bitcoin Script allows some contracts to be programmed, its abilities are limited. Also, a hard fork would be required to add new cryptographic primitives, such as ring signatures.

## Keywords
sigmastate, interpreter, repository, implementation, ergoscript, compiler, ergotree, family, sigma, protocol, authentication, language, coin, bitcoin, program, stack, script, context, variable, information

## Content
## The 'Sigma Language'#
The sigmastate-interpreter repository contains implementations of ErgoScript compiler and ErgoTree Interpreter for a family of Sigma-protocol based authentication languages (or simply Sigma language).

### Sigma Language Background#
Every coin in Bitcoin is protected by a program in the stack-based Script language. An interpreter for the language evaluates the program against a context (a few variables containing information about a spending transaction and the blockchain), producing a single boolean value. While Bitcoin Script allows some contracts to be programmed, its abilities are limited. Also, a hard fork would be required to add new cryptographic primitives, such as ring signatures.
Generalizing the Bitcoin Script, ErgoScript compiler and ErgoTree interpreter implement an authentication language which allows developers to specify coin spending conditions. The ErgoScript Compiler compiles the source code into ErgoTree byte code, which can be saved in UTXO coins to protect their spending (same as in Bitcoin).
ErgoTree, in turn, is a bytecode language and memory representation that can be deterministically interpreted in the given blockchain context.
Please note
ErgoTree defines guarding proposition for a coin as a logic formula which combines predicates over a context and cryptographic statements provable via Î£-protocols with AND, OR, k-out-of-n connectives.
