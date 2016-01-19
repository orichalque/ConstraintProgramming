# -*-coding:utf-8 -*

class node:

	def __init__(self, domains = dict(), subNodes = []):	
		self.domains = domains
		self.childrens = childrens
		
	def branch(node):
		subNodes.append(node)
		
	def printTree(depth = 1):
		for 0 to depth:
			print "---"
		print ">"
		domains
		for i in subNodes:
			i.printTree(depth+1)
		
		
n = node({'a': [1,2,3], 'b': [1,2]})
n.branche(node({'a': [1], 'b': [1,2]}))
n.branche(node({'a': [2], 'b': [1,2]}))
n.branche(node({'a': [3], 'b': [1,2]}))
