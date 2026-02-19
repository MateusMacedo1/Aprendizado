# 2) Crie a classe ContaBancaria com atributos titular e saldo (começa em 0).
# Crie métodos: depositar(valor) e sacar(valor) (só saca se tiver saldo).
# Na main, crie uma conta, faça 2 depósitos e 1 saque, e mostre o saldo final.

class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f'Depósito de R$ {valor} realizado!')

    def sacar(self, valor):
        self.saldo = self.saldo - valor
        print(f'Saque de R$ {valor} realizado!')


def main():
    conta = ContaBancaria('Mateus')
    conta.depositar(100)
    conta.depositar(50)
    conta.sacar(30)

    print(f'Saldo do {conta.titular}: R$ {conta.saldo}')

main()