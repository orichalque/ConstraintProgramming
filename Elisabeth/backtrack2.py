# -*- coding: utf-8 -*-
import abstractSolver
from nQueenProblem import NQueenProblem
from nQueenProblem import printNode
from node import Node

class BackTrack2(abstractSolver.AbstractSolver):
        def __init__(self):
                return None
			
        def solve(self, problem):
                sol = list()
                self.back(problem, problem.node.domains,sol)
                return sol
				
        def back(self, problem, domains, solutions):
                fini=True
                for clef in domains:
                        if len(domains[clef])>1:
                                fini = False
                if fini:
                        if problem.testSat(Node(domains)):
                                solutions.append(domains)
                else:
                        for domainsBis in self.branch(domains):
                                self.back(problem,dict(domainsBis),solutions)
                        
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
        def branch(self,domains):
                ens_domains_res=[]
                clef_min = self.find_min(domains)
                branches = domains[clef_min]
                #print ("branches",branches)
                for elem in branches:
                        #print ("elem : ", elem)
                        domains.update({clef_min:[elem]})
                        ens_domains_res.append(dict(domains))              
                return ens_domains_res

a={1: [1,2,3,4], 2: [1,2,3,4], 3:[2], 4:[1,2,3,4]}
b ={'5': [2, 3, 4], '1': [1], '3': [2, 4, 5], '4': [2, 3, 5], '2': [3]}
#b=a
x = BackTrack2()
z = NQueenProblem(7)
solutions = x.solve(z)
#solutions=x.branch(z.node.domains)
#solutions=x.pruneDiag(b)
for sol in solutions:
        printNode(Node(sol))
#print ("***b apres :",b)
