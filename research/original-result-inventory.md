# Original manuscript inventory

Source: Nicholas Ham, arXiv:1311.4766v5 (5 May 2021). Retrieved 16 October 2026.

Extracted **74 numbered environments**: all numbered theorems, propositions, lemmas, corollaries, definitions and examples in source Sections 2--5. Numbering is shared within each section. Statements below reproduce the author-owned source with comments removed and whitespace normalized, not a certified translation. Proofs are not reproduced here; the priority proof is extracted separately in dasgupta-maskin.md.

The ambient assumptions and explicit source references are recorded for each item. Explicit dependencies include references appearing inside the statement/proof; implicit dependencies and hidden assumptions remain to be audited. A missing explicit reference does not mean a result has no dependencies. Bibliography keys are the original source keys. External-source verification is separate from verification of Ham's statement.

## Coverage

| Section | Numbered environments |
|---|---:|
| 2 | 5 |
| 3 | 25 |
| 4 | 28 |
| 5 | 16 |

## Example 2.1

Source: `section-background.tex:54`. Ambient assumptions: Finite n>=2; nonempty finite A_i; real payoffs; mixed profiles are independent product distributions. Extra restrictions are in the reproduced statement.

Explicit assumptions/conclusion (source statement):

```latex
\label{fullsymeg} 3-player 2-strategy game.
        \begin{center}
        \begin{game}{2}{2}[$(a,,)$]
                     \>  $a$      \>  $b$      \\
                $a$  \>  $1,1,1$  \>  $2,2,3$  \\
                $b$  \>  $2,3,2$  \>  $4,5,5$
        \end{game}
        \hspace*{5mm}
        \begin{game}{2}{2}[$(b,,)$]
                 \>  $a$      \>  $b$      \\
                $a$  \>  $3,2,2$  \>  $5,4,5$  \\
                $b$  \>  $5,5,4$  \>  $6,6,6$
        \end{game}
        \end{center}
        We find the payoff to player $3$ for the strategy profile $(b, b, a) \in A$ as follows: reading the strategy profile from left to right, player $1$ has chosen the second matrix, player $2$ has chosen the second row and player $3$ has chosen the first column, the third value of which is the payoff to player $3$. Hence $u_3(b,b,a) = 4$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Proposition 2.2

Source: `section-background.tex:94`. Ambient assumptions: Finite n>=2; nonempty finite A_i; real payoffs; mixed profiles are independent product distributions. Extra restrictions are in the reproduced statement.

Explicit assumptions/conclusion (source statement):

```latex
The function $f$ defined above satisfies:
        \begin{enumerate}
            \item For each $\sigma = (\sigma_1, \ldots, \sigma_n) \in \nabla(A)$, $f(\sigma) = f(\sigma_1, \ldots, \sigma_n) \in \Delta(A)$ (ie. $f$ is well-defined);
            \item For each $\sigma, \sigma' \in \nabla(A)$, $f(\sigma) = f(\sigma')$ if and only if $\sigma = \sigma'$ (ie. $f$ is injective); and
            \item $f\left(\nabla(A)\right) \subset \Delta(A)$ (ie. $f$ is not surjective).
        \end{enumerate}
```

Explicit dependencies: source label eqn:zzz1; source label eqn:zzz3; source label eqn:zzz2; source label eqn:zzz4 Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Proposition 2.3

Source: `section-background.tex:243`. Ambient assumptions: Finite n>=2; nonempty finite A_i; real payoffs; mixed profiles are independent product distributions. Extra restrictions are in the reproduced statement.

Explicit assumptions/conclusion (source statement):

```latex
Given a game $\Gamma = (N, A, u)$, for each player $i \in N$:
        \[\underline{u}_i = \max_{\sigma_i \in \Delta(A_i)}\min_{\sigma_{-i} \in {\nabla(A)}_{-i}} u_i(\sigma_i, \sigma_{-i}) \leq \min_{\sigma_{-i} \in {\nabla(A)}_{-i}}\max_{\sigma_i \in \Delta(A_i)} u_i(\sigma_i, \sigma_{-i}) = \overline{u}_i.\]
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Proposition 2.4

Source: `section-background.tex:261`. Ambient assumptions: Finite n>=2; nonempty finite A_i; real payoffs; mixed profiles are independent product distributions. Extra restrictions are in the reproduced statement.

Explicit assumptions/conclusion (source statement):

```latex
Given a $2$-player zero-sum game $(\{1, 2\}, A_1 \times A_2, (u_1, u_2))$, the maximin and minimax values for each player are equal to minus the minimax and maximin values for the other player.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Proposition 2.5

Source: `section-background.tex:275`. Ambient assumptions: Finite n>=2; nonempty finite A_i; real payoffs; mixed profiles are independent product distributions. Extra restrictions are in the reproduced statement.

Explicit assumptions/conclusion (source statement):

```latex
\label{prop:2pzsminmax=maxmin}
        \cite{VNM} Given a $2$-player zero-sum game $\Gamma = (\{1, 2\}, A_1\times A_2, (u_1, u_2))$, the maximin and minimax values for each player are equal. Ie. $\underline{u}_i = \overline{u}_i$ for all $i \in \{1, 2\}$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: VNM.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 3.1

Source: `section-label-dependent-symmetric-games.tex:11`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{simpleactionprop}
    For each $s \in A$ and $\pi \in S_N$, $s \mapsto \pi(s)$ is a left action of $S_N$ on $A$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 3.2

Source: `section-label-dependent-symmetric-games.tex:24`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
For each $s \in A$ and $\pi \in S_N$, $s \mapsto \pi^{-1}(s)$ is a right action of $S_N$ on $A$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Corollary 3.3

Source: `section-label-dependent-symmetric-games.tex:30`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{utilityactionprop}
    For each $\pi, \tau \in S_N$, $u_{(\tau \circ \pi)(i)} \circ (\tau \circ \pi) = (u_{\tau(\pi(i))} \circ \tau) \circ \pi$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Proposition 3.4

Source: `section-label-dependent-symmetric-games.tex:51`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
For each $i \in N$, $\pi \in S_N$ and $\sigma \in \nabla(A)$, $\pi(\sigma_i, \sigma_{-i}) = \Bigl(\pi(\sigma_i), \pi(\sigma_{-i})\Bigr)$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Proposition 3.5

Source: `section-label-dependent-symmetric-games.tex:61`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{prop:firstgroupoidprop}
    $\set{\sigma_i \mapsto \pi(\sigma_i): i \in N, \pi \in S_N}$ is a subgroupoid of $\cup_{i, j \in N}\bij(\Delta(A_i), \Delta(A_j))$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Proposition 3.6

