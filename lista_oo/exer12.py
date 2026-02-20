class Pedido:
    def __init__(self):
        self.precos = []
        self.nomes = []

    def adicionar_item(self, nome, preco):
        self.nomes.append(nome)
        self.precos.append(preco)
        print(f"Item adicionado: {nome} - R$ {preco}")

    def total(self):
        resultado = sum(self.precos)
        print(f"O valor total do pedido é: R$ {resultado}")

def main():
    meu_pedido = Pedido()

    meu_pedido.adicionar_item("Hambúrguer", 25.00)
    meu_pedido.adicionar_item("Batata Frita", 12.00)
    meu_pedido.adicionar_item("Refrigerante", 8.00)
    meu_pedido.adicionar_item("Sorvete", 10.00)
    meu_pedido.total()

main()