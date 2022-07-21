lista = [1221, 2323, 34, 1, 312, 314, 412]


def tres_cifraslistas(list):
    for i in lista:
        if i in range(100, 1000):
            return True
        else:
            pass
    return False

resultado = tres_cifraslistas(lista)
print(resultado)
