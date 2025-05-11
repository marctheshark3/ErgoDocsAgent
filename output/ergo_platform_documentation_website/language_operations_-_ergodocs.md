# Language Operations - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/sigma/lang-ops/](https://docs.ergoplatform.com/dev/scs/sigma/lang-ops/)
Generated: 2025-05-11

## Summary
The 'S' in front of SGroupElement refers to the sigma state code under the ErgoScript. When working on the ErgoScript directly, you will use GroupElement. "AvlTree" -> SAvlTree case class AvlTreeData(digest: ADDigest

## Keywords
front, sgroupelement, sigma, state, code, ergoscript, groupelement, avltree, savltree, case, class, avltreedata(digest

## Content
### Opcodes#
Code
Operation
Comment




1
\(LT(left: Value[SInt], right: Value[SInt])\)$



2
\(LE(left: Value[SInt], right: Value[SInt])\)



3
\(GT(left: Value[SInt], right: Value[SInt])\)



4
\(GE(left: Value[SInt], right: Value[SInt])\)



5
\(EQ\)[\(T1 <: SType, T2 <: SType\)]\((left: Value[T1], right: Value[T2])\)



6
\(NEQ\)[\(T1 <: SType, T2 <: SType\)]\((left: Value[T1], right: Value[T2])\)



7
\(OR(input: Value[SCollection[SBoolean]])\)



8
\(AND(input: Value[SCollection[SBoolean]])\)



9
\(CAND(sigmaTrees: Seq[SigmaTree])\)



10
\(COR(sigmaTrees: Seq[SigmaTree])\)



11
\(Plus(left: Value[SInt], right: Value[SInt])\)



12
\(Minus(left: Value[SInt], right: Value[SInt])\)



13
\(Xor(left: Value[SByteArray], right: Value[SByteArray])\)



14
\(AppendBytes(left: Value[SByteArray], right: Value[SByteArray])\)



15
\(Exponentiate(left: Value[SGroupElement], right: Value[SBigInt])\)



16
\(MultiplyGroup(left: Value[SGroupElement], right: Value[SGroupElement])\)



17
\(IntToByteArray(input: Value[SInt])\)



18
\(ByteArrayToBigInt(input: Value[SByteArray])\)



19
\(CalcBlake2b256(input: Value[SByteArray])\)



20
\(ProveDiffieHellmanTuple(gv: Value[SGroupElement], hv: Value[SGroupElement], uv: Value[SGroupElement], vv: Value[SGroupElement])\)



21
\(IsMember(tree: Value[SAvlTree], key: Value[SByteArray], proof: Value[SByteArray])\)



22
\(IntConstant(value: Long)\)



23
\(TaggedInt(id: Byte)\)



24
\(BigIntConstant(value: BigInteger)\)



25
\(TaggedBigInt(id: Byte)\)



26
\(ByteArrayConstant(value: Array[Byte])\)



27
\(TaggedByteArray(id: Byte)\)



28
\(PropConstant(value: Array[Byte])\)



29
\(TaggedProp(id: Byte)\)



30
\(AvlTreeConstant(value: AvlTreeData)\)



31
\(TaggedAvlTree(id: Byte)\)



32
\(GroupElementConstant(value: GroupElement)\)



33
\(GroupGenerator\)



34
\(TaggedGroupElement(id: Byte)\)



35
\(BooleanConstant(val value: Boolean)\)



36
\(TaggedBoolean(id: Byte)\)



37
\(TaggedBox(id: Byte)\)



38
\(ConcreteCollection\)[\(V <: S...

### TaggedVariable#
Remove unused TaggedVariable node #657

### SGroupElement#
The 'S' in front of SGroupElement refers to the sigma state code under the ErgoScript. When working on the ErgoScript directly, you will use GroupElement.

#### SAvlTree (AvlTreeData)#
"AvlTree" -> SAvlTree


case class AvlTreeData(digest: ADDigest
