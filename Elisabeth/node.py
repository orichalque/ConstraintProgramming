# -*-coding:utf-8 -*

class node:

	def __init__(self, domains = dict(), subNodes = []):
		self.domains = domains
		self.subNodes = subNodes
		
	def branch(self, node):
		self.subNodes.append(node)
		return 0
		
	def printTree(self, depth = 1):
		for i in range(0, depth):
			print("---",end="")
		print(">",end="")
		print(self.domains)
		for nod in self.subNodes:
			nod.printTree(depth+1)
		return 0

n1 = node({'1': [1,2,3], '2': [1,2]},[])
n2 = node({'1': [1], '2': [1,2]},[])
n1.branch(n2)
n1.branch(node({'1': [2], '2': [1,2]},[]))
n1.branch(node({'1': [3], '2': [1,2]},[]))
n2.branch(node({'1': [1], '2': [1]},[]))
n2.branch(node({'1': [1], '2': [2]},[]))
n1.printTree()
