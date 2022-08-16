def describir_persona(nombre,**kwargs):
    print(f"Características de {nombre}:")
    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")
       
        
print(describir_persona("Sam",color_ojos ='Azules',color_pelo="rubius"))
    