# Velvet Forks
Source: docs/mining/gov/velvet-fork.md
Generated: 2025-05-11

## Summary
---
tags:
  - Forking
  - Fork
---

# Velvet Forks

Velvet forking is a novel approach introduced in the paper ["A Wild Velvet Fork Appears! Inclusive Blockchain Protocol Changes in Practice"](http://diyhpl.us/~bryan/papers2/bitcoin/A%20wild%20velvet%20fork%20appears:%20Inclusive%20blockchain%20protocol%20changes%20in%20practice%20-%202018.pdf) by Zamyatin et al. It allows for introducing protocol changes in a backward-compatible and inclusive manner. The key idea is to render modifications to the protocol backward-compatible, enabling a gradual deployment without harming miners who have not upgraded to the new rules. Velvet forks are a special form of protocol update where the new set of reducing protocol rules P' is conditionally applied only when the considered elements, such as blocks or transactions, are valid under the new rules.

## Keywords
forking, fork, velvet, forks, approach, paper, wild, inclusive, blockchain, protocol, changes, practice"](http://diyhpl.us/~bryan, papers2, bitcoin, a%20wild%20velvet%20fork%20appears:%20inclusive%20blockchain%20protocol%20changes%20in%20practice%20-%202018.pdf, zamyatin, change, manner, idea, modification

## Content
## Velvet Forks
Velvet forking is a novel approach introduced in the paper "A Wild Velvet Fork Appears! Inclusive Blockchain Protocol Changes in Practice" by Zamyatin et al. It allows for introducing protocol changes in a backward-compatible and inclusive manner. The key idea is to render modifications to the protocol backward-compatible, enabling a gradual deployment without harming miners who have not upgraded to the new rules.
Velvet forks are a special form of protocol update where the new set of reducing protocol rules P' is conditionally applied only when the considered elements, such as blocks or transactions, are valid under the new rules. If not, the new rules are ignored, and the previous protocol rules P are relied upon to determine validity. Since the new rules in P' are reducing, velvet protocol changes never incur a permanent protocol fork, as any element considered valid under P' is also considered valid under P.
The key advantages of velvet forks are:
Inclusive Deployment: They do not require support from a majority of participants and can potentially avoid rule disagreement forks altogether. Legacy nodes remain unaware of the changes introduced by the velvet fork.


Backward Compatibility: Valid blocks adhering to the new rules are also valid blocks under the old rules, ensuring compatibility with non-upgraded nodes.


Gradual Adoption: Velvet forks leverage the consensus mechanism of the existing protocol P to bootstrap their own consensus rules P', allowing for a gradual adoption of the new rules.
While velvet forks present a promising approach for introducing protocol changes, they may also introduce new potential attacks and threats, as well as impact the game-theoretic incentives of the underlying blockchain. Further research is needed to understand the security implications of velvet forks and their potential applications in various blockchain protocols.
Ergo's design allows for the implementation of velvet forks, enabling the introduction of new features and...
