import random
from itertools import permutations, product, combinations, combinations_with_replacement
from collections import Counter


def digitosRepetidos():
    combR = list(combinations_with_replacement(lista, 4))
    comb = list(combinations(lista, 4))
    combu = set(combR) - set(comb)
    combu = list(combu)
    return combu


########  M E N U  #########
salida = False
while salida == False:
    print("\n\nPROBLEMA #1 \na) Sucesiones de 4 digitos diferentes \nb) Sucesiones de 4 digitos con repetidos b\nc) Filtros de sucesiones con repetidos \nd) Salir")

    entrada = input("Ingrese su opcion: ")
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    if entrada == "a":
        perm = list(permutations(lista, 4))
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

        print("\nSe repite un elemento dos veces y los otros no se repiten: ", len(
            resp3), "veces")
        print(resp3)

        for tupla in combu:
            if any(x == 3 for x in Counter(tupla).values()):
                resp4.append(tupla)

        print("\nSe repite un dígito 3 veces y el otro no se repite: ",
              len(resp4), "veces")
        print(resp4)

        print("\n\nTotal de sucesiones con elementos que se repiten: ",
              len(resp1)+len(resp2)+len(resp3)+len(resp4))

    if entrada == "d":
        print("\nsaliendo...")
        salida = True
