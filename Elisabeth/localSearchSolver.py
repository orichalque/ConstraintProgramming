from abstractSolver import AbstractSolver
from node import Node
from nQueenProblem import NQueenProblem
from problem import Problem


class LocalSearchSolver(AbstractSolver):
    def __init__(self, maxRestart, maxMove):
        # store p last moves (avoid these moves)
        self.maxRestart = maxRestart
        self.maxMove = maxMove
        self.lastMoves = []

    # return 1 if a solution is found else 0
    def solve(self, problem):  # localSearch
        self.n = len(problem.initialNode().domains)
        solutions = []
        sol = self.localSearch(problem, self.maxRestart, self.maxMove)
        if sol is not None:
            solutions.append(sol)
        return solutions

    def localSearch(self, problem, maxRestart, maxMove):
        sol = None
        restart = 0
        while restart < maxRestart:
            if sol is not None:
                break
            sol = self.localSearchRun(problem, maxMove)
            restart = restart + 1
        return sol

    def localSearchRun(self, problem, maxMove):
        sol = self.generateRandom()
        move = 0
        while move < maxMove:
            if sol is None or problem.testSat(Node(sol)):
                break
            sol = self.doAmove(problem, sol)
            move += 1
        return sol

    def isSolution(self, problem, sol):
        return problem.testSat()

    def doAmove(self, problem, sol):
        minSol = None
        minCost = self.n
        grid = self.generateGrid(sol)
        for i in range(self.n):
            for j in range(i+1, self.n):
                #conflict, must generate new move
                [m] = sol[i]
                if sol[i] == sol[j] or sol[j] == [m+(j-i)] or sol[j] == [m-(j-i)]:
                    (move, cost) = self.generateMove(sol, grid, i)
                    if cost < minCost and move not in self.lastMoves:
                        minSol = move
                    (move, cost) = self.generateMove(sol, grid, j)
                    if cost < minCost and move not in self.lastMoves:
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

    def generateRandom(self):
        domains = {}
        grid = [[0 for x in range(self.n)] for x in range(self.n)]
        for i in range(self.n):
            #randomize?
            m = grid[i].index(min(grid[i]))
            domains[i] = [m]
            for j in range(i+1, self.n):
                #vertical
                grid[j][m] += 1
                #top diagonal
                if m+(j-i) < self.n:
                    grid[j][m+(j-i)] += 1
                #bot diagonal
                if m-(j-i) >= 0:
                    grid[j][m-(j-i)] += 1
        return domains

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
    solver = LocalSearchSolver(1, i*i)
    problem = NQueenProblem(i)
    solutions = solver.solve(problem)
    for solution in solutions:
        printNode(Node(solution))
        print()
