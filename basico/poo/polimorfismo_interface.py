class Forma():
    
    def area(self):
        pass
    
class Quadrado(Forma):
    
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
class Circulo(Forma):
    
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * self.raio ** 2
        

quadrado = Quadrado(5)
area_do_quadrado = quadrado.area()
print(area_do_quadrado)

quadrado2 = Quadrado(7)
area_do_quadrado2 = quadrado2.area()
print(area_do_quadrado2)

circulo = Circulo(4)
area_do_circulo = circulo.area()
print(area_do_circulo)

circulo2 = Circulo(6)
area_do_circulo2 = circulo2.area()
print(area_do_circulo2)