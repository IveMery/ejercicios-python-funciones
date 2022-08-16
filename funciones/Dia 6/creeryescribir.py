archivo = open('prueba.txt','a')
archivo.write('soy el nuevo texto')
archivo.writelines(['hola',' mundo',' aqui',' estoy'])
#ecibe una lista de palabras
lista = ['prueba', 'texto', 'con','for']
for i in lista:
    archivo.writelines(i + '\n')
 # va al final del strig y comienza a escribir desde ahi
archivo.write('BIENVENIDO')
archivo.close()
#w sobreescribe

"""ejercicio 1 Práctica Crear y Escribir Archivos 1
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura."""

"""archivo = open('mi_archivo.txt','w')
archivo.write('Nuevo texto')
archivo.close()
archivo = open('mi_archivo.txt')
print(archivo.read())"""

"""Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar."""
"""archivo = open('mi_archivo.txt','a')
archivo.write('Nuevo inicio de sesión')
archivo.close()
archivo = open('mi_archivo.txt')
print(archivo.read())"""

"""Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.

  
"""
"""registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

archivo = open('registro.txt','a')

for i in registro_ultima_sesion :
"""

"""
def abrir_leer(ejemplo):
    abrir = open('ejemplo.txt')
    return abrir.read()"""

"""def sobrescribir(ejemplo):
    abrir = open('ejemplo.txt','w')
    return abrir.write("contenido eliminado")"""


"""def registro_error(ejemplo):
    abrir = open('log_errores.txt','a')
    return abrir.write("se ha registrado un error de ejecución")"""