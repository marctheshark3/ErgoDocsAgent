# Proof-of-Work Backed Tokens
Source: docs/uses/PoW_tokens.md
Generated: 2025-05-11

## Summary
# Proof-of-Work Backed Tokens

Ergo allows the issuance of one token per transaction, where the token id must match the id of the box of the first input. When a box is generated, the id of the future token is known. This id is computed through hashing. By iterating over a register (for example, `R4`) used as a nonce, a token with specific id properties can be created. This could include ids starting with a certain number of zeroes.

## Keywords
work, backed, tokens, ergo, issuance, token, transaction, input, register, example, nonce, property, number, zero, vanitygen, address, concept, bitcoin, contract, proof

## Content
## Proof-of-Work Backed Tokens
Ergo allows the issuance of one token per transaction, where the token id must match the id of the box of the first input.
When a box is generated, the id of the future token is known. This id is computed through hashing.
By iterating over a register (for example, R4) used as a nonce, a token with specific id properties can be created. This could include ids starting with a certain number of zeroes. Therefore, some computational work may be required to generate such a token, similar to the VanityGen-address concept in Bitcoin, but applied to tokens.
Certain contracts may only accept these Proof-of-Work backed Non-Fungible Tokens (NFTs).
While specific use-cases have not been fully explored, potential applications could include spam filtering.
For more detailed discussions, refer to this link.
