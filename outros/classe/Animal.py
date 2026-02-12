class animal:
    def __init__(self, nome, peso, raca):
        self.nome = nome
        self.peso = peso
        self.raca = raca
    def pular(self):
        print(f'O animal {self.nome} pode pular')
    
    def voar(self):
        print(f'O animal {self.nome} pode Voar')

    def nadar(self):
        print(f'O animal {self.nome} pode nadar')