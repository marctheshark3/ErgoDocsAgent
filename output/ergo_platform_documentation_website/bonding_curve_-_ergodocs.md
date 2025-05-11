# Bonding Curve - ErgoDocs
Source: [https://docs.ergoplatform.com/uses/bonding/](https://docs.ergoplatform.com/uses/bonding/)
Generated: 2025-05-11

## Summary
Bonding curves are a useful primitive for continuous token offerings (CTOs), augmented bonded curves, and perhaps AMM DEXes. There is a cheap way to do bonding curves on Ergo, with most of the load performed off-chain. Assume a project is willing to issue 100 tokens and sell the first one for 100 ergs, second for 200, ..., 100th for 10,000 ergs (to raise 505,000) in total in case of full sale. This is a very simple example of a bonding curve. See this article for more details.

## Keywords
bonding, curve, primitive, offering, ctos, dexes, bond, ergo, load, chain, project, token, 100th, total, case, sale, example, article, detail, scenario

## Content
## Bonding Curves#
Bonding curves are a useful primitive for continuous token offerings (CTOs), augmented bonded curves, and perhaps AMM DEXes.
There is a cheap way to do bonding curves on Ergo, with most of the load performed off-chain.
Assume a project is willing to issue 100 tokens and sell the first one for 100 ergs, second for 200, ..., 100th for 10,000 ergs (to raise 505,000) in total in case of full sale. This is a very simple example of a bonding curve. See this article for more details.

### Sell-only#
First, assume a token sale scenario only. The token issuer creates 100 boxes with one token each, with a set price for the token in register R4 of a box. The box is spendable if the spending transaction pays the price to the issuer's address (issuer's script in general).

### Sell with buy-back#
Now assume that token sell comes with a buy-back guarantee, e.g. seller is buying back tokens within one year since selling for 95% of the selling price. The selling contract requires a spending transaction to lock 95% of the price, at least with buying contract. Buying contract is time-locked and requires a spending transaction to send token bought-back to a predefined address (e.g. issuer's).

### Clients#
As the curve is made upon many boxes, some work is required on the client-side, namely the possibility of finding boxes associated with the token and selling-script, and then sorting the boxes by R4.
