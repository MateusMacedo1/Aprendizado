#5) Crie a classe Carro com atributos modelo e velocidade (inicia em 0).
#Crie métodos acelerar(valor) e frear(valor) (não pode ficar negativo).
#Na main, simule uma sequência de acelerações e freadas e mostre a velocidade.

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f'Acelerando em: {self.velocidade} km/h')

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f'Freando em: {self.velocidade} km/h')

def main():
    meu_carro = Carro('Gol')
    meu_carro.acelerar(50)
    meu_carro.acelerar(20)
    meu_carro.frear(30)
    meu_carro.frear(60)

    print(f'Velocidade final do {meu_carro.modelo}: {meu_carro.velocidade} km/h')

main()