Source: `section-label-dependent-symmetric-games.tex:76`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{prop:secondgroupoidprop}
    $\set{\sigma_{-i} \mapsto \pi(\sigma_{-i}): i \in N, \pi \in S_N}$ is a subgroupoid of $\cup_{i, j \in N}\bij({\nabla(A)}_{-i}, {\nabla(A)}_{-j})$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 3.7

Source: `section-label-dependent-symmetric-games.tex:120`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
$\pi \in S_N$ is an \textit{invariant} of $\Gamma$ if for each $i \in N$, $u_i = u_{\pi(i)} \circ \pi$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 3.8

Source: `section-label-dependent-symmetric-games.tex:124`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
The invariants of a game form a group.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 3.9

Source: `section-label-dependent-symmetric-games.tex:136`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
$\Gamma$ is \textit{weakly anonymous} if for each $i \in N$, $\pi \in S_{N-\{i\}}$, $u_i = u_i \circ \pi$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 3.10

Source: `section-label-dependent-symmetric-games.tex:140`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{weaklyanoneg}
    Weakly Anonymous 3-player game.
    \begin{center}
    \begin{game}{2}{2}[$(a,,)$]
     \> $a$      \> $b$ \\
        $a$   \> $0,1,2$  \> $4,6,7$ \\
        $b$   \> $4,5,8$  \> $9,12,14$
    \end{game}
    \hspace*{10mm}
    \begin{game}{2}{2}[$(b,,)$]
     \> $a$     \> $b$ \\
        $a$   \> $3,6,8$ \> $10,11,14$ \\
        $b$   \> $10,12,13$ \> $15,16,17$
    \end{game}
    \end{center}
    The reader may like to verify that $u_i = u_i \circ (jk)$ for all distinct $i, j, k \in N$. For example, $u_1(a,b,a) = 4 = u_1\bigl((23)(a,b,a)\bigr) = u_1(a,a,b)$. Since $S_{N-\{i\}} = \{e, (jk)\}$ for all $i \in N$, $\Gamma$ is weakly anonymous.

    When we say that players do not distinguish between their opponents, we mean for example that when playing $a$, player $1$ is indifferent between the strategy profiles $(a,a,b)$ and $(a,b,a)$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 3.11

Source: `section-label-dependent-symmetric-games.tex:162`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
$\Gamma$ is \textit{anonymous} if for each $i \in N$, $\pi \in S_N$, $u_i = u_i \circ \pi$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 3.12

Source: `section-label-dependent-symmetric-games.tex:166`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{anoneg}
        Anonymous 3-player game.
        \begin{center}
        \begin{game}{2}{2}[$(a,,)$]
                  \> $a$      \> $b$ \\
            $a$   \> $0,1,2$  \> $3,4,5$ \\
            $b$   \> $3,4,5$  \> $6,7,8$
        \end{game}
        \hspace*{10mm}
        \begin{game}{2}{2}[$(b,,)$]
                  \> $a$     \> $b$ \\
            $a$   \> $3,4,5$ \> $6,7,8$ \\
            $b$   \> $6,7,8$ \> $9,10,11$
        \end{game}
        \end{center}
        The reader may like to verify the orbits of $A$ are given by $A/S_N = \bigl\{\{(a,a,a)\}, \newline\{(a,a,b), (a,b,a), (b,a,a)\}, \{(a,b,b), (b,a,b), (b,b,a)\}, \{(b,b,b)\}\bigr\}$ and that each player has the same payoff for each orbit in $A/S_N$.

        For example, let $\pi = (123)$, then we have $\pi(s_1, s_2, s_3) = (s_{\pi^{-1}(1)}, s_{\pi^{-1}(2)}, s_{\pi^{-1}(3)}) = (s_3, s_1, s_2)$ giving us $\pi(a,a,b) = (b,a,a)$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 3.13

Source: `section-label-dependent-symmetric-games.tex:188`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
$\Gamma$ is \textit{fully anonymous} if for each $i, j \in N$, $\pi \in S_N$, $u_i = u_j \circ \pi$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 3.14

Source: `section-label-dependent-symmetric-games.tex:192`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
Fully anonymous 3-player game.
        \begin{center}
        \begin{game}{2}{2}[$(a,,)$]
                  \> $a$      \> $b$ \\
            $a$   \> $1,1,1$  \> $2,2,2$ \\
            $b$   \> $2,2,2$  \> $3,3,3$
        \end{game}
        \hspace*{10mm}
        \begin{game}{2}{2}[$(b,,)$]
                  \> $a$     \> $b$ \\
            $a$   \> $2,2,2$ \> $3,3,3$ \\
            $b$   \> $3,3,3$ \> $4,4,4$
        \end{game}
        \end{center}
        The orbits of $A$ for the above game are the same as in Example \ref{anoneg}, however now all players have the same payoff for each orbit.
```

Explicit dependencies: Example 3.12 Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 3.15

Source: `section-label-dependent-symmetric-games.tex:218`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
$\Gamma$ is \textit{standard symmetric} \cite{NoahXE} if there exists a transitive subgroup $H$ of the player permutations such that for each $i \in N$ and $\pi \in H$, $u_i = u_{\pi(i)} \circ \pi$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: NoahXE.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 3.16

Source: `section-label-dependent-symmetric-games.tex:224`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{stdsymeg} Standard symmetric 3-player game.
        \begin{center}
        \begin{game}{2}{2}[$(a,,)$]
                \>  $a$      \>  $b$      \\
            $a$ \>  $1,1,1$  \>  $3,7,4$  \\
            $b$ \>  $7,4,3$  \>  $6,5,8$
        \end{game}
        \hspace*{5mm}
        \begin{game}{2}{2}[$(b,,)$]
                \>  $a$      \>  $b$      \\
            $a$ \>  $4,3,7$  \>  $8,6,5$  \\
            $b$ \>  $5,8,6$  \>  $2,2,2$
        \end{game}
        \end{center}

        The reader may like to verify that $\Gamma$ is invariant under $(123)$ and not invariant under $(12)$. Since $\langle (123)\rangle = \{e, (123), (132)\}$ is a transitive subgroup of $S_3$, $\Gamma$ is standard symmetric. Furthermore since $(12)$ is not an invariant the players are not indifferent between all possible position arrangements.

        A useful analogy for considering the fairness of $\Gamma$ is a game with three players sitting in a circle such that each player is indifferent between circular rotations of positions, and not indifferent to their opponents swapping positions. A similar notion of fairness/symmetry is often used by the author when coding map generators for artificial intelligence programming contests where users write bots to play games against each other. The maps are two dimensional grids with the edges wrapped, ie. on the surface of a torus, and constructed in such a way that everyone is indifferent between some reorderings of the players.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 3.17

Source: `section-label-dependent-symmetric-games.tex:246`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{fullsymdef}
    $\Gamma$ is \textit{fully symmetric} if it is invariant under $S_N$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Theorem 3.18

Source: `section-label-dependent-symmetric-games.tex:254`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{basicsymequivthm}
    The following conditions are equivalent:
    \begin{enumerate}
        \item $\Gamma$ is fully symmetric;
        \item $\Gamma$ is standard symmetric and weakly anonymous;
        \item For each $i \in N$ and $\pi \in S_N$, $u_{\pi(i)} = u_i \circ \pi^{-1}$;
        \item For each $i \in N$ and $\tau \in T_N$, $u_i = u_{\tau(i)} \circ \tau$; and
        \item For each $i \in N$ and $\tau \in T_N$, $u_i = u_{\tau(i)} \circ \tau^{-1}$.
    \end{enumerate}
```

