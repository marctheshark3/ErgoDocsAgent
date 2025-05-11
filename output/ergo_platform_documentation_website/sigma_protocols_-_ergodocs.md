# Sigma Protocols - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/sigma/](https://docs.ergoplatform.com/dev/scs/sigma/)
Generated: 2025-05-11

## Summary
(Back to: ErgoScript Overview) Sigma protocols (Î£-protocols) are a class of cryptographic proof systems that play a central role in the Ergo blockchain. These protocols allow a prover to convince a verifier that they know a value, such as a secret key, without revealing the value itself (a property related to zero-knowledge proofs). Î£-protocols are the foundation for many privacy-preserving and multi-signature functionalities in Ergo. In ErgoScript, proving and verifying cryptographic statements are first-class primitives, giving developers access to powerful Î£-protocols. Scripts protecting transaction outputs can contain Î£-statements, which must be proven (by generating Î£-proofs) before the outputs can be spent.

## Keywords
ergoscript, overview, sigma, protocol, î£-protocols, class, proof, system, role, ergo, blockchain, prover, verifier, value, property, knowledge, î£-protocol, foundation, privacy, functionality

## Content
## Sigma Protocols#
(Back to: ErgoScript Overview)

### Introduction#
Sigma protocols (Î£-protocols) are a class of cryptographic proof systems that play a central role in the Ergo blockchain. These protocols allow a prover to convince a verifier that they know a value, such as a secret key, without revealing the value itself (a property related to zero-knowledge proofs). Î£-protocols are the foundation for many privacy-preserving and multi-signature functionalities in Ergo.
In ErgoScript, proving and verifying cryptographic statements are first-class primitives, giving developers access to powerful Î£-protocols. Scripts protecting transaction outputs can contain Î£-statements, which must be proven (by generating Î£-proofs) before the outputs can be spent.
Conceptually, Î£-proofs are generalizations of digital signatures. The Schnorr signature scheme is the canonical example of a Î£-proof: it allows the recipient to prove knowledge of a secret (discrete logarithm) without revealing it. Î£-proofs in Ergo extend this concept, allowing the creation of more complex cryptographic protocols like multi-signature, ring signatures, and threshold signatures.

#### Elementary Î£-Protocols in ErgoScript#
ErgoScript offers two elementary Î£-protocols over a group of prime order, such as an elliptic curve group:
Proof of Knowledge of Discrete Logarithm (Schnorr Signature): This protocol proves knowledge of the discrete logarithm of a given public key with respect to a fixed generator. Essentially, this is the Schnorr signature scheme.
Proof of Equality of Discrete Logarithms (Diffie-Hellman Tuple): This protocol proves that two values share the same discrete logarithm across two different generators.
These basic protocols can be composed to create more advanced proofs using logical connectives like AND, OR, and THRESHOLD. This composability is what enables the creation of sophisticated smart contracts and multi-signature schemes.
For a detailed introduction to Î£-protocols, refer to the paper On Î£-protocols.

### Composability of Î£-Protocols#
A powerful feature of Î£-protocols in Ergo is their composability. You can create logical combinations of cryptographic statements using basic AND/OR logic.
Examples include:
Ring Signatures: A ring signature is a proof of knowledge of one of multiple secrets. For example:

Prove knowledge of either secret A or secret B.



Threshold Signatures: A threshold signature is a proof that a certain number of secrets are known. For example:

Prove knowledge of at least two of three secrets.
These constructions allow for flexible and privacy-preserving proofs. The THRESHOLD construct (also known as k-out-of-n) is particularly useful for multi-party agreements, ensuring that a subset of participants can authorize a transaction without requiring everyoneâs involvement.

##### Example: 3-out-of-5 Threshold Signature#
// Example ErgoScript for a 3-out-of-5 multi-signature contract
val thresholdScript = s"""
{
  atLeast( // Requires at least 3 proofs from the collection below
    3,
    Coll(
      PK("9f8ZQt1Sue6W5ACdMSPRzsHj3jjiZkbYy3CEtB4BisxEyk4RsNk"), // Public Key 1
      PK("9hFWPyhCJcw4KQyCGu4yAGfC1ieRAKyFg24FKjLJK2uDgA873uq"), // Public Key 2
      PK("9fdVP2jca1e5nCTT6q9ijZLssGj6v4juY8gEAxUhp7YTuSsLspS"), // Public Key 3
      PK("9gAKeRu1W4Dh6adWXnnYmfqjCTnxnSMtym2LPPMPErCkusCd6F3"), // Public Key 4
      PK("9gmNsqrqdSppLUBqg2UzREmmivgqh1r3jmNcLAc53hk3YCvAGWE")  // Public Key 5
    )
  )
}
"""
This contract is an example of a 3-out-of-5 threshold signature scheme. It can be compiled to a Pay-to-Script (P2S) address, where any three of the five public keys can authorize a transaction.

