# Tokens on Ergo
Source: docs/dev/data-model/box/tokens.md
Generated: 2025-05-11

## Summary
---
tags:
  - Data Model
  - Storage Rent
  - Registers
---

# Tokens on Ergo

Ergo's native tokens are incredibly versatile and can represent a wide range of assets, including shares, complementary currency units, and various tangible or intangible items. The infrastructure of Ergo is designed to seamlessly handle the representation and transfer of these diverse assets, integrating them into the blockchain as *first-class citizens*.

//// details | What are  **first-class citizens**? {type: info, open: false} This means that tokens in Ergo are not just metadata attached to transactions, but they are deeply integrated into the Ergo protocol. They can be manipulated and managed with the same level of support and functionality as the native Ergo token (see [EIP-0004](eip4.md)).

## Keywords
data, model, storage, rent, registers, tokens, ergo, token, range, asset, share, currency, unit, item, infrastructure, representation, transfer, blockchain, class, citizen

## Content
## Tokens on Ergo
Ergo's native tokens are incredibly versatile and can represent a wide range of assets, including shares, complementary currency units, and various tangible or intangible items. The infrastructure of Ergo is designed to seamlessly handle the representation and transfer of these diverse assets, integrating them into the blockchain as first-class citizens.
//// details | What are  first-class citizens? 
    {type: info, open: false}
This means that tokens in Ergo are not just metadata attached to transactions, but they are deeply integrated into the Ergo protocol. They can be manipulated and managed with the same level of support and functionality as the native Ergo token (see EIP-0004).
/// details | It is crucial to understand that ERG, the native token of Ergo, possesses two unique characteristics:
    {type: warning, open: false}
- ERGs cannot be burned; the total input and output amounts in any transaction must be equal.
- Storage rent can only be paid in ERGs.
///
////
/// details | How do I mint a token?
    {type: info, open: false}
- Use ergoutils to mint a token directly from your web browser. (Video Tutorial
))
- For programmatic token minting, refer to this guide: Minting a Token with Fleet SDK
///
There is no central database where tokens are registered currently, your best bet is to use community resources like supported tokens in the ergotipper bot and spectrum-finance/ergo-token-list.

### Token Storage
Tokens are stored in a special register R2 of a box in the form of (tokenId -> amount) pairs.
A single box can hold up to 255 secondary tokens.

### Register Usage
The Ergo reference implementation wallet uses specific registers in a unique way, although the protocol doesn't enforce this:
R4 - verbose name
R5 - description
R6 - number of decimal places
Additional registers (R7, R8, R9) can store asset-specific information

### Limitations
There are certain indirect limitations to consider:
The size of a box should not exceed 4 kilobytes.
The presence of tokens increases the computational cost of the transaction.

### Asset Creation
An exception to the rule of weak preservation (the total amount in inputs should be no less than the total amount in outputs) is that a transaction can generate tokens from thin air in its outputs if the asset identifier matches the identifier of the transaction's first input box. Given that the box identifier is cryptographically unique, it's impossible to have a second asset with the same identifier, assuming the hash function used is collision-resistant (which it indeed is). This rule also implies that only one new asset can be created per transaction.

### Examples
How to mint a token with Fleet SDK
Creating a perpetual token (designed to exist indefinitely, unless it is removed by garbage collection.)

### Resources
Token category on sigmaverse.io
Ergo Token Minter or CYTI which uses a Use CYTI minable smart contract to choose your token ID.
ergoutils.org
Video Tutorial
Why does the limitation of 1 new token per transaction exist?
