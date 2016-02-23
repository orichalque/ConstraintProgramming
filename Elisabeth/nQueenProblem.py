# -*-coding:utf-8 -*
import problem,

class NQueenProblem(Problem):
	__metaclass__ = ABCMeta
	
	domain = []
	def __init__(self):	
		return NotImplemented
	
	def initialNode(self):
		return NotImplemented
	
	def testSat(self, node):
		assigned = []
		for clef in node.domains:
			if len(node.domains[clef])==0:
				return False
			if len(node.domains[clef])==1:
				assigned.append(node.domains[clef][0]
			else
				assigned.append(-1)
		for i in range(0,len(assigned)):
			if assigned[i] != -1:
				for j in range(i+1,len(assigned)):
					if assigned[j] != -1:
						#test colonne
						if assigned[i] == assigned[j]:
							return False
						#test diag
						if j-i == abs(assigned[j]-assigned[i]):
							return False
		return True
	
	def printSolution(self, node):
		return NotImplemented		




	
