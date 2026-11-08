# Matriz: cada fila guarda [nombre del producto, orden de ingreso].
# El orden permite eliminar el mas reciente incluso despues de ordenar.
def buscarProducto(inventario, nombre):
    for f in range(len(inventario)):
        if inventario[f][0] == nombre:
            return f
    return -1


def agregarProducto(inventario, consecutivo):
    nombre = input("Nombre del producto: ").strip().lower()
    if nombre == "":
        print("El nombre no puede estar vacio.")
    elif buscarProducto(inventario, nombre) != -1:
        print("El producto ya existe.")
    else:
        inventario.append([nombre, consecutivo])
        consecutivo += 1
        print("Producto agregado.")
    return consecutivo


def ordenarProductos(inventario):
    # Ordenamiento con ciclos e intercambio de filas completas.
    for f in range(len(inventario) - 1):
        for c in range(f + 1, len(inventario)):
            if inventario[f][0] > inventario[c][0]:
                auxiliar = inventario[f]
                inventario[f] = inventario[c]
                inventario[c] = auxiliar


def main():
    inventario = []
    consecutivo = 1
    opcion = ""
    while opcion != "7":
        print("\nMENU")
        print("1. Agregar producto")
        print("2. Agregar lote de productos")
        print("3. Eliminar producto del inventario")
        print("4. Eliminar el producto mas reciente")
        print("5. Ordenar productos alfabeticamente")
        print("6. Mostrar numero total de productos")
        print("7. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            consecutivo = agregarProducto(inventario, consecutivo)
        elif opcion == "2":
            cantidad = int(input("Cuantos productos desea agregar: "))
            while cantidad <= 0:
                cantidad = int(input("Ingrese una cantidad mayor que cero: "))
            for i in range(cantidad):
                print(f"Producto {i + 1} del lote")
                consecutivo = agregarProducto(inventario, consecutivo)
        elif opcion == "3":
            nombre = input("Producto que desea eliminar: ").strip().lower()
            posicion = buscarProducto(inventario, nombre)
            if posicion == -1:
                print("El producto no esta en el inventario.")
            else:
                inventario.pop(posicion)
                print("Producto eliminado.")
        elif opcion == "4":
            if len(inventario) == 0:
                print("El inventario esta vacio.")
            else:
                posicion = 0
                for f in range(1, len(inventario)):
                    if inventario[f][1] > inventario[posicion][1]:
                        posicion = f
                eliminado = inventario.pop(posicion)
                print(f"Producto mas reciente eliminado: {eliminado[0]}")
        elif opcion == "5":
            ordenarProductos(inventario)
            print("Inventario ordenado.")
        elif opcion == "6":
            print(f"Numero total de productos: {len(inventario)}")
        elif opcion == "7":
            print("Programa finalizado.")
        else:
            print("Opcion incorrecta.")

        if opcion != "7":
            print("Inventario actual:")
            if len(inventario) == 0:
                print("Vacio")
            for f in range(len(inventario)):
                print(f"{f + 1}. {inventario[f][0]}")


if __name__ == "__main__":
    main()
