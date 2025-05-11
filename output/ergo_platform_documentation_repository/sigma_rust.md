# Sigma Rust
Source: docs/dev/stack/sigma-rust.md
Generated: 2025-05-11

## Summary
---
tags:
  - Rust
  - SigmaRust
  - Bindings
  - Wasm
  - JavaScript
  - TypeScript
  - Swift
  - iOS
  - Java
  - JVM
  - C
  - Go
  - Ruby
  - Python
---

# Sigma Rust

Rust implementation of [ErgoScript (sigmastate-interpreter)](sigmastate-interpreter.md) cryptocurrency scripting language. ## Crates

[ergo-lib](https://github.com/ergoplatform/sigma-rust/tree/develop/ergo-lib) [! [Latest Version](https://img.shields.io/crates/v/ergo-lib.svg)](https://crates.io/crates/ergo-lib) [![Documentation](https://docs.rs/ergo-lib/badge.svg)](https://docs.rs/crate/ergo-lib)

Overarching crate exposing wallet-related features: chain types (transactions, boxes, etc.), JSON serialization, box selection for tx inputs, tx builder and signing.

## Keywords
rust, sigmarust, bindings, wasm, javascript, typescript, java, ruby, python, sigma, implementation, ergoscript, sigmastate, cryptocurrency, scripting, language, crates, ergo, tree, version](https://img.shields.io

## Content
## Sigma Rust
Rust implementation of ErgoScript (sigmastate-interpreter) cryptocurrency scripting language.

### Crates
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

#### Bindings
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

### Usage Examples
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
