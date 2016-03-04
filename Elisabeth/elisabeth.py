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
    choix = 0
    while (choix != 1) and (choix != 2):
        choix = int(input("Rentrer un entier :  1:Complete        2:Locale           :"))
    if choix == 1:
        problem = NQueensProblem(N)
        print_function = printNode
        choix = 0
        while (choix != 1) and (choix != 2):
            choix = int(input("Rentrer un entier :  1:Backtracking    2:Branche & prune  :"))
        # instanciation algorithme
        if choix == 1:
            algorithm = BacktrackingSolver()
        else:
            algorithm = BranchingSolver()
    else:
        problem = N
        print_function = printSol
        algorithm = LocalSearchSolver(N, N * N)
    # lancement timer
    start_time = time()
    # resolution probleme
    solutions = algorithm.solve(problem)
    # arret timer
    end_time = time()
    t = (end_time - start_time) * 1000
    cpt = 0
    for sol in solutions:
        cpt = cpt + 1
        if print_function == printNode:
            print_function(Node(sol))
        elif print_function == printSol:
            print_function(sol)
    print("---%d solution(s) ---" % cpt)
    print("---temps d'execution : %s milliseconde(s) ---" % round(t, 4))


if __name__ == "__main__":
    main()