Explicit dependencies: Corollary 3.3 Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 3.19

Source: `section-label-dependent-symmetric-games.tex:281`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{brandtlemma}
    \cite{brandt2009symmetries} The following conditions are equivalent:
    \begin{enumerate}
        \item $\Gamma$ is fully anonymous; and
        \item $\Gamma$ is fully symmetric and $u_i = u_j$ for all $i, j \in N$.
    \end{enumerate}
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: brandt2009symmetries.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 3.20

Source: `section-label-dependent-symmetric-games.tex:289`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{DMlemma}
    Let $\pi, \tau \in S_N$. If $u_i = u_{\pi(i)} \circ \pi^{-1} = u_{\tau(i)} \circ \tau^{-1}$ for all $i \in N$ then $u_i = u_{(\tau \circ \pi)(i)} \circ (\pi \circ \tau)^{-1}$ for all $i \in N$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Theorem 3.21

Source: `section-label-dependent-symmetric-games.tex:296`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{DMprop}
    If $n \geq 3$ then the following conditions are equivalent:
    \begin{enumerate}
        \item $\Gamma$ is fully symmetric and $u_i = u_j$ for all $i, j \in N$; and
        \item For each $i \in N$ and $\pi \in S_N$, $u_i = u_{\pi(i)} \circ \pi^{-1}$.
    \end{enumerate}
```

Explicit dependencies: Lemma 3.20 Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 3.22

Source: `section-label-dependent-symmetric-games.tex:318`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
A $2$-player zero-sum game is \textit{fair} \cite[17.11, 28.1, 28.2]{VNM} if its value is $0$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: VNM.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Proposition 3.23

Source: `section-label-dependent-symmetric-games.tex:322`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\cite{VNM} If a $2$-player zero-sum game is fully symmetric then it is fair.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: VNM.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 3.24

Source: `section-label-dependent-symmetric-games.tex:326`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
We shall refer to a game $\Gamma = (N, A, u)$ as:
    \begin{enumerate}
        \item \textit{maximin fair} if $\underline{u}_i = \underline{u}_j$ for all $i, j \in N$;
        \item \textit{minimax fair} if $\overline{u}_i = \overline{u}_j$ for all $i, j \in N$;
        \item \textit{very-weakly-fair} if $\underline{u}_i = \underline{u}_j$ and $\overline{u}_i = \overline{u}_j$ for all $i, j \in N$;
        \item \textit{weakly-fair} if $\underline{u}_i = \overline{u}_i = \underline{u}_j = \overline{u}_j$ for all $i, j \in N$;
        \item \textit{fair} if $\underline{u}_i = \overline{u}_i = 0$ for all $i \in N$;
        \item \textit{standard fair} if utility values are preserved under a transitive subgroup of the player permutations;
        \item \textit{fully fair} if utility values are preserved under all player permutations;
        \item \textit{standard ordinally fair} if there is a transitive subgroup of player permutations that preserve preferences over pure strategy profiles;
        \item \textit{fully ordinally fair} if all player permutations preserve preferences over pure strategy profiles;
        \item \textit{standard cardinally fair} if there is a transitive subgroup of player permutations that preserve preferences over mixed strategy profiles; and
        \item \textit{fully cardinally fair} if all player permutations preserve preferences over mixed strategy profiles.
    \end{enumerate}
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Proposition 3.25

Source: `section-label-dependent-symmetric-games.tex:347`. Ambient assumptions: Common nonempty finite action set A, finite n>=2, real payoffs, left action (P_pi s)_j=s_{pi^{-1}(j)}; right-to-left composition.

Explicit assumptions/conclusion (source statement):

```latex
\label{prop:standsymgamesaremaxminandminmaxfair}
    If a (zero-sum) game $\Gamma = (N, A, u)$ is standard symmetric then it is maximin fair and minimax fair.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 4.1

Source: `section-bijections.tex:8`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{MPeg}
    Matching Pennies
    \begin{center}
        \begin{game}{2}{2}
                  \> $H$    \> $T$ \\
            $H$   \> $1,-1$  \> $-1,1$ \\
            $T$   \> $-1,1$  \> $1,-1$
        \end{game}
    \end{center}
    It is clear just by looking at the payoff matrix that Matching Pennies is fair, yet inside our label dependent framework the only invariant is the identity permutation, a problem that persists if we swap the strategy labels for either or both of the players.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 4.2

Source: `section-bijections.tex:21`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
A \textit{game bijection} from $\Gamma_1 = (N, A, u)$ to $\Gamma_2 = (M, B, v)$ consists of a bijection $\pi:N\rightarrow M$ and for each player $i \in N$, a bijection $\tau_i:A_i\rightarrow B_{\pi(i)}$, which we denote as $\bigl(\pi; (\tau_i)_{i \in N}\bigr)$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 4.3

Source: `section-bijections.tex:27`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{egisomgames}
        Consider the following $2$-player games.
        \begin{center}
            \begin{game}{2}{2}[$\Gamma_1$]
                        \> $c$  \> $d$ \\
                $a$   \> $1,2$  \> $3,4$ \\
                $b$   \> $5,6$  \> $7,8$
            \end{game}
            \hspace*{10mm}
            \begin{game}{2}{2}[$\Gamma_2$]
                        \> $h$ \> $i$ \\
                $e$   \> $4,3$ \> $8,7$ \\
                $f$   \> $2,1$ \> $6,5$ \\
            \end{game}
        \end{center}

        Given $(a, c) \in A$ and $g = \bigl((12) ; \bigl(\begin{smallmatrix} a & b \\ h & i \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ f & e \end{smallmatrix}\bigr)\bigr) \in \bij(\Gamma_1, \Gamma_2)$, $g(a,c) = (f,h)$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 4.4

