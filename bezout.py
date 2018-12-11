#!/usr/bin/python3
# -*- coding: utf-8 -*-
########### Robin Gehan ##############################


###########   Exercice 2  ##############################
import random
import math

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


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def inverse (x,n):

	if pgcd(x,n)!=1 :
		print("erreur, pas inversible")
		return 0

	tab=bezout(x,n)
	return tab[1]

# Fonction de tests de bezout
def test_bezout ():
	
	print("Bezout entre 11 et -7")
	print(bezout(11,-7))
	print("Bezout entre -20 et 5")
	print(bezout(-20,5))
	

# Fonction de tests de la fonction inverse
def test_inverse ():
	
	print("inverse modulaire de 3 mod 2¹⁰²⁴") # le resultat du TP ne correspond pas, peut etre une erreur dans le sujet car le resultat attendu est trouvé pour 2<<1024
	print (inverse(3,1<<1024))			# 1<<1024 = 2¹⁰²
	
	print("inverse modulaire de 3 mod 2¹⁰²⁴")
	print (inverse(3,2<<1024))
	
	
	print("inverse modulaire de 4 mod 5")
	print (inverse(4,5))
	print (modinv(4,5))


test_bezout()
test_inverse()


	
