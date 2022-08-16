from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/ivett/OneDrive/Escritorio/python/funciones/Dia 6/prueba.txt')
#ahora carpeta es un objeto path por lo tanto se puede
# acceder a otros
#metodos
#con esto se evita el open y el close
print(carpeta.read_text())
print(carpeta.name) #extrae el nombre del archivo
print(carpeta.suffix) #muestra el formato del archivo
print(carpeta.stem) #nos da el nombre sin la terminacion

#corroborar sin un archivo existe

if not carpeta.exists():
    print('este archivo no existe')
else:
    print('genial existe')

""" prubea de pure importar
ruta de window pura"""

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)