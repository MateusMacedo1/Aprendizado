class Televisao:
    def __init__(self):
        self.canal = 1
        self.volume = 10

    def aumentar_volume(self):
        self.volume = self.volume + 1
        print(f"Volume aumentado para: {self.volume}")

    def diminuir_volume(self):
        self.volume = self.volume - 1
        print(f"Volume diminuído para: {self.volume}")

    def trocar_canal(self, novo_canal):
        self.canal = novo_canal
        print(f"Canal trocado para: {self.canal}")

def main():
    minha_tv = Televisao()
    minha_tv.aumentar_volume()
    minha_tv.aumentar_volume()
    minha_tv.diminuir_volume()
    minha_tv.trocar_canal(5)
    minha_tv.trocar_canal(12)

    print(f"Canal atual: {minha_tv.canal}")
    print(f"Volume atual: {minha_tv.volume}")

main()