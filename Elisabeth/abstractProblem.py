# -*-coding:utf-8 -*
from abc import ABCMeta


class AbstractProblem:
    __metaclass__ = ABCMeta

    def __init__(self):
        return NotImplemented

    def initialNode(self):
        return NotImplemented

    def testSat(self, node):
        return NotImplemented

    def printSolution(self, node):
        return NotImplemented
