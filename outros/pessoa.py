class pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def andar(self):
        print(f'{self.nome} está andando')

    def atacar(self):
        print(f'A pessoa {self.nome} de {self.idade}')