Source: `section-bijections.tex:48`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
Consider Example \ref{stdsymeg} except with strategy labels $A_2 =\{c, d\}$ and $A_3 = \{e, f\}$ for players $2$ and $3$ respectively. We compose and invert bijections $g = \bigl((123) ; \bigl(\begin{smallmatrix} a & b \\ d & c \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ e & f \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ b & a \end{smallmatrix}\bigr)\bigr)$, $h = \bigl((12) ; \bigl(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ a & b \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ f & e \end{smallmatrix}\bigr)\bigr) \in S_{\Gamma}$ as follows:
        \begin{align*}

            h \circ g &= \bigl((12) ; \bigl(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ a & b \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ f & e \end{smallmatrix}\bigr)\bigr) \circ \bigl((123) ; \bigl(\begin{smallmatrix} a & b \\ d & c \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ e & f \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ b & a \end{smallmatrix}\bigr)\bigr) \\
                &= \bigl((12) \circ (123) ; \bigl(\begin{smallmatrix} c & d \\ a & b \end{smallmatrix}\bigr) \circ \bigl(\begin{smallmatrix} a & b \\ d & c \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ f & e \end{smallmatrix}\bigr) \circ \bigl(\begin{smallmatrix} c & d \\ e & f \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\bigr) \circ \bigl(\begin{smallmatrix} e & f \\ b & a \end{smallmatrix}\bigr)\bigr)\\
                &= \bigl((23) ; \bigl(\begin{smallmatrix} a & b \\ b & a \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ f & e \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ d & c \end{smallmatrix}\bigr)\bigr) \text{; and} \\
            g^{-1} &= \bigl((123) ; \bigl(\begin{smallmatrix} a & b \\ d & c \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ e & f \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ b & a \end{smallmatrix}\bigr)\bigr)^{-1} \\
                   &= \bigl((123)^{-1} ; \bigl(\begin{smallmatrix} e & f \\ b & a \end{smallmatrix}\bigr)^{-1}, \bigl(\begin{smallmatrix} a & b \\ d & c \end{smallmatrix}\bigr)^{-1}, \bigl(\begin{smallmatrix} c & d \\ e & f \end{smallmatrix}\bigr)^{-1}\bigr)\\
                   &= \bigl((132) ; \bigl(\begin{smallmatrix} a & b \\ f & e \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ b & a \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ c & d \end{smallmatrix}\bigr)\bigr).
        \end{align*}
```

Explicit dependencies: Example 3.16 Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 4.5

Source: `section-bijections.tex:61`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
$(h \circ g)(s) = h(g(s))$ for all $s \in A$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Corollary 4.6

Source: `section-bijections.tex:75`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
$u_{(h \circ g)(i)} \circ (h \circ g) = (u_{h(g(i))} \circ h) \circ g$ for all $i \in N$.
```

Explicit dependencies: Corollary 3.3 Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Theorem 4.7

Source: `section-bijections.tex:83`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{bijgroupoidthm}
        Game bijections form a groupoid.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 4.8

Source: `section-bijections.tex:106`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
A bijection $g \in \bij(\Gamma_1, \Gamma_2)$ is a \textit{game isomorphism} if $u_i = v_{g(i)}\circ g$ for all $i \in N$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Theorem 4.9

Source: `section-bijections.tex:112`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
Game isomorphisms form a groupoid.
```

Explicit dependencies: Theorem 4.7 Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Corollary 4.10

Source: `section-bijections.tex:122`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{isocorollary}
        If $\Gamma_1 \cong \Gamma_2 \cong \Gamma_3$ then $\isom(\Gamma_1, \Gamma_2) \cong \isom(\Gamma_2, \Gamma_3)$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 4.11

Source: `section-bijections.tex:135`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{cosetprop}
    Two bijections $g, h \in G$ have the same player permutation if and only if they are in the same coset of $G/G_N$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Corollary 4.12

Source: `section-bijections.tex:144`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{cosetcor}
    $G/G_N \cong \overrightarrow{G}$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 4.13

Source: `section-bijections.tex:155`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
A subgroup $G$ of $S_{\Gamma}$ is \textit{strategy trivial} \cite{NoahXE} if for each $i \in N$, $g(s_i) = s_i$ for all $g \in G_i$ and $s_i \in A_i$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: NoahXE.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 4.14

Source: `section-bijections.tex:159`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{NoahLemma} \cite{NoahXE}
    If $G$ is strategy trivial then for each $g, h \in G$ such that $g(i) = h(i)$, $g(s_i) = h(s_i)$ for all $s_i \in A_i$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: NoahXE.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Corollary 4.15

Source: `section-bijections.tex:166`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{cosetprop2}
    If $G$ is strategy trivial then $G_N = \{\id_{\Gamma}\}$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Corollary 4.16

Source: `section-bijections.tex:172`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{NoahCor}
    If $G \leq S_{\Gamma}$ is strategy trivial then for each $i \in N$ and $\tau \in \overrightarrow{G}$, there exists $g_{i\tau(i)} \in \bij(A_i, A_{\tau(i)})$ such that $G = \{(\pi; (g_{i\pi(i)})_{i \in N}): \pi \in \overrightarrow{G}\}$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 4.17

Source: `section-bijections.tex:178`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
A \textit{matching of $A_1, \ldots, A_n$} is a relation $M \subseteq \times_{i \in N} A_i$ which is $i$-total and $i$-unique for all $i \in N$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 4.18

Source: `section-bijections.tex:182`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{matchingeg}
Let $A_1 = \{a, b\}$, $A_2 = \{c, d\}$ and $A_3 = \{e, f\}$. One matching of $A_1 \times A_2 \times A_3$ is $M = \{(a,d,f), (b,c,e)\}$.
\begin{center}
\begin{tikzpicture}
    nodes={draw, ultra thick}
    \node (a) at (0,0) {$a$};   \node (c) at (1,0) {$c$};   \node (e) at (2,0) {$e$};
    \node (b) at (0,-0.5) {$b$};    \node (d) at (1,-0.5) {$d$};    \node (f) at (2,-0.5) {$f$};
    \draw (a) -- (d) -- (f);
    \draw (b) -- (c) -- (e);
\end{tikzpicture}
\end{center}
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 4.19

Source: `section-bijections.tex:199`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
$\{M_{ij}: i, j \in N\}$ is a groupoid.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 4.20

Source: `section-bijections.tex:210`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{matchinghomoprop}
    $M:S_N\rightarrow{S_{\Gamma}}$ is a homomorphism.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Corollary 4.21

Source: `section-bijections.tex:217`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
$M_{\pi^{-1}} = M_{\pi}^{-1}$ for all $\pi \in S_N$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 4.22

Source: `section-bijections.tex:221`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{matchingfixedpointlemma}
    For each $\pi \in S_N$, $M_{\pi}(s) = s$ for all $s \in M$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Theorem 4.23

Source: `section-bijections.tex:230`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{strattrivmatchingthm}
    Let $G \leq S_{\Gamma}$ be player transitive. There exists a matching $M$ such that $M_{\overrightarrow{G}} = G$ if and only if $G$ is strategy trivial.
```

