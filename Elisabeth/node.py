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
		print (">")
		self.domains
		for nod in self.subNodes:
			nod.printTree(depth+1)
		return 0
		

