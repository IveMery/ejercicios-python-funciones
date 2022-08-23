#metodos funciones para q haga algo

class Pajaro:
    alas = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
        
    #metodos
    def piar(self):
        print('pio')
        print(f'pio ,mi color es {self.color}')
        
    def volar(self,metros):
        print(f'El pajaro se ha movido {metros} metros')
      
       
piolin = Pajaro('amarillo','canario')

piolin.piar() 
piolin.volar(10)
  
#Que ladre el perro      
class Perro:
    def ladrar(self):
        print('Guau!')

perro1 = Perro()    

#lanzar hechizo
class Mago:
    def lanzar_hechizo(self):
        print('¡Abracadabra!')
        
merlin = Mago()  

##metodo de clase postergar
class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
        
alarma1 = Alarma()        