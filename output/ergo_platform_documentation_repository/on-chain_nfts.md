# On-chain NFTs
Source: docs/dev/tokens/nfts/on-chain.md
Generated: 2025-05-11

## Summary
---
tags:
  - On-Chain NFTs
  - NFTs
  - On-Chain
---


# On-chain NFTs

/// admonition | Warning
    type: warning

This method is not yet incorporated in [EIP-0004: Asset Standard](eip4.md). For more information, refer to this discussion [on Discord](https://discord.com/channels/668903786361651200/940209605299036170/942656843619106827). ///

## On-chain NFTs: Technical Aspects

On-chain NFTs on Ergo differ from [regular NFTs](#the-technical-aspects-of-regular-ergo-nfts) as they store images directly on the blockchain, specifically in the `R9` register of the NFT box. This eliminates the need for third-party storage. However, this comes with a size constraint.

## Keywords
chain, nfts, admonition, warning, type, method, eip-0004, asset, standard](eip4.md, information, discussion, discord](https://discord.com, channels/668903786361651200/940209605299036170/942656843619106827, technical, aspects, ergo, aspect, image, blockchain, register

## Content
## On-chain NFTs
/// admonition | Warning
    type: warning
This method is not yet incorporated in EIP-0004: Asset Standard. For more information, refer to this discussion on Discord.
///

### On-chain NFTs: Technical Aspects
On-chain NFTs on Ergo differ from regular NFTs as they store images directly on the blockchain, specifically in the R9 register of the NFT box. This eliminates the need for third-party storage. However, this comes with a size constraint. The maximum size for on-chain NFTs on Ergo is approximately 3.5 Kb, considering space for the NFT name, description, and other data within the total 4 Kb limit. This constraint challenges artists to create captivating pieces within a limited space.
Steps to create an on-chain SVG:
Draw a relatively simple image in SVG vector format and manually optimize your art: smooth lines, remove minor details, reduce the number of colors, etc. Further optimize using svg-optimizers.
Convert your *.svg file to Data URI format (there are many online/offline converters available).
Check if your data fits within the 4 kb box limit (<3.5 Kb). If not, return to the first step.
Place this data in the R9 register.
Most challenging part: Mint the NFT using a tool that allows you to manipulate the R9 register.
/// admonition | Textual Data
    type: tip
If the data is textual, you can embed the text (using the appropriate entities or escapes based on the enclosing document's type). Otherwise, you can specify base64 to embed base64-encoded binary data.
///

#### Examples of On-chain Collections
Vector Minimalism collection:
Landscape #06. View from the train window
Landscape #08. Flight over the desert
Monument #11. Moai
Monument #02. Spring Temple Buddha
Tokenart collection uses SVG as a container for ASСII art:
Tokenart Cat #2 
Tokenart Shark #2
The SVG contains pure text:

### A Brief History
During the spring and summer of 2021, there were several on-chain projects on Cardano. For instance, the on-chain interactive NFT stored an entire HTML page with JS in its metadata. However, if we delve deeper into history, we find that the pioneers were the team from Larva Labs with their autoglyphs project, which was an ETH smart contract dated April 2019.
The NFT hype in the fall of 2021 led to the emergence of guides like this on on-chain NFT mining.
The first Ergo on-chain NFT was minted on 18/8/2021. You can find the related discussion here. This was achieved by transforming the data into a Data URI and encoding it into the R9 register.
/// admonition | Size Restrictions
    type: note
There are no size restrictions for a register, only for the entire box itself, which is limited to 4 Kb.
///

### The Technical Aspects of Regular Ergo NFTs
What should we know about Ergo NFTs?
Let's consider an NFT with the ID
47394b9319353dee45621c5a8d1ffb00cc21c946913f148df5fa4f721fefa8d0, also known as AH v.1 link.
Here's how the NFT's name, description, and URL are stored on each Ergo node, among the 40 GB+ of all blockchain data.
NFT minting transaction on Ergo explorer: Tx


NFT name stored in register R4:



NFT description stored in register R5:



NFT image URL stored in register R9:
You can convert hex to string online
This is the underlying structure of the majority of NFTs on all blockchains (Ergo, Cardano, Ethereum, etc). In essence, only the name, description, and image link are stored on the blockchain (other technical parameters depending on the blockchain/NFT standard have been omitted for simplicity).
The image itself is stored on a third-party storage service (like ipfs, imgbb.com, etc).
