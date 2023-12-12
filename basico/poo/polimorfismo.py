class Animal:
    
    def emitir_som(self):
        print('Qual quer som ...')
        
class Cachorro(Animal):
    
    def emitir_som(self):
        print('Au Au!')

class Gato(Animal):
    
    def emitir_som(self):
        print('Miau!')

cachorro = Cachorro()
cachorro.emitir_som()

gato = Gato()
gato.emitir_som()
