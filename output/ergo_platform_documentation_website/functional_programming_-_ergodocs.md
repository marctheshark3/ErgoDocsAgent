# Functional Programming - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/ergoscript/functional-programming/](https://docs.ergoplatform.com/dev/scs/ergoscript/functional-programming/)
Generated: 2025-05-11

## Summary
Functional programming is a significant part of ErgoScript's capabilities. The next examples demonstrate the application of functional features in ErgoScript. Consider a situation where we want to allow a box to be spent only if all the following conditions are met: The conditions above can be coded into the following program: The address that corresponds to the program above is 3PwBHASpxaJa5i3vmLtUTvEqjbJWcpqnyuX9hSmUbaK2HAmoDLHmYSMm4up5pCRytSStEhsHnzTfpHzvCRZ. The absence of the var keyword might initially seem limiting as it enforces immutability. For example, to calculate the sum of all inputs, you might think about storing the cumulative value in a var and iterating over all inputs, updating the var with each iteration.

## Keywords
programming, part, ergoscript, capability, example, application, feature, situation, condition, program, address, absence, keyword, immutability, input, value, iteration, power, restriction, range

## Content
## Functional Programming in ErgoScript#
Functional programming is a significant part of ErgoScript's capabilities. The next examples demonstrate the application of functional features in ErgoScript. Consider a situation where we want to allow a box to be spent only if all the following conditions are met:
The spender knows the discrete log of the given elliptic curve (EC) point 0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352.
All input boxes must be protected by the same ErgoScript program.
The conditions above can be coded into the following program:
{
   val z = decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS"))
   def sameAsMe(box:Box) = box.propositionBytes == SELF.propositionBytes

   proveDlog(z) && INPUTS.forall(sameAsMe)       
}
The address that corresponds to the program above is 3PwBHASpxaJa5i3vmLtUTvEqjbJWcpqnyuX9hSmUbaK2HAmoDLHmYSMm4up5pCRytSStEhsHnzTfpHzvCRZ.
The absence of the var keyword might initially seem limiting as it enforces immutability. For example, to calculate the sum of all inputs, you might think about storing the cumulative value in a var and iterating over all inputs, updating the var with each iteration.
Here's an example of how you can compute the sum of all inputs in ErgoScript. Suppose an additional condition is that the box can only be spent if the sum of all inputs is greater than 1 Erg (or 1000000000 nanoErgs).
{
   val z = decodePoint(fromBase64("AlCGOtZKh66KL+g8GvGoQDy1P1PkhthRHa2KBIh+WyNS"))
   def sameAsMe(box:Box) = box.propositionBytes == SELF.propositionBytes
   val sum = INPUTS.fold(0L, { (accum:Long, box: Box) => accum + box.value }) 

   proveDlog(z) && INPUTS.forall(sameAsMe) && sum > 1000000000       
}
This corresponds to the address
49AkSSPuVSQHk17C4JLxhqxH7yL5NMWxdEsELp6MNzYeJZvF7iKk3Jgi4fh96o7RJeaU8JSVPvZ5EhCgboQy9d68QreWaYcVxSUcsd8UCamHPsv9kHzqhe4tAM5D7ZmF.
These examples demonstrate the power of functional programming in ErgoScript. Despite the apparent restriction of immutability, a wide range of functions can...
