# Saldos
saldo_da_conta = float(input('Insire o valor do saldo inicial R$: '))
saldo_devedor = 0.00
saldo_investido = 0.00
saldo_poupança = 0.00
#juros
juros_emprestimo = 0.10
poupança = 0.005
juros_investimento = 0.01
#opçoes
print('Saldo inicial: R$' , saldo_da_conta)
print('Escolha a opção a seguir:')
print('1 - para Depósito (Crédito)')
print('2 - para Efetuar pagamento (Débito)')
print('3 - para Efetuar saque (Débito)')
print('4 - para realizar um Emprestimo')
print('5 - para realizar um Investimento')
print('6 - para depositar na Poupança')
print('7 - Para cancelar operação')

Opção = int(input('Digite a opção de 1 a 7: ', ))

if Opção == 1:
    valor = float(input('Digite o valor do déposito: R$ '))
    if valor >= 0:
        saldo_da_conta = saldo_da_conta + valor
    print('Saldo atualizado de R$' , saldo_da_conta, 'realizado com sucesso')


elif Opção == 2:
    valor = float(input('Digite o valor do pagamento (débito): R$ '))
    if valor > 0 and saldo_da_conta >= valor:
        saldo_da_conta = saldo_da_conta - valor
        print('Pagamento de R$' , valor, 'Realizado com sucesso')
        print('Saldo foi atualizado para R$' , saldo_da_conta)
    elif valor <= 0:
        print('Pagamento invalido')
    else:
        print('Saldo insuficiente')

elif Opção == 3:
    valor = float(input('Digite o valor do saque (débito): R$ '))
    if valor > 0 and saldo_da_conta >= valor:
        saldo_da_conta = saldo_da_conta - valor
        print('Saque realizado de R$' , valor, 'Realizado com sucesso')
        print('Saldo foi atualizado para R$' , saldo_da_conta)
    elif valor <= 0:
        print('Saque invalido')
    else:
        print('Saldo insuficiente')
   
elif Opção == 4:
    valor_emprestimo = float(input('Digite o valor do emprestimo: R$ '))
    parcela = int(input('Digite de 1 a 12 quanto deseja parcelar: '))
    if valor_emprestimo > 0:
        juros = valor_emprestimo * juros_emprestimo * parcela
        valor_emprestimo = valor_emprestimo + juros
    print('Emprestimo contratado com sucesso, valor total a pagar: R$ ', valor_emprestimo, "\n"'Sua parcela ficará ao mês no valor de: R$ ', valor_emprestimo / parcela)

elif Opção == 5:
    saldo_investido = float(input('Digite o valor para investir: R$ '))
    if saldo_investido > 0:
        juros = saldo_investido * juros_investimento
        saldo_investido = saldo_investido + juros
    print('Retorno do investimento de R$' , saldo_investido)
    print('Saldo foi atualizado para R$' , saldo_da_conta + saldo_investido)

elif Opção == 6:
    saldo_poupança = float(input('Digite o valor para poupança: R$ '))
    if saldo_poupança > 0:
        juros = saldo_poupança * poupança
        saldo_poupança = saldo_poupança + juros
    print('Poupança de R$' , saldo_poupança, 'realizado com sucesso')
    print('Saldo foi atualizado para R$' , saldo_da_conta + saldo_poupança)

elif Opção == 7:
    print('Operação finalizadada')