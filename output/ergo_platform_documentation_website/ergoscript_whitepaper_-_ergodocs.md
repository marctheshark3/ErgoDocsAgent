# ErgoScript Whitepaper - ErgoDocs
Source: [https://docs.ergoplatform.com/doc/ergoscript-whitepaper/](https://docs.ergoplatform.com/doc/ergoscript-whitepaper/)
Generated: 2025-05-11

## Summary
Authors: Ergo Developers This paper describes \(\langname\), a powerful and protocol-friendly scripting language for cryptocurrencies. Programs in \(\langname\) are used to specify the conditions under which currency can be spent. The language supports a type of non-interactive zero-knowledge proofs called \(\Sigma\)-protocols and is flexible enough to allow for ring-signatures, multisignatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation. Since its early days, Bitcoin[@Nak08] has allowed more than simple money transfers between two public keys: its Bitcoin Script scripting language has allowed participants to specify conditions for how money could be spent. A program written in Bitcoin Script is attached to every transaction output (i.e., amount received); this program protects the transaction by determining how the transaction output can be used as an input to (i.e., spent in) a future transaction.

## Keywords
author, ergo, developers, paper, \(\langname\, protocol, scripting, language, cryptocurrencie, program, condition, currency, type, knowledge, proof, \(\sigma\)-protocol, ring, signature, multisignature, swap

## Content
## ErgoScript, a Cryptocurrency Scripting Language Supporting Noninteractive Zero-Knowledge Proofs#
Authors: Ergo Developers

### Abstract#
This paper describes \(\langname\), a powerful and protocol-friendly scripting language for cryptocurrencies. Programs in \(\langname\) are used to specify the conditions under which currency can be spent. The language supports a type of non-interactive zero-knowledge proofs called \(\Sigma\)-protocols and is flexible enough to allow for ring-signatures, multisignatures, multiple currencies, atomic swaps, self-replicating scripts, and long-term computation.

#### Background#
Since its early days, Bitcoin[@Nak08] has allowed more than simple money transfers between two public keys: its Bitcoin Script scripting language has allowed participants to specify conditions for how money could be spent. A program written in Bitcoin Script is attached to every transaction output (i.e., amount received); this program protects the transaction by determining how the transaction output can be used as an input to (i.e., spent in) a future transaction. The simplest condition is specified by a program that contains the recipient's public key and states that the money can be spent by creating a signature that verifies under this key. However, more general conditions are allowed by more sophisticated programs.
The Bitcoin Script language is a primitive stack-based language without loops[@bscript]. To spend an output protected by a program, a spending transaction must provide a program in the same language, and the concatenation of the two programs must evaluate to true. The creator of the spending transaction can be viewed as a prover (for example, proving knowledge of the secret key by producing a signature), where the statement that needs to be proven is specified by the output that is being spent. Transaction validity is verified by evaluating programs. Bounded validation time is ensured by the absence of loops in the programming language and a maximum program size of 10 kilobytes. Even so, some denial-of-service attacks exploiting script validation time have appeared [@bitcoindos] [@fivehrs] [@ethattacks]. On the other hand, the deliberate simplicity of the programming language limits the kinds of contracts that can be created on the Bitcoin platform.
On other end of the generality spectrum, Ethereum allows for arbitrary Turing-complete programs[@wood2014ethereum]. This approach requires charging for computation, in order to prevent denial-of-service attacks, because the running time of a Turing-complete program cannot, in general, be estimated without...

#### Our Contribution: ErgoScript#
In this paper we introduce a new language called \(\langname\) that is specifically designed to be friendly to cryptographic protocols and applications. \(\langname\) is considerably more powerful than Bitcoin Script. As \(\langname\) contains no unbounded looping or recursive constructs, individual scripts in \(\langname\) are not Turing-complete. In fact, given a program in \(\langname\), it is easy to obtain an estimate of its running time. However, because \(\langname\) allows for self-replication, \(\langname\) can be used to create Turing-complete processes in a blockchain, as shown in [@CKM18] (see also Self-Replicating Code).

##### Built-in \(\Sigma\)-protocols#
Our new language incorporates proving and verifying as first-class primitives, giving developers access to a subclass of cryptographic proof systems known as non-interactive \(\Sigma\)-protocols (pronounced "sigma-protocols"). Thus, a script protecting a transaction output can contain statements (\(\Sigma\)-statements) that need to be proven (by producing \(\Sigma\)-proofs) in order to spend the output.
Conceptually, \(\Sigma\)-proofs [@Cra96] are generalizations[@CL06] of digital signatures. In fact, Schnorr signature scheme[@Sch91] (whose more recent version is popularly known as EdDSA [@BDLSY12,@rfc8032]) is the canonical example of a \(\Sigma\)-proof: it proves that the recipient knows the discrete logarithm of the public key (the proof is attached to a specific message, such as a particular transaction, and thus becomes a signature on the message; all \(\Sigma\)-proofs described here are attached to specific messages). \(\Sigma\)-protocols exist for proving a variety of properties and, importantly for \(\langname\), elementary \(\Sigma\)-protocols can be combined into more sophisticated ones using the techniques of [@CDS94]. For an introduction to \(\Sigma\)-protocols, we refer the reader to [@Dam10] and [@HL10].
\(\langname\) provides two elementary \(\Sigma\)-protocols over a group of prime order (such as an elliptic curve), written here in multiplicative notation:
A proof of knowledge of discrete logarithm with respect to a fixed group generator: given a group element \(h\), the proof convinces a verifier that the prover knows \(w\) such that \(h=g^w\), where \(g\) is the group generator (also known as base point), without revealing \(w\). This is the same as a Schnorr signature with public key \(h\).
A proof that of equality of discrete logarithms (i.e., a proof of a Diffie-Hellman tuple): given group elements \(g_1, g_2, u_1, u_2\), the proof convinces a verifier that the prover knows \(w\) such that \(u_1=g_1^w\) and \(u_2=g_2^w\), without revealing \(w\)...

##### Rich context, enabling self-replication#
In addition to \(\Sigma\)-protocols, \(\langname\) allows for predicates over the state of the blockchain and the current transaction. These predicates can be combined, via Boolean connectives, with \(\Sigma\)-statements, and are used during transaction validation. The set of predicates is richer than in Bitcoin, but still lean in order to allow for efficient processing even by light clients. Like in Bitcoin, we allow the use of current height of the blockchain; unlike Bitcoin, we also allow the use of information contained in the spending transaction, such as inputs it is trying to spend and outputs it is trying to create. This feature enables self-replication and sophisticated (even Turing-complete) long-term script behaviour, as described in examples below.
\(\langname\) is statically typed (with compile-time type checking) functional language with first-class lambda expressions, collection, tuple and optional type values, it allows standard operations, such as integer arithmetic, logical and comparison operations as well as operations on group elements and authenticated dictionaries.
In addition to \(\Sigma\)-protocols, \(\langname\) allows for predicates over the state of the blockchain and the current transaction. These predicates can be combined, via Boolean connectives, with \(\Sigma\)-statements, and are used during transaction validation. The set of predicates is richer than in Bitcoin, but still lean in order to allow for efficient processing even by light clients. Like in Bitcoin, we allow the use of current height of the blockchain; unlike Bitcoin, we also allow the use of information contained in the spending transaction, such as inputs it is trying to spend and outputs it is trying to create. This feature enables self-replication and sophisticated (even Turing-complete) long-term script behaviour, as described in examples below.
\(\langname\) is statically typed (with compile-time type checking) functional language with first-class lambda expressions,...

### ErgoScript Language Description#
The language syntax is a subset of Scala with the same meaning, and therefore many of the constructs are easy to read for those familiar with Scala.
Before we describe the language, let us fix some terminology. A box (often called a "coin" in other literature) contains some amount (value, measured in Ergo tokens) and is protected by a script (boxes also contain additional information, such as other tokens; this information is described in detail in Section Box Registers). A transaction spends the value of boxes that are its inputs (which are outputs of some earlier transaction) and produces boxes that are its outputs. In a given transaction, the sum of the values of the inputs must equal the sum of the values of the outputs (as we describe below, the scripting language is rich enough to allow for payment transactions fees and for minting of new coins without violating this rule).
All the unspent transaction outputs (UTXO) at a given time represent the value stored in the blockchain. A script for a box must evaluate to "true" when this box is used as an input to a transaction. This evaluation is helped by a proof (for \(\Sigma\)-statements) and a context, which are part of the transaction. The proof is produced by someone who knows the relevant secrets, such as secret keys; the context contains information about the spending transaction, such as details of its inputs and outputs, and the current state of the blockchain, such as the current height of the blockchain and last 10 block headers from the blockchain.

#### \(\Sigma\)-Statements#
The simplest script allows the owner of a public key to spend an output box in a future transaction by issuing a signature with the corresponding secret key. If the variable \(\texttt{pk}\)holds the public key, then this script is specified simply as a string
$$
\begin{aligned}
        pk
\end{aligned}
$$
In order for the compiler to know what value the variable \(\texttt{pk}\) is referring to, the compiler needs to be supplied with an environment, which, in this case, is a single-element map, mapping the string \(\texttt{"pk"}\)to the object holding the public key.\footnote{This map is an object in Scala, and is passed to the compiler as a parameter together with the script (which is passed in as a string) when the compiler is invoked from within Scala code. We defer the discussion of how to invoke the compiler outside of Scala code to another article.
The value of public key is hardwired into the script at compile time, thus \(\texttt{"pk"}\) can also be called named constant to reflect the fact that it cannot change. When the script is later evaluated (i.e., when the box is used as a transaction input), a \(\Sigma\)-proof of knowledge of the corresponding secret key must be supplied by the prover.
A slightly more complex script may allow either one of two people to spend an box. If Alice owns public key \(\texttt{pkA}\) and Bob owns public key \(\texttt{pkB}\)(with corresponding secret key \(\texttt{skA}\) and $\texttt{skB}), then the script that would allow either one of them to spend the box is
\[
\begin{aligned}
        pkA || pkB
\end{aligned}
\]
Again, \(\texttt{pkA}\) and \(\texttt{pkB}\)need to be mapped to public key objects by an environment map.
Note that Alice and Bob individually can construct the proof necessary to spend this box using just one of the two corresponding secret keys, and, by the zero-knowledge property of \(\Sigma\)-protocols, the proof will not reveal whether \(\texttt{skA}\)or \(\texttt{skB}\) was used. This construct is known as a r...

#### Mixing \(\Sigma\)-statements with other statements#
\(\langname\) allows combining statements that require proofs with other boolean statements. These statements can refer to the context, which has predefined variables with information about the transaction in which the script is evaluated (i.e., the box is spent). For example,
\[
\begin{aligned}
   pkA || pkB || (pkC && HEIGHT > 500)
\end{aligned}
\]
uses the predefined variable HEIGHT, which is the sequential block number (since the beginning of the blockchain, starting at 1) of the block in which the script is evaluated. This script allows Alice or Bob to spend the box before \(\texttt{HEIGHT}\) reaches 501, and Alice, Bob, or Carol to spend the box after that. If the height has not reached 501 and the box is spent, then the proof reveals that \(\texttt{skA}\) or \(\texttt{skB}\) was used in its construction, but does not reveal which one of the two. If \(\texttt{HEIGHT}\) is greater than 500, then the proof does not reveal which of the three secret keys was used. Thus, depending on the value of \(\texttt{HEIGHT}\), the script becomes either equivalent to \(\texttt{pkA || pkB}\) or equivalent to \(\texttt{pkA || pkB || pkC}\).
In general, script evaluation reduces the script to a \(\Sigma\)-statement by first evaluating all the Boolean predicates that are not \(\Sigma\)-statements. As we saw in the above example, the resulting \(\Sigma\)-statement will, in general, depend on the values of the Boolean predicates (such as whether \(\texttt{HEIGHT > 500}\)).
We emphasize that this evaluation is not the same as the usual left-to-right lazy evaluation of logical expressions, because expressions involving \(\Sigma\)-statements are not treated the same way as usual boolean expressions: they are evaluated last and in zero-knowledge.
In fact, \(\texttt{pkA}\) is not of type \(\texttt{Boolean}\). It is a constant of type \(\texttt{SigmaProp}\) with the concrete value \(\texttt{ProveDlog(\texttt{ge})}\), for some public key \(\texttt{ge}\) of \(\texttt{GroupElement}\) type. ...

#### Accessing the Context and Box Contents#
In addition to the predefined variable \(\texttt{HEIGHT}\), the context contains predefined collections \(\texttt{INPUTS}\) and \(\texttt{OUTPUTS}\), which refer to the inputs and outputs of the spending transaction. Elements of these collections are of type \(\texttt{Box}\). The script also has access to its own box via the context variable \(\texttt{SELF}\) of type \(\texttt{Box}\). Note that \(\texttt{SELF}\) is also an element of the \(\texttt{INPUTS}\) collection, because the script is executed when the box is being spent.
To access information inside a box \(\texttt{b}\), scripts can use \(\texttt{b.value}\) for the amount, \(\texttt{b.propositionBytes}\) for the protecting script, and \(\texttt{b.id}\) for the identifier of the box, which is the BLAKE2b-256 hash of the contents of the box. Boxes include additional information in registers;  each box is unique, because one of its registers includes the transaction id in which it was created as an output, and its own index in the outputs of the transaction which created the box, accessible through \(\texttt{b.R3}\) (see Section \(\ref{sec:box-registers}\) for more on registers).

##### Example: two boxes together#
Access to this information allows us, for example, to create an output box that can be spent only in the same transaction as another known box, and only if no other inputs are present in the transaction. If \(\texttt{friend}\) stands for an already existing box (per the environment mapping), then we create a new box that can be spent only together with \(\texttt{friend}\) and no other input by the following script (note that it uses the collection property \(\texttt{size}\) and collection indexing, starting at 0, denoted by parentheses):
\[
\begin{aligned}
        INPUTS.size == 2 && INPUTS(0).id == friend.id
\end{aligned}
\]
Note that the script does not prevent the \(\texttt{friend}\)box from being spent on its own, in which case the output box protected by the script above will become not spendable.
We can be more permissive and allow for other inputs in addition to the friend box. To do so, we will examine the input collection using the \(\texttt{exists}\) operator, which applies a boolean function to each collection element until it finds one that satisfies the function or finds that none exists. To define a function, we use lambda syntax; the argument type (in this case \(\texttt{Box}\)) is specified with a colon after the argument name \(\texttt{inputBox}\). We name the function using the \(\texttt{def}\) keyword.
\[
\begin{aligned}
        {
                def isFriend(inputBox: Box) = inputBox.id == friend.id
                INPUTS.exists (isFriend)
        }
\end{aligned}
\]
This is our first example of a script with more than one statement; note that such scripts require braces, and their output is determined by the last statement.
It can also be written in one statement, as follows:
$$
\begin{aligned}
        INPUTS.exists { (inputBox: Box) => inputBox.id == friend.id }
\end{aligned}
$$

##### Example: crowdfunding#
Access to the context allows us to create a script for the following crowdfunding situation: a project backer (with key  \(\texttt{backerPubKey}\)) wishes to give money to a project (with key \(\texttt{projectPubKey}\)), but only if the project raises enough money (at least \(\texttt{minToRaise}\)) from other sources by a deadline (expressed in terms of \(\texttt{HEIGHT}\)).
To give money to the project, the backer will create an output box protected by the following script. The script contains two conditions: one for the case the deadline has passed (enabling the backer to get the money back) and one for the case it succeeded (enabling the project to spend the money if the amount is at least \(\texttt{minToRaise}\) before the deadline).  In order to ensure enough money has been raised, the script will search the output collection for a box with a sufficient value going to the \(\texttt{projectPubKey}\). To check where the value of the output box is going, the script will read the script protecting the output box and compare it to the script \(\texttt{"projectPubKey"}\) (that is the simple script described in Section 4.2); bytes of this script can be obtained by \(\texttt{projectPubKey.propBytes}\).
{
                val fundraisingFailure = HEIGHT >= deadline && backerPubKey
                val enoughRaised = {(outBox: Box) =>
                        outBox.value >= minToRaise &&
                        outBox.propositionBytes == projectPubKey.propBytes
                }
                val fundraisingSuccess = HEIGHT < deadline &&
                         projectPubKey &&
                         OUTPUTS.exists(enoughRaised)

                fundraisingFailure || fundraisingSuccess
        }
As before, the values of \(\texttt{deadline}\), \(\texttt{minToRaise}\), and the two public keys are defined by the environment map and hardwired into the script at compile time.

#### Context Extension and Hashing#
A context can also contain typed variables that can be retrieved by numerical id using the operator \(\texttt{getVar}\). These variables are supplied by the prover specifically for a given input box (via a \(\texttt{ContextExtension}\)) together with the proof for that box. The id can be any one-byte value (from -128 to 127) and is scoped for each box separately (so variable with id 17 for one input box in a transaction is not the same as variable with id 17 for another input box in the same transaction).
Such context extensions can be useful, for example, for requiring a spending transaction to produce hash preimages (the BLAKE2b-256 and SHA-256 hash functions can be invoked in \(\langname\), using keywords \(\texttt{blake2b256}\) and \(\texttt{sha256}\)). For example,
pkA && blake2b256(getVar[Coll[Byte]](1).get) ==  hashOutput
says that spending can be done only using the signature of Alice, and only if the preimage of \(\texttt{hashOutput}\) is written in the context. Specifically, the script requires that the context extension should contain a variable (with id \(\texttt{1}\)), which is a collection of bytes that hashes to the value of \(\texttt{hashOutput}\) (the value of \(\texttt{hashOutput}\), like \(\texttt{pkA}\), is defined in the environment and is hardwired into the script at compile time).  Note that although the script requires both the secret key corresponding to \(\texttt{pkA}\) and the hash preimage corresponding to \(\texttt{hashOutput}\), there is the stark difference between how these two values are used: the secret key is not revealed in the proof (by the zero-knowledge property of \(\Sigma\)-proofs), while the hash preimage is explicitly written into the context extension and can be seen by anyone once the transaction takes place.

##### Example: atomic transactions and cross-chain trading#
Suppose there are two separate blockchains, for two different asset types. Alice wants to receive some assets in her blockchain in exchange for giving some assets to Bob in his blockchain. \(\langname\) allows to accomplish it in a simpler way than proposed for Bitcoin, for example, in [@Nol13].
Alice creates a random secret \(\texttt{x}\) of 256 bits (32 bytes), hashes it to obtain the value $\texttt{hx}, and creates a transaction in Bob's blockchain with the output box protected by the following script:
anyOf( Coll(
                HEIGHT > deadlineBob && pkA,
                pkB && blake2b256(getVar[Coll[Byte]](1).get) == hx
        ))
Bob can receive the value of this box only upon presentation of a hash preimage of \(\texttt{hx}\). Alice can reclaim it after \(\texttt{deadlineBob}\).
From this output, Bob learns $\texttt{hx}. He creates a transaction in Alice's blockchain with an output box protected by the following script:
val x = getVar[Coll[Byte]](1).get
        anyOf( Coll(
                HEIGHT > deadlineAlice && pkB,
                allOf( Coll(
                        pkA,
                        x.size < 33,
                        blake2b256(x) == hx
                ))
        ))
If Alice is satisfied with the amount Bob is giving her, she claims the value of this box by revealing \(\texttt{x}\). Alice is protected as long as the hash function is one-way and she keeps her \(\texttt{x}\) secret until she claims the value of this box. (She should be careful to submit her transaction in enough time before \(\texttt{deadlineAlice}\)to make sure it gets processed before Bob can reclaim this money, because once she submits the transaction, \(\texttt{x}\)is public and thus, if the \(\texttt{deadlineAlice}\)passes before the transaction is processed, Bob can both reclaim this box and claim the box Alice left in his blockchain.)
Bob is protected, because in order for Alice to claim the value of this box, she must present a hash preimage of \(\texttt{hx}\) as ...

#### Box Registers and Additional Tokens#
Context variables are passed at box spending time whereas registers at box creation time. Together with its value and protecting script, a box can contain up to 10 numbered registers, \(\texttt{R0}\) through \(\texttt{R9}\). The first four of these have fixed meaning, as follows. For a box \(\texttt{b}\), \(\texttt{b.R0}\) is the same as \(\texttt{b.value}\) and \(\texttt{b.R1}\) is the same as \(\texttt{b.propositionBytes}\).
The third register, \(\texttt{b.R2}\), specifies additional, secondary tokens contained in the box, while the primary token amount is specified in \(\texttt{b.value}\). \(\texttt{b.R2}\) holds a collection of pairs, where each pair's first element specifies the token id (as a collection of 32 bytes) and the second element specifies the amount (as a long value). The maximum number of tokens in a box is limited to 4. For every token id, the sum of amounts in input boxes must be at least equal to the sum of amounts in output boxes. An exception to this rule exists for the creation of new tokens. When a new token type is created in a transaction, its id is set to the id of input box 0. Therefore, the exception for new token creation is that if the token id in an output box matches the id of input box 0, an arbitrary amount of this token can be output. Since each box has a unique id (see Section~\ref{sec:context}), this exception can be applied exactly once per token type. A newly created token can be emitted in a time-controlled mannerâsee this.
The fourth register, \(\texttt{b.R3}\), contains a pair of integer and 34-byte collection (its type then is \(\texttt{(Int, Coll[Byte])}\)). The collection specifies the 32-byte unique transaction id where this box appears as an output followed by a 2-byte sequence number of this box in the \(\texttt{OUTPUTS}\) collection of that transaction. This ensures that each box has unique \(\texttt{R3}\) and therefore a unique \(\texttt{id}\) as long as there are no hash collisions (because the \(\texttt{id}\) of...

##### Example: atomic exchange on a single block chain#
These box registers provide additional capabilities to \(\langname\). Consider, for example, Alice and Bob who want to exchange tokens: they agree that Bob will give Alice 60 tokens of type \(\texttt{token1}\) (this type is mapped to an actual token id in the environment map) in exchange for 100 Ergo tokens. Alice could create an output box with value 100 and protect it with the following script:
(HEIGHT > deadline && pkA) || {
    val tokenData = OUTPUTS(0).R2[Coll[(Coll[Byte], Long)]].get(0)
    allOf(Coll(
        tokenData._1 == token1,
        tokenData._2 >= 60L,
        OUTPUTS(0).propositionBytes == pkA.propBytes,
        OUTPUTS(0).R4[Coll[Byte]].get == SELF.id
    ))
  }
This script ensures that the box can be spent only in a transaction that produces an output with 60 tokens of type \(\texttt{token1}\) and gives them to Alice (Alice can reclaim the box after the deadline).
Moreover, the last condition (\(\texttt{OUTPUTS(0).R4[Col[Byte]].get == SELF.id}\)) ensures that if Alice has multiple such boxes outstanding at a given time, each will produce a separate output that identifies the corresponding input. This condition prevents the following attack: if Alice has two such boxes outstanding but the last condition is not present, then they can be both used in a single transaction that contains just one output with 60 tokens of type \(\texttt{token1}\)--- the script of each input box will be individually satisfied, but Alice will get less only half of what owed to her.
Bob, similarly, could create an output box with value about 0 and 60 tokens of type \(\texttt{token1}\) and protect it by the following script:
&(HEIGHT > deadline && pkB) ||
        &allOf( Coll(
        &        OUTPUTS(1).value >= 100L,
        &        OUTPUTS(1).propositionBytes == pkB.propBytes,
        &        OUTPUTS(1).R4[Coll[Byte]].get == SELF.id,
        & ))
A transaction containing these two boxes as inputs must produce two outputs: the first giving at least 60 tokens of type1 to...

#### Self-Replicating Code#
Access to box registers allows us to create self-replicating boxes, because a script can check that an output box contains the same script as \(\texttt{SELF}\). As shown in [@CKM18], this powerful tool allows for Turing-completeness as computation evolves from box to box, even if each individual script is not Turing-complete. We will demonstrate two examples of complex behavior via self-replication.

##### Example: time-controlled coin emission#
In this example, we will create a self-replicating box that emits new coins at each time step in order to add to the total amount of currency available. This box appears as an output in the genesis block (at height 0) of the blockchain; all "new" coins come from this box or its descendants, thus maintaining the invariant that for every transaction after the genesis block, the combined value of all inputs  is equal to the combined value of all outputs.
The value of this box initially is equal to the total amount of currency that will eventually be available. This value will go down by a prespecified amount each time this box is transacted. Because in each transaction, the sum of input values must equal the sum of output values, when the value of this box goes down, the difference must be claimed by someone. The box is set up to allow the difference to go to anyone---presumably, it will be claimed by the miner who created the block that contains the transaction. This box will store, in \(\texttt{R4}\), the height at which it was created. Using this information, it will be able to determine how much value to emit. The box will be set to emit a fixed amount specified by \(\texttt{fixedRate}\) per block until \(\texttt{HEIGHT}\) reaches \(\texttt{fixedRatePeriod}\), and a linearly decreasing amount thereafter. The script will verify that the output box has the same script as itself, and that the new height stored in \(\texttt{R4}\) and the new value are correctly computed (and that the height has increased, so that a miner cannot emit more than once per block). The following script accomplishes this goal:
\[
\begin{aligned}
    &\text{val epoch} = 1 + \left(\frac{\text{HEIGHT} - \text{fixedRatePeriod}}{\text{epochLength}}\right) \\
    &\text{val out} = \text{OUTPUTS}(0) \\
    &\text{val coinsToIssue} = 
    \begin{cases} 
    \text{fixedRate}, & \text{if HEIGHT} < \text{fixedRatePeriod} \\
    \text{fixedRate} - (\text{oneEpochReduction} \times \text{epoch}), & \text{o...

##### Example: arbitrary computation via a simple cellular automaton#
The example in the paragraph is not meant for practical implementation; rather, it is here merely to demonstrate the Turing-complete power of self-replication. It implements the so-called rule 110 one-dimensional cellular automaton [@wolfram1986theory], which is known to be Turing-complete [@cook2004universality] (with only polynomial-time overheard --- i.e., \(P\)-complete [@NW06]). See [@CKM18] for more details. The code for this example is too complex to be put here; it is available here.
\bibliography
