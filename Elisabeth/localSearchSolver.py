import abstractSolver, problem, node

class LocalSearchSolver(AbstractSolver):
	def __init__(self, maxRestart, maxMove):
		#store p last moves (avoid these moves)
		self.maxRestart = maxRestart
		self.maxMove = maxMove

	#return 1 if a solution is found else 0
	def solve(self, problem): #localSearch
		#generate random assignment
		#while until a candidate assignment has cost 0
		self.problem = problem
		self.lastMoves = list()
		restart = 0
		while restart < self.maxRestart:
			if localSearchRun():
				return 1
			restart += 1
		return 0

	def localSearchRun(self):
		move = 0
		while move < self.maxMove:
			if self.problem.testSat(node):
				return True
			else:
				pass
			move += 1
		return False

	def cost(self, node):
		return 0

	def generateCandidate(self, node):
		pass
