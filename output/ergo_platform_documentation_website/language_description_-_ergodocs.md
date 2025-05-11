# Language Description - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/sigma/lang-spec/](https://docs.ergoplatform.com/dev/scs/sigma/lang-spec/)
Generated: 2025-05-11

## Summary
ð From sigmastate-interpreter ErgoScript is a language to write contracts for Ergo blockchain. ErgoScript contracts can be compiled to ErgoTrees, serialized and stored in UTXOs. A good starting point to writing contracts is to use ErgoScript by Example with Ergo Playgrounds or Appkit. The ErgoScript compiler is published
as a library which is cross compiled for Java 7 and Java 8+ and can be used from any JVM lanugage, Android or JavaFX.

## Keywords
ð, sigmastate, interpreter, ergoscript, language, contract, ergo, blockchain, ergotrees, utxo, starting, point, writing, example, playgrounds, appkit, compiler, library, cross, java

## Content
## ErgoScript Language Description#
ð From sigmastate-interpreter

#### Introduction#
ErgoScript is a language to write contracts for Ergo blockchain. ErgoScript contracts can be compiled to ErgoTrees, serialized and stored in UTXOs.
A good starting point to writing contracts is to use ErgoScript by Example with Ergo Playgrounds or Appkit.
The ErgoScript compiler is published
as a library which is cross compiled for Java 7 and Java 8+ and can be used from any JVM lanugage, Android or JavaFX.
The following example shows how source code of ErgoScript contract can be used to create new transaction using Appkit, see FreezeCoin.java for more details.
// To create transaction we use a builder obtained from the context
// the builder keeps relationship with the context to access necessary blockchain data.
UnsignedTransactionBuilder txB = ctx.newTxBuilder();

// create new box using new builder obtained from the transaction builder
// in this case we compile new ErgoContract from source ErgoScript code
OutBox newBox = txB.outBoxBuilder()
        .value(amountToPay)
        .contract(ctx.compileContract(
                ConstantsBuilder.create()
                        .item("freezeDeadline", ctx.getHeight() + newBoxDelay)
                        .item("pkOwner", prover.getP2PKAddress().pubkey())
                        .build(),
                "{ " +
                "  val deadlinePassed = sigmaProp(HEIGHT > freezeDeadline)" +
                "  deadlinePassed && pkOwner " +
                "}"))
        .build();
The contract is given as the string literal which contains the block of val declarations followed by the logical expression. The expression defines the all possible conditions to spend the box. The contract can also contain named
constants (which cannot be represented as literals in the source code).
In the example freezeDeadline and pkOwner are named constants. The concrete values of named constants should be given to the compiler (see compileContract method)
**The following sections describe ErgoScript and its operations. **

##### ErgoScript language features overview#
Syntax borrowed from Scala
Standard syntax and semantics for well known constructs (operations, code blocks, if branches etc.)
High-order language with first-class lambdas which are used in collection operations
Call-by-value (eager evaluation)
Statically typed with local type inference
Blocks are expressions 
Semicolon inference in blocks
Type constructors: Pair, Coll, Option

##### Operations and constructs overview#
Binary operations: >, <, >=, <=, +, -, &&, ||, ==, !=, |, &, *, /, %, ^, ++
Predefined primitives: blake2b256, byteArrayToBigInt, proveDlog etc. 
Val declarations: val h = blake2b256(pubkey)
If-then-else clause: if (x > 0) 1 else 0
Collection literals: Coll(1, 2, 3, 4)
Generic high-order collection operations: map, filter, fold, exists, forall, etc.
Accessing fields of any predefined types: box.value
Method invocation for predefined types: coll.map({ x => x + 1 })
Function invocations (predefined and user defined): proveDlog(pubkey) 
User defined function declarations: def isProven(pk: GroupElement) = proveDlog(pk).isProven
Lambdas and high-order methods: OUTPUTS.exists { (out: Box) => out.value >= minToRaise }

##### Data types#
In ErgoScript, everything is an object in the sense that we can call member functions and properties on any variable.
Some of the types can have a special internal representation - for example, numbers and booleans can be
represented as primitive values at runtime - but to the user they look like ordinary classes.
NOTE: in ErgoScript we use type, class and trait as synonyms, we prefer type when talking about primitive values and
trait or class when talking about methods.
Type Name
Description




Any
a supertype of any other type (not used directly in ErgoScript)


Unit
a type with a single value ()


Boolean
a type with two logical values true and false


Byte
8 bit signed integer


Short
16 bit signed integer


Int
32 bit signed integer


Long
64 bit signed integer


BigInt
256 bit signed integer


SigmaProp
a type representing a sigma proposition which can be verified by executing a Sigma protocol with zero-knowledge proof of knowledge. Every contract should return a value of this type.


