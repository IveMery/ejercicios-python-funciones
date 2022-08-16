"""Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio"""


"""def devolver_distintos(uno,dos,tres):
    suma = 0
    suma = uno + dos + tres
    print(suma)
    if suma > 15:
        if uno > dos and uno > tres :
            print(uno)
        elif dos > uno and dos > tres :
            print(dos)
        else:
            print(tres)    
    elif  suma < 10:
        if uno < dos and uno < tres :
            print(uno)
        elif dos < uno and dos < tres :
            print(dos)
        else:
            print(tres)  
    elif suma >=10 and suma <= 15:
        if uno > dos and uno < tres:
            print(uno)
        elif  dos > uno and dos < tres:
            print(dos)
        else:
            print(tres)                     
            """


def devolver_distintos(*args):
    lista=[]
    for arg in args:
        lista.append(arg)
    suma = sum(lista)
    print(suma)
    if suma > 15:
        print(max(lista))
    elif suma < 10:
        print("menor a 10")
        print(min(lista))    
    elif suma >=10 and suma <=15:
        print("estoy aca")
        lista.sort()
        print(lista[1])
       # lista.remove(max(lista))
        #lista.remove(min(lista))
        #print(lista[0])   
         
      
print(devolver_distintos(2,4,7))    