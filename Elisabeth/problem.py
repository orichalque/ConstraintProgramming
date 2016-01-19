# -*-coding:utf-8 -*
from abc import ABCMeta

class Problem:
	__metaclass__ = ABCMeta
	
	domain = []
	def __init__(self):	
		return NotImplemented
	
	def initialNode(self):
		return NotImplemented
	
	def testSat(self, node):
		return NotImplemented		
	
	def printSolution(self, node):
		return NotImplemented		

p = Problem ()



	
