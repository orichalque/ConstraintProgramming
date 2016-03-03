# coding=utf-8
from abstractSolver import AbstractSolver


class BranchingSolver(AbstractSolver):
    def __init__(self):
        pass

        # Fonction de résolution principale
        def solve(self, problem):
            sol = list()
            self.branchAndPruneRec(problem, problem.node.domains, sol)
            return sol

        # fonction recursive ajoutant les solutions dans la liste "solutions"
        def branchAndPruneRec(self, problem, domains, solutions):

            # pruning sur les domaines actuels
            dom = self.pruneDiag(domains)

            # on verifie que chaque variable pruné a toujours une affectation possible -> sinon on arrete la fonction pour cette branche
            for clef in dom:
                if len(dom[clef]) == 0:
                    return []

            if self.estSolution(dom):
                solutions.append(dom)
            else:
                # on fait des branches pour chaque element du domaine de la variable ayant le plus petit domaine
                for domainsBis in self.branch(dom):
                    self.branchAndPruneRec(problem, dict(domainsBis),
                                           solutions)  # copie du dictionnaire pour éviter les problèmes dans la recursion (plusieurs branche travaillerai sur le meme)

        def estSolution(self, domains):
            for clef in domains:
                if len(domains[clef]) != 1:
                    return False
            return True

        # prunage simple : si on a une affectation, on enleve la valeur du domaine de chaque variable
        def pruneSimple(self, domains):
            for clef in domains:
                if len(domains[clef]) == 1:
                    val_to_del = domains[clef][0]
                    for variable in domains:
                        if domains[variable].count(val_to_del) != 0 and variable != clef:
                            domains[variable].remove(val_to_del)
            return domains

        # prunage Diag : si on a une affectation, on enleve des autres variables les diagonales déja affectées et la valeur
        # prunage simple + prunage en diagonale.
        # en supposant qu'on connait deja le probleme(Nqueens)
        def pruneDiag(self, domainsGlob):
            domains = dict(domainsGlob)
            clefs = sorted(domains)
            for clef_i in domains:
                domains[clef_i] = list(domainsGlob[clef_i])
            for clef_i in clefs:
                if len(domains[clef_i]) == 1:
                    val_to_del = domains[clef_i][0]
                    for clef_j in clefs:
                        if clef_j != clef_i:
                            # colonne
                            if domains[clef_j].count(val_to_del) != 0:
                                domains[clef_j].remove(val_to_del)
                            offset = int(float(clef_i)) - int(float(clef_j))
                            # diagonale
                            if domains[clef_j].count(val_to_del - offset) != 0:
                                domains[clef_j].remove(val_to_del - offset)
                            # Anti-diagonale
                            if domains[clef_j].count(val_to_del + offset) != 0:
                                domains[clef_j].remove(val_to_del + offset)
            return domains

        # renvoie la clef correspondant au domaine le plus petit du dico
        def find_min(self, dico):
            # on prend le premier élément comme etant le plus petit
            min_clef = sorted(dico)[0]
            # on cherche une clef qui aurait plus de 1 element dans son domaine (si on branche un domaine d'un élément cela ne nous servirait a rien)
            for clef in sorted(dico):
                if (len(dico[clef]) > 1):
                    min_clef = clef
                    break
            min_domaine = dico[min_clef]
            min_taille_domaine = len(min_domaine)

            # recherche du minimum
            for clef in dico:
                domaine = dico[clef]
                taille_domaine = len(domaine)

                # domaine plus grand que 1 mais on veut le plus petit quand meme
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

            # pour chaque element du domaine de la variable aillant le plus petit domaine :
            # on creer un nouveau domaine ayant 1 seul élément pour cette variable puis on l'ajoute dans un ensemble
            for elem in branches:
                # update modifie la valeur de cle_min à [elem] dans le dico domains
                domains.update({clef_min: [elem]})
                ens_domains_res.append(dict(domains))  # recopie du domaine dans un nouveau dictionnaire
            return ens_domains_res
