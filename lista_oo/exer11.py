class Cronometro:
    def __init__(self):
        self.segundos = 0

    def tic(self):
        self.segundos = self.segundos + 1
        print("Tic...")

    def avancar(self, n):
        self.segundos = self.segundos + n
        print(f"Avançando {n} segundos.")

    def zerar(self):
        self.segundos = 0
        print("Cronômetro zerado!")

def main():
    meu_relogio = Cronometro()
    meu_relogio.tic()
    meu_relogio.tic()
    meu_relogio.tic()
    meu_relogio.avancar(30)
    meu_relogio.zerar()
    meu_relogio.avancar(10)
    print(f"\nTempo final marcado: {meu_relogio.segundos} segundos")

main()