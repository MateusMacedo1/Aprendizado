transações = []
saldo = 0.0
opt = 1

while opt != 0:
    print('Finaceiro da Bretiney')
    print('Saldo: R$', saldo)
    print('1 - Registrar Entrada')
    print('2 - Registrar Saída')
    print('3 - Relatório Mensal')
    print('4 - Sair')
    
    opt = int(input('Digite a opção: '))

    match opt:
        case 1:
            print('Registrar Entrada')
            tipo = input('Recebeu(nome da transação): ')
            valor = float(input('Valor R$: '))
            data = input('Data: ')
            
            transações.append({'Tipo': tipo, 'Valor': valor, 'Data': data, 'Categoria': 'Entrada'})
            
            saldo = saldo + valor 
            print('Entrada registrada')

        case 2:
            print('Registrar Saída')
            tipo = input('Gastou(nome da transação): ')
            valor = float(input('Valor R$: '))
            data = input("Data: ")
            
            if valor > saldo:
                print('Saldo insuficiente. Você só tem R$', saldo)
            else:
                transações.append({'Tipo': tipo, 'Valor': valor, 'Data': data, 'Categoria': 'Saída'})
                
                saldo = saldo - valor
                print("Pagamento registrado.")

        case 3:
            print('Relatório mensal')
            total_entradas = 0
            total_saidas = 0
            
            for item in transações:
                sinal = '+'
                if item.get('Categoria') == 'Saída':
                    sinal = '-'
                
                print(item.get('Data'), '|', item.get('Tipo'), '|', sinal, 'R$', item.get('Valor'))
                
                if item.get('Categoria') == 'Entrada':
                    total_entradas = total_entradas + item.get('Valor')
                else:
                    total_saidas = total_saidas + item.get('Valor')
            
            print('Total Recebido: R$', total_entradas)
            print('Total Gasto: R$', total_saidas)
            print('Saldo: R$', saldo)

        case 4:
            print('Sair')
