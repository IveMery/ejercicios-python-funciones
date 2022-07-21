"""
lista_numeros = [2,5,2,7,34,3,98,22,1001]

def suma_menores(lista_numeros):
    sum = 0
    for i in lista_numeros:
        if i > 0 and i < 1000:
            sum+=i
    return sum

resultado = suma_menores(lista_numeros)
print(resultado)"""


lista_numeros = [2,5,2,7,34,3,98,22,1001]
sum = 0 
def suma_menores(lista_numeros):
    
    for i in lista_numeros:
        if i > 0 and i < 1000:
          global sum
          sum+=i
    return sum

resultado = suma_menores(lista_numeros)
print(resultado)