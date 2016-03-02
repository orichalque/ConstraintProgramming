from abstractSolver import AbstractSolver
from node import Node
from nQueenProblem import NQueenProblem
from problem import Problem
from random import choice

class LocalSearchSolver(AbstractSolver):
    def __init__(self, maxRestart, maxMove):
        # store p last moves (avoid these moves)
        self.maxRestart = maxRestart
        self.maxMove = maxMove
        self.lastMoves = []

    # return 1 if a solution is found else 0
    def solve(self, problem):  # localSearch
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
        sol = self.generateRandom()
        move = 0
        while move < self.maxMove:
            if sol is None or self.problem.testSat(Node(sol)):
                break
            sol = self.doAmove(sol)
            move += 1
        return sol

    def isSolution(self, sol):
        return self.problem.testSat()

    def doAmove(self, sol):
        lastQueens = []
        minSol = None
        minCost = self.n
        grid = self.generateGrid(sol)
        for i in range(self.n):
            for j in range(i+1, self.n):
                #conflict, must generate new move
                [m] = sol[i]
                if sol[i] == sol[j] or sol[j] == [m+(j-i)] or sol[j] == [m-(j-i)]:
                    if i not in lastQueens:
                        lastQueens.append(i)
                        #for (move, cost) in self.generateMoves(sol, grid, i):
                        (move, cost) = self.generateMove(sol, grid, i)
                        if cost < minCost and move not in self.lastMoves:
                            minCost = cost
                            minSol = move
                    if j not in lastQueens:
                        lastQueens.append(j)
                        #for (move, cost) in self.generateMoves(sol, grid, j):
                        (move, cost) = self.generateMove(sol, grid, j)
                        if cost < minCost and move not in self.lastMoves:
                            minCost = cost
                            minSol = move
        if minSol is not None:
            #set maxLastMoves
            self.lastMoves.append(minSol)
        return minSol

    def generateMove(self, sol, grid, m):
        cost = 0
        move = {}
        for i in range(self.n):
            if i == m:
                cost = grid[i][m]
                move[i] = [grid[i].index(min(grid[i]))]
            else:
                move[i] = sol[i]
        return (move, cost)


    def generateGrid(self, sol):
        grid = [[0 for x in range(self.n)] for x in range(self.n)]
        for i in range(self.n):
            [m] = sol[i]
            for j in range(self.n):
                #vertical
                grid[j][m] += 1
                #top diagonal
                if m+abs(j-i) < self.n:
                    grid[j][m+abs(j-i)] += 1
                #bot diagonal
                if m-abs(j-i) >= 0:
                    grid[j][m-abs(j-i)] += 1
        return grid

    def find(self, l, e):
        ids = []
        i = 0
        for v in l:
            if v == e:
                ids.append(i)
            i += 1
        return ids

    def generateRandom(self):
        sol = {}
        grid = [[0 for x in range(self.n)] for x in range(self.n)]
        for i in range(self.n):
            m = choice(self.find(grid[i], min(grid[i])))
            sol[i] = [m]
            for j in range(i+1, self.n):
                #vertical
                grid[j][m] += 1
                #top diagonal
                if m+(j-i) < self.n:
                    grid[j][m+(j-i)] += 1
                #bot diagonal
                if m-(j-i) >= 0:
                    grid[j][m-(j-i)] += 1
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

for i in range(1, 100):
    solver = LocalSearchSolver(i, i*i)
    problem = NQueenProblem(i)
    solutions = solver.solve(problem)
    if not solutions:
        print(i, "no solution")
    #else:
    #    for solution in solutions:
    #        printNode(Node(solution))
    #        print()
