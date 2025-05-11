# ErgoScript FAQ
Source: docs/dev/scs/ergoscript/ergoscript-faq.md
Generated: 2025-05-11

## Summary
# ErgoScript FAQ

## Why Does Ergo Use [Coll] Instead of an Array?

Ergo uses [Coll] instead of an Array to maintain a one-to-one correspondence between ErgoScript and Scala. In Scala, an Array is mutable, which means its elements can be changed after it's created. However, all elements in ErgoScript are immutable - they can't be altered after creation. This difference could lead to confusion if both languages used the term "Array".

## Keywords
ergoscript, ergo, array, correspondence, scala, element, creation, difference, confusion, language, term, design, discussion, slack, channel, name, none, coll, collection[int, choice

## Content
### Why Does Ergo Use [Coll] Instead of an Array?
Ergo uses [Coll] instead of an Array to maintain a one-to-one correspondence between ErgoScript and Scala. In Scala, an Array is mutable, which means its elements can be changed after it's created. However, all elements in ErgoScript are immutable - they can't be altered after creation. This difference could lead to confusion if both languages used the term "Array".
During the design discussions in our Slack channel in 2018-2019, several names were considered, but none seemed more suitable than "Coll". The term "Collection[Int]" was also considered, but it appeared visually unappealing and cumbersome to type.
"Seq" wasn't an ideal choice either, as it is covariant in Scala while Coll is not covariant in ErgoScript. Covariance refers to the ability of a type to change its element type to a subtype, which doesn't align with the principles of ErgoScript.
