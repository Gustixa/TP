import numpy as np


def main():
    urnas = np.array([1/3, 1/3, 1/3])
    limon = np.array([1/3, 2/5, 1/3])
    toroShape = np.array([2/3, 1/2, 2/5])
    result1 = np.multiply(urnas, limon)
    result2 = np.multiply(result1, toroShape)

    # Problema A
    final_result = np.sum(result2)
    print(
        f"La probabilidad de que sea de limon y tenga forma de toro es: {final_result}")

    # Problema B
    problemB = result2[2] / final_result
    print(f"La probabilidad de que surja de la urna 2, es de: {problemB}")
    # Problema C
    problemC = result2[1] / final_result
    print(f"La probabilidad de que surja de la urna 1, es de: {problemC}")
    # Problema D
    problemD = result2[0] / final_result
    print(f"La probabilidad de que surja de la urna 0, es de: {problemD}")


if __name__ == "__main__":
    main()
