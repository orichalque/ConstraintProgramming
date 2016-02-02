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
		

	def branch(self,domains)
		branches = domains[find_min(domains)]
		
		return branches

	def find_min(dico):
	  min_clef = sorted(dico)[0]
	  min_domaine = dico[min_clef]
	  min_taille_domaine = len(min_domaine)
		  for clef in dico:
			  domaine = dico[clef]
			  taille_domaine = len(domaine)
			  if(taille_domaine<min_taille_domaine):
				  min_clef=clef
				  min_domaine = domaine
				  min_taille_domaine = taille_domaine
	  return min_clef
