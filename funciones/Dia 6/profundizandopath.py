from pathlib import Path

"""base = Path.home()
guia = Path(base,"Europa" ,"Espania",Path("Barcelona","Sagrada_familia.txt"))
# print(base)
print(guia)
print(guia.parent.parent.parent)
guia2 = guia.with_name("la_pedrera.txt")
print(guia2)
"""

guia = Path(Path.home(),"Europa")

for txt in Path(guia).glob('*.txt'):
    print(txt) # esto esta en el directorio europa por eso
    #muestra esos dos archivos

#para que muestre todos los archivos txt en las otras carpetas
#de europa se usa:

for txt in Path(guia).glob('**/*.txt'):
    print(txt)

    #asi muestras los archivos en los subdirectorios de
    #carpeta


#relative to
guia = Path("Europa","Espania","Barcelona","Sagrada_familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa,Espania"))
print(en_europa)
print(en_espania)