Explicit dependencies: Lemma 4.20; Corollary 4.16 Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Corollary 4.24

Source: `section-bijections.tex:243`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
The following conditions are equivalent:
    \begin{enumerate}
        \item There exists weakly anonymous $\Gamma'$ such that $\Gamma \cong \Gamma'$;
        \item There exists player $n$-transitive and strategy trivial $G \leq \Gamma$ such that for each $i \in N$ and $g \in G_i$, $u_i = u_i \circ g$; and
        \item There exists a matching $M$ such that for each $i \in N$ and $\pi \in S_{N-\{i\}}$, $u_i = u_i \circ M_{\pi}$.
    \end{enumerate}
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 4.25

Source: `section-bijections.tex:254`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\begin{enumerate}
        \item If $m = n = 2$ then, letting $A_1 = \{a, b\}$ and $A_2 = \{c, d\}$,
        \begin{align*}
            M(2, 2) = \bigl\{\{(a, c), (b, d)\}, \{(a, d), (b, c)\}\bigr\}.
        \end{align*}
        \item If $m = 3$ and $n = 2$ then, letting $A_1 = \{a, b, c\}$ and $A_2 = \{d, e, f\}$, \
        \begin{align*}
            M(2, 3) = \bigl\{&\{(a, d), (b, e), (c, f)\}, \{(a, d), (b, f), (c, e)\}, \{(a, e), (b, d), (c, f)\}, \\
                        &\{(a, e), (b, f), (c, d)\}, \{(a, f), (b, d), (c, e)\}, \{(a, f), (b, e), (c, d)\}\bigr\}.
        \end{align*}
    \end{enumerate}
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 4.26

Source: `section-bijections.tex:270`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{matchinglemma1}
    For each $n \geq 2$: $M(n, 2)$ is a partition of $A$; and $|M(n, 2)| = 2^{n-1}$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Lemma 4.27

Source: `section-bijections.tex:277`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
\label{matchinglemma2}
    For each $n \geq 2$ and $m \geq 3$, $|M(n, m)| = m^{n-1}|M(n, m-1)|$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Theorem 4.28

Source: `section-bijections.tex:284`. Ambient assumptions: Finite n>=2; nonempty finite player strategy sets; typed bijections as in Definition 4.2. Subgroups and stabilizers refer to the explicitly named group; no equal labels assumed.

Explicit assumptions/conclusion (source statement):

```latex
For each $m, n \geq 2$, $|M(n, m)| = (m!)^{n-1}$.
```

Explicit dependencies: Lemma 4.26; Lemma 4.27 Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Corollary 5.1

Source: `section-label-independent-symmetric-games.tex:5`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
\label{indchar1}
    The following conditions are equivalent:
    \begin{enumerate}
        \item There exists standard symmetric $\Gamma'$ such that $\Gamma \cong \Gamma'$;
        \item $\Gamma$ has a player transitive and strategy trivial subgroup $G$; and
        \item There exists a matching $M$ and player transitive $T \leq S_N$ such that $M_{T} \leq \Aut(\Gamma)$.
    \end{enumerate}
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Corollary 5.2

Source: `section-label-independent-symmetric-games.tex:14`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
\label{indchar2}
    The following conditions are equivalent:
    \begin{enumerate}
        \item There exists fully symmetric $\Gamma'$ such that $\Gamma \cong \Gamma'$;
        \item $\Gamma$ has a player $n$-transitive and strategy trivial subgroup $G$; and
        \item There exists a matching $M$ such that $M_{S_N} \leq \Aut(\Gamma)$.
    \end{enumerate}
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Corollary 5.3

Source: `section-label-independent-symmetric-games.tex:25`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
If $\Gamma$ is standard symmetric then there exists a matching $M$ such that for each $s \in M$, $u_i(s) = u_j(s)$ for all $i, j \in N$.
```

Explicit dependencies: Lemma 4.22 Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 5.4

Source: `section-label-independent-symmetric-games.tex:34`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
A game is \textit{symmetric} \cite{NoahXE} if its automorphism group is player transitive and \textit{$n$-transitively symmetric} if its automorphism group is player $n$-transitive.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: NoahXE.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 5.5

Source: `section-label-independent-symmetric-games.tex:38`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
The automorphism group of Matching Pennies in Example \ref{MPeg} is \begin{align*}
        \Aut(\Gamma) = \langle &\bigl((12) ; \bigl(\begin{smallmatrix} H & T \\ H & T \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} H & T \\ T & H \end{smallmatrix}\bigr)\bigr)\rangle \\
        = \{ &\bigl(e ; \bigl(\begin{smallmatrix} H & T \\ H & T \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} H & T \\ H & T \end{smallmatrix}\bigr)\bigr),
        \bigl(e ; \bigl(\begin{smallmatrix} H & T \\ T & H \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} H & T \\ T & H \end{smallmatrix}\bigr)\bigr), \\
        &\bigl((12) ; \bigl(\begin{smallmatrix} H & T \\ H & T \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} H & T \\ T & H \end{smallmatrix}\bigr)\bigr),
        \bigl((12) ; \bigl(\begin{smallmatrix} H & T \\ T & H \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} H & T \\ H & T \end{smallmatrix}\bigr)\bigr) \}.
    \end{align*}
    Since $\Aut(\Gamma)$ is player transitive, is not strategy trivial and contains no proper transitive subgroups, Matching Pennies is an $n$-transitively non-standard symmetric game.
```

Explicit dependencies: Example 4.1 Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Proposition 5.6

Source: `section-label-independent-symmetric-games.tex:52`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
\label{subisoimpliesinter}
    If $\Gamma$ has a subgroup $G$ isomorphic to $S_N$ with $G_N = \{\id_{\Gamma}\}$ then it is $n$-transitively standard symmetric.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 5.7

