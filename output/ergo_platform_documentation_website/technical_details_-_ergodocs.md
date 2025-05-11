# Technical Details - ErgoDocs
Source: [https://docs.ergoplatform.com/node/modes/light-spv-mode-workflow/](https://docs.ergoplatform.com/node/modes/light-spv-mode-workflow/)
Generated: 2025-05-11

## Summary
The technical workflow for the light-SPV mode in Ergo is as follows:

## Keywords
workflow, mode, ergo

## Content
## Light SPV Mode Technical Workflow#
The technical workflow for the light-SPV mode in Ergo is as follows:

#### Bootstrap#
Send GetPoPoWProof for all connections.
On receiving PoPoWProof, apply it to History (History should determine whether this PoPoWProof is better than its current best header chain).
GOTO regular regime.

#### Regular#
Send ErgoSyncInfo message to connected peers
Get a response with an INV message containing the ids of blocks, better than
    our best block.
Request headers for all ids from 2.
On receiving Header:
if(History.apply(header).isSuccess) {
        State.apply(header) // just change state roothash
    if(!isInitialBootstrapping) Broadcast INV for this header
    } else {
        blacklist peer
    }
