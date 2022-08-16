mi_archivo = open('prueba.txt') #abrir archivo open
#open recibe 2 parametros
 # el segundo puede ser  r,w,a
 # lectura ,REESCRIBIR ,escritura

print(mi_archivo.read())
print(mi_archivo.readline())
mi_archivo.close() #siempre cerrar el archivo


