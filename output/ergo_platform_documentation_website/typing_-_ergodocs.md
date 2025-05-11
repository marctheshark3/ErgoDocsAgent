# Typing - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/scs/ergotree/typing/](https://docs.ergoplatform.com/dev/scs/ergotree/typing/)
Generated: 2025-05-11

## Summary
\(\langname\) is a strictly typed language, in which every term should have a type in order to be wellformed and evaluated. Typing judgement of the form \(\Der{\Gamma}{e : T}\) say that \(e\) is a term of type \(T\) in the typing context \(\Gamma\). \(\frac{\DerEnv{e_1 :~T_1}~\wedge~\forall k\in\{2,\dots,n\}~\Der{\Gamma,x_1:~T_1,\dots,x_{k-1}:~T_{k-1}}{e_k:~T_k}~\wedge~\Der{\Gamma,x_1:~T_1,\dots,x_n:~T_n}{e:~T}}{ \DerEnv{\{ \Ov{\text{val}}~x_i = e_i;}~e\}~:~T} ~(BlockExpr)\) Note that each well-typed term has exactly one type; hence we assume there exists a function \(termType: Term \to \mathcal{T}\) which relates each well-typed term with the corresponding type. Primitive operations can be parameterized with type variables; for example,addition has the signature \(+~:~ (T,T) \to T\) where \(T\) is a numeric type. Function \(ptype\), defined in primops, returns a type of primitive operation specialized for concrete types of its arguments, for example, \(ptype(+,Int, Int) = (Int, Int) \to Int\).

## Keywords
\(\langname\, language, term, type, order, judgement, form, \(e\, context, \(\frac{\derenv{e_1, ~t_1}~\wedge~\forall, k\in\{2,\dots, n\}~\der{\gamma, x_1:~t_1,\dots, x_{k-1}:~t_{k-1}}{e_k:~t_k}~\wedge~\der{\gamma, x_n:~t_n}{e:~t, \derenv{\, \ov{\text{val}}~x_i, e_i;}~e\}~:~t, function

## Content
## ErgoTree Typing#
\(\langname\) is a strictly typed language, in which every term should have a type in order to be wellformed and evaluated. Typing judgement of the form \(\Der{\Gamma}{e : T}\) say that \(e\) is a term of type \(T\) in the typing context \(\Gamma\).

#### Figure 3: Typing rules of ErgoTree#
\[\frac{}{\Der{\Gamma}{C(\_, T)~:~T}}~(Const)\]
\[\frac{}{\Der{\Gamma,x~:~T}{x~:~T}}~(Var)\]
\[\frac{\Ov{\DerEnv{e_i:~T_i}}~~ptype(\delta, \Ov{T_i}) :~(T_1,\dots,T_n) \to T}{\Apply{\delta}{\Ov{e_i}}:~T}~(Prim)\]
\[\frac{\DerEnv{e_1 :~T_1}~~\dots~~\DerEnv{e_n :~T_n}}      {\DerEnv{(e_1,\dots,e_n)~:~(T_1,\dots,T_n)}}~(Tuple)\]
\[\frac{\DerEnv{e~:~I,~e_i:~T_i}~~mtype(m, I, \Ov{T_i})~:~(I, T_1,\dots,T_n) \to T}{ \Apply{e.m}{\Ov{e_i}}:~T }~(MethodCall)\]
\[\frac{\Der{\TEnv,\Ov{x_i:~T_i}}{e~:~T}}{\Der{\Gamma}{\TyLam{x_i}{T_i}{e}~:~(T_0,\dots,T_n) \to T}}~(FuncExpr)\]
\[\frac{\Der{\TEnv}{e_f:~(T_1,\dots,T_n) \to T}~~~\Ov{\Der{\TEnv}{e_i:~T_i}} }{ \Der{\Gamma}{\Apply{e_f}{\Ov{e_i}}~:~T} }~(Apply)\]
\[\frac{\DerEnv{e_{cond}:~\lst{Boolean}}~~\DerEnv{e_1:~T}~~\DerEnv{e_2 :~T} }{\DerEnv{\IfThenElse{e_{cond}}{e_1}{e_2}~:~T} }~\lst{(If)}\]
\(\frac{\DerEnv{e_1 :~T_1}~\wedge~\forall k\in\{2,\dots,n\}~\Der{\Gamma,x_1:~T_1,\dots,x_{k-1}:~T_{k-1}}{e_k:~T_k}~\wedge~\Der{\Gamma,x_1:~T_1,\dots,x_n:~T_n}{e:~T}}{ \DerEnv{\{ \Ov{\text{val}}~x_i = e_i;}~e\}~:~T} ~(BlockExpr)\)
Note that each well-typed term has exactly one type; hence we assume there exists a function \(termType: Term \to \mathcal{T}\) which relates each well-typed term with the corresponding type.
Primitive operations can be parameterized with type variables; for example,addition has the signature \(+~:~ (T,T) \to T\) where \(T\) is a numeric type. Function \(ptype\), defined in primops, returns a type of primitive operation specialized for concrete types of its arguments, for example, \(ptype(+,Int, Int) = (Int, Int) \to Int\).
Similarly, the function \(mtype\) returns a type of method specialized for concrete types of the arguments of the MethodCall term.
BlockExpr rule defines a type of well-formed block expression. It assumes a total ordering on val definitions. If a block expression is not well-formed, than is cannot be typed and evaluated.
The rest of the rules are standard for typed lambda calculus.
