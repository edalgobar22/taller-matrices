def crearMatrices(n):
    matrices = []
    # Se construyen las ocho matrices en el orden del PDF.
    for tipo in range(1, 9):
        matriz = []
        numero = 1
        for f in range(n):
            fila = []
            for c in range(n):
                if tipo == 1:
                    valor = numero
                    numero += 1
                elif tipo == 2:
                    if f % 2 == 0:
                        valor = c + 1
                    else:
                        valor = n - c
                elif tipo == 3:
                    if f == c:
                        valor = 1
                    else:
                        valor = 0
                elif tipo == 4:
                    if f + c == n - 1:
                        valor = 1
                    else:
                        valor = 0
                elif tipo == 5:
                    if c <= f:
                        valor = 1
                    else:
                        valor = 0
                elif tipo == 6:
                    if c >= f:
                        valor = 1
                    else:
                        valor = 0
                elif tipo == 7:
                    valor = c * n + f + 1
                else:
                    if c <= f:
                        if c % 2 == 0:
                            valor = "A"
                        else:
                            valor = "B"
                    else:
                        valor = " "
                fila.append(valor)
            matriz.append(fila)
        matrices.append(matriz)
    return matrices


def imprimirMatriz(matriz):
    # El ancho se adapta incluso si los numeros tienen mas de dos cifras.
    ancho = len(str(len(matriz) * len(matriz))) + 1
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(str(matriz[f][c]).rjust(ancho), end=" ")
        print()


def main():
    n = int(input("Tamano de las matrices cuadradas: "))
    while n <= 0:
        n = int(input("Ingrese un tamano mayor que cero: "))
    matrices = crearMatrices(n)
    for i in range(len(matrices)):
        print(f"\nMatriz {i + 1}:")
        imprimirMatriz(matrices[i])


if __name__ == "__main__":
    main()
