import random

lista_numeros = [1, 2, 3, 4, 5]

def lanzar_moneda():
    resultado = random.choice(['Cara', 'Cruz'])
    print(resultado)
    return resultado

def probar_suerte(param1, param2):
    if param1 == "Cara":
        print(f'La lista se autodestruira')
        return []
    else:
        print(f'La lista fue salvada')
        return param2

moneda = lanzar_moneda()
suerte = probar_suerte(moneda, lista_numeros)
print(suerte)
