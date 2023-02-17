# -*- coding: utf-8 -*-
"""Laboratorio 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lFeG0LIXNkyaqclillgtyBMYbEX6hQ88

# Parte 1
"""

import random
from itertools import permutations, product, combinations, combinations_with_replacement
from collections import Counter

def digitosRepetidos():
    combR = list(combinations_with_replacement(lista,4))
    comb = list(combinations(lista,4))
    combu = set(combR) - set(comb)
    combu = list(combu)
    return combu

########  M E N U  #########
salida = False
while salida == False:
    print("\n\nPROBLEMA #1 \na) Sucesiones de 4 digitos diferentes \nb) Sucesiones de 4 digitos con repetidos b\nc) Filtros de sucesiones con repetidos \nd) Salir")

    entrada = input("Ingrese su opcion: ")
    lista = [0,1,2,3,4,5,6,7,8,9]


    if entrada == "a":
        perm = list(permutations(lista,4))
        print(perm)
        cant = len(perm)
        print(cant)
        
        
    if entrada == "b":
        combu = digitosRepetidos()  
        cant = len(combu)
        print(combu)
        print(cant)
        
        
    if entrada == "c":
      
        
        combu = digitosRepetidos()
        resp1 = []
        resp2 = []
        resp3 = []
        resp4 = []
        
        for tupla in combu:
            if all(x == tupla[0] for x in tupla):
                resp1.append(tupla)
        
        print("\nSe repite el digito 4 veces: ", len(resp1), "veces")
        print(resp1)
        
        for tupla in combu:
            if all(x == 2 for x in Counter(tupla).values()):
                resp2.append(tupla)
                
        
        print("\nSe repiten dos digítos 2 veces cada uno: ", len(resp2), "veces")
        print(resp2)
        
        for tupla in combu:
            if any(x == 2 for x in Counter(tupla).values()):
                resp3.append(tupla)
                
        resp3 = set(resp3) - set(resp2)
                
        
        print("\nSe repite un elemento dos veces y los otros no se repiten: " , len(resp3), "veces")
        print(resp3)

        for tupla in combu:
            if any(x == 3 for x in Counter(tupla).values()):
                resp4.append(tupla)
        
        
        print("\nSe repite un dígito 3 veces y el otro no se repite: " , len(resp4), "veces")
        print(resp4)            
                
        
        print("\n\nTotal de sucesiones con elementos que se repiten: ", len(resp1)+len(resp2)+len(resp3)+len(resp4)  )
        
    if entrada == "d":
        print("\nsaliendo...")
        salida = True

"""# Parte 2"""

import math
num = 100
num2 = 100
flag = True
lista = [2]

#Llena la primera lista con los primeros primos hasta sqrt(num)
for i in range(3,math.ceil(math.sqrt(num))):
  flag = True
  if math.sqrt(num).is_integer:
    for j in range(2,i):
      #print(i, " % ", j, ": ", i%j)
      if i%j == 0:
        flag = False
        break
    if flag:
      lista.append(i)

lista2=[]
lista3=[]

for i in range(len(lista)):
    num -= math.floor(100/lista[i])

    for i2 in lista[i+1:]:
        num += math.floor(100/(i2*lista[i]))
        lista2.append(i2*lista[i])

for i in range(1,3):
    for i2 in range(3-i): 
        num -= math.floor(100/(lista[-i]*lista2[i2]))
        lista3.append(lista[-i]*lista2[i2])

num -= 1 #No se cuenta el 1
num += 4 #Hay que volver a incluir el 2, 3, 5 y 7

print("Cantidad de primos menores que 100:", num)
print("Listas utilizadas: ")
print(lista)
print(lista2)
print(lista3)

flag = True
print("\nLista de primos del 1 al",num2, ": ")
for i in lista:
  print(f"{i}", end = ' ')

for i in range(2, num2):
  flag = True
  for j in lista:
    if  i%j == 0:
      flag = False
      break
  if flag:
    print(f"{i}", end = ' ')

"""# Parte 3"""

'''
Algo a resaltar para este ejercicio, es que, básicamente al poseer el orde de 
i5-i1, los valores a tomar en cuenta siempre serán de menor a mayor, y es que, 
se rige en parte por el teorema de inclusión-exclusión, indicando que siempre, 
el primer valor será mayor o igual a 1, y el resto de valores que le siguen (
o preceden) serán mayores o iguales a este.

Esto se da, pues los valores que pueden ser seleccionados tiene cierto criterio, 
en este caso, pueden ser cualquier valor del 1-7, pero  con la condición 
previamente descrita. Esto quiere decir que los valores N(in) son los valores 
que estarán en la tupla. Al final de cuentas, estos valores poseen la condición 
que posee el iterador, es decir, el siguiente iterador posee el mismo inicio, 
pero diferente final, es decir, si el primer iterador empieza en 1, el final 
para el siguiente es 2, con lo cual, siempre habra un momento de espera entre 
los valores, con lo cual, se cumple que el iterador interno tiene la regla de 
ser mayor o igual a 1, y los externos, mayores o iguales al interno, pero 
ninguno de ellos, menores a este.

Algo más a tomar en cuenta, es que al convertir el arreglo de tuplas GENERAL 
(así se llama), concibe el mismo valor al que se obtiene utilizando la función 
“combination_with_replacement” para la generación de otros valores siguiendo el 
mismo patrón. Esto indica que, ambos casos se rigen por la misma regla,  es decir, 
el siguiente valor de la tupla nunca será menor al previo.

'''

from itertools import combinations_with_replacement as cwr

def main():
    n = 7   
    m = 5
    k = 0
    general = []
    values = [1,2,3,4,5,6,7]
    for i1 in range (1, n+1):
        for i2 in range (1, i1+1):
            for i3 in range(1, i2+1):
                for i4 in range (1, i3+1):
                    for i5 in range (1, i4+1):
                        general.append((i5,i4,i3,i2,i1))
                        k += 1
    
    print(f"valor de K: {k}")
    #Descomentar la siguiente linea de codigo, para ver los valores originales de
    # del arreglo GENERAL.
    # print(general) 
    setOfTuplas = set(general)
    print(f"Conjunto de tuplas resultante: {setOfTuplas}")
    setOfTuplasWithReplace = set(cwr(values,m))
    print(f"Conjunto con muestra de 5 elementos con valore de 1-7, con reemplazo: {setOfTuplasWithReplace}")
    
    # Ambas formas me dio lo mismo...podrian usarse ambas, pero mas seguron con issubset()
    #subconjunto1 = setOfTuplas <= setOfTuplasWithReplace
    #subconjunto2 =  setOfTuplasWithReplace <= setOfTuplas
    
    subconjunto1 = setOfTuplas.issubset(setOfTuplasWithReplace)
    subconjunto2 = setOfTuplasWithReplace.issubset(setOfTuplas)
    
    print(f"subconjunto de setOfTuplas con setOfTuplasWithReplace: {subconjunto1}")
    print(f"subconjunto de setOfTuplasWithReplace con setOfTuplas: {subconjunto2}")
    
if __name__ == "__main__":
    main()