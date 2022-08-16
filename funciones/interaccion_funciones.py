from random import shuffle

# Lista palitos
palitos = ['-', '--', '---', '----']

# Mezclar palitos
def mezclar_palitos(lista):
    shuffle(lista)
    print(lista)
    return lista

# pedir intento
def pedir_intento():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input("ingresa un numero del 1 al 4")
    return int(intento)        

# Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento -1 ] == "-":
        print("Sacaste el palito mas corto :( toca lavar los paltos")
    else:
        print("Te salvaste anda a jugar")  
        
#llamo a las funciones        
palitos_mezclados = mezclar_palitos(palitos)
seleccion = pedir_intento()
chequear_intento(palitos_mezclados,seleccion)        
    
    
 
