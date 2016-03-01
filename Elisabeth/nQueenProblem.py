# -*-coding:utf-8 -*
from problem import Problem
from node import node

#Pre: Une reine par ligne
def printNode(n):
	arrayToPrint = []
	print("Affichage de la solution")
	for key, value in sorted(n.domains.items()):
		line = ''
		for i in range(1, len(n.domains) + 1):
			if i is value[0]:
				line = line + b'\xe2\x99\x9b'.decode('utf-8') + ' '
			else:
				line = line + b'\xe2\x96\xa1'.decode('utf-8') + ' '
		arrayToPrint.append(line)
	
	for i in arrayToPrint:
		print(i)

class NQueenProblem(Problem):
	#__metaclass__ = ABCMeta

	def __init__(self, n):	
 		self.sz = n;
 		self.initialNode()
	
	def initialNode(self):
		d = dict()
		l = list(range(1, self.sz+1))
		for x in range(1, self.sz+1):			
			d.update({str(x) : l})				
		self.node = node(d, [])
		return self.node
		
	def testSat(self, node):
		assigned = []
		clefs = sorted(node.domains)
		for clef in clefs:
			if len(node.domains[clef])==0:
				return False
			if len(node.domains[clef])==1:
				assigned.append(node.domains[clef][0])
			else:
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
	
	def printSolution(self):
		self.node = node({'1': [1], '2': [2], '3': [3] , '4': [4] , '5': [5]},[])
		arrayToPrint = []
		print("Affichage de la solution")
		for key, value in sorted(self.node.domains.items()):
			line = ''
			for i in range(1, self.sz + 1):
				if i is value[0]:
					line = line + b'\xe2\x99\x9b'.decode('utf-8') + ' '
				else:
					line = line + b'\xe2\x96\xa1'.decode('utf-8') + ' '
			arrayToPrint.append(line)
		
		for i in arrayToPrint:
			print(i)
	
	def printNode(self):
		self.node.printTree()	


p = node({'1': [1], '2': [2], '3': [3] , '4': [4] , '5': [5]},[])
printNode(p)

#print(n.testSat(node({'1': [3], '2': [1], '3': [4], '4': [2]},[])))


