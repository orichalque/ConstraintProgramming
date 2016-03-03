# coding=utf-8

class Node:
    def __init__(self, domains=dict(), subNodes=[]):
        self.domains = domains
        self.subNodes = subNodes

    def branch(self, node):
        self.subNodes.append(node)

    def printTree(self, depth=1):
        for i in range(0, depth):
            print("---", end="")
            print(">", end="")
            print(self.domains)
            for nod in self.subNodes:
                nod.printTree(depth + 1)
