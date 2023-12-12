class Celular:
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = 'Não'
    bateria = 'Infinita'

    def fazer_ligacao(self):
        print('Fazendo ligação ...')

    def jogar_cobrinha(self):
        print('Jogando cobrinha')

    def despertador(self):
        print('Despertador')
        
    def calcular(self, valor_1, valor_2):
        return valor_1 + valor_2

celular = Celular()
#print(f'Marca ... {celular.marca}')
#print(f'Modelo ... {celular.modelo}')
#print(f'Bateria ... {celular.bateria}')
#print(f'Tem camera ... {celular.tem_camera}')

#celular.fazer_ligacao()
#celular.jogar_cobrinha()
#celular.despertador()

calculo = celular.calcular(2,3)
print(calculo)

