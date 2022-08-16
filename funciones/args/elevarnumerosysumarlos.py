def suma_cuadrados(*args):
    
    total = 0
    for arg in args: # hay q recorrer args
       print(arg)
       potencia = arg**2
       print(potencia)
       total+=potencia
    return total
 
print(suma_cuadrados(1,2,3,1)) 