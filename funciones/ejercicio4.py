lista_numeros = [2,5,2,7,34,-23,98,22,-10]
def todos_positivos(lista_numeros):
    for i in lista_numeros:
        print(i)
        if i < 0 :
            return False
        else:
            pass
    return True 