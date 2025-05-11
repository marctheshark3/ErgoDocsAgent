# Transaction Fees in Ergo
Source: docs/dev/protocol/tx/min-fee.md
Generated: 2025-05-11

## Summary
---
tags:
  - Fees
  - Transaction Fees
---

# Transaction Fees in Ergo

Each Ergo [transaction](transactions.md) is an atomic state transition operation, involving the destruction of one or more [boxes](format.md) from the state and the creation of new ones. Unlike Bitcoin's implicit fee system, Ergo's fee structure is explicit, requiring a separate output to a specific address for fees. Ergo's transaction fee system is designed to be both flexible and explicit. While the protocol does not enforce a minimum transaction fee, transactions without a fee are less likely to be included in a block by miners.

## Keywords
transaction, fees, ergo, each, transaction](transactions.md, state, transition, operation, destruction, creation, bitcoin, system, structure, output, address, protocol, block, miner, likelihood, minimum

## Content
## Transaction Fees in Ergo
Each Ergo transaction is an atomic state transition operation, involving the destruction of one or more boxes from the state and the creation of new ones. Unlike Bitcoin's implicit fee system, Ergo's fee structure is explicit, requiring a separate output to a specific address for fees.
Ergo's transaction fee system is designed to be both flexible and explicit. While the protocol does not enforce a minimum transaction fee, transactions without a fee are less likely to be included in a block by miners. Therefore, it is generally recommended to include a fee to incentivize miners to process your transaction. The larger the fee, the higher the likelihood of your transaction being included in a block and processed quickly.

### Minimum Values
Although the protocol does not enforce a specific transaction fee, it employs a spam-prevention strategy that requires each box to contain a minimum amount of ERG. This minimum value is determined by a parameter voted on by miners and the size of the box. Every output box in a transaction must adhere to this rule. This strategy helps prevent the creation of dust in Ergo, thereby mitigating potential spam attacks.
This fee is calculated based on the serialized size of the boxes being created, with a minimum threshold set at 360 nanoerg per byte and is adjustable via miner voting. As a guideline, it is suggested to allocate 0.001 ERG (1,000,000 NanoErg) for each box involved in the transaction.
/// details | Dust
    {type: info, open: true}
To clarify, the Dust-prevention Fee is not an actual fee that users must pay to others (e.g., miners). Instead, it serves as a security measure for the box. If users avoid creating new boxes, the Dust-prevention Fee can be reused by transferring the same amount into a newly created single box. If the new box remains under your control, you can be assured that there will be no loss of funds.
///

### Miner Transaction Prioritization
Miners prioritize transactions based on either the fee per byte or the validation cost unit. These criteria are adjustable via a voting mechanism among miners. Nodes can sort transactions based on these metrics, settable in the node configuration.
```conf

## Mempool transaction sorting scheme ("random", "bySize", or "byExecutionCost")
mempoolSorting = "random"
```
When calculating the fee per byte or the fee per validation cost unit, miners initially filter out the fee boxes by checking the propositionBytes in the R1 register using the feeProposition method. Subsequently, they sum up the ERG value of these boxes. This sum is then divided by either the transaction's size or the total validation cost to yield a result. This final result serves as the basis for sorting transactions in the mempool.
/// details | Special Considerations
    {type: info, open: true}
Although the minimal fee is a standard, miners can select transactions based on their economic incentives. This means transactions offering higher fees per byte or per execution unit are typically prioritized. However, miners may also choose to include their transactions above others when collecting storage rent.
///

### Fee Collection
Transaction fees are secured in a contract, which can only be spent through a miner's script. The address used for fees is not fixed by the protocol but is a standard in the Ergo node reference implementation. The ErgoScript for this contract, implicitly defined in the ErgoTree, is detailed in this method.
/**
    * This proposition allows sending coins to a box protected by the following proposition:
    * prove the discrete logarithm of the miner's public key and that the height is at least `delta` blocks greater than the current one.
    */
  def feeProposition(delta: Int = 720): ErgoTree = {
    val out = ByIndex(Outputs, IntConstant(0))
    AND(
      EQ(Height, boxCreationHeight(out)),
      EQ(ExtractScriptBytes(out), expectedMinerOutScriptBytesVal(delta, MinerPubkey)),
      EQ(SizeOf(Outputs), 1)
    ).toSigmaProp.treeWithSegregation
  }
In essence, the fee script requires the spending transaction to have one output that pays to the miner's public key 720+ blocks later.
And the method to extract the transaction fee method is as follows:
private def extractFee(tx: ErgoTransaction): Long = {
    tx.outputs
      .filter(_.ergoTree == settings.chainSettings.monetary.feeProposition)
      .map(_.value)
      .sum
  }
/// details | Why is it like this?
    {type: question, open: true}
Ergo's design philosophy emphasizes explicitness in its transactional model. This includes aspects such as emission, which is handled via a contract, and transaction fees. This approach simplifies the transactional model where possible.
///

### Determining Appropriate Fees
The appropriate transaction fee must meet the protocol's minimum requirements, based on the box size. For best practices, see the ErgoTransaction.scala.

### Confirmation Levels and Security
The recommended confirmation levels vary depending on the network hashrate. Higher hashrates reduce double-spend attack risks, thus requiring fewer confirmations.

#### Babel Fees
Babel Fees enable users to pay transaction fees using tokens like SigmaUSD instead of ERG. This involves creating a new box with Babel tokens as change. The necessary ERGs for the transaction recipient and the miner's fee are sourced from this Babel fee box. For more details, see Babel Fees documentation.

#### ErgoMixer
ErgoMixe offers token mixing and dynamic fee management for consistent transaction inclusion in blocks. It uses blockchain-stored parameters for client guidance, supporting transparent and flexible fee and token management. For more insights, see this forum post.
