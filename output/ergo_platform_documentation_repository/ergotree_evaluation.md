# ErgoTree Evaluation
Source: docs/dev/scs/ergotree/evaluation.md
Generated: 2025-05-11

## Summary
# ErgoTree Evaluation
$$
\newcommand{\TEnv}{\Gamma}
\newcommand{\Der}[2]{#1~\vdash~#2}
\newcommand{\DerV}[2]{#1~\vdash^{\text{\lst{v}}}~#2}
\newcommand{\DerC}[2]{#1~\vdash^{\text{\lst{c}}}~#2}
\newcommand{\DerEnv}[1]{\Der{\TEnv}{#1}}
\newcommand{\DerEnvV}[1]{\DerV{\TEnv}{#1}}
\newcommand{\DerEnvC}[1]{\DerC{\TEnv}{#1}}
\newcommand{\lst}[1]{#1}
\newcommand{\Tup}[1]{(#1)}
\newcommand{\Apply}[2]{#1\langle#2\rangle}
\newcommand{\MSig}[3]{\text{def}~#1(#2): #3}
\newcommand{\Ov}[1]{\overline{#1}}
\newcommand{\TyLam}[3]{\lambda(\Ov{#1:#2}).#3}
\newcommand{\Trait}[2]{\text{trait}~#1~\{ #2 \}}
\newcommand{\To}{\mapsto}
\newcommand{\Low}[1]{\mathcal{L}{[\![#1]\!]}}
\newcommand{\Lam}[2]{\lambda#1.#2}
\newcommand{\IfThenElse}[3]{\text{if}~(#1)~#2~\text{else}~#3}
\newcommand{\False}{\text{false}}
\newcommand{\True}{\text{true}}
\newcommand{\langname}{ErgoTree}
\newcommand{\corelang}{Core-\lambda}
\newcommand{\Denot}[1]{[\![#1]\!]}  
$$


Evaluation of $\langname$ is specified by its translation to $\corelang$, whose terms form a subset of $\langname$ terms. Thus, typing rules of $\corelang$ form a subset of typing rules of $\langname$.

Here we specify evaluation semantics of $\corelang$, which is based on call-by-value (CBV) lambda calculus. Evaluation of $\corelang$ is specified using denotational semantics. To do that, we first specify denotations of types, then typed terms and then equations of denotational semantics. /// details | Definition 1
    {type: note, open: true}

**The following $\corelang$ terms are called values:**

$$V :== x \mid C(d, T) \mid \Lam{x}{M}$$

All $\corelang$ terms are called ***producers***.

## Keywords
ergotree, evaluation, \newcommand{\tenv}{\gamma, \newcommand{\der}[2]{#1~\vdash~#2, \newcommand{\derenv}[1]{\der{\tenv}{#1, \newcommand{\derenvv}[1]{\derv{\tenv}{#1, \newcommand{\derenvc}[1]{\derc{\tenv}{#1, \newcommand{\lst}[1]{#1, \newcommand{\tup}[1]{(#1, \newcommand{\msig}[3]{\text{def}~#1(#2, \newcommand{\ov}[1]{\overline{#1, \newcommand{\tylam}[3]{\lambda(\ov{#1:#2}).#3, \newcommand{\low}[1]{\mathcal{l}{[\![#1]\, \newcommand{\lam}[2]{\lambda#1.#2, \newcommand{\ifthenelse}[3]{\text{if}~(#1)~#2~\text{else}~#3, \newcommand{\false}{\text{false, \newcommand{\true}{\text{true, \newcommand{\langname}{ergotree, \langname$, translation

## Content
## ErgoTree Evaluation
$$
\newcommand{\TEnv}{\Gamma}
\newcommand{\Der}[2]{#1~\vdash~#2}
\newcommand{\DerV}[2]{#1~\vdash^{\text{\lst{v}}}~#2}
\newcommand{\DerC}[2]{#1~\vdash^{\text{\lst{c}}}~#2}
\newcommand{\DerEnv}[1]{\Der{\TEnv}{#1}}
\newcommand{\DerEnvV}[1]{\DerV{\TEnv}{#1}}
\newcommand{\DerEnvC}[1]{\DerC{\TEnv}{#1}}
\newcommand{\lst}[1]{#1}
\newcommand{\Tup}[1]{(#1)}
\newcommand{\Apply}[2]{#1\langle#2\rangle}
\newcommand{\MSig}[3]{\text{def}~#1(#2): #3}
\newcommand{\Ov}[1]{\overline{#1}}
\newcommand{\TyLam}[3]{\lambda(\Ov{#1:#2}).#3}
\newcommand{\Trait}[2]{\text{trait}~#1~{ #2 }}
\newcommand{\To}{\mapsto}
\newcommand{\Low}[1]{\mathcal{L}{[![#1]!]}}
\newcommand{\Lam}[2]{\lambda#1.#2}
\newcommand{\IfThenElse}[3]{\text{if}~(#1)~#2~\text{else}~#3}
\newcommand{\False}{\text{false}}
\newcommand{\True}{\text{true}}
\newcommand{\langname}{ErgoTree}
\newcommand{\corelang}{Core-\lambda}
\newcommand{\Denot}[1]{[![#1]!]}
$$
Evaluation of $\langname$ is specified by its translation to $\corelang$, whose terms form a subset of $\langname$ terms. Thus, typing rules of $\corelang$ form a subset of typing rules of $\langname$.
Here we specify evaluation semantics of $\corelang$, which is based on call-by-value (CBV) lambda calculus. Evaluation of $\corelang$ is specified using denotational semantics. To do that, we first specify denotations of types, then typed terms and then equations of denotational semantics.
/// details | Definition 1
    {type: note, open: true}
The following $\corelang$ terms are called values:
$$V :== x \mid C(d, T) \mid \Lam{x}{M}$$
All $\corelang$ terms are called producers. (This is because, when evaluated, they produce a value.)
///
We now describe and explain a denotational semantics for the $\corelang$ language. The key principle is that each type $A$ denotes a set $\Denot{A}$ whose elements are the denotations of values of the type $A$.
Thus the type $\lst{Boolean}$ denotes the 2-element set ${\lst{true},\lst{false}}$, because there are two values of type $\lst{Boolean}$....
