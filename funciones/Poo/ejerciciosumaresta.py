class Operaciones:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def suma(self):
        return self.num1 + self.num2
    def resta(self):
        return self.num1 - self.num2
    
instancia1 = Operaciones(3,7)
print(instancia1.suma())        
print(instancia1.resta())
instancia2 = Operaciones (5,3)
print(instancia2.suma())