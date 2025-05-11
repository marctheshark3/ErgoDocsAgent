# Funding
Source: docs/dev/scs/tx/ico.md
Generated: 2025-05-11

## Summary
Another popular use case on Ethereum is an Initial Coin Offering (ICO) contract. An ICO mirrors an Initial Public Offering (IPO), providing a mechanism for a project to collect funding (often in stablecoins or the platform's native token) and then issue project "shares" (in the form of new tokens) to investors. Generally, an ICO comprises 3 stages:

- [**Funding**](#funding): During this period, investors are allowed to fund the project.
- [**Issuance**](#issuance): A new asset token is created and issued to investors.

## Keywords
case, ethereum, initial, coin, offering, contract, mirror, public, mechanism, project, funding, stablecoin, platform, token, share, form, investor, stage, period, asset

## Content
### Funding
The project initiates the ICO by creating a box guarded by the script shown below. This initial box also contains, in its R5 register, the authenticated digest of an empty dictionary intended to store (investor PK hash, invested amount) pairs. Here, an "investor PK hash" refers to the hash of the script (typically a standard P2PK script) that will guard the box containing the investor's withdrawn ICO tokens after the funding period ends.
```scala
// check if the index of the current input is 0
val selfIndexIsZero = INPUTS(0).id == SELF.id
// get the AVL tree proof from a register
val proof = getVarColl[Byte].get
// collect pk and value of all inputs, except for the first one
val toAdd = INPUTS.slice(1, INPUTS.size).map({(b: Box) =>
    val pk = b.R4[Coll[Byte]].get
    val value = longToByteArray(b.value)
    (pk, value)
})
// insert the collected inputs into the AVL tree, using the proof
val modifiedTree = SELF.R5[AvlTree].get.insert(toAdd, proof).get
// get the expected AVL tree from the first output
val expectedTree = OUTPUTS(0).R5[AvlTree].get
// check if the self output is correct by comparing the script
// if the current height is less than 2000, compare the script to the current box
// otherwise, compare the script to the issuance script
val selfOutputCorrect =
    if (HEIGHT < 2000) OUTPUTS(0).propositionBytes == SELF.propositionBytes
    else OUTPUTS(0).propositionBytes == issuanceScript
// check if there is only one output and if the self output is correct
val outputsCorrect = OUTPUTS.size == 1 && selfOutputCorrect
// check if the index is 0, outputs are correct, and the expected tree matches the modified tree
selfIndexIsZero && outputsCorrect && modifiedTree == expectedTree
```
The first funding transaction spends this initial box and creates a new box containing the same script but with an updated dictionary digest in R5 reflecting the first investment. Subsequent funding transactions spend the box created by the previous funding transaction. The script ...

### Issuance
This stage involves a single transaction to transition to the withdrawal stage. The spending transaction performs the following actions, verified by the issuanceScript:
1.  Updates AVL Tree Flags: It changes the allowed operations on the dictionary from "inserts only" to "removals only" by updating the enabledOperations flag in the AvlTreeData.
2.  Verifies Token Issuance: It checks that the correct amount of ICO tokens are issued. In Ergo, a transaction can issue a new token, whose ID is determined by the ID of the first input box. The issuanceScript verifies that a new token (with this ID) is created in the first output box (OUTPUTS(0)) with a total supply equal to the total nanoErgs collected during the funding stage (SELF.value).
3.  Transitions to Withdrawal Script: It ensures the output box (OUTPUTS(0)) containing the tokens and the dictionary digest is protected by the withdrawScript for the next stage.
4.  Checks Outputs: It verifies that the transaction has exactly two outputs: OUTPUTS(0) (the main contract box for the withdrawal stage) and OUTPUTS(1) (a box sending the collected Ergs to the project's designated address, identified by projectPubKeyHash).
The complete issuanceScript is shown below.
```scala
// Get the open and closed trees
val openTree = SELF.R5[AvlTree].get
val closedTree = OUTPUTS(0).R5[AvlTree].get
// Check that the digests, key lengths and values are the same
val correctDigest = openTree.digest == closedTree.digest
val correctKeyLength = openTree.keyLength == closedTree.keyLength
val correctValue = openTree.valueLengthOpt == closedTree.valueLengthOpt
// Check that the closed tree is a remove-only tree
val removeOnlyTree = closedTree.enabledOperations == 4
// Check that the token IDs and amounts are correct
val tokenId: Coll[Byte] = INPUTS(0).id
val tokenIssued = OUTPUTS(0).tokens(0)._2
val correctTokenNumber = OUTPUTS(0).tokens.size == 1 && OUTPUTS(1).tokens.size == 0
val correctTokenIssued = SELF.value == tokenIssued
val correctTokenId ...

### Withdrawal
Investors can now withdraw their allocated ICO tokens. The withdrawal process typically happens in batches. A withdrawal transaction spends the current ICO box (SELF) and creates N + 1 outputs:
*   OUTPUTS(0): The new ICO box, containing the remaining tokens and the updated dictionary digest (with withdrawn entries removed). It is protected by the same withdrawScript.
*   OUTPUTS(1) to OUTPUTS(N): Boxes sent to the withdrawing investors. Each box is protected by the investor's script (whose hash was stored as the key in the dictionary) and contains the corresponding amount of ICO tokens.
The withdrawScript requires two AVL tree proofs provided in context variables:
1.  lookupProof: Proves the existence and amounts associated with the investor keys being withdrawn.
2.  removeProof: Proves that these investor entries have been correctly removed from the dictionary, resulting in the updated dictionary digest found in OUTPUTS(0).
The complete withdrawScript is shown below:
```scala
// Get removeProof and lookupProof
val removeProof = getVarColl[Byte].get
val lookupProof = getVarColl[Byte].get
// Get withdraw indexes and tokenId
val withdrawIndexes = getVarColl[Int].get
val tokenId: Coll[Byte] = SELF.R4[Coll[Byte]].get
// Map over withdrawIndexes and find tokenIds
val withdrawals = withdrawIndexes.map({(idx: Int) =>
    val b = OUTPUTS(idx)
    if (b.tokens(0)._1 == tokenId)
        (blake2b256(b.propositionBytes), b.tokens(0)._2)
    else
        (blake2b256(b.propositionBytes), 0L)
    })
// Get withdrawValues and calculate the total amount withdrawn
val withdrawValues = withdrawals.map({(t: (Coll[Byte], Long)) => t._2})
val total = withdrawValues.fold(0L, {(l1: Long, l2: Long) => l1 + l2 })
// Get list of nodes to remove and removed values
val toRemove = withdrawals.map({(t: (Coll[Byte], Long)) => t._1})
val initialTree = SELF.R5[AvlTree].get
val removedValues = initialTree.getMany(toRemove, lookupProof).map(
    {(o: Option[Coll[Byte]]) => byteArrayToLong(o.get)}
   ...

### Comet Refundable ICO
Comet has a refundable ICO live at thecomettoken.com/ICO
The contract used is provided:
```scala
{
  // Receipt Tokens held in Contract
  val receiptTokens = SELF.tokens(0)._2
  // Comet Held in Contract
  val cometTokens = SELF.tokens(1)._2
  // Receipt Token Id
  val receiptId = fromBase58("5HWxQHyjjVFNEWtswcc71922Bq84LsmtMbgEG5eNxAKZ")
  // Comet Token Id
  val cometId = fromBase58("s9d3vUc6AhNAPZhxnGXCitQFqdAXN6X7gXT3h9GupWE")
  // Swap Price
  val amountToSwap = 15 * (OUTPUTS(0).value - SELF.value) / 100000
  // Refund Price
  val amountToRefund = 15 * (SELF.value - OUTPUTS(0).value) / 100000
// Conditions that are always true
  val alwaysTrue = allOf(Coll(
    OUTPUTS(0).propositionBytes == SELF.propositionBytes, // OUTPUT(0) is contract box
    OUTPUTS(0).R4[Coll[Byte]].get == SELF.id, // Protect against spending two contract boxes of same value in 1 tx.
    OUTPUTS(0).tokens(0)._1 == receiptId // Contract always holds receipt tokens
  ))
// Conditions that depend on spending action
  val conditionals = if (OUTPUTS(0).value > SELF.value) { // Purchase comet condition
    allOf(Coll(
      OUTPUTS(0).tokens(0)._2 >= receiptTokens - amountToSwap, // Unlock value amount of receipt for spending
      OUTPUTS(0).tokens(1)._1 == cometId,
      OUTPUTS(0).tokens(1)._2 >= cometTokens - amountToSwap // Unlock value amount of comet for spending
    ))
  } else { // Refund comet condition
    allOf(Coll(
      OUTPUTS(0).tokens(0)._2 >= receiptTokens + amountToRefund, // Unlock receipt amount of Erg for spending
      OUTPUTS(0).tokens(1)._1 == cometId,
      OUTPUTS(0).tokens(1)._2 >= cometTokens + amountToRefund // Unlock comet amount of Erg for spending
    ))
  }
val drainAddressConditions = allOf(Coll(
    OUTPUTS(0).value == SELF.value,
    OUTPUTS(0).tokens(0)._2 == receiptTokens, // Cannot withdraw receipt tokens
    OUTPUTS(0).tokens(1)._1 == cometId,
    OUTPUTS(0).tokens(1)._2 >= 1 // Free up all comet
  ))
val addFunds = alwaysTrue && allOf(Coll(
    OUTPUTS...
