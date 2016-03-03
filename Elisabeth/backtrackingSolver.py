# coding=utf-8
from abstractSolver import AbstractSolver
from node import Node


class BacktrackingSolver(AbstractSolver):
    def __init__(self):
        pass

        # fonction principale, resoud le probleme entierement
        def solve(self, problem):
            sol = list()
            self.back(problem, problem.node.domains, sol)
            return sol

        # fonction recursive, ajout des solutions petit a petit dans la liste "solution"
        def back(self, problem, domains, solutions):
            # on verifie que l'algorithme n'est pas terminé (il reste des variables à affecter)
            fini = True
            for clef in domains:
                if len(domains[clef]) > 1:
                    fini = False

            if fini:
                if problem.testSat(
                        Node(domains)):  # teste si le probleme verifie encore les contraintes (cast en noeud)
                    solutions.append(domains)
            else:
                # algo pas terminé, on "branch" et on relance l'algo sur chaque branche
                for domainsBis in self.branch(domains):
                    self.back(problem, dict(domainsBis),
                              solutions)  # recopie pour eviter les probleme de dico communs dans la recursion

        # voir le fichier branchingStrat pour les infos sur les 2 fonctions suivantes
        # on prend la variable ayant le plus petit domaine, ce qui est inutile pour le backtracking.
        def find_min(self, dico):
            min_clef = sorted(dico)[0]
            for clef in sorted(dico):

                if (len(dico[clef]) > 1):
                    min_clef = clef
                    break
            min_domaine = dico[min_clef]
            min_taille_domaine = len(min_domaine)
            for clef in dico:
                domaine = dico[clef]
                taille_domaine = len(domaine)
                if (taille_domaine < min_taille_domaine and taille_domaine != 1 and taille_domaine != 0):
                    min_clef = clef
                    min_domaine = domaine
                    min_taille_domaine = taille_domaine
            return min_clef

        # Stratégie : on choisit celui qui a le moins de "branches" et on branch !
        def branch(self, domains):
            ens_domains_res = []
            clef_min = self.find_min(domains)
            branches = domains[clef_min]
            for elem in branches:
                domains.update({clef_min: [elem]})
                ens_domains_res.append(dict(domains))
            return ens_domains_res
