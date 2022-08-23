#tipos de metodos
#Decoradores
#metodos de instancia

    

#metodos de clase @classmethod


#metodos estaticos @staticmethod
#no aceptan parametros ni self ni cls
#un metodo no podra modificar estados de la clase

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
    
    def pintar_negro(self):
        self.color = 'negro'
        print(f'ahora el pajaro es {self.color}') 
#accede y modifica los atributos del objeto

piolin = Pajaro('amarillo','canario')
piolin.pintar_negro()

#metodos de nstancias afecatn a self

