"""Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False"""

"""def validar(*args):
    lista = []
    for arg in args:
        lista.append(arg)
        if [arg]== 0 and [arg + 1] == 0:
            print("numero cero consecutivo")
    print(lista)"""
    
    
def ceros_vecinos(*args):
        contador = 0
        for arg in args:
            if contador + 1 == len(args):
                
                return False
            
            elif args[contador]== 0 and args[contador +1] == 0:
                print(contador)
                return True
            else:
                contador+=1
                
        return False    
    
    
    
def funcion(*args):
    ceroseguidos=0
    for n in args:
        if n == 0:
            ceroseguidos += 1
            if ceroseguidos == 2:
                return True
        else:
            ceroseguidos = 0
    return False
print(funcion(2,4,4,0,2,0,0,4))    
            
            
    
    
     
 
print(ceros_vecinos(5,6,1,0,0,9,3,5))   
"""print(ceros_vecinos(6,0,5,1,0,3,0,1))     
print(ceros_vecinos(0,2,5,1,0,3,9,0)) """