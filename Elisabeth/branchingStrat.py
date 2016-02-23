import abstractSolver

class BranchingStrat(abstractSolver.AbstractSolver):
        def __init__(self):
                return None
		
        def solve(self, problem):
                sol = list()
                self.branchAndPruneRec(problem, dom(prob),sol)
                return sol
				
        def branchAndPruneRec(self, problem, domains, solutions):
                
###		E ’ := Prune (Prob , E )
                domains = self.prune(domains)
###		if E ’ is empty then
                if domains =={}:                       
###			fail
                        return {}
###		else if E ’ is a solution then
                elif self.estSolution(domains):
###			label E ’ as a solution
                        solutions.append(domains)
###		else
                else:
###			foreach E ’ ’ in Branch (E ’) do
                        for domainsBis in self.branch(domains):
###				BranchAndPruneRec (P ,E ’ ’)
                                self.branchAndPruneRec(problem,domainBis,solutions)
                        

        #prunage simple : si on a une affectation, on enleve la valeur du domaine de chaque variable
        def pruneSimple(self, domains):
                for clef in domains:
                        if len(domains[clef])==1:
                                val_to_del = domains[clef][0]
                                for variable in domains:
                                        if domains[variable].count(val_to_del) !=0 and variable!=clef:
                                                domains[variable].remove(val_to_del)
                return domains
        
        #prunage Diag : si on a une affectation, on enleve des autres variables les diagonales déja affectées
        def pruneDiag(self, domains):
                for clef in domains:
                        if len(domains[clef])==1:
                                val_to_del = domains[clef][0]
                                for variable in domains:
                                        if domains[variable].count(val_to_del) !=0 and variable!=clef:
                                                domains[variable].remove(val_to_del)
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

        #Stratégie : on choisit celui qui a le moins de "branches" et on branch !
        def branch(self,domains):
                ens_domains_res=[]
                clef_min = self.find_min(domains)
                branches = domains[clef_min]
                for elem in branches:
                        domains.update({clef_min:[elem]})
                        ens_domains_res.append(dict(domains))              
                return ens_domains_res

a={'a': [1,2,3], 'b': [1, 2],'c':[1]}
b=a
x = BranchingStrat()
ens=[];dico={'a':[5]}


for e in [1,2]:
        dico.update({'a':e})
        ens.append(dict(dico))

