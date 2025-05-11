# Rock/Paper/Scissors - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/tx/rock-paper-scissor/](https://docs.ergoplatform.com/dev/scs/tx/rock-paper-scissor/)
Generated: 2025-05-11

## Summary
Our next example of a multi-stage contract is the Rock-Paper-Scissors game, often used as an introductory example for smart contracts. The game is played between two players, Alice and Bob. Each player chooses a secret move independently, and the game outcome is decided after both secrets are revealed. Let a, b â Z3 be the secret choices of Alice and Bob, respectively, where (0, 1, 2) represent (rock, paper, scissors). If a = b, the game is a draw.

## Keywords
example, contract, rock, paper, scissors, game, player, alice, move, outcome, secret, choice, represent, scissor, draw, challenge, party, world, revelation, blockchain

## Content
## Rock/Paper/Scissors
Our next example of a multi-stage contract is the Rock-Paper-Scissors game, often used as an introductory example for smart contracts. The game is played between two players, Alice and Bob. Each player chooses a secret move independently, and the game outcome is decided after both secrets are revealed.
Let a, b â Z3 be the secret choices of Alice and Bob, respectively, where (0, 1, 2) represent (rock, paper, scissors). If a = b, the game is a draw. Otherwise, if a - b mod 3 = 1, Alice wins; if a - b mod 3 = 2, Bob wins. A key challenge is that the first party to reveal their secret is disadvantaged, as the other party could then adaptively choose their move to guarantee a win. In the physical world, simultaneous revelation prevents this. In the virtual world of blockchains, however, simultaneity cannot be strictly enforced. This potential attack must be handled using cryptographic commitments. The first party (Alice) initially reveals only a commitment to her secret, not the secret itself.
The modified game using commitments proceeds as follows:
Commitment Phase: Alice chooses her secret move a and a secret random value s. She computes a commitment c = H(a || s) (where H is a hash function like Blake2b256) and publishes c (e.g., by locking funds in a contract containing c).
Reveal Phase (Bob): Bob chooses and reveals his move b. At this point, Alice knows the outcome based on a and b, but Bob doesn't know a.
Reveal Phase (Alice): Alice reveals her original move a and the secret s. Anyone can now verify that c = H(a || s), confirming Alice didn't change her move after seeing Bob's. The winner is then determined based on a and b.
This protocol works assuming Alice behaves honestly and reveals a and s regardless of the outcome. However, a malicious Alice might refuse to reveal her commitment if she knows she lost. Smart contracts must handle such edge cases, as they cannot be easily fixed after deployment. In this example, we must penalize Alice (e.g., by forfeiting ...
