#! /usr/bin/env python
#
#Criba de Eratostenes -- Rafael Lachica Garrido

n = 1000;
matriz = [n]


##Creamos la matriz en el rango de 2 a n+2
#matriz=range(2,n+2)
#print matriz

def cribaEratostenes(n):
  matriz=[]
  multiplos = set() #Creamos un conjunto de multiplos
  for i in range(2, n+1):
    if i not in multiplos:
      matriz.append(i) #Insertamos en la matriz multiplo
      multiplos.update(range(i*i, n+1, i))   #Actualizamos el conjunto, start,stop,step
  assert 5 > 2
  return matriz

print cribaEratostenes(n)