AvlTree
represents a digest of authenticated dynamic dictionary and can be used to verify proofs of operations performed on the dictionary


GroupElement
elliptic curve points


Box
a box containing a monetary value (in NanoErgs), tokens and registers along with a guarding proposition


Option[T]
a container which either have some value of type T or none.


Coll[T]
a collection of arbitrary length with all values of type T


(T1,T2)
a pair of values where T1, T2 can be different types
The type constructors Coll, (_,_) can be used to construct complex
types as in the following example.
{
  val keyValues = OUTPUTS(0).R4[Coll[(Int, (Byte, Long))]].get
  ...
}

##### Literal syntax and Constants#
Literals are used to introduce values of some types directly in program text
like in the following example:
val unit: Unit = ()       // unit constant
val long: Int = 10        // interger value literal
val bool: Boolean = true  // logical literal
val arr = Coll(1, 2, 3)   // constructs a collection with given items
val str = "abc"           // string of characters 

Note that many types don't have literal syntax and their values are introduced 
by applying operations, for example deserialize function can be used to introduce
a constant of any type by using Base64 encoded string (See predefined function).

##### Primitive Types#
Below we specify methods of pre-defined types using Scala-like declaration of classes.
Note, the Boolean type doesn't have pre-defined methods in addition to the standard operations.
Note, ErgoScript doesn't allow to define new class types, however it has many pre-defined classes with methods defined below.
Every numeric type has the following methods.
/** Base supertype for all numeric types. */
class Numeric {
  /** Convert this Numeric value to Byte. 
   * @throws ArithmeticException if overflow happens. 
   */
  def toByte: Byte

  /** Convert this Numeric value to Short. 
   * @throws ArithmeticException if overflow happens. 
   */
  def toShort: Short

  /** Convert this Numeric value to Int. 
   * @throws ArithmeticException if overflow happens. 
   */
  def toInt: Int

  /** Convert this Numeric value to Long. 
   * @throws ArithmeticException if overflow happens. 
   */
  def toLong: Long

  /** Convert this Numeric value to BigInt. */
  def toBigInt: BigInt
}
All the predefined numeric types inherit Numeric class and its methods.
They can be thought of as being pre-defined, like the following.
class Byte extends Numeric
class Short extends Numeric
class Int extends Numeric
class Long extends Numeric
class BigInt extends Numeric

##### Context Data#
Every script is executed in a context, which is a collection of data available
for operations in the script. The context data is available using the CONTEXT
variable which is of pre-defined class Context which is shown below.
There are also shortcut variables which are available in every script to
simplify access to the most commonly used context data.
Variable
Type
Shortcut for ...




HEIGHT
Int
CONTEXT.HEIGHT


SELF
Box
CONTEXT.SELF


INPUTS
Coll[Box]
CONTEXT.INPUTS


OUTPUTS
Coll[Box]
CONTEXT.OUTPUTS
The following listing shows the methods of pre-defined Context, Header,
PreHeader types.
/** Represents data available in ErgoScript using `CONTEXT` global variable */
class Context {
  /** Height (block number) of the block which is currently being validated. */
  def HEIGHT: Int

  /** Box whose proposition is being currently executing */
  def SELF: Box

  /** Zero based index in `inputs` of `selfBox` */
  def selfBoxIndex: Int

  /** A collection of inputs of the current transaction, the transaction where
    * selfBox is one of the inputs. 
    */
  def INPUTS: Coll[Box]

  /** A collection of data inputs of the current transaction. Data inputs are
    * not going to be spent and thus don't participate in transaction validation
    * as `INPUTS`, but data boxes are available in guarding propositions of
    * `INPUTS` and thus can be used in spending logic.
    */
  def dataInputs: Coll[Box]

  /** A collection of outputs of the current transaction. */
  def OUTPUTS: Coll[Box]

  /** Authenticated dynamic dictionary digest representing Utxo state before
    * current state. 
    */
  def LastBlockUtxoRootHash: AvlTree

  /** A fixed number of last block headers in descending order (first header is
    * the newest one) */
  def headers: Coll[Header]

/** Fields of a new block header, that can be predicted by a miner before block's formation */
  def preHeader: PreHeader
  /** Bytes of encoded miner's public key.
    * Same as `preHeader.minerPk.getEncoded`
    *...

##### Box type#
Box represents a unit of storage in Ergo blockchain. It contains 10 registers
(indexed 0-9). First 4 are mandatory and the others are optional.
/** Representation of Ergo boxes used during execution of ErgoTree operations. */
class Box {
  /** Box monetary value in NanoErg */
  def value: Long 

  /** Blake2b256 hash of this box's content, basically equals to
    * `blake2b256(bytes)` 
    */
  def id: Coll[Byte] 

