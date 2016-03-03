from abstractSolver import AbstractSolver
from collections import deque
from copy import copy
from node import Node
from nQueenProblem import NQueenProblem
from problem import Problem
from random import choice


class LocalSearchSolver(AbstractSolver):
    def __init__(self, maxRestart, maxMove, maxLastMoves=-1):
        self.maxRestart = maxRestart
        self.maxMove = maxMove
        if maxLastMoves < 0:
            self.lastMoves = []
        else:
            self.lastMoves = deque([], maxLastMoves)

    def solve(self, problem):
        self.problem = problem
        self.n = len(problem.initialNode().domains)
        solutions = []
        sol = self.localSearch()
        if sol is not None:
            solutions.append(sol)
        return solutions

    def localSearch(self):
        sol = None
        restart = 0
        while restart < self.maxRestart:
            if sol is not None:
                break
            sol = self.localSearchRun()
            restart = restart + 1
        return sol

    def localSearchRun(self):
        sol = self.generateRandomStart()
        move = 0
        while move < self.maxMove:
            if sol is None or self.isSolution(sol):
                break
            sol = self.doAmove(sol)
            move += 1
        return sol

    def isSolution(self, sol):
        #return self.problem.testSat(Node(sol))
        for i in range(self.n):
            [mi] = sol[i]
            for j in range(i + 1, self.n):
                [mj] = sol[j]
                if (mi == mj) or (mj == (mi + (j - i))) or (mj == (mi - (j - i))):
                    return False
        return True

    def doAmove(self, sol):
        lastQueens = []
        minSol = None
        minCost = self.n
        grid = self.generateGrid(sol)
        for i in range(self.n):
            for j in range(i + 1, self.n):
                [m] = sol[i]
                if sol[i] == sol[j] or sol[j] == [m + (j - i)] or sol[j] == [m - (j - i)]:
                    for q in [i, j]:
                        if q not in lastQueens:
                            lastQueens.append(q)
                            for (move, cost) in self.generateRandomMove(sol, grid, q):
                                if cost < minCost and move not in self.lastMoves:
                                    minCost = cost
                                    minSol = move
        if minSol is not None:
            self.lastMoves.append(minSol)
        return minSol

    def generateMove(self, sol, grid, q):
        m = grid[q].index(min(grid[q]))
        cost = grid[q][m]
        move = copy(sol)
        move[q] = [m]
        return [(move, cost)]

    def generateAllMove(self, sol, grid, q):
        moves = []
        for m in self.find(grid[q], min(grid[q])):
            cost = grid[q][m]
            move = copy(sol)
            move[q] = [m]
            moves.append((move, cost))
        return moves

    def generateRandomMove(self, sol, grid, q):
        m = choice(self.find(grid[q], min(grid[q])))
        cost = grid[q][m]
        move = copy(sol)
        move[q] = [m]
        return [(move, cost)]

    def generateGrid(self, sol):
        grid = [[0 for x in range(self.n)] for x in range(self.n)]
        for i in range(self.n):
            [m] = sol[i]
            for j in range(self.n):
                # vertical
                grid[j][m] += 1
                # top diagonal
                if m + abs(j - i) < self.n:
                    grid[j][m + abs(j - i)] += 1
                # bot diagonal
                if m - abs(j - i) >= 0:
                    grid[j][m - abs(j - i)] += 1
        return grid

    def find(self, l, e):
        indexes = []
        for (i, x) in enumerate(l):
            if x == e:
                indexes.append(i)
        return indexes

    def generateRandomStart(self):
        sol = {}
        grid = [[0 for x in range(self.n)] for x in range(self.n)]
        for i in range(self.n):
            m = choice(self.find(grid[i], min(grid[i])))
            sol[i] = [m]
            for j in range(i + 1, self.n):
                # vertical
                grid[j][m] += 1
                # top diagonal
                if m + (j - i) < self.n:
                    grid[j][m + (j - i)] += 1
                # bot diagonal
                if m - (j - i) >= 0:
                    grid[j][m - (j - i)] += 1
        return sol


def printNode(n):
    arrayToPrint = []
    for key, value in sorted(n.domains.items()):
        line = ''
        for i in range(len(n.domains)):
            if i is value[0]:
                line = line + b'\xe2\x99\x9b'.decode('utf-8') + ' '
            else:
                line = line + b'\xe2\x96\xa1'.decode('utf-8') + ' '
        arrayToPrint.append(line)
    for i in arrayToPrint:
        print(i)

for i in range(10):
    print("Solving {}-queens problem:".format(i))
    solver = LocalSearchSolver(i, i*i)
    problem = NQueenProblem(i)
    solutions = solver.solve(problem)
    if solutions:
        print("success")
    else:
        print("failure")
