import os
from pathlib import Path
#para conocer la ruta con la que estoy trabajando
#ruta = os.getcwd()
#print(ruta)

carpeta = Path('/Users/ivett/OneDrive/Escritorio/python/funciones/Dia 6')
archivo = carpeta / 'Prueba.txt'
mi_archivo = open(archivo)
print(mi_archivo.read())

"""
otra forma resumida

carpeta = Path('/Users/ivett/OneDrive/Escritorio/python/funciones/Dia 6') / 'Prueba.txt'
mi_archivo = open(archivo)
print(mi_archivo.read())"""