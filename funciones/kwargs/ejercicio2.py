# devolver en una lista los valores de los atributos
def lista_atributos(**kwargs):
    lista = []
    for clave, valor in kwargs.items():
        lista.append(valor)
    return lista

resultado = lista_atributos(x='uno', y='dos', z='tres')
print(resultado)
