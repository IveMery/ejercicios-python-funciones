#crea una funcion llamada cantidad de atributos q cuente la cantidad de parametros 
#q se entrega y devuelva esa cantidad como resultado

def cantidad_atributos(**kwargs):
    return len(kwargs)

atributos = cantidad_atributos(y=1,x=3,z=6,o=8)
print(atributos)