  /** Serialized bytes of guarding script, which should be evaluated to true in
    * order to open this box. 
    */
  def propositionBytes: Coll[Byte] 

  /** Serialized bytes of this box's content, including proposition bytes. */
  def bytes: Coll[Byte] 

  /** Serialized bytes of this box's content, excluding transactionId and index
    * of output. 
    */
  def bytesWithoutRef: Coll[Byte]

  /** If `tx` is a transaction which generated this box, then `creationInfo._1`
    * is a height of the tx's block. The `creationInfo._2` is a serialized
    * transaction identifier followed by box index in the transaction outputs.
    */
  def creationInfo: (Int, Coll[Byte]) 

  /** Synonym of R2 obligatory register */
  def tokens: Coll[(Coll[Byte], Long)] 

  /** Extracts register by id and type.
    * ErgoScript is typed, so accessing a register is an operation which involves some
    * expected type given in brackets. Thus `SELF.R4[Int]` expression should evaluate to a
    * valid value of the `Option[Int]` type.
    *
    * For example `val x = SELF.R4[Int]` expects the
    * register, if it is present, to have type `Int`. At runtime the corresponding type
    * descriptor is passed as `implicit t: RType[T]` parameter of `getReg` method and
    * checked against the actual value of the register.
    *
    * There are three cases:
    * 1) If the register doesn't exist.
    *   Then `val x = SELF.R4[Int]` succeeds and returns the None value, which conforms to
    *   any value of type `Option[T]` for any T. (In the example above T is equal to
    *   `Int`)...

##### GroupElement#
/** Base class for points on elliptic curves. */
class GroupElement {
  /** Exponentiate this <code>GroupElement</code> to the given number.
    * @param k The power.
    * @return <code>this to the power of k</code>.
    */
  def exp(k: BigInt): GroupElement

  /** Group operation. */
  def multiply(that: GroupElement): GroupElement

  /** Inverse element in the group. */
  def negate: GroupElement

  /** Get an encoding of the point value.
    *
    * @return the point encoding
    */
  def getEncoded: Coll[Byte]
}

##### AvlTree#
/** Type of data which efficiently authenticates potentially huge dataset having key-value dictionary interface.
  * Only root hash of dynamic AVL+ tree, tree height, key length, optional value length, and access flags are stored
  * in an instance of the datatype.
  *
  * Please note that standard hash function from `scorex.crypto.hash` is used, and height is stored along with root hash of
  * the tree, thus `digest` size is always CryptoConstants.hashLength + 1 bytes.
  */
class AvlTree {
  /** Returns digest of the state represented by this tree.
    * Authenticated tree digest = root hash bytes ++ tree height
    */
  def digest: Coll[Byte]

  /** Flags of enabled operations packed in single byte.
    * isInsertAllowed == (enabledOperations & 0x01) != 0
    * isUpdateAllowed == (enabledOperations & 0x02) != 0
    * isRemoveAllowed == (enabledOperations & 0x04) != 0
    */
  def enabledOperations: Byte

  /** All the elements under the tree have the same length of the keys */
  def keyLength: Int

  /** If non-empty, all the values under the tree are of the same length. */
  def valueLengthOpt: Option[Int]

  /** Checks if Insert operation is allowed for this tree instance. */
  def isInsertAllowed: Boolean

  /** Checks if Update operation is allowed for this tree instance. */
  def isUpdateAllowed: Boolean

  /** Checks if Remove operation is allowed for this tree instance. */
  def isRemoveAllowed: Boolean

  /** Replace digest of this tree producing a new tree.
    * Since AvlTree is immutable, this tree instance remains unchanged.
    * @param newDigest   a new digest
    * @return a copy of this AvlTree instance where `this.digest` replaced by
    *         `newDigest`
    */
  def updateDigest(newDigest: Coll[Byte]): AvlTree

  /** Enable/disable operations of this tree producing a new tree.
    * Since AvlTree is immutable, `this` tree instance remains unchanged.
    * @param newOperations a new flags which specify available operations on a
    *         ...

##### Option[T]#
/** Represents optional values. Instances of `Option`
 *  are either an instance of `Some(x)` or the value `None`.
 */
class Option[A] {
  /** Returns true if the option is an instance of Some(value), false otherwise. 
   */
  def isDefined: Boolean;

  /** Returns the option's value if the option is nonempty, otherwise
    * return the result of evaluating `default`.
    * NOTE: the `default` is evaluated even if the option contains the value
    * i.e. not lazily.
    *
    * @param default  the default expression.
    */
  def getOrElse[B](default: B): B  

  /** Returns the option's value.
   *  @note The option must be nonempty.
   *  @throws InterpreterException if the option is empty.
   */
  def get: A

