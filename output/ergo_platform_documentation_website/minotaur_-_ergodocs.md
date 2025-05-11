# Minotaur - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/wallet/minotaur/](https://docs.ergoplatform.com/dev/wallet/minotaur/)
Generated: 2025-05-11

## Summary
Minotaur stands as the inaugural multi-platform wallet tailored for the Ergo ecosystem, offering a suite of features designed to enhance user experience. For a visual and detailed guide on how to use Minotaur, watch the comprehensive video tutorial available here. Ensure Node.js version 20.11 is installed before attempting to build Minotaur: Open the android directory within the project using Android Studio and proceed with the build process using the IDE or alternative build tools. iOS developers can open the project in Xcode and build the desired version directly from the IDE. For desktop builds, enter the Electron directory and execute the following commands:
   npm run build
npm run electron:pack
npm run electron:make Apple Silicon (M-series) users should opt for the arm64 build to avoid camera issues.

## Keywords
minotaur, wallet, ergo, ecosystem, suite, feature, user, experience, guide, video, tutorial, node.js, version, directory, project, android, studio, build, process, tool

## Content
## Minotaur Wallet#
Minotaur stands as the inaugural multi-platform wallet tailored for the Ergo ecosystem, offering a suite of features designed to enhance user experience.
Comprehensive Video Guide
For a visual and detailed guide on how to use Minotaur, watch the comprehensive video tutorial available here.

### Key Features:#
Wallet generation and restoration compatible with Yoroi, Ergo node, and Ergo's Android app.
Supports mnemonic phrases of various lengths: 12, 15, 18, 21, and 24 words.
Mnemonic passphrase for additional security.
Read-only wallet functionality.
Integration with cold wallet devices.
Token and NFT management:
Displays token names as per EIP-04 standards.
Facilitates token transactions.
Enables issuing and burning of tokens within dApps.


Transaction display within the wallet, including pre-signing transaction previews.
Embedded dApp support, with three dApps currently available for token issuance, token burning, and sigma-usd operations.
Cross-platform support for Android, iOS, Windows, MacOS, and Linux.
Wallet encryption via user-defined password.
ErgoPay integration for seamless transactions.

### Upcoming Features:#
Dynamic dApp integration protocol to add new dApps without requiring wallet updates.
Minotaur dApp connector extension for Chrome and Firefox.
Multilingual wallet interface.
Mempool transaction monitoring.

### Building the Wallet from Source#
Ensure Node.js version 20.11 is installed before attempting to build Minotaur:
Clone the repository:
   git clone [email protected]:minotaur-ergo/minotaur-wallet.git

Navigate to the cloned directory and install dependencies:
   cd minotaur-wallet
npm install

Build the project with the following commands:
   npm run build
npx cap sync
npx cap update

   The last two commands synchronize the codebase for Android and iOS platforms. For desktop builds, synchronize the Electron code with:
   npx cap sync electron
npx cap update electron

#### Android#
Open the android directory within the project using Android Studio and proceed with the build process using the IDE or alternative build tools.

#### iOS#
iOS developers can open the project in Xcode and build the desired version directly from the IDE.

#### Desktop#
For desktop builds, enter the Electron directory and execute the following commands:
   npm run build
npm run electron:pack
npm run electron:make

#### MacOS#
Apple Silicon (M-series) users should opt for the arm64 build to avoid camera issues. If encountering a "damaged file" error, execute:
   sudo xattr -r -d com.apple.quarantine /Applications/minotaur.app

### Support the Developer#
Contributions are appreciated and help fuel ongoing development. To tip the developer, send your support to:
9hN2UY1ZvvWMeWRBso28vSyjrAAfGJHh2DkZpE47J7Wqr51YLAR

### Testnet Trials#
Minotaur is compatible with both Mainnet and Testnet. To test the wallet, generate a new wallet and acquire test Ergos from Ergo's Testnet Faucet.
