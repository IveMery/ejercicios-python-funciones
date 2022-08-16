def numeros_persona(name,*args):
    suma_numeros = 0
    for arg in args:
        suma_numeros +=arg
    return f'{name}, la suma de tus numeros es {suma_numeros}'
    
print(numeros_persona('Homero',1,2,3,4,5))


def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'

print(numeros_persona('Homero',1,2,3,4,5,2))