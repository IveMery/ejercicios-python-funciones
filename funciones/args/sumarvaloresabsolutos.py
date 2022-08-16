def suma_absolutos(*args):
    suma = 0
    for arg in args:
      suma += abs(arg)
    return suma
   
print(suma_absolutos(1,2,3,4,-5,-3)) 
   