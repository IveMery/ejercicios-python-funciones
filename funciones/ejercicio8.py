lista_numeros = [1, 2, 15, 7, 2]

def reducir_lista(lista):
    mi_lista = list(set(lista)) #elimina los duplicados y list convierte en lista
    mi_lista.remove(max(mi_lista)) #elimina el numero mas mayor de la lista
    return mi_lista


reducir = reducir_lista(lista_numeros)
print(reducir)

def promedio(param):
    suma = 0
    for i in param:
        suma += i
        print(suma)
        promedio = suma / len(param)
    return promedio

promedio_lista = promedio(reducir)
print(promedio_lista)
