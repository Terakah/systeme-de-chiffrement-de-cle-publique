# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:30:43 2022

@author: TeRaKa
6"""

#import numbers
import math
import numpy
import random
import fractions
import copy

#interieur de la fonction qui permet de choisir le nombre de sommet
list_sommet = [] #liste vide qui contiendra les sommets
valeur_sommet = []
nombre = input('Entrer le nombre de sommet que vous voulez :') #Choix de l'utilisateur du nombre de sommet
nombre1 = int(nombre) # Conversion du string recupérer en entrée en entier
for i in range(nombre1):
    list_sommet.append(i) #remplisssage de liste des sommets
    valeur_sommet.append(0)
print('Nom des sommets :',list_sommet) # Affichage de la liste

#interieur de la fonction qui choisit les sommets principaux
list_sommetP = [] #liste vide qui contiendra les sommets principaux
valeur_sommetP = []
taille = len(list_sommet) # On regarde la taille de la liste de sommet
nombre_max = int(taille//5) # on determine le nombre de sommet principaux voulut
for i in range(nombre_max):
    tirage = True
    while tirage:
        numero = random.randint(0,(nombre1)-1)
        if not numero in list_sommetP:
            list_sommetP.append(numero) # boucle qui nous permet de choisir aléatoirement les sommets principaux
            tirage = False
for j in list_sommetP:
    valeur_sommetP.append(0)
print('Sommets principaux :',list_sommetP)#Affichage de la liste des sommmets principaux

arretes = []

#Ajouts des arretes avec les sommets principaux
for s in list_sommet:
    if not s in list_sommetP:
        arrete = (s, list_sommetP[random.randint(0, nombre_max-1)])
        arretes.append((min(arrete), max(arrete)))

#ajout d'arretes aléatoires
nb_ajout = 8 * (taille // 5)

for i in range(nb_ajout):
    drapeau = True
    while drapeau:
        s1 = list_sommet[random.randint(0, nombre1-1)]
        s2 = list_sommet[random.randint(0, nombre1-1)]
        if s2 < s1:
            s1, s2 = s2, s1
        if s1 != s2 and (s1, s2) not in arretes and s1 not in list_sommetP and s2 not in list_sommetP:
            drapeau = False
            arretes.append((s1, s2))

print('Arretes :',arretes)#Affichage des arretes

alphabet = ' abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
la = len(alphabet)



 



def code(message):
    '''transforme une chaine de caractÃ¨re 10en nombre'''
    n = 0
    for c in message:
        n = la * n + alphabet.index(c)
    return n


message = input('Entrer le message de votre choix: ')
a = code(message)       
print('Le message étant: ' + str(message))
print('On code le message par:' + str(a))  
print('le code du message sera attribué à la lettre "a"')


def chiffrement(a):
    V = valeur_sommet
    V[0] = random.randint(1,a//taille)
    b=V[0]
    for i in range(1,len(V)-1):
        V[i] = random.randint(1,abs(a-b)-len(V)+i)
        b += V[i]
    V[-1] = (a - b)
    V1 = V.copy()
    for p in list_sommet:
      for q in list_sommet:
            if (p,q) in arretes:
                V1[p] = V1[p] + V[q] 
                V1[q] = V1[q] + V[p]
    print('La liste des valeurs ponctuelles est:    ' + str(V))
    print('La liste des valeurs par regroupement est:  ')                          
    return V1
    
   
        


def decode(L):
    n = 0
    for q in list_sommetP:
        n += L[q]
    '''renvoie la chaine correspondante'''
    s = ''
    while n > 0:
        s = alphabet[n%la] + s
        n = n // la
    return s

