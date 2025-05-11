# As a Language - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/ergotree/ergotree-lang/](https://docs.ergoplatform.com/dev/scs/ergotree/ergotree-lang/)
Generated: 2025-05-11

## Summary
This section provides improved and clearer documentation for the ErgoTree language. ErgoTree is a typed, call-by-value, higher-order functional language without recursion. It supports various features such as single-assignment blocks, tuples, optional values, indexed collections with higher-order operations, short-circuiting logical operations, and ternary if-else expressions with lazy branches. It is important to note that all operations in ErgoTree are deterministic, without side effects, and all values are immutable. The semantics of ErgoTree are specified by first translating it to a lower-level language called Core-Î» and then providing its denotational evaluation semantics.

## Keywords
section, documentation, ergotree, language, call, value, order, recursion, feature, assignment, block, tuple, collection, operation, expression, branch, side, effect, semantic, level

## Content
## ErgoTree as a Language#
This section provides improved and clearer documentation for the ErgoTree language. ErgoTree is a typed, call-by-value, higher-order functional language without recursion. It supports various features such as single-assignment blocks, tuples, optional values, indexed collections with higher-order operations, short-circuiting logical operations, and ternary if-else expressions with lazy branches. It is important to note that all operations in ErgoTree are deterministic, without side effects, and all values are immutable.
The semantics of ErgoTree are specified by first translating it to a lower-level language called Core-Î» and then providing its denotational evaluation semantics. The abstract syntax of ErgoTree is defined in Table 1, which represents the Value class hierarchy in the reference implementation. The values in the "Mnemonic" column correspond to specific classes in the reference implementation.

#### Table 1: Abstract syntax of ErgoTree language#
Set Name
Syntax
Mnemonic
Description




\(\mathcal{T} \ni T\)
P
SPredefType
See Types



\(\tau\)
STypeVar
Type variable



\((T_1, \ldots, T_n)\)
STuple
Tuple of \(n\) elements (see [Tuple] type)



\((T_1, \ldots, T_n) \to T\)
SFunc
Function of \(n\) arguments (see [Func] type)



\({{Coll}}[T]\)
SCollection
Collection of elements of type \(T\)



\({{Option}}[T]\)
SOption
Optional value of type \(T\)


\(Term \ni e\)
\(C(v, T)\)
Constant
Typed constant



\(x\)
ValUse
Variable



\(\TyLam{x_i}{T_i}{e}\)
FuncExpr
Lambda expression



\(\Apply{e_f}{\Ov{e_i}}\)
Apply
Application of a functional expression



\(\Apply{e.m}{\Ov{e_i}}\)
MethodCall
Method invocation



\(\Apply{e_f}{\Ov{e_i}}\)
Tuple
Constructor of a tuple with \(n\) items



\(\Apply{\delta}{\Ov{e_i}}\)

Primitive application



\(\text{if}~(e_{\text{cond}})~e_1~\text{else}~e_2\)
If
If-then-else expression



\(\{{ \overline{{\text{val}}}~x_i = e_i;}~e\}\)
BlockExpr
Block expression


\(cd\)
\(\Trait{I}{\overline{ms_i}}\)
STypeCompanion
Interface declaration


\(ms\)
\(\MSig{m[\overline{\tau_i}]}{\overline{x_i : T_i}}{T}\)
SMethod
Method signature declaration
The terms in ErgoTree are assigned types according to the typing rules specified in Typing.
Constants contain both the type and the data value of that type. The type of a constant must correspond to its value for it to be well-formed.
Variables are always typed and identified by a unique ID, which refers to either a lambda-bound variable or a val-bound variable.
Lambda expressions can take a list of lambda-bound variables, which can be used in the body expression. The body expression itself can also be a block expression.
Function application takes an expression of functional type (e.g., \((T_1, \ldots, T_n) \to T\)) and a list of arguments. The notation \(e_f(\Ov{e})\) is not used to represent function application because it suggests that \((\Ov{e})\) is a subterm, which it is not.
Method invocation allows the application of functions defined as...

### Figure 2: Lowering to Core-Î»#
\(Term_{ErgoTree}\)

\(Term_{Core}\)




\(\Low{ \TyLam{x_i}{T_i}{e}      }\)
\(\To\)
\(\Lam{   x:(T_0,\dots,T_n)}{ \Low{ \{ \Ov{\lst{val}~x_i: T_i = x.\_i;}~e\} } }\)


\(\Low{ \Apply{e_f}{\Ov{e_i}}    }\)
\(\To\)
\(\Apply{ \Low{e_f} }{ \Low{(\Ov{e_i})} }\)


\(\Low{ \Apply{e.m}{\Ov{e_i}}    }\)
\(\To\)
\(\Apply{ \Low{e}.m}{\Ov{ \Low{e_i} }}\)


\(\Low{ \Tup{e_1, \dots ,e_n}    }\)
\(\To\)
\(\Tup{   \Low{e_1}, \dots ,\Low{e_n}}\)


\(\Low{ e_1~\text{\|\|}~e_2        }\)
\(\To\)
\(\Low{   \IfThenElse{ e_1 }{ \True }{ e_2 }}\)


\(\Low{ e_1~\text{&&}~e_2      }\)
\(\To\)
\(\Low{   \IfThenElse{ e_1 }{ e_2 }{ \False } }\)


\(\Low{ \IfThenElse{e_{cond}}{e_1}{e_2} }\)
\(\To\)
\(\Apply{(if(\Low{e_{cond}} ,~\Lam{(\_:Unit)}{\Low{e_1}} ,~\Lam{(\_:Unit)}{\Low{e_2}} ))}{}\)


\(\Low{ \{ \Ov{\text{val}~x_i: T_i = e_i;}~e\} }\)
\(\To\)
\(\Apply{ (\Lam{(x_1:T_1)}{( \dots \Apply{(\Lam{(x_n:T_n)}{\Low{e}})}{\Low{e_n}} \dots )}) }{\Low{e_1}}\)\


\(\Low{ \Apply{\delta}{\Ov{e_i}} }\)
\(\To\)
\(\Apply{\delta}{\Ov{ \Low{e_i} }}\)


\(\Low{ e }\)
\(\To\)
\(e\)
All \(n\)-ary lambdas where \(n > 1\) are transformed into single-argument lambdas using tupled arguments.
It should be noted that the \(\IfThenElse{e_{\text{cond}}}{e_1}{e_2}\) term in ErgoTree has lazy evaluation of its branches, while the right-hand-side \(\lst{if}\) is a primitive operation with strict evaluation of the arguments. Laziness is achieved using lambda expressions of type \(\lst{Unit} \to \lst{Boolean}\).
Logical operations (\(\lst{||}\), &&) in ErgoTree, which are lazy (short-circuiting) on the second argument, are translated to \(\lst{if}\) terms in ErgoTree, which are then recursively translated to the corresponding Core-Î» terms.
Syntactic blocks in ErgoTree are eliminated and translated into nested lambda expressions, which unambiguously specify the evaluation semantics of blocks. The evaluation semantics of Core-Î» are specified in evaluation.
Note that the lowering transformation is used solely to specify s...
