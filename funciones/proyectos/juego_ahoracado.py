import random
#lista con palabras
lista_palabras =['TELEVISOR','PERRO','MESA','GATOS','PASTEL','COCODRILO','TRIANGULO']

def palabra_azar(lista):
    palabra = random.choice(lista)
    return palabra

def guiones(palabra):
    guion = []
    for i in palabra:
       guion.append('_')
    return guion

def ingresar_letra():
        letra = input("Ingresa una letra: ")
        while True:
            if letra.isalpha():
                return letra.upper()
            else:
                print('El caracter no es correcto, por favor ingresa una letra valida')
                letra = input("Ingresa una letra valida")
                
def chequear_letra(palabra):
    vidas = 6
    letras_incorrectas = []
    #print(f"{mostrar_guiones}")
    print(f'{" ".join(mostrar_guiones)}')
    while vidas > 0:
        if "_" not in mostrar_guiones:
            print(f'{"".join(mostrar_guiones)}')
        #if "".join(mostrar_guoines) == palabra:
        #El método join() devuelve una cadena concatenada con los elementos de iterable . 
        #devuelve el elemento de la cadena sin espacios en este caso la palabra
        #si la palabra es igual  a la elgida gano!
            print('Felicidades ganaste!')
            break
        letra = ingresar_letra()   
        if letra in palabra:
            for index,char in enumerate(palabra):
                if char == letra:
                    mostrar_guiones[index] = letra
            #print(f'{mostrar_guiones}') 
            print(f'{" ".join(mostrar_guiones)}') 
        else:
            letras_incorrectas.append(letra)
            vidas-=1
            print(f' Te quedan {vidas} vidas :P')  
            print(f'letras incorrectas: {letras_incorrectas}')  


palabra  = palabra_azar(lista_palabras)   
mostrar_guiones = guiones(palabra)       
chequear_letra(palabra)   

      
                    