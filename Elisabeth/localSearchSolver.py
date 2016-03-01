from abstractSolver import AbstractSolver
from node import Node
from problem import Problem


class LocalSearchSolver(AbstractSolver):
    def __init__(self, n, maxRestart, maxMove):
        # store p last moves (avoid these moves)
        self.n = n
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
        sol = self.generateRandom(self.n)
        while iter and move < maxMove:
            if problem.testSat(Node(sol)):
                found = True
                iter = False
            else:
                (sol, iter) = self.doAmove(problem, sol)
            move = move + 1
        return found

    def isSolution(self, problem, sol):
        return problem.testSat()

    def doAmove(self, problem, sol):
        minCost = self.n
        minSol = {}
        iter = True
        grid = self.generateGrid(sol)
        for i in range(self.n):
            for j in range(i+1, self.n):
                #conflict, must generate new solution
                if sol[i] == sol[j] or sol[j] == [sol[i]+(j-i)] or sol[j] == [sol[i]-(j-i)]:
                    (move, cost) = self.generateMove(sol, grid, i)
                    if(cost < minCost):
                        minSol = move
                    (move, cost) = self.generateMove(sol, grid, j)
                    if(cost < minCost):
                        minSol = move
        return (minSol, iter)

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
