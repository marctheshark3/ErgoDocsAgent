# EIP-0024: Artwork Contract
Source: docs/dev/tokens/standards/eip24.md
Generated: 2025-05-11

## Summary
---
tags:
  - EIP
---

# EIP-0024: Artwork Contract

> 🔗 From [EIP-0024:](https://github.com/ergoplatform/eips/blob/master/eip-0024.md)


## Motivation 
With the discovery that we can easily use spent boxes in contracts ([see here](https://www.ergoforum.org/t/ergoscript-design-patterns/222/23?u=anon_real)), some new features are introduced for artworks and can be extended further in the future. This EIP is an extension of [Asset standard](eip4.md) and tends to standardize artwork issuance in particular.

## Design V1

There are two important boxes in the issuance process of an artwork.

- The issuance box, which follows [Asset standard](eip4.md) depending on the type of artwork.
- The issuer box, which is the first input of the transaction that is issuing the artwork. In particular, the box with the same ID as the artwork's token ID.

## Keywords
eip-0024, artwork, contract, eip-0024:](https://github.com, ergoplatform, blob, master, eip-0024.md, motivation, discovery, here](https://www.ergoforum.org, design, patterns/222/23?u, anon_real, feature, future, extension, asset, standard](eip4.md, issuance

## Content
## EIP-0024: Artwork Contract
🔗 From EIP-0024:

### Motivation
With the discovery that we can easily use spent boxes in contracts (see here), some new features are introduced for artworks and can be extended further in the future. This EIP is an extension of Asset standard and tends to standardize artwork issuance in particular.

### Design V1
There are two important boxes in the issuance process of an artwork.
The issuance box, which follows Asset standard depending on the type of artwork.
The issuer box, which is the first input of the transaction that is issuing the artwork. In particular, the box with the same ID as the artwork's token ID.
Now we will discuss why the issuer box is important and define a standard for it.
The issuer box is important because it has the same ID as the artwork's token ID and we can include it (although it is spent) in our transactions either in registers or as context data. This means that we can prove/verify certain features that an artwork may have using this box. The following is the v1 standard for this box - which may be extended in the future (refer to Design V2 part).
R4 of this box is an Int, showing 1000 * royalty percentage of the artwork. e.g, 20 for 2% royalty. If R4 of the issuer box of an artowrk is empty or non-positive, then royalty is considered to be 0%.
In the current design of the Auction contranct, proposition bytes of this box is the contract that the royalty percentage will be sent to. This is a suboptimal design because of AOT costing mechanism which is supposed to be replaced with JIT costing with a soft-fork that will happen with v5.0 of ergo node.
As mentioned, royalty amount will go to the propositiona bytes of the issuer box. In the case of a simple proxy contract (proposition bytes of the issuer box), this means that the artist will receive the royalty share. However, the proxy contract may enforce the royalty to go to any other complex contract - e.g., 20% to the artist, and 80% to some charity.

### Design V2
Version 2 of this proposal is created to both extend this proposal to include collections and fix some poor design choices that were caused by the AOT costing issues. The following is the v2 standard for the issuer box.
R4 is an integer showing the artwork standard version. If This register is empty, the type is something other than Int, or the number is greater or equal to 100 then it should be considered as part of V1 design. Otherwise, this register shows the version number for the standard, i.e., 2 for Design V2.

R5 is of type Coll[(Coll[Byte], Int)] that encodes information about royalty recipients and percentages. In particular, a list of royalty recipients and their respective percentage. The Coll[Byte] part is the ergo tree of one of the royalty recipients and the Int part shows 1000 * royalty percentage of this recipient (e.g. 50 if the receipient receives 5% of the sale). The total royalty percentage of the artwork is the sum of percentages of this list. If the list is empty, the artwork's royalty is 0%.
Royalty amount must go to royalty recipients based on the explained share of recipients. An important note here is that it is the responsibility of the auction contract to follow the appropriate version of this standard and consequently send the royalty amount to appropriate recipient(s). 


R6 contains three types of traits:

Properties: These are textual traits such as specifying sex as male.
Levels: These are numerical traits that encode some sort of level-like information such as specifying speed as 60 out of 100.
Stats: These are numerical traits that encode any numerical information about the NFT such as specifying age as 25 out of 50.
Although the structure of levels and stats are similar, they can be considered different in marketplaces both for UI/UX purposes and also for filtering purposes.
The following specifies the structure for traits.
scala
( // properties
  Coll[(  
    Coll[Byte],  // key
    Coll[Byte]   // value
  )],
  ( // levels
    ...

### Artist Identity
Artist identity is very important for any auction house to eliminate NFT copies and scams for the end-users.
The identity of the artist can not necessarily be determined with the issuance box (unless it is a P2PK box) since its correctness can not be verified, e.g., one can impersonate an artist.
Hence, the artist's identity and address are determined with the first P2PK input in the chain of transactions leading to the artwork issuance. This means that in the case of using proxy contracts, the first input of the transaction that is sending the funds to the proxy contract is going to determine the artist's identity.
