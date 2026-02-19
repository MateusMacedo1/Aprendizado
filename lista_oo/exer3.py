#3) Crie a classe Produto com atributos nome, preco.
# Crie o método aplicar_desconto(percentual) que reduz o preço.
# Na main, crie 3 produtos e aplique descontos diferentes, mostrando o preço final.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, desconto):
        self.preco = self.preco - (self.preco * desconto / 100)


def main():
    p1 = Produto('Camiseta', 100)
    p2 = Produto('Calça', 200)
    p3 = Produto('Tênis', 300)
    p1.aplicar_desconto(10) 
    p2.aplicar_desconto(20)
    p3.aplicar_desconto(50)

    print(f'Produto: {p1.nome} - Novo Preço: R$ {p1.preco} \n Produto: {p2.nome} - Novo Preço: R$ {p2.preco} \n Produto: {p3.nome} - Novo Preço: R$ {p3.preco}')
main()