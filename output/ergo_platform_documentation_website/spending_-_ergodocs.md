# Spending - ErgoDocs
Source: [https://docs.ergoplatform.com/mining/rent/rent-spending/](https://docs.ergoplatform.com/mining/rent/rent-spending/)
Generated: 2025-05-11

## Summary
Spending an expired Ergo box involves satisfying specific conditions that differ from spending a regular box. The following criteria must be met: The following line of code checks whether the box has been stored for the required minimum duration, comparing the height of the upcoming block (context.preHeader.height) with the box's creation height (context.self.creationHeight): Reference: ErgoInterpreter.scala, line 73 The term "spending proof" typically refers to a cryptographic authorization required for spending a box. However, in the context of an expired box, this requirement is waived. The spending proof for the expired box must be empty, meaning that no cryptographic validation is needed to authorize its spending.

## Keywords
ergo, condition, criterion, line, code, check, minimum, duration, height, block, context.preheader.height, creation, reference, ergointerpreter.scala, term, spending, proof, authorization, context, requirement

## Content
## How to Spend an Expired Ergo Box#
Spending an expired Ergo box involves satisfying specific conditions that differ from spending a regular box. The following criteria must be met:

### Conditions for Spending an Expired Box#
Storage Fee Duration: The box must have been retained for at least the designated storage fee period. This is validated by calculating the difference between the height of the upcoming block, as indicated in the preheader, and the creation height of the box. This difference should be greater than or equal to the storage fee period.
Spending Proof: For an expired box, the spending proof must be left empty, eliminating the need for cryptographic authorization for the box's spending.
Storage Rent Awareness: If the expired box is affected by storage rent, it must be processed through the appropriate storage rent mechanism. The storage rent endpoint must be queried to ensure compliance with Ergoâs storage rent rules.

#### Code Snippet for Verifying Storage Fee Duration#
The following line of code checks whether the box has been stored for the required minimum duration, comparing the height of the upcoming block (context.preHeader.height) with the box's creation height (context.self.creationHeight):
context.preHeader.height - context.self.creationHeight >= Constants.StoragePeriod
Reference: ErgoInterpreter.scala, line 73

#### Spending Proof for Expired Boxes#
The term "spending proof" typically refers to a cryptographic authorization required for spending a box. However, in the context of an expired box, this requirement is waived. The spending proof for the expired box must be empty, meaning that no cryptographic validation is needed to authorize its spending. This allows any participant to spend the expired box without needing to prove ownership, as long as the storage fee duration condition is fulfilled.

#### Additional Details for Spending an Expired Box#
If both the above conditions are met, the expired box can be spent by anyone. To do so, one needs to provide an index of a newly recreated box (or an index of any box, if the expired box lacks sufficient funds for the storage fee) in the context extension variable #127, which will be stored as part of the input.

#### Storage Rent-Specific Handling#
Querying Storage Rent Endpoint
Expired boxes should be validated against the dedicated storage rent endpoint before spending.

This ensures that the expired box has fulfilled the required storage rent conditions before it is spent.


Integration with Mining Pools

Mining pools using Miningcore can now query storage rent block candidates through MiningRequestSRBlockCandidateAsync() using this fork

This ensures that block templates correctly account for expired boxes under storage rent rules.


Implementation in ErgoClient

The ErgoClient class has been updated to include a SrUrl field, allowing seamless communication with the storage rent service.

The MiningRequestSRBlockCandidateAsync() method fetches block templates that consider storage rent rules, ensuring compliance with Ergoâs state management policies.


Spending an Expired Box Affected by Storage Rent

If an expired box lacks sufficient ERG to pay the required storage rent fee, a new valid box must be referenced in the transaction.
This new box should either contain sufficient funds to cover storage rent or comply with mining pool policies for processing expired boxes.
The storage rent logic ensures that old, unused boxes do not persist indefinitely in the blockchain state.

#### Summary#
With these updates, expired Ergo boxes can be efficiently processed while adhering to storage rent policies. The mining pool and Ergo client implementations ensure that expired boxes are properly accounted for in block templates, maintaining blockchain sustainability and efficiency.
