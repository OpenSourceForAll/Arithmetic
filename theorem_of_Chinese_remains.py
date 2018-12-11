#!/usr/bin/python3
# -*- coding: utf-8 -*-
########### Robin Gehan ##############################


###########   Exercice 3  ##############################
import random

def theoreme_chinois (nombre, mod):
	n1,n2,n3=mod[0],mod[1],mod[2]
	a1,a2,a3=nombre[0],nombre[1],nombre[2]
	N=n1*n2*n3
	N1=N//n1	# La division entière ici permet que l'algorithme fonctionne pour des très grand nombres comme dans l'exemple 2
	N2=N//n2
	N3=N//n3	
	resultat=bezout(N1,n1)
	u1=resultat[1]
	resultat=bezout(N2,n2)
	u2=resultat[1]
	resultat=bezout(N3,n3)
	u3=resultat[1]
	x=(u1*a1*N1)+(u2*a2*N2)+(u3*a3*N3)
	x=x%N
	return x


def pgcd (x, y):
	x=abs(x)
	y=abs(y)
	r=0
	
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

def bezout (x, y):
	u0,u1=1,0
	v0,v1=0,1
	
	while y!=0:
		q=x//y
		r=x%y
		x,y=y,r
		u0,u1=u1,u0-q*u1
		v0,v1=v1,v0-q*v1
	if x<0:
		x=-x
		u0=-u0
		v0=-v0
	return (pgcd(x,y),u0,v0)

# Fonction de tests des restes chinois
def test_restes ():
	
	print("Restes chinois entre [3,4,5] et [17,11,6] :")
	print(theoreme_chinois([3,4,5],[17,11,6]))
	print("Restes chinois entre [3,4,5] et [(1<<1024)-1,1<<1024 ,(1<<1024)+1] :")
	print(theoreme_chinois([3,4,5],[(1<<1024)-1,1<<1024,(1<<1024)+1]))
	




# Appel des fonctions
test_restes()


	