Source: `section-label-independent-symmetric-games.tex:74`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
A \textit{division} of a $2$-dimensional shape in to $n \in \mathbb{Z}^+$ colours is a partition of the shape in to $n$ regions, each region coloured with a unique colour.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 5.8

Source: `section-label-independent-symmetric-games.tex:80`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
An \textit{automorphism} of a shape division in to $n$ colours is any combination of rotating and/or reflecting the divided/coloured shape that leads to the exact same shape with the same division.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 5.9

Source: `section-label-independent-symmetric-games.tex:92`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
We shall refer to the division of a $2$-dimensional shape in to $n \in \mathbb{Z}^+$ colours as:
    \begin{enumerate}
        \item \textit{fair} if each colour/region fills the same area;
        \item \textit{symmetric} if the automorphism group of the shape division is non-trivial; and
        \item \textit{strongly symmetric} if the shape division has an automorphism that is not the identity but does preserve the colours of permuted regions, ie. the associated colour permutation is the identity.
    \end{enumerate}
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Definition 5.10

Source: `section-label-independent-symmetric-games.tex:161`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
We shall refer to the division of a $2$-dimensional shape in to $n \in \mathbb{Z}^+$ colours as:
    \begin{enumerate}
        \item \textit{transitively symmetric} if every colour permutation in a transitive subgroup of all colour permutations is associated to at least one automorphism of the shape division; and
        \item \textit{$n$-transitively symmetric} if every colour permutation is associated to at least one automorphism of the shape division.
    \end{enumerate}
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Theorem 5.11

Source: `section-label-independent-symmetric-games.tex:182`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
If a two person zero-sum game $\Gamma$ is symmetric then it is fair (as mentioned earlier, this result is also in von Neumann and Morgenstern \cite[Pages 165-166]{VNM}).
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: VNM.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 5.12

Source: `section-label-independent-symmetric-games.tex:213`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
\label{constructeg}
    Let $G = \{\bigl((12) ; \bigl(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ a & b \end{smallmatrix}\bigr)\bigr)\}$. For $\Gamma(G)$ we require:
    \begin{align*}
        u_1(a, c) &= u_2(a, c) = \alpha   &   u_1(a, d) &= u_2(b, c) = \gamma \\
        u_1(b, c) &= u_2(a, d) = \beta   &   u_1(b, d) &= u_2(b, d) = \delta
    \end{align*}
    \begin{center}
    \begin{game}{2}{2}[$\Gamma(G)$]
              \> $c$  \> $d$ \\
        $a$   \> $\alpha, \alpha $  \> $\gamma, \beta $ \\
        $b$   \> $\beta, \gamma $  \> $\delta, \delta $
    \end{game}
    \end{center}

    We call $\alpha, \beta, \gamma, \delta \in \mathbb{R}$ the \textit{parameters} of $\Gamma(G)$. Note that distinct parameter choices may lead to strategically inequivalent games, even though both games will have the same automorphism group. All fully symmetric $2$-player $2$-strategy games are isomorphic to $\Gamma(G)$ for at least one choice of parameters, hence $\Gamma(G)$ is a general form for fully symmetric $2$-player $2$-strategy games, or equivalently standard symmetric $2$-player $2$-strategy games.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 5.13

Source: `section-label-independent-symmetric-games.tex:331`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
\label{egntransstandnonfull}
    An $n$-transitively non-fully standard symmetric $3$-player game.
    \begin{center}
    \begin{game}{2}{2}[$(a,,)$]
            \>  $e$      \>  $f$      \\
        $c$ \>  $\alpha,\alpha,\alpha$  \>  $\beta,\gamma,\delta$  \\
        $d$ \>  $\gamma,\delta,\beta$  \>  $\delta,\gamma,\beta$
    \end{game}
    \hspace*{5mm}
    \begin{game}{2}{2}[$(b,,)$]
            \>  $e$      \>  $f$      \\
        $c$ \>  $\delta,\beta,\gamma$  \>  $\beta,\delta,\gamma$  \\
        $d$ \>  $\gamma,\beta,\delta$  \>  $\alpha,\alpha,\alpha$
    \end{game}
    \end{center}

    \begin{align*}
        G = \{\bigl((123) ; \bigl(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ e & f \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ a & b \end{smallmatrix}\bigr)\bigr), \bigl((12) ; \bigl(\begin{smallmatrix} a & b \\ d & c \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ b & a \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ f & e \end{smallmatrix}\bigr)\bigr)\}
    \end{align*}

    Since $\langle{G}\rangle$ is $n$-transitive, and the first generator generates a player transitive and strategy trivial group with the matching $M  = \{(a,c,e), (b,d,f)\}$, $\Gamma(G)$ is $n$-transitively and standard symmetric. Furthermore since the bijections induced by $M$ from player transpositions are not automorphisms, $\Gamma(G)$ is non-fully symmetric.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 5.14

Source: `section-label-independent-symmetric-games.tex:468`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
\label{OTNSeg}
Two only-transitive non-standard symmetric $4$-player games.
\begin{center}
  \begin{game}{2}{2}[$(a,c,,)$]
       \>  $g$          \>  $h$          \\
    $e$  \>  $\alpha,\beta,\gamma,\delta$  \>  $\rho,\tau,\sigma,\omega$  \\
    $f$  \>  $\sigma,\omega,\rho,\tau$  \>  $\omega,\rho,\tau,\sigma$
  \end{game}
  \hspace*{5mm}
  \begin{game}{2}{2}[$(a,d,,)$]
       \>  $g$          \>  $h$          \\
    $e$  \>  $\delta,\alpha,\beta,\gamma$  \>  $\tau,\sigma,\omega,\rho$  \\
    $f$  \>  $\gamma,\delta,\alpha,\beta$  \>  $\beta,\gamma,\delta,\alpha$
  \end{game}
  \\
  \begin{game}{2}{2}[$(b,c,,)$]
       \>  $g$          \>  $h$          \\
    $e$  \>  $\beta,\gamma,\delta,\alpha$  \>  $\gamma,\delta,\alpha,\beta$  \\
    $f$  \>  $\tau,\sigma,\omega,\rho$  \>  $\delta,\alpha,\beta,\gamma$
  \end{game}
  \hspace*{5mm}
  \begin{game}{2}{2}[$(b,d,,)$]
       \>  $g$          \>  $h$          \\
    $e$  \>  $\omega,\rho,\tau,\sigma$  \>  $\sigma,\omega,\rho,\tau$  \\
    $f$  \>  $\rho,\tau,\sigma,\omega$  \>  $\alpha,\beta,\gamma,\delta$
  \end{game}
