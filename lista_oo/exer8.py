# 8) Crie a classe Livro com atributos titulo, autor, qtd (quantidade disponível).
# Crie métodos emprestar() (retorna True/False) e devolver().
# Na main, tente emprestar até acabar e depois devolva e empreste novamente.

class Livro:
    def __init__(self, titulo, autor, qtd):
        self.titulo = titulo
        self.autor = autor
        self.qtd = qtd

    def emprestar(self):
        if self.qtd > 0:
            self.qtd = self.qtd - 1
            print(f'Empréstimo feito! Restam {self.qtd} unidades.')
            return True
        else:
            return False

    def devolver(self):
        self.qtd = self.qtd + 1
        print(f'Livro devolvido! Agora temos {self.qtd} unidades.')

def main():
    meu_livro = Livro('Pé de feijão', 'joao', 2)
    
    meu_livro.emprestar()
    meu_livro.emprestar()
    meu_livro.emprestar()
    meu_livro.devolver()
    meu_livro.emprestar()

main()