  /** Returns a Some containing the result of applying $f to this option's
   * value if this option is nonempty.
   * Otherwise return None.
   *
   * @note This is similar to `flatMap` except here, $f does not need to wrap its result in an $option.
   *
   * @param  f   the function to apply
   * @since  2.0
   * @see flatMap
   */
  def map[B](f: A => B): Option[B]


  /** Returns this option if it is nonempty '''and''' applying the predicate $p to
   * this option's value returns true. Otherwise, return $none.
   *
   * @param  p   the predicate used for testing.
   * @since  2.0
   */
  def filter(p: A => Boolean): Option[A]
}

##### Coll[T]#
/** Indexed (zero-based) collection of elements of type `A` 
  * @tparam A the collection element type
  */
class Coll[A] {
  /** The number of elements in the collection */
  def size: Int

  /** The element at given index.
   *  Indices start at `0`; `xs.apply(0)` is the first element of collection `xs`.
   *  Note the indexing syntax `xs(i)` is a shorthand for `xs.apply(i)`.
   *
   *  @param    i   the index
   *  @return       the element at the given index
   *  @throws       ArrayIndexOutOfBoundsException if `i < 0` or `length <= i`
   */
  def apply(i: Int): A

  /** The element of the collection or default value. 
   * If an index is out of bounds (`i < 0 || i >= length`) then `default` value is returned.
   *  @param    i   the index
   *  @return       the element at the given index or default value if index is out or bounds
   */
  def getOrElse(i: Int, default: A): A

  /** Builds a new collection by applying a function to all elements of this collection.
   *
   *  @param f      the function to apply to each element.
   *  @tparam B     the element type of the returned collection.
   *  @return       a new collection of type `Coll[B]` resulting from applying the given function
   *                `f` to each element of this collection and collecting the results.
   */
  def map[B](f: A => B): Coll[B]

  /** For this collection (x0, ..., xN) and other collection (y0, ..., yM)
   * produces a collection ((x0, y0), ..., (xK, yK)) where K = min(N, M) 
   */
  def zip[B](ys: Coll[B]): Coll[(A, B)]

  /** Tests whether a predicate holds for at least one element of this collection.
   *  @param   p     the predicate used to test elements.
   *  @return        `true` if the given predicate `p` is satisfied by at least one element of this collection, otherwise `false`
   */
  def exists(p: A => Boolean): Boolean

  /** Tests whether a predicate holds for all elements of this collection.
   *  @param   p   the predicate used to test elements.
   *  @return      ...

#### Predefined global functions#
ErgoScript standard library include predefined functions that can be called 
without prior declaration.
The following function declarations are automatically imported into any script:
/** Returns true if all the elements in collection are true. */
def allOf(conditions: Coll[Boolean]): Boolean

/** Returns true if at least on element of the conditions is true */
def anyOf(conditions: Coll[Boolean]): Boolean

/** Similar to allOf, but performing logical XOR operation instead of `&&` */
def xorOf(conditions: Coll[Boolean]): Boolean 

/** Returns SigmaProp value which can be ZK proven to be true 
 * if at least k properties can be proven to be true. 
 */
def atLeast(k: Int, properties: Coll[SigmaProp]): SigmaProp

/** Embedding of Boolean values to SigmaProp values. As an example, this
 * operation allows boolean expressions to be used as arguments of
 * `atLeast(..., sigmaProp(myCondition), ...)` operation.
 */
def sigmaProp(condition: Boolean): SigmaProp

/** Cryptographic hash function Blake2b256 (See scorex.crypto.hash.Blake2b256) */
def blake2b256(input: Coll[Byte]): Coll[Byte]

/** Cryptographic hash function Sha256 (See scorex.crypto.hash.Sha256) */
def sha256(input: Coll[Byte]): Coll[Byte]

/** Create BigInt from a collection of bytes. */
def byteArrayToBigInt(input: Coll[Byte]): BigInt

/** Create Long from a collection of bytes. */
def byteArrayToLong(input: Coll[Byte]): Long  

/** Returns bytes representation of Long value. */
def longToByteArray(input: Long): Coll[Byte]

/** Convert bytes representation of group element (ECPoint) 
  * to a new value of GroupElement (using
  * org.bouncycastle.math.ec.ECCurve.decodePoint())
  */
def decodePoint(bytes: Coll[Byte]): GroupElement 


/** Extracts Context variable by id and type.
  * ErgoScript is typed, so accessing a the variables is an operation which involves
  * some expected type given in brackets. Thus `getVar[Int](id)` expression should
  * evaluate to a valid value of the `Option[Int]` type.
  *
  * For ...

### Examples#
See white paper for examples