\end{center}

\[ G = \{ \bigl((1234) ; \bigl(\begin{smallmatrix} a & b \\ d & c \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ e & f \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ g & h \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} g & h \\ a & b \end{smallmatrix}\bigr)\bigr)\} \]

Since there does not exist any profile where the payoffs are equal and $\langle{G}\rangle$ is transitive, $\Gamma(G)$ is non-standard symmetric. Now for the strategy profile $(a,c,e,g)$ we have payoffs $(\alpha, \beta, \gamma, \delta)$. If $\Gamma(G)$ had an automorphism using $(23)$ then there would be a strategy profile $s \in A$ with payoffs $(\alpha, \gamma, \beta, \delta)$. Since no such profile exists $\Gamma(G)$ is only-transitive.

\begin{center}
  \begin{game}{2}{2}[$(a,c,,)$]
       \>  $g$          \>  $h$          \\
    $e$  \>  $\alpha,\alpha,\beta,\beta$  \>  $\gamma,\delta,\delta,\gamma$  \\
    $f$  \>  $\delta,\gamma,\gamma,\delta$  \>  $\beta,\beta,\alpha,\alpha$
  \end{game}
  \hspace*{5mm}
  \begin{game}{2}{2}[$(a,d,,)$]
       \>  $g$          \>  $h$          \\
    $e$  \>  $\gamma,\delta,\delta,\gamma$  \>  $\alpha,\alpha,\beta,\beta$  \\
    $f$  \>  $\beta,\beta,\alpha,\alpha$  \>  $\delta,\gamma,\gamma,\delta$
  \end{game}
  \\
  \begin{game}{2}{2}[$(b,c,,)$]
       \>  $g$          \>  $h$          \\
    $e$  \>  $\delta,\gamma,\gamma,\delta$  \>  $\beta,\beta,\alpha,\alpha$  \\
    $f$  \>  $\alpha,\alpha,\beta,\beta$  \>  $\gamma,\delta,\delta,\gamma$
  \end{game}
  \hspace*{5mm}
  \begin{game}{2}{2}[$(b,d,,)$]
       \>  $g$          \>  $h$          \\
    $e$  \>  $\beta,\beta,\alpha,\alpha$  \>  $\delta,\gamma,\gamma,\delta$  \\
    $f$  \>  $\gamma,\delta,\delta,\gamma$  \>  $\alpha,\alpha,\beta,\beta$
  \end{game}
\end{center}

\begin{align*}
G' = \{ \bigl((12) \circ (34) &; \bigl(\begin{smallmatrix} a & b \\ d & c \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ a & b \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ h & g \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} g & h \\ e & f \end{smallmatrix}\bigr)\bigr), \\
               \bigl((13) \circ (24) &; \bigl(\begin{smallmatrix} a & b \\ f & e \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ h & g \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ a & b \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} g & h \\ c & d \end{smallmatrix}\bigr)\bigr), \\
               \bigl((14) \circ (23) &; \bigl(\begin{smallmatrix} a & b \\ h & g \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ f & e \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ c & d \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} g & h \\ a & b \end{smallmatrix}\bigr)\bigr)\}
\end{align*}

That $\Gamma(G')$ is only-transitive non-standard symmetric follows by the same argument used for $\Gamma(G)$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 5.15

Source: `section-label-independent-symmetric-games.tex:535`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
An $n$-transitively non-standard symmetric $4$-player game.
\begin{center}
\begin{game}{2}{2}[$(a,c,,)$]
       \>  $g$          \>  $h$ \\
    $e$  \>  $\alpha,\beta,\beta,\beta$  \>  $\beta,\alpha,\beta,\beta$  \\
    $f$  \>  $\beta,\beta,\beta,\alpha$  \>  $\beta,\beta,\beta,\alpha$
\end{game}
\hspace*{5mm}
\begin{game}{2}{2}[$(a,d,,)$]
       \>  $g$          \>  $h$          \\
    $e$  \>  $\beta,\beta,\alpha,\beta$  \>  $\beta,\alpha,\beta,\beta$  \\
    $f$  \>  $\beta,\beta,\alpha,\beta$  \>  $\alpha,\beta,\beta,\beta$
\end{game}
\\
\begin{game}{2}{2}[$(b,c,,)$]
       \>  $g$          \>  $h$          \\
    $e$  \>  $\alpha,\beta,\beta,\beta$  \>  $\beta,\beta,\alpha,\beta$  \\
    $f$  \>  $\beta,\alpha,\beta,\beta$  \>  $\beta,\beta,\alpha,\beta$
\end{game}
\hspace*{5mm}
\begin{game}{2}{2}[$(b,d,,)$]
       \>  $g$          \>  $h$          \\
    $e$  \>  $\beta,\beta,\beta,\alpha$  \>  $\beta,\beta,\beta,\alpha$  \\
    $f$  \>  $\beta,\alpha,\beta,\beta$  \>  $\alpha,\beta,\beta,\beta$
\end{game}
\end{center}

\[G = \{ \bigl((1234) ; \bigl(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ e & f \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ h & g \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} g & h \\ a & b \end{smallmatrix}\bigr)\bigr),
               \bigl((12) ; \bigl(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ a & b \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ e & f \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} g & h \\ h & g \end{smallmatrix}\bigr)\bigr)\}\]

$\Gamma(G)$ is $n$-transitive since $\langle{G}\rangle$ is $n$-transitive, and non-standard symmetric since there does not exist any profile where all players receive the same payoff.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.

## Example 5.16

Source: `section-label-independent-symmetric-games.tex:569`. Ambient assumptions: Finite games and exact isomorphisms as in Section 4; later use of standard/fully symmetric is the label-independent characterization. Additional geometric definitions are analogies, not automatically game results.

Explicit assumptions/conclusion (source statement):

