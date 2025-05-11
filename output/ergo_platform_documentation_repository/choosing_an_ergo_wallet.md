# Choosing an Ergo Wallet
Source: docs/dev/wallets.md
Generated: 2025-05-11

## Summary
---
title: Choosing an Ergo Wallet
description: An overview of recommended Ergo wallets for different platforms and use cases, including mobile, desktop, browser extensions, and cold storage. tags:
  - Wallet
  - Mobile Wallet
  - Desktop Wallet
  - Browser Extension
  - Cold Storage
  - Security
  - Getting Started
---

# Choosing an Ergo Wallet

A wallet is your essential gateway to the Ergo ecosystem. It allows you to securely store, send, and receive ERG and other [tokens](tokens.md) built on Ergo, as well as interact with [decentralized applications (dApps)](get-started.md). Choosing the right wallet depends on your technical comfort, security needs, and how you plan to use Ergo. <!--

## Keywords
title, ergo, wallet, description, overview, platform, case, mobile, desktop, browser, extension, storage, cold, security, gateway, ecosystem, tokens](tokens.md, interact, application, dapps)](get

## Content
## Choosing an Ergo Wallet
A wallet is your essential gateway to the Ergo ecosystem. It allows you to securely store, send, and receive ERG and other tokens built on Ergo, as well as interact with decentralized applications (dApps). Choosing the right wallet depends on your technical comfort, security needs, and how you plan to use Ergo.
!!! warning "Disclaimer"
    The wallets listed here are primarily developed and maintained by independent teams within the Ergo community. Always download software from official sources linked here and practice strong security habits (like safeguarding your seed phrase). This information is for guidance only; conduct your own research before entrusting funds to any wallet.

### How to Choose a Wallet?
Consider these common needs:
📱 Mobile Use: If you need access to your funds primarily on your smartphone (iOS or Android), look at Mobile Wallets.
💻 Desktop Management: If you prefer managing funds on your computer (Windows, macOS, Linux), check out Desktop Wallets.
🌐 dApp Interaction: If you plan to frequently interact with Ergo dApps directly through your web browser, a Browser Extension Wallet is often the most convenient.
🔒 Maximum Security / Long-Term Storage: For storing significant amounts of ERG or holding funds offline ("cold storage"), consider a Paper Wallet or the offline/cold wallet features available in some mobile/desktop wallets.

### Recommended Wallets by Type
Here are popular and well-regarded wallets used by the Ergo community:

#### Mobile Wallets (iOS & Android)
Ergo Mobile Wallet (Terminus on iOS)

Description: A user-friendly, feature-rich mobile wallet. Supports ERG, tokens, NFTs, creating offline ("cold") wallets, and ErgoPay QR code scanning. A community favorite.
Best For: Everyday mobile use, managing diverse assets, easy payments.



Minotaur Wallet

Description: Offers advanced features like multi-signature capabilities (requiring multiple approvals for transactions).
Best For: Users needing shared fund control or enhanced security via multi-sig. May be more complex for beginners. (Note: Check development status for latest features/stability).

#### Browser Extension Wallets
Nautilus Wallet
Description: A very popular browser extension wallet (similar to MetaMask). Enables seamless connection to Ergo dApps. Manages ERG, tokens, and NFTs. Includes privacy features and transaction optimization.
Best For: Users frequently interacting with DeFi, NFT marketplaces, and other web-based Ergo applications.

#### Desktop Wallets
Satergo Wallet

Description: A desktop wallet specifically designed to run alongside a full Ergo Node. Provides a user-friendly interface for managing funds while contributing to network decentralization.
Best For: Users who want to run their own full node for maximum trust and verification, without needing complex command-line interaction.



Node Wallet (Core)

Description: The basic wallet functionality built into the core Ergo reference node software. Accessed via command line or API.
Best For: Developers or advanced users comfortable with command-line interfaces who are already running a core node. Satergo offers a graphical alternative for node users.

#### Other Wallet Types
SAFEW Wallet

Description: A web-based wallet (accessed via a website, requires careful URL verification). Offers advanced features like ErgoMixer integration (for enhanced privacy) and developer tools.
Best For: Experienced users needing specific features like mixing or advanced transaction control.



Ergo Paper Wallet

Description: A method to generate wallet keys offline and print them on paper (or save securely offline). Provides maximum security from online threats.
Best For: Long-term "cold storage" of significant amounts, gifting ERG. Less convenient for frequent use.

### Quick Comparison Table
This table provides a simplified overview to help you compare options:
| Wallet Type             | Platform(s)        | Ease of Use (Beginner) | Connects to dApps? | Good for Offline/Cold Storage? | Key Feature                                    |
|-------------------------|--------------------|------------------------|--------------------|--------------------------------|------------------------------------------------|
| Ergo Mobile / Terminus  | iOS, Android       | High                   | Limited (ErgoPay)  | Yes (via offline mode)         | Convenient mobile use, NFT support             |
| Nautilus                | Browser Extension  | Medium                 | Yes (Directly)     | No                             | Seamless dApp interaction, popular             |
| Satergo                 | Desktop (Win/Mac/Lin)| Medium                 | No                 | Yes (if PC is offline)         | User-friendly full node wallet                 |
| SAFEW                   | Web                | Medium-Low             | Yes (Directly)     | No                             | Advanced features, Mixer access                |
| Minotaur                | Mobile             | Medium-Low             | Limited (ErgoPay)  | Yes (via offline mode)         | Multi-signature security                       |
| Paper Wallet            | Offline Generation | N/A (Setup is simple)  | No                 | Yes (Primary purpose)          | Maximum security for long-term holding         |
| Node Wallet (Core)      | Desktop (Win/Mac/Lin)| Low                    | No                 | Yes (if PC is offline)         | Integrated with core node (Advanced users)     |
!!! details "Advanced Feature Comparison (Expand)"
    The table below provides a more detailed technical comparison based on community contributions. Note: TBC means the feature status needs confirmation.
| Features                     | Satergo   | Nautilus |   Terminus   | Minotaur |  SafeW  | Node Wallet | Paper Wallet |
|----...

### Additional Resources
PDF Guide: Ergo Wallet Wonderland: Exploring the Best Wallet for Your Needs (May require update)
Developer: SwiftAPI for iOS Wallet Dev
Community Project: Ergo Light Client (iOS Beta) (Requires a full node)
