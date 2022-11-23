Basic Existence and Uniqueness Theorems for ODEs
------------------------------------------------

In this document, we will attempt to prove some of the classic existence and uniqueness theorems for first-order ODEs. We will begin with existence.

------------------

This first theorem is called Cauchy-Peano:

**Theorem.** Given some $f : [t_0, t_1] \times \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$ which is continuous and bounded by $M$, we are given the IVP $x'(t) = f(t, x(t))$ for all $t \in [t_0, t_1]$, and 
$x(t_0) = x0$. Then, this IVP has at least one solution.

*Proof.* To prove this theorem, we will attempt to use Scauder-Tychonoff fixed point theorem. The map we will use is defined as:

$$T(y) = x_0 + \displaystyle\int_{t_0}^{t} f(t, x(t)) \ dt$$

We will show that this map has a fixed point, which will cleary be a solution to the IVP. To do this, we need to show that $T$ is continuous and maps to a family of equicontinuous functions.

More formally, note that:

$$|T(y)| \leq |x_0| + M |t_1 - t_0|$$

In the case that this quantity, which is independent of $y$, is less than $1$, then we have $T$ mapping into $B$, so we truly can consider $T : B \rightarrow B$ for all $y \in T$. To show that 
$T(B)$ is equicontinuous, consider $Ty(t)$ and $Ty(t')$:

$$|Ty(t) - Ty(t')| \leq \displaystyle\int_{t}^{t'} f(t, y(t)) \leq M|t - t'|$$

which implies that the functions $Ty$ are Lipschitz, and each has the same Lipschitz constant $M$, so $T(B)$ is equicontinuous (this is like uniform convergence, but using the same $\delta$ for a whole family of functions).

To prove continuity, we need to be a bit more creative. Recall that we are working in the uniform metric on our space of functions. Hence, we can use the sequence definition of continuity. Suppose $x_k \to x$. Then:

$$|Tx(t) - Tx_k(t)| \leq \displaystyle\int_{t_0}^{t} |f(s, x(s)) - f(s, x_k(s))| \leq \sup_{s} |f(s, x(s)) - f(s, x_k(s))| (t_1 - t_0) \ ds$$

Our claim is that we can choose $N$ such that with $k \geq N$, the right-hand side is less than $\epsilon$. Indeed, $f$ is uniformly continuous, as 
its domain is compact, so we choose $\delta$ such that $|(s, x(s)) - (s, x_k(s))| = |x(s) - x_k(s)| < \delta$ implies that the difference of function is less than $\epsilon$, 
and $k$ such that $|x(s) - x_k(s**| < \delta$ for all $s$, and we are done.

Thus, we satisfy Schauder-Tychonoff, so the IVP has a solution.

------------------------------

We can also prove an existence and uniqueness theorem using Banach's fixed point theorem, which essentially dictates that in a complete metric space, a contraction will have a unique 
fixed point.

**Theorem.** Given some $f : D \subset \mathbb{R} \times \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$ (where $D$ is open) that is continuous in $x$ and Lipschitz in $y$ with constant $K$, then there exists some $a > 0$ such that the IVP 
corresponding to $y'(x) = f(x, y(x))$ and $y(0) = x_0$ has a unique solution on $(x_0 - a, x_0 + a)$.

The main idea is to show that the map $\Gamma$ which acts as:

$$\Gamma(y) = x_0 + \displaystyle\int_{x_0}^{x} f(s, y(s)) \ ds$$

is a contraction. Indeed, note that:

$$|\Gamma(y) - \Gamma(z)| \leq \displaystyle\int_{x_0}^{x} |f(s, y(s)) - f(s, z(s))| \ ds \leq \displaystyle\int_{x_0}^{x} K |y(s) - z(s)| \ ds \leq K A \sup_{s} |y(s) - z(s**|$$ 


---------------------------------

Funnily enough, one of the concepts introduced in MAT267 that I don't find completely and utterly boring is the notion of the limit set of an ODE.

**Definition.**: The $\omega$-limit set of a solution $x$ to an ODE of the form $x' = f(x)$ is precisely the set of all points that the solution continues to come arbitrarily close to passing through for arbitrarily 
large times. More specifically:

$$\omega(x) = \{y \in D \ | \ \text{there exists some sequence} \ t_j \ \text{such that} \ \lim_{j \to \infty} x(t_j) = y\}$$

There is an analogous definition of an $\alpha$-limit set for arbitrarily small (negative) times.

This limit set has some nice properties. For one, it is closed and connected.

Let us begin by proving that it is closed. We do this by showing that it is equal to its closure. In other words, suppose there exists a sequence of points $x_k$ in $\omega(x)$ which converge to $y$. Then, 
for each of these points, we construct a sequence $t_{\ell k}$ such that $\lim_{\ell \to \infty} x(t_{\ell k}) = x_k$. We then define a new sequence of times $t'_{k} = t_{kk}$. This is a sort-of diagonal argument, 
which will yield a sequence of times which goes to $y$.

Indeed, given some $\epsilon > 0$. Choose $N_1$ such that $k \geq N_1$ implies $|x_k - y| < \epsilon/2$, as well as 

