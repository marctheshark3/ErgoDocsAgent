# ErgoPay - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/wallet/payments/ergopay/ergo-pay/](https://docs.ergoplatform.com/dev/wallet/payments/ergopay/ergo-pay/)
Generated: 2025-05-11

## Summary
ErgoPay is Ergo's dedicated dApp connector for non-web wallet applications. It has been fully operational for some time now and has been thoroughly tested by end-users. While many may associate a dApp connector with a bridge between a website-based dApp and a browser extension wallet, like Yoroi and Metamask, not all users prefer to use a web extension wallet, and not all dApps are websites. To cater to this diversity, ErgoPay was developed, a versatile connector that can link any wallet with any dApp. For a non-technical overview of ErgoPay, click here.

## Keywords
ergopay, ergo, dapp, connector, wallet, application, time, user, bridge, website, browser, extension, yoroi, metamask, dapps, diversity, overview, demonstration, burn, token

## Content
## ErgoPay#
ErgoPay is Ergo's dedicated dApp connector for non-web wallet applications. It has been fully operational for some time now and has been thoroughly tested by end-users.
While many may associate a dApp connector with a bridge between a website-based dApp and a browser extension wallet, like Yoroi and Metamask, not all users prefer to use a web extension wallet, and not all dApps are websites. To cater to this diversity, ErgoPay was developed, a versatile connector that can link any wallet with any dApp. For a non-technical overview of ErgoPay, click here.
ErgoPay was integrated into Ergo Wallet App 1.6, and a demonstration dApp for minting and burning tokens has been live for a while.
If you're interested in trying it out, follow these steps:
Ensure you have installed Ergo Wallet App 1.6. It's available on Google Play (join) and on TestFlight (DM me your Apple ID to join). Alternatively, download the APK on GitHub and sideload.
Visit the demonstration app: https://golfgl.de/ergopayshowcase/. ErgoPay supports both mobile and desktop devices, and even Cold wallets.
The demonstration dApp has a menu on the left side where you can choose to mint a new token or burn a token. The dApp supports both testnet and mainnet, and will automatically detect this through the information provided by ErgoPay.
To mint a token, enter the required information and scan the presented QR code with your wallet app if you are on a desktop. If you are on mobile, tap the button to open the wallet app. The wallet app will ask which wallet should process the request, and a confirmation screen will show you the transaction details.
Confirm the transaction and wait for your new token to be minted once the transaction is confirmed. (Note: Emojis in the token name are supported.)
To burn a token, select the "Burn a token" option from the demonstration dApp. For this, the dApp needs to connect to your wallet to display a list of available tokens to burn. Do this by scanning the QR code or tapping the ...

### Implementing a dApp using ErgoPay#
Ergo Wallet App 1.6 and above support ErgoPay, a protocol that facilitates transaction data exchange with dApps. With ErgoPay, your dApp can prepare a transaction for the user to sign within their wallet app. The user can then choose to accept or decline the transaction. This ensures that the user's secrets never leave their device and they can verify the transaction before confirming it.

#### ErgoPay vs web dApp connector#
ErgoPay differs from a web dApp connector like those provided by SAFEW and Nautilus wallet in its versatility. While a web dApp connector is limited to web extension wallets and website dApps, ErgoPay can connect any wallet with any dApp. However, this means that some of your dApp logic must run on a server that can be accessed by userâs wallet applications. For a website dApp, this means that some of your code needs to live on your backend. This doesn't necessarily complicate things. In fact, on the backend, you aren't restricted to using JavaScript or its derivatives. You are free to choose the language and framework that best suits your needs.

### Resources#
ergopay-payment-portal
