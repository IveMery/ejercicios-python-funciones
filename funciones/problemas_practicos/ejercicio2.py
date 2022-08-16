"""Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']"""

def letras_sin_repetir(param):
    letras = list(set(param))
    letras.sort() #sort no retorna el valor 
    return letras #retornar la lista o 

    #sorted(newList)
    """ new_list = sorted(letras)
    return new_list"""
   
print(letras_sin_repetir('entretenido'))    