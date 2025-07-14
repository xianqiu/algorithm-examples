import numpy as np


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


def partition_to_knapsack(a):
    """ Given a Partition instance, return a Knapsack instance.
    """
    w = a
    v = a
    C = sum(v) // 2
    return w, v, C


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


if __name__ == '__main__':
    a = [3, 1, 1, 2, 2, 1]  # True
    print(partition(a))
    a = [2, 10, 3, 8, 5, 7, 9, 5, 3, 2]  # True
    print(partition(a))
    a = [3, 4, 5]  # False
    print(partition(a))