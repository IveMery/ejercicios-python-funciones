#convertir a str para poder recorrerlo
#agregar a la lista y transformarlo a numero
#revertir lista
def digitize(n):
    lista = []
    for i in str(n): 
        print(i)
        lista.append(int(i))
    return lista[::-1]
       

print(digitize(35231))

def digitize(n):
    return [int(c) for c in str(n)[::-1]]

def digitize(n):
    return list(map(int, str(n)))[::-1]

#str(n)[::-1] and reversed(str(n))