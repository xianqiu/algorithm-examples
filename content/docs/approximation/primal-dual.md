---
weight: 440
title: "Primal Dual"
description: ""
icon: "article"
date: "2025-07-03T14:30:04+08:00"
lastmod: "2025-07-03T14:30:04+08:00"
draft: true
toc: true
katex: true
---

In **linear programming**, the primal and dual problems are "equal" in the sense that they have the same optimal objective function value.

Take minimization problem as an example. The primal problem is defined as

{{<katex>}}
$$
\begin{aligned}
\min~ & c^T x \\
\text{s.t. } & Ax = b\\
& x \geq 0
\end{aligned}
$$
{{</katex>}}

The dual problem is defined as
{{<katex>}}
$$
\begin{aligned}
\max~ & b^T y \\
\text{s.t. } & A^T y \leq c
\end{aligned}
$$
{{</katex>}}

If $x^{\*}$ is the optimal solution of the primal problem, and $y^{\*}$ is the optimal solution of the dual problem, then it holds that $c^T x^{\*} = A y^{\*}$.