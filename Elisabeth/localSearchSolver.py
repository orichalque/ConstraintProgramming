from abstractSolver import AbstractSolver
from collections import deque
from copy import copy
from random import choice


class LocalSearchSolver(AbstractSolver):
    def __init__(self, maxRestart, maxMove, maxLastMoves=-1):
        self.maxRestart = maxRestart
        self.maxMove = maxMove
        self.maxLastMoves = maxLastMoves

    def solve(self, n):
        self.n = n
        self.solutions = []
        if self.maxLastMoves < 0:
            self.lastMoves = []
        else:
            self.lastMoves = deque([], self.maxLastMoves)
        self.localSearch()
        return self.solutions

    def localSearch(self):
        found = False
        restart = 0
        while not found and restart < self.maxRestart:
            found = self.localSearchRun()
            restart = restart + 1
        return found

    def localSearchRun(self):
        iter = True
        found = False
        move = 0
        sol = self.generateRandomStart()
        while iter and move < self.maxMove:
            if self.isSolution(sol):
                found = True
                iter = False
                self.solutions.append(sol)
            else:
                (sol, iter) = self.doAmove(sol)
            move += 1
        return found

    def isSolution(self, sol):
        for i in range(self.n):
            mi = sol[i]
            for j in range(i + 1, self.n):
                mj = sol[j]
                if (mi == mj) or (mj == (mi + (j - i))) or (mj == (mi - (j - i))):
                    return False
        return True

    def doAmove(self, sol):
        iter = False
        lastQueens = []
        minSol = None
        minCost = self.n
        grid = self.generateGrid(sol)
        for i in range(self.n):
            mi = sol[i]
            for j in range(i + 1, self.n):
                mj = sol[j]
                if (mi == mj) or (mj == (mi + (j - i))) or (mj == (mi - (j - i))):
                    for q in [i, j]:
                        if q not in lastQueens:
                            lastQueens.append(q)
                            for (move, cost) in self.generateRandomMove(sol, grid, q):
                                if cost < minCost and move not in self.lastMoves:
                                    minCost = cost
                                    minSol = move
                                    iter = True
        if iter:
            self.lastMoves.append(minSol)
        return (minSol, iter)

    def generateSimpleMove(self, sol, grid, q):
        m = grid[q].index(min(grid[q]))
        cost = grid[q][m]
        move = copy(sol)
        move[q] = m
        return [(move, cost)]

    def generateAllMove(self, sol, grid, q):
        moves = []
        for m in self.find(grid[q], min(grid[q])):
            cost = grid[q][m]
            move = copy(sol)
            move[q] = m
            moves.append((move, cost))
        return moves

    def generateRandomMove(self, sol, grid, q):
        m = choice(self.find(grid[q], min(grid[q])))
        cost = grid[q][m]
        move = copy(sol)
        move[q] = m
        return [(move, cost)]

    def generateGrid(self, sol):
        grid = [[0 for x in range(self.n)] for x in range(self.n)]
        for i in range(self.n):
            m = sol[i]
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
            sol[i] = m
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


def printSol(sol):
    for value in sol.values():
        print((b"\xe2\x96\xa1".decode("utf-8") + " ") * value + b"\xe2\x99\x9b".decode("utf-8") + (
            " " + b"\xe2\x96\xa1".decode("utf-8")) * (len(sol) - value - 1))
