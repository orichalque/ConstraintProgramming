# -*- coding: utf-8 -*-
import abstractSolver
from node import Node
from nQueenProblem import NQueenProblem

class BackTrackingAlgorithm(abstractSolver.AbstractSolver):
        def __init__(self):
                return None
        

        def solve(self, problem):
                sol = list()
                self.backtrack(problem,problem.node,sol)
                return sol

        def backtrack(self,problem, node, solutions):
                fini=True
                for clef in node.domains:
                        if len(node.domains[clef])>1:
                                fini = False
                if fini:
                        if problem.testSat(node):
                                solutions.append(node)
                else:
                        self.branche(node)
                        for noeud in node.subNodes:
                                self.backtrack(problem, Node(noeud.domains),solutions)

        def find_min(self,dico):
                min_clef =sorted(dico)[0]
                for clef in sorted(dico):
                        #print("longueur :",len(dico[clef]))
                        if (len(dico[clef]) >1):
                              min_clef = clef
                              break
                #print([min_clef])
                min_domaine = dico[min_clef]
                min_taille_domaine = len(min_domaine)
                for clef in dico:
                        domaine = dico[clef]
                        taille_domaine = len(domaine)
                        #print ("clef : ", [clef], " -taille_domaine :", taille_domaine, " -domaine :", domaine)
                        if(taille_domaine<min_taille_domaine and taille_domaine!=1 and taille_domaine !=0):
                                #print ("clef : ", clef, " -taille_domaine :", taille_domaine, " -domaine :", domaine)
                                min_clef=clef
                                min_domaine = domaine
                                min_taille_domaine = taille_domaine
                return min_clef

        #Stratégie : on choisit celui qui a le moins de "branches" et on branch !
        def branche(self,node):
                domains=dict(node.domains)
                clef_min = self.find_min(domains)
                branches = domains[clef_min]
                for elem in branches:
                        domains.update({clef_min:[elem]})
                        node.branch(Node(dict(domains)))
                        #ens_domains_res.append(dict(domains))              

b=BackTrackingAlgorithm()
z = NQueenProblem(4)
a=Node({'4': [1, 2, 3, 4], '2': [1], '3': [1, 2, 3, 4], '1': [1]})
#sol=b.solve(z)
b.branche(a)
#print(sol)
for sn in a.subNodes:
        print (sn.domains)
        
