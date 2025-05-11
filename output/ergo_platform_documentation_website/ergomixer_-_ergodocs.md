# ErgoMixer - ErgoDocs
Source: [https://docs.ergoplatform.com/eco/ergomixer/](https://docs.ergoplatform.com/eco/ergomixer/)
Generated: 2025-05-11

## Summary
ErgoMixer is the first non-custodial, programmable, non-interactive mixer in the space (and the only token mixer to our knowledge). Download the latest release here ErgoMixer utilises Ergo's Sigma protocols to enable efficient, trustless mixing of funds, enabling a high degree of privacy and security. Introductory Video Tutorials Documentation ErgoMixer introduces two privacy-centric features to transactions on the Ergo blockchain: Covert Addresses and Stealth Addresses. These methods are designed to obscure the linkage between transactions and a user's public address, adding a layer of anonymity not common in standard blockchain transactions. Covert Addresses are akin to having a pseudonym in the blockchain world.

## Keywords
ergomixer, mixer, space, knowledge, release, ergo, sigma, protocol, trustless, mixing, fund, degree, privacy, security, introductory, video, tutorials, documentation, feature, transaction

## Content
## ErgoMixer#
ErgoMixer is the first non-custodial, programmable, non-interactive mixer in the space (and the only token mixer to our knowledge).
Download the latest release here
ErgoMixer utilises Ergo's Sigma protocols to enable efficient, trustless mixing of funds, enabling a high degree of privacy and security.

### Features#
Token mixing
Covert Addresses
Stealth Addresses
Token Mixing
SigmaUSD minting
Tor support
Introductory
Ergo: What are 'Mixers' ?
ErgoMixer ELI5
Video Tutorials
ErgoMixer Tutorial - Taking Fire
How to set up and configure mixer on Windows
Video: How to mix tokens with ErgoMixer
Documentation
Technical Paper
Presentation
GitHub

### Enhanced Privacy: Covert and Stealth Addresses#
ErgoMixer introduces two privacy-centric features to transactions on the Ergo blockchain: Covert Addresses and Stealth Addresses. These methods are designed to obscure the linkage between transactions and a user's public address, adding a layer of anonymity not common in standard blockchain transactions.

#### Covert Addresses#
Covert Addresses are akin to having a pseudonym in the blockchain world. They allow a user to showcase a public-facing address that doesnât directly tie back to their actual wallet address. This is highly beneficial for individuals, like shop owners, who wish to receive payments without revealing their true wallet address to every customer, aiding in preventing the tracking of transactions linked to their personal wallet. Typically, this involves generating a new address that redirects to the user's real address, keeping the true address concealed from public view.

#### Stealth Addresses#
Stealth Addresses elevate user privacy by creating a unique, one-time address for every transaction, even between the same parties. This feature is invaluable for situations where users wish to publicly display an address, like on a website, for receiving multiple transactions. Given that each transaction utilizes a unique address, linking them to each other or to the original published address becomes nearly impossible. The functionality hinges on a non-interactive cryptographic procedure. Initially, the recipient shares a Stealth Address. When a sender wants to make a payment, they use the shared Stealth Address to generate a unique Stealth Payment Address for that particular transaction. The recipient, with the right private key, can identify and access funds sent to this Stealth Payment Address. In Ergo's setup, this is facilitated through a variant of the Diffie-Hellman key exchange, ensuring a secure cryptographic key exchange over a public channel.
Both Covert and Stealth Addresses aim to amplify transactional privacy. However, Stealth Addresses, with their per-transaction uniqueness, provide a superior level of privacy, significantly hampering any transaction tracking efforts.
See the Stealth Addresses page for more information.

### Tor support#
Since ErgoMixer v3.0.0, there is Tor support available.

### Resources#
A tutorial for importing magnum (or any other wallet)
Second ErgoMix vulnerability blog post (fixed in 2020) 
2020: ErgoMixer, ZeroJoin Mixer for ERG and Tokens
2019: ErgoMix: approximately fair mining fees
2019: Paying fee in ErgoMix in primary tokens
More on ergoforum.org
Join #ergomixer on Discord
