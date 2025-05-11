# Reversible Address - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/tx/reversible-address/](https://docs.ergoplatform.com/dev/scs/tx/reversible-address/)
Generated: 2025-05-11

## Summary
A reversible address is an example of a multi-stage contract designed with anti-theft features. It functions as follows: funds sent to this address can initially only be spent in a way that allows the payment to be reversed by a trusted party for a specific period. After this period, only the intended recipient can spend the funds. This mechanism is particularly useful for managing hot wallets (e.g., for exchanges or mining pools handling customer withdrawals). A hot wallet's private key is typically stored on a server, making it vulnerable to compromise and theft.

## Keywords
address, example, contract, feature, fund, payment, party, period, recipient, mechanism, wallet, exchange, mining, pool, customer, withdrawal, server, compromise, theft, case

## Content
## Reversible Addresses#
A reversible address is an example of a multi-stage contract designed with anti-theft features. It functions as follows: funds sent to this address can initially only be spent in a way that allows the payment to be reversed by a trusted party for a specific period. After this period, only the intended recipient can spend the funds. This mechanism is particularly useful for managing hot wallets (e.g., for exchanges or mining pools handling customer withdrawals). A hot wallet's private key is typically stored on a server, making it vulnerable to compromise and theft. To recover funds in case of such a compromise, a trusted party (with a private key stored securely offline) can intervene.
The reversible address uses a two-stage protocol. The first stage ensures that withdrawals from the hot wallet adhere to specific rules, creating outputs protected by a second-stage script. The second stage allows either the intended recipient (after a delay) or the trusted party (before the delay) to spend the funds. If an unauthorized transaction is detected originating from the hot wallet (first stage), the trusted party can use their private key to trigger an abort procedure on the second-stage boxes, diverting the funds to a secure address. Besides securing hot wallets, these addresses can be used for automated-release escrow payments in online shopping.
Let's assume:
*   alice represents the SigmaProp (public key) of the hot wallet.
*   carol represents the SigmaProp of the trusted party (whose private key is stored offline and used for reversals).
*   blocksIn24h is a constant representing the estimated number of blocks in 24 hours (the reversal period).
*   bob represents the SigmaProp of a customer wishing to withdraw funds.
In Ethereum, a similar outcome might be achieved by sending funds to an account with a contract (let's call it Cb) that allows carol to withdraw funds for blocksIn24h blocks, after which only bob can withdraw. While the same contract instance could handle...
