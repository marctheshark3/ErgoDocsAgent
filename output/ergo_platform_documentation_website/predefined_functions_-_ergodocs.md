# Predefined Functions - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/ergotree/functions/](https://docs.ergoplatform.com/dev/scs/ergotree/functions/)
Generated: 2025-05-11

## Summary
This page is a WIP. Please see ErgoTree.pdf for full details.

## Keywords
page, ergotree.pdf, detail

## Content
## ErgoTree Functions#
This page is a WIP. Please see ErgoTree.pdf for full details.
Code
Mnemonic
Description
Description




115
ConstantPlaceholder
Int    => T
Create special ErgoTree node which can be replaced by constant with given id.


116
SubstConstants
Coll[Byte], Coll[Int], Coll[T]    => Coll[Byte]
...


122
LongToByteArray
Long    => Coll[Byte]
Converts Long value to big-endian bytes representation.


123
ByteArrayToBigInt
Coll[Byte]    => BigInt
Convert big-endian bytes representation (Coll[Byte]) to BigInt value.


124
ByteArrayToLong
Coll[Byte]    => Long
Convert big-endian bytes representation (Coll[Byte]) to Long value.


125
Downcast
(T    => R)
Cast this numeric value to a smaller type (e.g. Long to Int). Throws exception if overflow.


126
Upcast
(T    => R)
Cast this numeric value to a bigger type (e.g. Int to Long)


140
SelectField
(T, Byte    => R)
Select tuple field by its 1-based index. E.g. input._1 is transformed to SelectField(input, 1


143
LT
T, T    => Boolean
Returns true is the left operand is less then the right operand, false otherwise.


144
LE
T, T    => Boolean
Returns true is the left operand is less then or equal to the right operand, false otherwise.


145
GT
T, T    => Boolean
Returns true is the left operand is greater then the right operand, false otherwise.


146
GE
T, T    => Boolean
Returns true is the left operand is greater then or equal to the right operand, false otherwise.


147
EQ
T, T    => Boolean
Compare equality of left and right arguments


148
NEQ
T, T    => Boolean
Compare inequality of left and right arguments


149
If
Boolean, T, T    => T
Compute condition, if true then compute trueBranch else compute falseBranch


150
AND
Coll[Boolean]    => Boolean
Returns true if \emph{all the elements in collection are true.


151
OR
Coll[Boolean]    => Boolean
Returns true if \emph{any the elements in collection are true.


152
AtLeast
Int, Coll[SigmaProp]    => SigmaProp
...


153
Minus
T, T    => T
Returns a result of subtracting second...
