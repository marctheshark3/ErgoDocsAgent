# SigmaRust - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/stack/sigma-rust/](https://docs.ergoplatform.com/dev/stack/sigma-rust/)
Generated: 2025-05-11

## Summary
Rust implementation of ErgoScript (sigmastate-interpreter) cryptocurrency scripting language. ergo-lib Overarching crate exposing wallet-related features: chain types (transactions, boxes, etc.), JSON serialization, box selection for tx inputs, tx builder and signing. Exports other crates API, probably the only crate you'd need to import. ergotree-interpreter ErgoTree interpreter ergotree-ir ErgoTree IR and serialization. ergoscript-compiler ErgoScript compiler.

## Keywords
rust, implementation, ergoscript, sigmastate, interpreter, cryptocurrency, scripting, language, ergo, overarch, crate, wallet, feature, chain, type, transaction, json, serialization, selection, input

## Content
## Sigma Rust#
Rust implementation of ErgoScript (sigmastate-interpreter) cryptocurrency scripting language.

### Crates#
ergo-lib
Overarching crate exposing wallet-related features: chain types (transactions, boxes, etc.), JSON serialization, box selection for tx inputs, tx builder and signing. Exports other crates API, probably the only crate you'd need to import.
ergotree-interpreter
ErgoTree interpreter
ergotree-ir
ErgoTree IR and serialization.
ergoscript-compiler
ErgoScript compiler.
sigma-ser
Ergo binary serialization primitives.

#### Bindings#
This section lists available language bindings for sigma-rust, allowing developers to interact with the Ergo blockchain using various programming languages.
Wasm:
Crate: ergo-lib-wasm  


JavaScript / TypeScript:
Browser: ergo-lib-wasm-browser 
Node.js: ergo-lib-wasm-nodejs 


Swift (iOS):
Repo: ergo-lib-ios


Java / JVM:
Repo: ergo-lib-jni  


C:
Repo: ergo-lib-c  


Go:
Repo: ergo-lib-go  (Note: Community maintained)


Ruby:
Repo: sigma_rb  (Note: Community maintained)


Python:
Package: ergo-lib-python   (Note: Uses ergo-lib crate docs)
See also: ergo-lib-python docs

### Usage Examples#
To get better understanding on how to use it in your project check out how its being used in the following projects:
Rust:
Oracle Core;
Ergo Headless dApp Framework;
Ergo Node Interface Library;
Spectrum Off-Chain Services for Ergo;
AgeUSD Stablecoin Protocol;
ErgoNames SDKs
TS/JS:
Ergo SDK (Wasm bindings);
Yoroi wallet (Wasm bindings);
Ergo Desktop Wallet (Wasm bindings);
Examples:
Create transaction demo (TS)
Address generation demo (TS)
Also take a look at tests where various usage scenarios were implemented.
