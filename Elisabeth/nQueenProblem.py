# -*-coding:utf-8 -*
#import problem
from node import node

class NQueenProblem():
	#__metaclass__ = ABCMeta

	def __init__(self, n):	
 		self.sz = n;
 		self.initialNode()
	
	def initialNode(self):
		d = dict()
		for x in range(1, self.sz+1):
			l = list(range(1, self.sz+1))
			d.update({str(x) : l})				
		self.node = node(d, [])
		
	def testSat(self, node):
		return NotImplemented		
	
	def printSolution(self, node):
		return NotImplemented	
		
	def printNode(self):
		self.node.printTree()	


n = NQueenProblem(5)
n.printNode()
