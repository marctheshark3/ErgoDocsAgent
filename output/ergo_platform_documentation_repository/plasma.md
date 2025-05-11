# Plasma
Source: docs/dev/lib/plasma.md
Generated: 2025-05-11

## Summary
---
tags:
  - Plasma
  - AVL Trees
  - Layer 2
  - Library
  - GetBlok
---

# Plasma

[GetBlok Plasma](https://github.com/GetBlok-io/GetBlok-Plasma) is a library on top of Ergo [Appkit](appkit.md) that provides an abstraction layer to simplify the process of integrating AVL Trees (AKA Plasma) into off-chain code. The goal is to give developers an easy way to use this Layer-2 scaling solution in contracts, off-chain code, and distributed systems managing the Plasma itself. GetBlok Plasma uses the default versioned storage implementation powered by LevelDB, with another SwayDB implementation in the works. **This allows for distributed systems to keep track of the key-value pairs held in digests stored on-chain.

## Keywords
plasma, trees, layer, library, getblok, plasma](https://github.com, ergo, abstraction, process, chain, code, goal, developer, layer-2, scale, solution, contract, system, default, storage

## Content
## Plasma
GetBlok Plasma is a library on top of Ergo Appkit that provides an abstraction layer to simplify the process of integrating AVL Trees (AKA Plasma) into off-chain code. The goal is to give developers an easy way to use this Layer-2 scaling solution in contracts, off-chain code, and distributed systems managing the Plasma itself. GetBlok Plasma uses the default versioned storage implementation powered by LevelDB, with another SwayDB implementation in the works. This allows for distributed systems to keep track of the key-value pairs held in digests stored on-chain.
See these documents to get started;
AVL Trees / Plasma In ErgoScript: Basics, Tips, and Design Patterns
Mining Pool Operating At Layer 2

### Details
Creating and managing AVL Trees is greatly simplified when using the library. To create a normal,
un-stored / temporary AVL Tree, we use Plasma Maps. Plasma Maps look similar to normal Scala maps on the surface
with a few changes that make them compatible with on-chain AVL Trees.
scala
import io.getblok.getblok_plasma.PlasmaParameters
import io.getblok.getblok_plasma.collections.PlasmaMap
import org.ergoplatform.appkit.ErgoId
import sigmastate.{AvlTreeFlags, Values}
// Plasma Map that uses ErgoId's as keys, and ErgoTrees as values
val plasmaMap = new PlasmaMap[ErgoId, Values.ErgoTree](AvlTreeFlags.AllOperationsAllowed, PlasmaParameters.default)
All Plasma Maps use 32 byte digests and Blake2b256 hashing. Any class may be inserted into a Plasma Map
so long as there is a corresponding implicit ByteConversion for that class.
```scala
import io.getblok.getblok_plasma.ByteConversion
import org.ergoplatform.appkit.ErgoId
import sigmastate.Values
import sigmastate.serialization.ErgoTreeSerializer
// Default ByteConversions for ErgoId and ErgoTree
implicit val convertsId: ByteConversion[ErgoId] = new ByteConversion[ErgoId] {
  override def convertToBytes(t: ErgoId): Array[Byte] = t.getBytes
override def convertFromBytes(bytes: Array[Byte]): ErgoId = new ErgoId(bytes)
}
implicit val convertsErgoTree: ByteConversion[Values.ErgoTree] = new ByteConversion[Values.ErgoTree] {
  override def convertToBytes(t: Values.ErgoTree): Array[Byte] = t.bytes
override def convertFromBytes(bytes: Array[Byte]): Values.ErgoTree = ErgoTreeSerializer.DefaultSerializer.deserializeErgoTree(bytes)
}
```
Custom classes may also be used with their own definitions to allow for flexibility in contracts:
```scala
import com.google.common.primitives.{Ints, Longs}
import io.getblok.getblok_plasma.ByteConversion
import org.bouncycastle.util.encoders.Hex
import org.ergoplatform.appkit.{ErgoType, ErgoValue}
import sigmastate.eval.Colls
import special.collection.Coll
case class StateScore(score: Long, paid: Boo...

### LocalPlasmaMap
Interacting with a locally stored Plasma Map is done in a similar way, except that you must use the
LocalPlasmaMap class instead.
```scala
import io.getblok.getblok_plasma.PlasmaParameters
import io.getblok.getblok_plasma.collections.LocalPlasmaMap
import io.getblok.getblok_plasma.ByteConversion.convertsLongKey
import scorex.crypto.authds.avltree.batch.VersionedLDBAVLStorage
import scorex.crypto.hash.{Blake2b256, Digest32}
import scorex.db.LDBVersionedStore
import sigmastate.{AvlTreeFlags, Values}
import java.io.File
val ldbStore = new LDBVersionedStore(new File("./level"), 10)
val avlStorage = new VersionedLDBAVLStorageDigest32(Blake2b256)
val localMap = new LocalPlasmaMapLong, Values.ErgoTree
```

### ProxyPlasmaMap
It can be useful to apply changes to a tree without necessarily committing to them. This is especially
true in the context of chained transactions or unexpected errors. For example, if changes are applied to the
tree but latency causes connection to the node to be lost, then the locally stored tree may have changes
that do not exist on-chain!
To deal with this problem, you can use a ProxyPlasmaMap. This PlasmaMap applies changes on a temporary
tree which allows you to receive proofs for the operations you perform. However, none of these changes
are saved to storage until the commitChanges() function is called. This ensures that unexpected errors
can be dealt with easily.
When dealing with the ProxyPlasmaMap, changes must first be explicitly enabled by calling
initiate(). This function initializes the internal temporary map. Following this, operations
may be performed on the map. All operations are applied to the temporary map, but are also kept
track of inside an internal Queue. Once commitChanges() is called, the Queued operations are applied
to persistent storage, and the temporary map is destroyed.
```scala
import io.getblok.getblok_plasma.PlasmaParameters
import io.getblok.getblok_plasma.collections.{LocalPlasmaMap, ProxyPlasmaMap}
import org.ergoplatform.appkit.ErgoId
import scorex.crypto.authds.avltree.batch.VersionedLDBAVLStorage
import scorex.crypto.hash.{Blake2b256, Digest32}
import scorex.db.LDBVersionedStore
import sigmastate.{AvlTreeFlags, Values}
import io.getblok.getblok_plasma.ByteConversion.convertsLongVal
import java.io.File
val ldbStore = new LDBVersionedStore(new File("./level"), 10)
val avlStorage = new VersionedLDBAVLStorageDigest32(Blake2b256)
val proxyMap = new ProxyPlasmaMapErgoId, Long
val ergopadId: ErgoId = ErgoId.create("d71693c49a84fbbecd4908c94813b46514b18b67a99952dc1e6e4791556de413")
val tokenDataErgoPad: Seq[(ErgoId, Long)] = Seq(ergopadId -> 100L)
// This will fail due to the ProxyMap being un-initiated
proxyMap.insert(tokenDataErgoP...

### Resources
Plasma Example: Off-chain Bank operating at Layer 2
GetBlok Plasma
GetBlok: SmartPool Plasma
Paideia - Plasma Staking
