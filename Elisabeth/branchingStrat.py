import abstractSolver

class BranchingStrat(abstractSolver.AbstractSolver):
	def __init__(self):
		self.__init__(self)
		return NotImplemented
		
	def solve(self, problem):
	domains = problem.node
		return branchAndPruneRec(problem, domains)
				
	def branchAndPruneRec(self, problem, domains)
		domainsBis = prune(problem, domains)
###		E ’ := Prune (P , E )
###		if E ’ is empty then
###			fail
###		else if E ’ is a solution then
###			label E ’ as a solution
###		else
###			foreach E ’ ’ in Branch (E ’) do
###				BranchAndPruneRec (P ,E ’ ’)

	def prune(self,problem, domains)
		return domains
		
	def branchMinDomain(domains)
		branches = []
		#recherche de cardinalitéMin dans domains
		for k,v in domains
			print l(v)
		return branches

