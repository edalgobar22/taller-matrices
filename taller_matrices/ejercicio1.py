# Cada fila representa un producto y cada columna un dia.
def lstTotalProductosxsem(Ventas, Precios):
    fils = len(Ventas)
    cols = len(Ventas[0])
    lstTotales = []
    for f in range(fils):
        suma = 0
        for c in range(cols):
            suma += Ventas[f][c] * Precios[f]
        lstTotales.append(suma)
    return lstTotales


def lstTotalVentasxdia(Ventas, Precios):
    fils = len(Ventas)
    cols = len(Ventas[0])
    lstTotales = []
    for c in range(cols):
        suma = 0
        for f in range(fils):
            suma += Ventas[f][c] * Precios[f]
        lstTotales.append(suma)
    return lstTotales


def main():
    lstDias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    matVentas = []
    lstPrecios = []
    for f in range(5):
        print(f"\nProducto {f + 1}")
        precio = int(input("Precio unitario (sin puntos ni comas): "))
        while precio <= 0:
            precio = int(input("Ingrese un precio mayor que cero: "))
        lstPrecios.append(precio)
        fila = []
        for c in range(7):
            cantidad = int(input(f"Unidades vendidas el {lstDias[c]}: "))
            while cantidad < 0:
                cantidad = int(input("Ingrese una cantidad mayor o igual a cero: "))
            fila.append(cantidad)
        matVentas.append(fila)

    print("\nMatriz de ventas (lunes a domingo):")
    for f in range(len(matVentas)):
        print(matVentas[f])

    lstTotales = lstTotalProductosxsem(matVentas, lstPrecios)
    maxTotal = max(lstTotales)
    # Se recorren los resultados para mostrar todos los productos si hay empate.
    for f in range(len(lstTotales)):
        if lstTotales[f] == maxTotal:
            print(f"El producto {f + 1} genera mas ingresos en la semana: ${maxTotal:,}")

    lstTotalesDias = lstTotalVentasxdia(matVentas, lstPrecios)
    maxDia = max(lstTotalesDias)
    for c in range(len(lstTotalesDias)):
        if lstTotalesDias[c] == maxDia:
            print(f"El {lstDias[c]} tiene los mayores ingresos: ${maxDia:,}")


if __name__ == "__main__":
    main()
