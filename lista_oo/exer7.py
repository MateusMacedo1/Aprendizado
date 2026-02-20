#7) Crie a classe Lampada com atributo ligada (começa False).
# Crie métodos ligar(), desligar() e estado() (retorna “Ligada” ou “Desligada”).
# Na main, ligue e desligue algumas vezes e imprima o estado.

class Lampada:
    def __init__(self):
        self.ligada = False

    def ligar(self):
        self.ligada = True
        print('Você apertou o interruptor para ligar.')

    def desligar(self):
        self.ligada = False
        print('Você apertou o interruptor para desligar.')

    def estado(self):
        if self.ligada == True:
            print('A lâmpada está: Ligada')
        else:
            print('A lâmpada está: Desligada')

def main():
    minha_lampada = Lampada()

    minha_lampada.estado()

    minha_lampada.ligar()
    minha_lampada.estado()

    minha_lampada.desligar()
    minha_lampada.estado()

main()