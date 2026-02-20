# 6) Crie a classe Aluno com atributos nome, nota1, nota2.
# Crie métodos media() e situacao() (>= 7 aprovado, senão reprovado).
# Na main, crie 3 alunos e mostre média e situação.

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        m = (self.nota1 + self.nota2) / 2
        print(f'A média do {self.nome} é {m}')

    def situacao(self):
        if (self.nota1 + self.nota2) / 2 >= 7:
            print('Aprovado')
        else:
            print('Reprovado')

def main():
    a1 = Aluno('João', 8, 7)
    a2 = Aluno('Maria', 5, 6)
    a3 = Aluno('José', 10, 9)

    a1.media()
    a1.situacao()
    
    a2.media()
    a2.situacao()
    
    a3.media()
    a3.situacao()

main()