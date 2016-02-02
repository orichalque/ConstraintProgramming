# -*-coding:utf-8 -*
from abc import ABCMeta
import problem

class AbstractSolver:
	__metaclass__ = ABCMeta
	
	def __init__(self):
		return NotImplemented
		
	def solve(self, problem):
		return NotImplemented

	
