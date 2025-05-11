# The Ergo 'Box' model
Source: docs/dev/data-model/box.md
Generated: 2025-05-11

## Summary
---
tags:
  - Data Model
  - Box
  - UTXO
  - eUTXO
---

# The Ergo 'Box' model

*(Back to: [Data Model Overview](data-model.md))* Ergo uses a transactional model similar to Bitcoin's [Unspent Transaction Output (UTXO)](eutxo.md) model. In this model, [transactions](transactions.md) create and consume single-use entities called ***'boxes'***. In [ErgoScript](ergoscript.md), a 'box' is a versatile version of a UTXO.

## Keywords
data, model, utxo, eutxo, ergo, overview](data, bitcoin, unspent, transaction, output, utxo)](eutxo.md, transactions](transactions.md, entity, ergoscript](ergoscript.md, version, amount, cryptocurrency, address](address.md, registers](registers.md, datum

## Content
## The Ergo 'Box' model
(Back to: Data Model Overview)
Ergo uses a transactional model similar to Bitcoin's Unspent Transaction Output (UTXO) model. In this model, transactions create and consume single-use entities called 'boxes'.
In ErgoScript, a 'box' is a versatile version of a UTXO. It represents not only the amount of cryptocurrency owned by an address, but also contains 'registers' for additional data. This data can range from simple values to complex structures, which can be used in transactions and smart contract execution.
This makes Ergo's box different from a traditional UTXO, which only represents an amount of unspent cryptocurrency associated with a certain address. In UTXO-based cryptocurrencies, each transaction consumes one or more UTXOs as inputs and creates one or more UTXOs as outputs, with the 'unspent' outputs being the 'coins' that can be spent in future transactions.
The term 'box' in Ergo's context captures the idea that these entities are like containers holding various types of information (value, tokens, custom data, etc.), beyond just the unspent transaction output balance. This makes the boxes in Ergo significantly more flexible and functional, enabling more complex operations, such as running scripts or smart contracts, directly on the blockchain.

### Key Points
A box is an immutable unit, which can be created or removed, but never altered.
The box is not just a simple coin; it houses data, code, and registers, with all of its contents exclusively stored in the registers.
Four pre-defined registers contain the box's monetary value, its protection script (the ErgoTree), and the ID of the transaction that created the box.
Each box has a unique ID, derived from the unique contents of the box, including the data of the transaction that created it.
Boxes are integral to the Ergo protocol. The active box set (UTXO set) is authenticated through a hash-based data structure, facilitating the development of lightweight full nodes, as detailed in this paper.
A box can hold up to six additional registers (R4-R9) with typed data, accessible by the script.
Transactions consist of both input and output boxes.

### An example box
Consider the 'proof-of-no-premine' box from the Ergo genesis state. This box contains the last block IDs from Bitcoin and Ethereum at the launch time, as well as the latest news headlines:
JSON
     {
    "boxId": "b8ce8cfe331e5eadfb0783bdc375c94413433f65e1e45857d71550d42e4d83bd",
    "value": 1000000000,
    "ergoTree": "10010100d17300",
    "assets": [],
    "creationHeight": 0,
    "additionalRegisters": {
      "R5": "0e42307864303761393732393334363864393133326335613261646162326535326132333030396536373938363038653437623064323632336337653365393233343633",
      "R6": "0e464272657869743a20626f746820546f727920736964657320706c617920646f776e207269736b206f66206e6f2d6465616c20616674657220627573696e65737320616c61726d",
      "R8": "0e45d094d0b8d0b2d0b8d0b4d0b5d0bdd0b4d18b20d0a7d0a2d09fd09720d0b2d18bd180d0b0d181d182d183d18220d0bdd0b02033332520d0bdd0b020d0b0d0bad186d0b8d18e",
      "R7": "0e54e8bfb0e8af84efbc9ae5b9b3e8a1a1e38081e68c81e7bbade38081e58c85e5aeb9e28094e28094e696b0e697b6e4bba3e5ba94e5afb9e585a8e79083e58c96e68c91e68898e79a84e4b8ade59bbde4b98be98193",
      "R4": "0e4030303030303030303030303030303030303031346332653265376533336435316165376536366636636362363934326333343337313237623336633333373437"
    }
  }

### Additional Box Functions
Besides the registers, each box features a unique identification hash that can be referenced using the id function in ErgoScript. Box ids are computed by applying the blake2b256 hash function to the box's content, expressed as a Coll[Byte]. You can directly access the un-hashed byte collection representing a box using the bytes function. Note that each box’s content and id are cryptographically unique, meaning that no two boxes within the blockchain can share the same id or content bytes. This uniqueness is guaranteed by the inclusion of creationInfo (R3 register) in each box, as transaction ids and associated output indexes must be unique to a given UTXO. The bytesWithoutRef function can be used to retrieve a Coll[Byte] that excludes such information.

#### Example
```scala
{ // Example ErgoScript using box properties
    // Retrieve the value and token multipliers from the registers of the current box (SELF)
    val valueMultiplier = SELF.R4[Int].get
    val tokenMultiplier = INPUTS(1).R4[Int].get // Accessing register of another input box
// Check if the current box being spent (SELF) is the same as the first input box
if(SELF.id == INPUTS(0).id){
    // If it is, check if the first output box has the correct value and token amounts
    val outputValue = OUTPUTS(0).value == SELF.value * valueMultiplier
    val outputTokens = OUTPUTS(0).tokens(0)._2 == SELF.value * tokenMultiplier
    // Return a Sigma proposition that is true only if both outputValue and outputTokens are true
    sigmaProp(outputValue && outputTokens)
}else{
    // If the current box is not the same as the first input box, check if the output goes to a specified address
    val outputGoesToCheese = {
        // Create a public key that corresponds to a specific address
        PK("9etXmP7D3ZkWssDopWcWkCPpjn22RVuEyXoFSbVPWAvvzDbcDXE").propBytes
            == OUTPUTS(0).propositionBytes // propositionBytes holds the script (ErgoTree)
    }
    // Return a Sigma proposition that is true only if outputGoesToCheese is true
    sigmaProp(outputGoesToCheese)
}
}
// Context Variables used: SELF, INPUTS, OUTPUTS (See ../scs/blockchain-context.md)
// Functions used: sigmaProp, PK (See ../scs/sigma.md)
```

### Additional Resources
See the Transaction Format page for details on how boxes are serialized within transactions.
For the box type description in the ErgoScript language specification.
Visit ErgoAddress.scala, ErgoBoxCandidate, and ErgoBox in the reference client codebase.
For an in-depth explanation on Ergo box modeling, see this page.
