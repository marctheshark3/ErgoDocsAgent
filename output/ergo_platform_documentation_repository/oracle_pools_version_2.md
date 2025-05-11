# Oracle Pools Version 2
Source: docs/eco/oracles-v2.md
Generated: 2025-05-11

## Summary
---
tags:
  - Oracle Pools
  - Oracles
  - EIP-23
  - DeFi
---

# Oracle Pools Version 2


/// details | Latest Developments
     {type: tip, open: true}
See the latest overview video from the summit here: [Oracle Pool v2 | greenhat | Ergoversary Summit 2023](https://youtube.com/watch?v=WeQcUmVUhoI)
/// The document described below outlines a proposed upgrade to Oracle Pool version 1.0, as presently deployed and detailed in [EIP16](https://github.com/ergoplatform/eips/blob/eip16/eip-0016.md). The necessity for these modifications emerges from several perceived limitations within Oracle Pool v1.0:

1. Excessive dust generation from rewards.

## Keywords
oracle, pools, oracles, eip-23, defi, version, detail, latest, developments, type, overview, video, summit, pool, greenhat, ergoversary, 2023](https://youtube.com, watch?v, weqcumvuhoi, document

## Content
## Oracle Pools Version 2
/// details | Latest Developments
     {type: tip, open: true}
See the latest overview video from the summit here: Oracle Pool v2 | greenhat | Ergoversary Summit 2023
///
The document described below outlines a proposed upgrade to Oracle Pool version 1.0, as presently deployed and detailed in EIP16. The necessity for these modifications emerges from several perceived limitations within Oracle Pool v1.0:
Excessive dust generation from rewards.
Inadequate reward provision (interrelated with point 1).
Two distinct types of pool boxes, complicating dApps and the update mechanism.
Non-transferability of Oracle tokens, resulting in the permanent locking of oracles. This issue also applies to ballot tokens.
Version 2.0 of Oracle Pool aims to mitigate these issues. The main features and enhancements compared to v1.0 are summarised as follows:
Single Pool Address: In v2.0, the pool will have only a singular address, known as the pool address.
Epoch Counter: To accommodate more complex dApps, the pool box will store an additional counter that increments upon each collection.
Compact Pool Box: The pool box is dissociated from pool management logic, which is now encapsulated within a refresh box. This results in a considerably smaller pool box, conducive for use in other dApps.
Refresh Box: This box functions for the collection of data-points.
Reward in Tokens: Instead of Ergs, rewards for posting will be issued in tokens. These tokens can be redeemed separately, outside of the protocol.
The pool box will emit these reward tokens.


No Separate Funding Process: The pool box will only emit reward tokens and will not distribute Ergs. Consequently, a separate funding process is not required.
Reward Accumulation: To avoid dust, a new box for each reward posting will not be created. Instead, rewards will be directly accumulated within the oracle boxes.
Oracle Boxes Used in Collection: As rewards must be accumulated, the oracle boxes will function as inputs instead of data-inputs whe...
