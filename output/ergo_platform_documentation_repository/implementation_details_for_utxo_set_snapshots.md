# Implementation Details for UTXO Set Snapshots
Source: docs/node/modes/pruned/pruned-impl.md
Generated: 2025-05-11

## Summary
# Implementation Details for UTXO Set Snapshots

The UTXO set authentication uses an AVL+ tree, outlined in [this research paper](https://eprint.iacr.org/2016/994.pdf) and available in the [Scrypto framework](https://github.com/input-output-hk/scrypto) on GitHub. Snapshots are taken every 51,200 blocks (~72 days), specifically after a block where *h % 51200 == 51199*. [This research paper](https://eprint.iacr.org/2018/129) indicates that this method can be as secure as processing all blocks under certain statistical assumptions. ### Implementation Details

#### Chunk Format

*To be provided*

#### Manifest Format

*To be provided*

#### Networking Layer

*To be provided*

#### Bootstrapping

*To be provided*

#### Node Configuration

Bootstrapping with a UTXO set snapshot is enabled by setting *ergo.node.utxoBootstrap = true* in the [configuration](conf-node.md). #### Sync Info V3

*To be provided*

## Technical Workflow (WIP)

## Keywords
implementation, details, utxo, snapshots, authentication, tree, research, paper](https://eprint.iacr.org/2016/994.pdf, scrypto, framework](https://github.com, output, github, snapshot, block, paper](https://eprint.iacr.org/2018/129, method, assumption, detail, chunk, format

## Content
## Implementation Details for UTXO Set Snapshots
The UTXO set authentication uses an AVL+ tree, outlined in this research paper and available in the Scrypto framework on GitHub. Snapshots are taken every 51,200 blocks (~72 days), specifically after a block where h % 51200 == 51199.
This research paper indicates that this method can be as secure as processing all blocks under certain statistical assumptions.

##### Chunk Format
To be provided

##### Manifest Format
To be provided

##### Networking Layer
To be provided

##### Bootstrapping
To be provided

##### Node Configuration
Bootstrapping with a UTXO set snapshot is enabled by setting ergo.node.utxoBootstrap = true in the configuration.

##### Sync Info V3
To be provided

### Technical Workflow (WIP)
A pruned client downloads all headers, validates proofs-of-work, and links structures, followed by downloading a UTXO snapshot from peers and the full blocks succeeding it. The process is as follows:
ErgoSyncInfo: Message to connected peers.
Receive INV message with better block ids.
Request headers for received ids.
On Header Reception:
    java
    if(History.apply(header).isSuccess) {
        if(!(localScore == networkScore)) GOTO 1
        else GOTO 5
    } else {
        blacklist peer
    }
Request UTXOManifest for at least BlocksToKeep back.
On UTXOSnapshotManifest Reception:
    java
    UTXOSnapshotManifest.chunks.foreach { chunk =>
        request chunk from sender() //Or from random full node
    }
On UTXOSnapshotChunk Reception:
    java
    State.applyChunk(UTXOSnapshotChunk) match {
         case Success(Some(newMinimalState)) => GOTO 8
         case Success(None) => stay at 7
         //Request missed chunks periodically
         case Failure(e) => ???
         //Invalid hash or state
    }
Request BlockTransactions starting from available State.
    java
    History.headersStartingFromId(State.headerId).foreach { header =>
        send message(GetBlockTransactionsForHeader(header)) to Random full node
    }
On BlockTransactions Reception: same as Fullnode.7.
Operate as Fullnode.
This revised workflow streamlines the operation of a pruned full node, emphasizing efficiency and security, positioning Ergo and similar blockchains for broader adoption within the constraints of typical hardware. For a deeper dive into nipopows, you can explore this paper.
