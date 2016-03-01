import abstractSolver
from nQueenProblem import NQueenProblem
from nQueenProblem import printNode
from node import Node

class BranchingStrat(abstractSolver.AbstractSolver):
        def __init__(self):
                return None
			
        def solve(self, problem):
                sol = list()
                self.branchAndPruneRec(problem, problem.node.domains,sol)
                return sol
				
        def branchAndPruneRec(self, problem, domains, solutions):
                dom= self.pruneDiag(domains)
                for clef in dom:
                        if len(dom[clef])==0:
                                return []

                if self.estSolution(dom):
                        solutions.append(dom)
                else:
                        #print ("_____domains",domains)
                        for domainsBis in self.branch(dom):
                                #print("___domainsbis________", domainsBis)
                                self.branchAndPruneRec(problem,dict(domainsBis),solutions)
                        

        #prunage simple : si on a une affectation, on enleve la valeur du domaine de chaque variable
        
        def estSolution(self, domains):
                for clef in domains:
                        if len(domains[clef])!=1:
                                return False
                return True
			
        def pruneSimple(self, domains):
                for clef in domains:
                        if len(domains[clef])==1:
                                val_to_del = domains[clef][0]
                                for variable in domains:
                                        if domains[variable].count(val_to_del) !=0 and variable!=clef:
                                                domains[variable].remove(val_to_del)
                return domains
        
        #prunage Diag : si on a une affectation, on enleve des autres variables les diagonales déja affectées et la valeur
        # prunage simple + prunage en diagonale.
        def pruneDiag(self, domainsGlob):
                domains=dict(domainsGlob)
                clefs = sorted(domains)
                for clef_i in domains:
                        domains[clef_i] = list(domainsGlob[clef_i])
                for clef_i in clefs:
                        if len(domains[clef_i])==1:
                                val_to_del = domains[clef_i][0]
                                for clef_j in clefs:
                                        if clef_j!=clef_i:
                                                #colonne
                                                if domains[clef_j].count(val_to_del) !=0:
                                                        domains[clef_j].remove(val_to_del)
                                                offset = int(float(clef_i)) - int(float(clef_j))
                                                #diagonale
                                                if domains[clef_j].count(val_to_del - offset) !=0:
                                                        domains[clef_j].remove(val_to_del - offset)
                                                #Anti-diagonale
                                                if domains[clef_j].count(val_to_del + offset) !=0:
                                                        domains[clef_j].remove(val_to_del + offset)
                return domains
                
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
x = BranchingStrat()
z = NQueenProblem(5)
solutions = x.solve(z)
#solutions=x.branch(z.node.domains)
#solutions=x.pruneDiag(b)
for sol in solutions:
        printNode(Node(sol))
#print ("***b apres :",b)
