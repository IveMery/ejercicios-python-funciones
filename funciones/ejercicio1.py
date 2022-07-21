def tres_cifras(numero):
       return numero in range(100,1000)
   
resultado = tres_cifras(12)
print(resultado)


lista=[1221,2323,34,1,312,314,412]
acc = []
def tres_cifraslistas(list):
    for i in lista:
         if i in range(100,1000):
           acc.append(i)
           
    return acc
                
   
resultado = tres_cifraslistas(lista)
print(resultado)