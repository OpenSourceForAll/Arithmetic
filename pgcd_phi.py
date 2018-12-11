#!/usr/bin/python3
# -*- coding: utf-8 -*-
########### Robin Gehan ##############################


###########   Exercice 1  ##############################
import random

def pgcd (x, y):
	x=abs(x)
	y=abs(y)
	r=0
	# On échange les valeurs si y est supérieur à x
	if y>x:
		r=y
		y=x
		x=r
	r=0
	while y!=0:
		r=x%y
		x=y
		y=r
	return x



def proba_pgcd ():
	total =1000
	s=0
	for i in range (0,total):
		x=random.randint(1, 1<<1024)	# Le symbole << fonctionne car il signifie un décalage de bit à gauche. Soit 1 = 0001. On décale 1024 fois le bit vers la gauche soit 2 puissance 1024
		y=random.randint(1, 1<<1024)
		if pgcd(x,y) == 1:
			s+=1
	print("La proba est de ", s/total)


def phi(n) :
	if n == 1:
		return 1
	s=0
	for i in range (1, n):
		if(pgcd(i,n)) == 1:
			s+=1
	return s
	
# Fonction de tests des pgcd
def test_pgcd ():
	
	print("pgcd de 2 et 3 :")
	print(pgcd(2,3))
	print("pgcd de -2 et 3 :")
	print(pgcd(-2,3))
	print("pgcd de 2 et 0 :")
	print(pgcd(2,0))
	print("pgcd de -2 et 4 :")
	print(pgcd(-2,4))

# Fonction de tests des phi
def test_phi ():
	
	print("phi de 1 :")
	print(phi(1))
	print("phi de 10 :")
	print(phi(10))
	print("phi de 100 :")
	print(phi(100))
	


# Ici on appelle toutes les fonctions
test_pgcd ()
proba_pgcd()
print("---------------")
test_phi()