#### 1. Multi-Signature Wallets#
Multi-signature wallets are a natural use case for Î£-protocols, where multiple parties are required to authorize a transaction. Î£-protocols allow you to set up flexible conditions such as requiring two out of three signatures, or even more complex schemes involving multiple participants.

#### 2. Ring Signatures for Privacy#
Ring signatures provide privacy by allowing a user to sign a transaction on behalf of a group without revealing which group member signed it. This is particularly useful for creating anonymous transactions and decentralized mixers, such as ErgoMixer. The privacy of ring signatures makes them ideal for applications where anonymity is crucial, such as anonymous donations or private payments.

#### 3. Threshold Signatures#
Threshold signatures are critical for decentralized control. For example, a corporate wallet could be protected by a 3-out-of-5 signature scheme, ensuring that no single party can unilaterally control the funds.

#### 4. Time-Locked Conditions#
Î£-protocols can be combined with time-locked conditions. For instance, you can construct a contract that allows a transaction to be spent if either a ring signature is provided by a set of participants before a certain block height, or the funds can be refunded by a single party after the block height has passed.

#### 5. Decentralized Mixers#
ErgoMixer is an advanced, non-custodial token mixer based on Î£-protocols. It leverages ring signatures and zero-knowledge proofs to provide enhanced privacy while ensuring that no third party is needed to manage or approve the mixing process. SigmaJoin, an off-chain implementation concept related to ErgoMixer, further extends the idea of trustless and decentralized privacy mechanisms.

### Prover and Verifier Workflow#
In Ergo, transaction processing using Î£-protocols involves two main actors: the Prover and the Verifier.
Prover:

The Prover uses the ErgoTree interpreter to reduce a high-level spending condition into a SigmaBoolean (the cryptographic proposition that needs to be proven). The SigmaBoolean is then converted into a cryptographic proof using the Fiat-Shamir transformation, ensuring that the transaction can only be authorized by parties who possess the necessary secrets (such as private keys).



Verifier:

The Verifier also uses the ErgoTree interpreter to reduce the spending condition into a SigmaBoolean. It then checks the cryptographic proof against this proposition, ensuring that the transaction is valid and all required conditions are met.

### Fiat-Shamir Transformation#
The Fiat-Shamir transformation is a cryptographic technique that makes interactive proof systems non-interactive, suitable for use in blockchain environments. This is crucial for Sigma protocols, as it allows Î£-proofs to be created and verified without requiring real-time interaction between the prover and the verifier.
In Ergo, Î£-protocols rely on the Fiat-Shamir transformation to generate challenges (hash values) from the commitments and messages involved in the proof. This ensures that the proofs are non-interactive and can be verified deterministically on-chain.

#### Applications#
ErgoMixer: A state-of-the-art, non-custodial token mixer using Î£-protocols for privacy and anonymity.
SigmaJoin: An off-chain implementation concept related to ErgoMixer for decentralized privacy-preserving transactions.
Ergo Threshold Signature Contracts: Use Î£-protocols to create custom multi-signature wallets and contracts.

#### DarkFund0#
DarkFund0: A ZK fund for privacy applications, sponsoring developments in privacy-focused decentralized finance (DeFi) on Ergo.

#### Tutorials#
Verifying Schnorr Signatures in ErgoScript
Updateable Multisig Pattern

#### Presentations#
Sigma Protocols
On Î£-protocols

### Conclusion#
Sigma protocols form the backbone of Ergoâs smart contracts and cryptographic proofs, enabling flexible and privacy-preserving transactions. Whether it's for simple multi-signature wallets, complex threshold signatures, or advanced privacy-preserving ring signatures, Î£-protocols provide the necessary cryptographic tools for building secure and decentralized applications on the Ergo blockchain.
With their composability and integration into ErgoScript, Î£-protocols make Ergo a versatile platform for privacy-focused cryptographic applications.
