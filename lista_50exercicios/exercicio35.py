# Leia um código de operação bancária (depósito, saque, extrato, sair) e exiba apenas mensagens simulando a operação.

print('--- CAIXA ELETRÔNICO ---')
print('1 - Depósito')
print('2 - Saque')
print('3 - Extrato')
print('4 - Sair')

codigo = int(input('Digite o código da operação desejada: '))

if codigo == 1:
    print('\nIniciando Depósito...')
    print('Por favor, insira o envelope no local indicado.')

elif codigo == 2:
    print('\nIniciando Saque...')
    print('Aguarde a contagem das notas...')
    print('Retire seu dinheiro.')

elif codigo == 3:
    print('\nGerando Extrato...')
    print('Saldo atual: R$ 1.500,00 (Simulação)')
    print('Última compra: Padaria Pão Bom - R$ 15,00')

elif codigo == 4:
    print('\nEncerrando sessão...')
    print('Obrigado por usar nosso banco. Retire seu cartão.')

else:
    print('\nErro: Código inválido!')