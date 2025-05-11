# Auction Contract - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/tokens/standards/eip22/](https://docs.ergoplatform.com/dev/tokens/standards/eip22/)
Generated: 2025-05-11

## Summary
ð From EIP-0022: Decentralized auctioning of any kind of tokens (artwork, share tokens, etc.) is an important part of any blockchain. This EIP is proposing the auction contract with various features listed in the Design section This proposed contract allows any kind of tokens to be auctioned while supporting the following features:

## Keywords
ð, eip-0022, kind, token, artwork, share, part, blockchain, auction, contract, feature, design, section

## Content
## EIP-0022: Auction Contract#
ð From EIP-0022:

### Motivation#
Decentralized auctioning of any kind of tokens (artwork, share tokens, etc.) is an important part of any blockchain. This EIP is proposing the auction contract with various features listed in the Design section

### Design#
This proposed contract allows any kind of tokens to be auctioned while supporting the following features:
Any token as the auction's currency alongside ERG
"Buy it now" which allows a buyer to instantly buy the auctioned token by paying the predefined amount in the auction's currency
Auction duration as timestamp which is much more precise than block height and is independent of the network difficulty
Auto extending the duration near the end of the auction based on a global config
Minimum bid step - each bidder has to increase the previous bid at least by this amount
Royalty - The original owner (whomever issued the token) gets a share of the auction every time his/her token is auctioned using a global config

### The contract#
{
  // R4: The seller's ergo tree
  // R5: Current bidder's ergo tree
  // R6: (Minimum bid, minimum step)
  // R7: The auction's end time in timestamp
  // R8: The auction's "Buy it now" amount. -1 if it is not enabled.
  // R9: Auction info that is needed for UI/UX purposes - stringfied json encoded as Coll[Byte]:
  //     - initialBid: The auction's initial bid
  //     - startTime: The auction's start time
  //     - description: The auction's description
  //     - Any other info needed in the future
  //
  // tokens(0): auctioned token
  // tokens(1): current bid for non-ERG auctions - doesn't exist otherwise
  //
  // dataInputs(0): Auction house configuration - contains configs like UI fee and artist fee
  //     - R4: UI fee in thousand, e.g. 10 for 1% or 5 for 0.5%
  //     - R5: UI implementor's ergo tree
  //     - R6: Maximum miner fee for withdrawal
  //     - R7: Extend configuration as a Coll[Long] with two values (extendThreshold, extendNum)
  //             e.g., (30 * 60 * 1000L, 40 * 60 * 1000L) to extend the duration for 40min if 30min is left when the bid is placed

  // originalIssuanceBox: Spent box with ID equal to the NFT ID
  //     - R4: Royalty percentage - 0 if empty
  //     - R5: Artist address

  val seller = SELF.R4[Coll[Byte]].get
  val currBidder = SELF.R5[Coll[Byte]].get
  val minBid = SELF.R6[Coll[Long]].get(0)
  val minStep = SELF.R6[Coll[Long]].get(1)
  val endTime = SELF.R7[Long].get
  val buyItNowAmount = SELF.R8[Long].get

  // auction currency can be any token like SigUSD
  val auctionCurrency = if (SELF.tokens.size > 1) SELF.tokens(1)._1
                        else Coll[Byte]()
  val isCurrencyERG = auctionCurrency.size == 0
  val getBoxVal = {(b: Box) => {
     if (isCurrencyERG) b.value
     else {
       if (b.tokens.size == 1 && b.tokens(0)._1 == auctionCurrency) b.tokens(0)._2
       else if (b.tokens.size == 2 && b.tokens(1)._1 == auctionCurrency) b.tokens(1)._2
       else 0L
     }
  }}

  val currBid = getBoxVal...
