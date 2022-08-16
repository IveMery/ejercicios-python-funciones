#atributos de clase
#atributos de instancia
#cosntructor  __init__(self)
#argumento pocisional color
class Pajaro:
    volar = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
        
        
pajaro1 = Pajaro("rojo","Tucan") #instancia de la clase pajaro con atributos de instancia pasadas directamente desde instancia

print(f'El Pajaro {pajaro1.especie}  y es de color {pajaro1.color} ')  
print(Pajaro.volar)#atributo de clase
print(pajaro1.volar) #atributo de clase


class Casa:
    def __init__(self,color,cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
    
casa_blanca = Casa('blanco',4)


class Cubo:
    caras = 6
    def __init__(self,color):
        self.color = color
        
cubo_rojo = Cubo('rojo')

class Personaje:
    real = False
    def __init__(self,especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad =edad
        
harry_potter =Personaje('Humano',True,17) 