```latex
\label{sixplayereg}
An only-transitive non-standard symmetric $6$-player game that has a subgroup $\langle{G}\rangle$ isomorphic to $\overrightarrow{\langle{G}\rangle}$ with $\langle{G}\rangle_N = \{\id_{\Gamma}\}$.

\begin{center}


\begin{game}{2}{2}[$(a,c,e,g,,)$]
    \>$k$                 \>$l$  \\
    $i$\>$1,2,1,2,1,2$     \>$3,4,5,6,7,8$\\
    $j$\>$9,10,11,12,13,14$\>$15,16,17,18,19,20$
\end{game}
\hspace*{5mm}
\begin{game}{2}{2}[$(a,c,e,h,,)$]
    \>$k$                  \>$l$ \\
    $i$\>$5,6,7,8,3,4$      \>$20,15,19,17,18,16$\\
    $j$\>$21,22,23,24,25,26$\>$27,27,28,28,28,27$
\end{game}
\\
\begin{game}{2}{2}[$(a,c,f,g,,)$]
    \>$k$                  \>$l$ \\
    $i$\>$11,12,13,14,9,10$ \>$29,29,30,30,30,29$\\
    $j$\>$26,24,22,23,21,25$\>$4,8,6,7,5,3$
\end{game}
\hspace*{5mm}
\begin{game}{2}{2}[$(a,c,f,h,,)$]
    \>$k$                  \>$l$ \\
    $i$\>$17,18,19,20,15,16$\>$8,3,7,5,6,4$\\
    $j$\>$31,32,32,32,31,31$\>$16,20,18,19,17,15$
\end{game}
\\
\begin{game}{2}{2}[$(a,d,e,g,,)$]
    \>$k$                  \>$l$   \\
    $i$\>$7,8,3,4,5,6$      \>$18,16,20,15,19,17$\\
    j\>$30,29,29,29,30,30$\>$6,4,8,3,7,5$
\end{game}
\hspace*{5mm}
\begin{game}{2}{2}[$(a,d,e,h,,)$]
    \>$k$                  \>$l$  \\
    $i$\>$19,17,18,16,20,15$\>$32,31,32,31,32,31$\\
    $j$\>$13,11,12,10,14,9$ \>$22,26,24,25,23,21$
\end{game}
\\
\begin{game}{2}{2}[$(a,d,f,g,,)$]
    \>$k$                  \>$l$   \\
    $i$\>$23,24,25,26,21,22$\>$12,10,14,9,13,11$\\
    $j$\>$14,12,10,11,9,13$ \>$2,2,2,1,1,1$
\end{game}
\hspace*{5mm}
\begin{game}{2}{2}[$(a,d,f,h,,)$]
    \>$k$                  \>$l$  \\
    $i$\>$28,28,28,27,27,27$\>$24,25,23,21,22,26$\\
    $j$\>$25,23,24,22,26,21$\>$10,14,12,13,11,9$
\end{game}
\\
\begin{game}{2}{2}[$(b,c,e,g,,)$]
    \>$k$                  \>$l$  \\
    $i$\>$13,14,9,10,11,12$ \>$25,26,21,22,23,24$\\
    $j$\>$21,25,26,24,22,23$\>$31,31,31,32,32,32$
\end{game}
\hspace*{5mm}
\begin{game}{2}{2}[$(b,c,e,h,,)$]
    \>$k$                  \>$l$  \\
    $i$\>$30,30,30,29,29,29$\>$14,9,13,11,12,10$\\
    $j$\>$9,13,14,12,10,11$ \>$26,21,25,23,24,22$
\end{game}
\\
\begin{game}{2}{2}[$(b,c,f,g,,)$]
    \>$k$                  \>$l$  \\
    $i$\>$22,23,21,25,26,24$\>$10,11,9,13,14,12$\\
    $j$\>$27,28,27,28,27,28$\>$16,17,15,19,20,18$
\end{game}
\hspace*{5mm}
\begin{game}{2}{2}[$(b,c,f,h,,)$]
    \>$k$                  \>$l$  \\
    $i$\>$6,7,5,3,4,8$      \>$2,1,1,1,2,2$\\
    $j$\>$15,19,20,18,16,17$\>$4,5,3,7,8,6$
\end{game}
\\
\begin{game}{2}{2}[$(b,d,e,g,,)$]
    \>$k$                  \>$l$  \\
    $i$\>$19,20,15,16,17,18$\>$28,27,27,27,28,28$\\
    $j$\>$5,3,4,8,6,7$      \>$17,15,16,20,18,19$
\end{game}
\hspace*{5mm}
\begin{game}{2}{2}[$(b,d,e,h,,)$]
    \>$k$            \>$l$ \\
    $i$\>$7,5,6,4,8,3$\>$23,21,22,26,24,25$\\
    $j$\>$1,1,2,2,2,1$\>$11,9,10,14,12,13$
\end{game}
\\
\begin{game}{2}{2}[$(b,d,f,g,,)$]
    \>$k$                  \>$l$ \\
    $i$\>$32,32,31,31,31,32$\>$24,22,26,21,25,23$\\
    $j$\>$20,18,16,17,15,19$\>$8,6,4,5,3,7$
\end{game}
\hspace*{5mm}
\begin{game}{2}{2}[$(b,d,f,h,,)$]
    \>$k$                  \>$l$ \\
    $i$\>$18,19,17,15,16,20$\>$12,13,11,9,10,14$\\
    $j$\>$3,7,8,6,4,5$      \>$29,30,29,30,29,30$
\end{game}
\\
\vspace{-6mm}


\end{center}

\begin{align*}
G = \{ \bigl((14) \circ (25); &\bigl(\begin{smallmatrix} a & b \\ h & g \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ i & j \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ f & e \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} g & h \\ b & a \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} i & j \\ c & d \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} k & l \\ l & k \end{smallmatrix}\bigr)\bigr),\\
               \bigl((135) \circ (246); &\bigl(\begin{smallmatrix} a & b \\ e & f \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} c & d \\ g & h \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} e & f \\ i & j \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} g & h \\ k & l \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} i & j \\ a & b \end{smallmatrix}\bigr), \bigl(\begin{smallmatrix} k & l \\ c & d \end{smallmatrix}\bigr)\bigr)\}
\end{align*}

Since there does not exist any profile where the payoffs are equal and $\langle{G}\rangle$ is transitive, $\Gamma$ is non-standard symmetric. Now the payoffs for $(a,c,e,g,i,k)$ are $(1, 2, 1, 2, 1, 2)$. If there was an automorphism for $(12)$ then there would be $s \in A$ with payoffs $(2, 1, 1, 2, 1, 2)$. Since no such profile exists $\Gamma$ is only-transitive. It can be verified that $\langle{G}\rangle$ has order $12$, which is equal to the order of $\langle (14) \circ (25), (135) \circ (246)\rangle$, hence $\langle{G}\rangle \cong \langle (14) \circ (25), (135) \circ (246)\rangle$ and $\langle{G}\rangle_N = \{\id_{\Gamma}\}$.
```

Explicit dependencies: none cited inside this environment; ambient definitions still apply. Original citation keys: none.

Audit: see theorem-audit.md or definition-audit.md; extraction alone is not verification.
