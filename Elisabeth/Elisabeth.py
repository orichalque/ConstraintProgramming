#!/usr/bin/env python3
# -*-coding:utf-8 -*
from nQueenProblem import NQueenProblem
from nQueenProblem import printNode
from backTrackingAlgo import BackTrackingAlgorithm
from branchingStrat import BranchingStrat
from localSearchSolver import LocalSearchSolver
from node import Node
import time

N=-1
while (N<1):
	N=int(input("Rentrer la taille du damier (>0)"))
#instanciation du probleme
problem = NQueenProblem(N)
choix=0
while (choix!=1) and (choix!=2):
	choix=int(input("Rentrer un entier :  1:Complete        2:Locale           :"))
if choix==1:
	choix=0
	while (choix!=1) and (choix!=2):
		choix=int(input("Rentrer un entier :  1:Backtracking    2:Branche & prune  :"))
	#instanciation algorithme
	if choix==1:
		algorithm = BackTrackingAlgorithm()
	else:
		algorithm = BranchingStrat()
else:
	algorithm = LocalSearchSolver()
#lancement timer
start_time = time.time()
#resolution probleme
solutions = algorithm.solve(problem)
#arret timer
time = (time.time() - start_time)*1000
cpt=0
for sol in solutions:
	cpt=cpt+1
	printNode(Node(sol))
print("---%d solutions ---" % cpt)
print("---temps d'execution : %s millisecondes ---" % round(time,4))

