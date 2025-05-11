# Light SPV Mode Technical Workflow
Source: docs/node/modes/light-spv-mode-workflow.md
Generated: 2025-05-11

## Summary
# Light SPV Mode Technical Workflow The technical workflow for the light-SPV mode in Ergo is as follows:

### Bootstrap

1. Send **`GetPoPoWProof`** for all connections. 2.  On receiving **`PoPoWProof`**, apply it to History (History should determine whether this PoPoWProof is better than its current best header chain). 3.

## Keywords
light, mode, technical, workflow, ergo, bootstrap, getpopowproof, connection, popowproof, history, header, chain, goto, regime, message, peer, response, block, request, java

## Content
## Light SPV Mode Technical Workflow
The technical workflow for the light-SPV mode in Ergo is as follows:

#### Bootstrap
Send GetPoPoWProof for all connections.
On receiving PoPoWProof, apply it to History (History should determine whether this PoPoWProof is better than its current best header chain).
GOTO regular regime.

#### Regular
Send ErgoSyncInfo message to connected peers
Get a response with an INV message containing the ids of blocks, better than
    our best block.
Request headers for all ids from 2.
On receiving Header:
java
    if(History.apply(header).isSuccess) {
        State.apply(header) // just change state roothash
    if(!isInitialBootstrapping) Broadcast INV for this header
    } else {
        blacklist peer
    }
