#metodos funciones para q haga algo

class Pajaro:
    alas = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
        
    #metodos
    def piar(self):
        print('pio')
        
    def volar(self,metros):
        print(f'El pajaro se ha movido {metros} metros')
      
       
piolin = Pajaro('amarillo','canario')

piolin.piar() 
piolin.volar(10)
      
