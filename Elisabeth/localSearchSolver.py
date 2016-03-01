from abstractSolver import AbstractSolver
from node import node
from problem import Problem


class LocalSearchSolver(AbstractSolver):
    def __init__(self, maxRestart, maxMove):
        # store p last moves (avoid these moves)
        self.maxRestart = maxRestart
        self.maxMove = maxMove

    # return 1 if a solution is found else 0
    def solve(self, problem):  # localSearch
        if self.localSearch(problem, self.maxRestart, self.maxMove):
            return 1
        else:
            return 0

    def localSearch(self, problem, maxRestart, maxMove):
        found = False
        restart = 0
        while not found and restart < maxRestart:
            found = self.localSearchRun(problem, maxMove)
            restart = restart + 1

    def localSearchRun(self, problem, maxMove):
        iter = True
        found = False
        move = 0
        sol = self.generateRandom(len(problem.initialNode().domains))
        while iter and move < maxMove:
            if problem.testSat(node(sol)):
                found = True
                iter = False
            else:
                self.doAmove(problem, sol)
            move = move + 1
        return found

    def isSolution(self, problem, sol):
        return problem.testSat()

    def doAmove(self, problem, solution):
        return 0

    def generateRandom(self, n):
        domains = {}
        grid = [[0 for x in range(n)] for x in range(n)]
        for i in range(n):
            #randomize?
            m = grid[i].index(min(grid[i]))
            domains[i] = [m]
            for j in range(i+1, n):
                #row
                grid[j][m] += 1
                #top diagonal
                if m+(j-i) < n:
                    grid[j][m+(j-i)] += 1
                #bot diagonal
                if m-(j-i) >= 0:
                    grid[j][m-(j-i)] += 1
        return domains
