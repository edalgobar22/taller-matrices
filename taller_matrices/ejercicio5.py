def superReducedString(s):
    letras = []
    for letra in s:
        if len(letras) > 0 and letras[-1] == letra:
            letras.pop()
        else:
            letras.append(letra)

    resultado = ""
    for i in range(len(letras)):
        resultado += letras[i]
    if resultado == "":
        return "Empty String"
    return resultado


def main():
    s = input("Ingrese una cadena con letras minusculas de a a z: ")
    print(superReducedString(s))


if __name__ == "__main__":
    main()
