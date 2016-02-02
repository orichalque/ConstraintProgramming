import abstractSolver

class BranchingStrat(abstractSolver.AbstractSolver):
        def __init__(self):
                return None
		
        def solve(self, problem):
                domains = problem.node
                return branchAndPruneRec(problem, domains)
				
        def branchAndPruneRec(self, problem, domains, solutions):
                
###		E ’ := Prune (P , E )
                domainsBis = self.prune(problem, domains)
###		if E ’ is empty then
                if domains =={}:                       
###			fail
                        return {}
###		else if E ’ is a solution then
                elif estSolution(domains):
###			label E ’ as a solution
                        solutions.append(domains)
###		else
                else:
###			foreach E ’ ’ in Branch (E ’) do
                        for domainsBis in self.branch(domains):
###				BranchAndPruneRec (P ,E ’ ’)
                                self.branchAndPruneRec(problem,domainBis,solutions)
                        

        def prune(self,problem, domains):
                return domains
		
        def find_min(self,dico):
                min_clef = sorted(dico)[0]
                min_domaine = dico[min_clef]
                min_taille_domaine = len(min_domaine)
                for clef in dico:
                        domaine = dico[clef]
                        taille_domaine = len(domaine)
                        if(taille_domaine<min_taille_domaine):
                                min_clef=clef
                                min_domaine = domaine
                                min_taille_domaine = taille_domaine
                return min_clef
        
        def branch(self,domains):
                ens_domains_res=[]
                clef_min = self.find_min(domains)
                branches = domains[clef_min]
                for elem in branches:
                        domains.update({clef_min:[elem]})
                        ens_domains_res.append(dict(domains))              
                return ens_domains_res

a={'a': [1,2,3], 'b': [1, 2]}
b=a
x = BranchingStrat()
ens=[];dico={'a':[5]}


for e in [1,2]:
        dico.update({'a':e})
        ens.append(dict(dico))

