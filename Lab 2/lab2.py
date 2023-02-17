from itertools import combinations_with_replacement as cwr


def main():
    n = 7
    m = 5
    k = 0
    general = []
    values = [1, 2, 3, 4, 5, 6, 7]
    for i1 in range(1, n+1):
        for i2 in range(1, i1+1):
            for i3 in range(1, i2+1):
                for i4 in range(1, i3+1):
                    for i5 in range(1, i4+1):

                        general.append((i5, i4, i3, i2, i1))
                        k += 1

    print(f"valor de K: {k}")
    print(general)
    setOfTuplas = set(general)
    print(setOfTuplas)
    #print(f"Conjunto de tuplas resultante: { setOfTuplas }")
    setOfTuplasWithReplace = set(cwr(values, m))
    #print(f"Conjunto con muestra de 5 elementos con valore de 1-7, con reemplazo: {setOfTuplasWithReplace}")

    # Ambas formas me dio lo mismo...podrian usarse ambas, pero mas seguron con issubset()
    subconjunto1 = setOfTuplas <= setOfTuplasWithReplace
    subconjunto2 = setOfTuplasWithReplace <= setOfTuplas

    #subconjunto1 = general.issubset(setOfTuplasWithReplace)
    #subconjunto2 = setOfTuplasWithReplace.issubset(setOfTuplas)

    print(
        f"subconjunto de setOfTuplas con setOfTuplasWithReplace: {subconjunto1}")
    print(
        f"subconjunto de setOfTuplasWithReplace con setOfTuplas: {subconjunto2}")


if __name__ == "__main__":
    main()
