import random
#crear funcion lanzar dados
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2= random.randint(1, 6)
    print(dado1,dado2)
    return dado1,dado2
    
dado1,dado2 = lanzar_dados()    
    
    
    #definir funcion evaluar juagada 
def evaluar_jugada(dado1,dado2):
    suma_dados= dado1 + dado2
    if suma_dados <= 6:
         return f'La suma de tus dados es {suma_dados}. Lamentable'
    elif suma_dados > 6  and suma_dados < 10:
        return f'La suma de tus dados es {suma_dados}. Tienes buenas chances'
    elif suma_dados >= 10 :
        return f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora'
#
jugada = evaluar_jugada(dado1,dado2)
print(jugada)