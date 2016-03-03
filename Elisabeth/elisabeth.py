#!/usr/bin/env python3
# coding=utf-8
from nQueensProblem import NQueensProblem, printNode
from backtrackingSolver import BacktrackingSolver
from branchingSolver import BranchingSolver
from localSearchSolver import LocalSearchSolver, printSol
from node import Node
from time import time


def main():
    N = -1
    while (N < 1):
        N = int(input("Rentrer la taille du damier (>0)"))
    # instanciation du probleme
    problem = NQueensProblem(N)
    choix = 0
    while (choix != 1) and (choix != 2):
        choix = int(input("Rentrer un entier :  1:Complete        2:Locale           :"))
    if choix == 1:
        choix = 0
        while (choix != 1) and (choix != 2):
            choix = int(input("Rentrer un entier :  1:Backtracking    2:Branche & prune  :"))
        # instanciation algorithme
        if choix == 1:
            algorithm = BacktrackingSolver()
        else:
            algorithm = BranchingSolver()
    else:
        algorithm = LocalSearchSolver()
    # lancement timer
    start_time = time()
    # resolution probleme
    solutions = algorithm.solve(problem)
    # arret timer
    t = (time() - start_time) * 1000
    cpt = 0
    for sol in solutions:
        cpt = cpt + 1
        printNode(Node(sol))
    print("---%d solutions ---" % cpt)
    print("---temps d'execution : %s millisecondes ---" % round(t, 4))


if __name__ == "__main__":
    main()

## LocalSearchSolver example
# for i in range(500):
#	print("Solving {}-queens problem:".format(i))
#	solver = LocalSearchSolver(i, i * i)
#	solutions = solver.solve(i)
#	if solutions:
#		print("success")
#		for sol in solutions:
#			printSol(sol)
#	else:
#		print("failure")
#	print()
