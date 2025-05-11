# Utilizing (E)mail Client for Restricted or Unavailable Internet Access
Source: docs/uses/blocked_web.md
Generated: 2025-05-11

## Summary
# Utilizing (E)mail Client for Restricted or Unavailable Internet Access

This concept is driven by two primary factors. 1. Certain countries, including China and Belarus, have already implemented restrictions on Tor. It's plausible to anticipate similar restrictions on cryptocurrency protocols in the future. 2.

## Keywords
utilizing, e)mail, client, restricted, unavailable, internet, access, concept, factor, country, china, belarus, restriction, cryptocurrency, protocol, future, period, unrest, government, egypt

## Content
## Utilizing (E)mail Client for Restricted or Unavailable Internet Access
This concept is driven by two primary factors.
Certain countries, including China and Belarus, have already implemented restrictions on Tor. It's plausible to anticipate similar restrictions on cryptocurrency protocols in the future.
During periods of civil unrest, governments often resort to shutting down the Internet. This has been observed in countries like Egypt, Ethiopia, Sudan, Iran, and Turkey.
Regardless, individuals should have the ability to secure their assets, especially when these assets are threatened by monetary policies, political instability, or warfare.
The combination of digital communication and digital currency can provide a solution to this issue.
For Bitcoin, one potential solution could be the Blockstream satellite network. However, the satellite signal is susceptible to jamming. Alternatives include email (typically the last to be blocked) or other low-bandwidth, non-interactive communication methods (fax, modem call over a landline to a bulletin board system, mail).
Let's consider a scenario where Alice wants to purchase X ERGs from Bob (paying with cash), but their area has limited or no Internet access. Bob owns a box protected by a public key (stored locally). The protocol could proceed as follows.
Bob initiates a transaction from his box, creating a new box where X ERG are secured by the condition Before deadline: Bob's signature and spending transaction have an output of *X* ergs which belongs to Alice's public key; After deadline: Bob's signature. This new box is referred to as the "deal box".
It's important to note that outputs with respective identifiers are known for a signed transaction.
Bob transmits the transaction via (e)mail to a gateway. The gateway sends an efficient NiPoPoW proof for a header with sufficient confirmations + proof of box membership against the state digest from the header. This proof is compact, only tens of kilobytes. For enhanced security, Bob may also request header proof from another gateway.


Bob prese...
