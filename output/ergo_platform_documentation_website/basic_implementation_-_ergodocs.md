# Basic Implementation - ErgoDocs
Source: [https://docs.ergoplatform.com/uses/lets/basic-imp/](https://docs.ergoplatform.com/uses/lets/basic-imp/)
Generated: 2025-05-11

## Summary
The basic blueprint of our system encompasses two contracts: an administrative contract and a trade contract. Before delving into the details, we recommend acquainting yourself with the foundational aspects of Ergo by reviewing this ICO article as well as ErgoScript tutorials. Despite the aforementioned recommendations, we will elucidate a few novel terms in the upcoming sections. In Ergo, when a token is minted with a value of one, it is termed a singleton token. Similarly, a box containing a singleton token is known as a singleton box.

## Keywords
blueprint, system, contract, trade, detail, aspect, ergo, article, ergoscript, tutorial, recommendation, term, section, token, value, singleton, committee, composition, time, logic

## Content
### Overview#
The basic blueprint of our system encompasses two contracts: an administrative contract and a trade contract. Before delving into the details, we recommend acquainting yourself with the foundational aspects of Ergo by reviewing this ICO article as well as ErgoScript tutorials.
Despite the aforementioned recommendations, we will elucidate a few novel terms in the upcoming sections.

#### Singleton Tokens and Boxes#
In Ergo, when a token is minted with a value of one, it is termed a singleton token. Similarly, a box containing a singleton token is known as a singleton box.

#### Purpose#
The administrative contract oversees a singleton box that encompasses the members of the LETS system. 
This contract facilitates the addition of new members, at a rate of one member per transaction. 
Instead of storing members, the box merely holds a succinct digest of an authenticated data structure based on the members' directory. 
Each member is linked with a singleton token minted during a transaction that adds the member to the directory. 
This transaction generates a new member's box, housing the member's singleton token. 
The trade contract safeguards the member's box. 
Moreover, the freshly generated member's box records the initial balance in the R4 register, which in this case is zero.
The transaction that adds a new member is obligated to validate the correctness of the directory transformation.

#### Committee Management#
A committee generally manages the administrative contract box, and the composition of this committee may change over time. To accommodate this, we allow the committee's logic to reside in the R5 register. For instance, if a new member is added to both the committee and the LETS system, the incoming administrative contract box would require signatures from two out of three members, while the outgoing box would require three out of four signatures. Consequently, the data within the R5 register of the input and output boxes would vary.
Below, we provide the administrative contract's code written in ErgoScript, complete with comments. Note that userContractHash corresponds to the hash of the trade contract.
val selfOut = OUTPUTS(0)

    // Administrative script
    val adminScript = selfOut.R5[SigmaProp].get

    // Confirming that the script replicates itself and the administrative script is satisfied
    val scriptIsCorrect = (selfOut.propositionBytes == SELF.propositionBytes) && adminScript

    // A spending transaction creates boxes for the directory, user, and fee
    val isOutputSizeCorrect = OUTPUTS.size == 3

    // Verifies the replication of the administrative label token 
    val isTokenOutputCorrect = (selfOut.tokens.size == 1) && (selfOut.tokens(0)._1 == letsToken)

    // Validates the issuance of a new token and its amount
    // OUTPUTS(0) tokens are already checked via isTokenOutputCorrect
    val issuedTokenId = INPUTS(0).id
    val userOut = OUTPUTS(1)
    val areTokenAmountsCorrect =
      (userOut.tokens.size == 1 &&
        userOut.tokens(0)._1 == issuedTokenId &&
        userOut.tokens(0)._2 == 1 &&
        OUTPUTS(2).tokens.size == 0 &&
        isTokenOutputCorrect)

    // Verifies that the new user is created with a zero balance
    val isUserBalanceZero  = userOut.R4[Long

].get == 0

    val isUserScriptProper = blake2b256(userOut.propositionBytes) == userContractHash

    // Validates the addition of the new token identifier to the director...
