#Poo
#6 principios
#Herencia/Polimorfismo/Cohesion/Abstraccion/Acoplamiento/Encapsulamiento

#Herencia
#Cuando una clase hereda otra clase
#clase hija hereda la clase desde el padre

class Animal:
    def __init__(self,edad,color):
        self.edad = edad 
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")
        

class Pajaro(Animal):
    pass

print(Pajaro.__bases__)#dice de que clase hereda(bases)
#Animal__subclases__()

piolin = Pajaro(2,'amarilo')
piolin.nacer()
print(piolin.edad)

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
class Alumno(Persona):
    pass

class Mascota:
    def __init__(self,edad,nombre,cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
        
        
class Perro(Mascota):
    pass
    
    
 class Vehiculo:
        def acelerar(self):
        pass
    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass   