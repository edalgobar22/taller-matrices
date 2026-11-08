def solution(a):
    totales = [0, 0]
    for i in range(len(a)):
        if i % 2 == 0:
            totales[0] += a[i]
        else:
            totales[1] += a[i]
    return totales


def main():
    cantidad = int(input("Numero de personas: "))
    while cantidad < 1 or cantidad > 100000:
        cantidad = int(input("Ingrese una cantidad entre 1 y 100000: "))
    pesos = []
    for i in range(cantidad):
        peso = int(input(f"Peso de la persona {i + 1}: "))
        while peso < 45 or peso > 100:
            peso = int(input("Ingrese un peso entre 45 y 100: "))
        pesos.append(peso)
    print(solution(pesos))


if __name__ == "__main__":
    main()
