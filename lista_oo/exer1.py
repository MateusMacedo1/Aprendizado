# 1) Crie a classe Pessoa com atributos nome e idade.
# Crie o método apresentar() que retorna uma frase tipo: “Olá, eu sou ___ e tenho ___ anos”.
# Na main, crie 2 pessoas e imprima a apresentação de cada uma.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'Olá, eu sou {self.nome} e tenho {self.idade} anos.'

def main():
    p1 = Pessoa('Danilo', 25)
    p2 = Pessoa('Ana', 22)

    print(p1.apresentar())
    print(p2.apresentar())

main()