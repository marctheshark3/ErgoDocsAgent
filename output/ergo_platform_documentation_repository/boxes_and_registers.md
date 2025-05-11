# Boxes and Registers
Source: docs/dev/scs/boxes-and-registers.md
Generated: 2025-05-11

## Summary
---
tags:
  - Box
  - Registers
---

# Boxes and Registers

In [ErgoScript](ergoscript.md), a ['box'](box.md) is akin to a more versatile version of what a [UTXO (Unspent Transaction Output)](eutxo.md) represents in Bitcoin and many other [cryptocurrencies](protocol-overview.md). A box is not only a ledger entry denoting the amount of cryptocurrency owned by a particular [address](address.md), but it also carries ['registers'](registers.md), allowing it to contain additional data. This data could range from simple values to more complex structures, which can later be integrated into [transactions](transactions.md) and used in the execution of [smart contracts](contracts.md). Interpreting this register data off-chain is a common task; see [Fleet SDK Recipes](fleet-sdk-recipes.md) for examples using JavaScript/TypeScript. This makes Ergo's box different from a traditional UTXO, which only represents an amount of unspent cryptocurrency associated with a certain address.

## Keywords
registers, boxes, ergoscript](ergoscript.md, version, utxo, unspent, transaction, bitcoin, ledger, entry, amount, cryptocurrency, registers'](registers.md, datum, value, structure, transactions](transactions.md, execution, contracts](contracts.md, chain

## Content
## Boxes and Registers
In ErgoScript, a 'box' is akin to a more versatile version of what a UTXO (Unspent Transaction Output) represents in Bitcoin and many other cryptocurrencies. A box is not only a ledger entry denoting the amount of cryptocurrency owned by a particular address, but it also carries 'registers', allowing it to contain additional data. This data could range from simple values to more complex structures, which can later be integrated into transactions and used in the execution of smart contracts. Interpreting this register data off-chain is a common task; see Fleet SDK Recipes for examples using JavaScript/TypeScript.
This makes Ergo's box different from a traditional UTXO, which only represents an amount of unspent cryptocurrency associated with a certain address. In UTXO-based cryptocurrencies, each transaction consumes one or more UTXOs as inputs and creates one or more UTXOs as outputs, with the 'unspent' outputs being the 'coins' that can be spent in future transactions.
The term 'box' in Ergo's context captures the idea that these entities are like containers holding various types of information (value, tokens, custom data, etc.), beyond just the unspent transaction output balance. This makes the boxes in Ergo significantly more flexible and functional, enabling more complex operations, such as running scripts or smart contracts, directly on the blockchain.
