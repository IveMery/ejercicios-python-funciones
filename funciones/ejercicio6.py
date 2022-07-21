lista_numeros = [22, 13, 7, 5, 4, 9, 8]


def cantidad_pares(lista_numeros):
    cantidad = 0
    for i in lista_numeros:
        if i % 2 == 0:
            cantidad += 1
    return cantidad


resultado = cantidad_pares(lista_numeros)
print(resultado)
