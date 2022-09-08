#tipos de metodos
#Decoradores
#metodos de instancia o normales son
#loque contienen self
#acceden y modifican los atributos del objeto
#acceden a otros metodos
#pueden modificar el estado de la clase

    

#metodos de clase @classmethod
# def mi_metodo(cls):
    #print(algo)

    

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
piolin.volar(10)

#metodos de nstancias afecatn a self

