---
weight: 510
title: "Partition to Knapsack"
description: ""
icon: "article"
date: "2025-07-03T14:08:09+08:00"
lastmod: "2025-07-03T14:08:09+08:00"
draft: false
toc: true
katex: true
---

Reduction is a fundamental technique for relating different problems. It is commonly used to establish the computational complexity of optimization problems and to gain insights into their structure, which can aid in designing algorithms.

The core idea is to transform one problem into another so that a solution to the second problem can be applied to solve the first.

Let’s look at an example to illustrate this approach. 

## Partition

**Partition** is defined as follows: Given a set $S=\set{a_1, a_2, ..., a_n}$ of integers, assert whether $S$ can be partitioned into two subsets $S_1, S_2$ such that their sums are equal, i.e. 
$$\sum_{i\in S_1} a_i = \sum_{i\in S_2} a_i.$$

Note that $S_2 = S \backslash S_1$.

We are going to design an algorithm for Partition. A straightforward way is to solve the problem directly, for instance, by brute force. 

An alternative way is to use the reduction approach. The idea is to transform Partition into a new problem, whose algorithm is already known, then use this known algorithm to solve Partition.

Next, we show a reduction from Partition to Knapsack.

## Knpasack

**Knapsack** is defined as below: Given $n$ items of weights $w_i$ and values $v_i$, for $i=0, 1, ..., n-1$ and a knapsack with a maximum weight capacity $C$, pack some items into the knapsack such that the total weight does not exceed $C$ and maximize the total value of the packed items. Assume that the weights, the values and the capacity are all integers.

We know that [Knapsack](docs/dynamic-programming/knapsack/) can be solved by dynamic programming. The following Python implementation returns the optimal value for Knapsack.

```python
def knapsack_value(w, v, C):
    """
    :param w: list of weights
    :param v: list of values
    :param C: capacity
    :return: maximum value
    """
    n = len(w)
    f = [[0 for _ in range(C+1)] for _ in range(n)]
    for i in range(1, n):
        for s in range(1, C+1):
            if w[i-1] > s:
                f[i][s] = f[i-1][s]
            else:
                f[i][s] = max(f[i-1][s], f[i-1][s-w[i-1]] + v[i-1])
    return f[n-1][C]
```

## Reduction

Now we reduce Partition to Knapsack.

Note that Partition is given by $n$ integers $a_1, a_2, ..., a_n$. Assume w.l.o.g. that $\sum_{i=1}^n a_i$ is an even number, otherwise the answer is `No`. 

We construct a Knapsack instance as below:

* item weights $w_i = a_i$, for $i = 1, 2, ..., n$
* item values $v_i = a_i$, for $i = 1, 2, ..., n$
* knapsack capacity $C = \sum_{i=1}^n a_i / 2$

As item weights equal item values, the maximum value of Knapsack is at most the knapsack capacity $C$. Also note that $C$ is exactly half of the total sum, if the maximum value is strictly less than $C$, it implies the answer to Partition is `No`; Otherwise `Yes`. Thus, Partition can be solved by examing the maximum value of the Knapsack problem.

The following code implements the reduction from Partition to Knapsack. 

```python
def partition_to_knapsack(a):
    """ Given a Partition instance, return a Knapsack instance.
    """
    w = a
    v = a
    C = sum(v) // 2
    return w, v, C
```

Based on the above observation, we can solve Partition by any Knsapack algorithm.

```python
import numpy as np


def partition(a):
    """ Solve Partition by Knapsack algorithm.
    """
    w, v, C = partition_to_knapsack(a)
    if not np.isclose(2*C, sum(a)):
        # sum(a) is not even
        return False
    knapsack_opt = knapsack_value(w, v, C)
    if np.isclose(knapsack_opt, C):
        # C == knapsack_opt
        return True
    return False
```

Here are some test examples.

```python

if __name__ == '__main__':
    a = [3, 1, 1, 2, 2, 1]  # True
    print(partition(a))
    a = [2, 10, 3, 8, 5, 7, 9, 5, 3, 2]  # True
    print(partition(a))
    a = [3, 4, 5]  # False
    print(partition(a))
```
