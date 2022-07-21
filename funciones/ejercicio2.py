list = [1,2,3,4,5]
lista2=[23,23,23,453,345,23423423423,]

def sumar_lista(param):
    sum = 0
    for i in param:
        sum+=i
    return sum
        
print(sumar_lista(list))     
print(sumar_lista(lista2))  


