revistas = []
vendas = []
opt = 1

while opt != 0:
    print('Banca Do Aloir')
    print('1 - Cadastrar revista')
    print('2 - Registrar venda')
    print('3 - Autoatendimento')
    print('4 - Gerar relatório diário')
    print('5 - Sair')
    
    opt = int(input('Digite a opção: '))

    match opt:
        case 1:
            print('Novo Cadastro')
            titulo = input('Título da Revista: ')
            categoria = input('Categoria: ')
            preço = float(input('Preço R$: '))
            
            revistas.append({'Titulo': titulo, 'Categoria': categoria, 'Preço': preço})
            print('Revista cadastrada com sucesso!')

        case 2:
            print('Registrar Venda')
            busca = input('Qual revista foi vendida? ')
            
            encontrou = 0
            
            for item in revistas:
                if item.get('Titulo') == busca:
                    
                    print('Revista encontrada:', item.get('Titulo'), '| Preço: R$', item.get('Preço'))
                    
                    qtd = int(input('Quantidade vendida: '))
                    data = input('Data (dd/mm): ')
                    
                    total_venda = item.get('Preço') * qtd
                    
                    vendas.append({
                        'Revista': item.get('Titulo'),
                        'Qtd': qtd,
                        'Total': total_venda,
                        'Data': data
                    })
                    
                    print('Venda registrada! Total: R$', total_venda)
                    
                    encontrou = 1
            
            if encontrou == 0:
                print('Revista não encontrada.')

        case 3:
            print('Autoatendimento')
            print('Revistas Disponíveis:')
            for item in revistas:
                print('-', item.get('Titulo'), 'R$', item.get('Preço'))
            
            escolha = input('Digite o nome da revista que deseja comprar: ')
            
            encontrou = 0
            
            for item in revistas:
                if item.get('Titulo') == escolha:
                    print('Preço unitário: R$', item.get('Preço'))
                    qtd = int(input('Quantas unidades? '))
                    
                    total_pagar = item.get('Preco') * qtd
                    
                    print('Valor a pagar: R$', total_pagar)
                    confirmar = input('Confirmar compra? (S/N): ')
                    
                    if confirmar == 'S':
                        vendas.append({
                            'Revista': item.get('Titulo'), 'Qtd': qtd, 'Total': total_pagar, 'Data': 'Hoje'})
                        print('Compra realizada!')
                    else:
                        print('Compra cancelada.')
                    
                    encontrou = 1
            
            if encontrou == 0:
                print('Revista não encontrada.')

        case 4:
            print('Relatório do dia')
            faturamento = 0
            itens_vendidos = 0
            
            for v in vendas:
                print(v.get('Data'), '|', v.get('Revista'), '| Qtd:', v.get('Qtd'), '| Total: R$', v.get('Total'))
                
                faturamento = faturamento + v.get('Total')
                itens_vendidos = itens_vendidos + v.get('Qtd')
            
            print('Total itens vendidos:', itens_vendidos)
            print('Lucro do dia: R$', faturamento)

        case 5:
            print('Sair')