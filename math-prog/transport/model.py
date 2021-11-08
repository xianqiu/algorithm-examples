from ortools.linear_solver import pywraplp
import numpy as np


class TransportModel(object):

    def __init__(self, a, d, C):
        """
        :param a: 供给量(m维向量), m代表仓库数量
        :param d: 需求量(n维向量), n代表客户数量
        :param C: 单位运输成本(m*n维矩阵), C[i][j]代表仓库i到客户j的单位运输成本
        """
        self._solver = pywraplp.Solver('TransportModel',
                                       pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
        self._a = a
        self._d = d
        self._C = C
        self._m = len(self._a)  # 仓库数量
        self._n = len(self._d)  # 客户数量
        self._x = None  # 决策变量
        self._obj = None  # 优化目标（对象）
        self._solution_x = None  # 计算结果
        self._obj_val = None  # 目标函数值

    def _init_decision_variables(self):
        self._x = [
            # 0 <= x[i][j] <= infinity
            [self._solver.NumVar(0, self._solver.infinity(), "x[%d][%d]" % (i, j))
             for j in range(self._n)] for i in range(self._m)
        ]

    def _init_constraints(self):
        # 每个仓库的出库量不能超过其供给量
        # sum(x[i][j]) <= a[i], over j
        for i in range(self._m):
            ct = self._solver.Constraint(0, self._a[i])
            for j in range(self._n):
                ct.SetCoefficient(self._x[i][j], 1)
        # 每个客户的需求应该被满足
        # sum(x[i][j]) == b[j], over i
        for j in range(self._n):
            ct = self._solver.Constraint(self._d[j], self._d[j])
            for i in range(self._m):
                ct.SetCoefficient(self._x[i][j], 1)

    def _init_objective(self):
        self._obj = self._solver.Objective()
        for i in range(self._m):
            for j in range(self._n):
                self._obj.SetCoefficient(self._x[i][j], self._C[i][j])
        self._obj.SetMinimization()

    def solve(self):
        self._init_decision_variables()
        self._init_constraints()
        self._init_objective()
        self._solver.Solve()
        # 求解器返回的解
        self._solution_x = [[
            self._x[i][j].solution_value()
            for j in range(self._n)]
            for i in range(self._m)]
        # sum(C[i][i] * x[i][j]) over i,j
        self._obj_val = self._obj.Value()

    def print_result(self):
        print("最优值 = ", self._obj_val)
        print("最优解 x = ")
        print(np.array(self._solution_x))
