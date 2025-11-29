biblioteca = []
opt = 1

while opt != 0:
    print('Biblioteca do Julios')
    print('1 - Cadastrar livro')
    print('2 - Buscar por nome')
    print('3 - Buscar por autor')
    print('4 - Buscar por gênero')
    print('5 - Listar todos')
    print('6 - Marcar como lido')
    print('7 - Sair')
    
    opt = int(input('Digite a Opção: '))
    
    match opt:
        case 1:
            print('Cadastrar livro')
            nome = str(input('Nome: '))
            autor = str(input('Autor: '))
            genero = str(input('Gênero: '))
            ano = int(input('Ano: '))
            
            biblioteca.append({'Nome': nome, 'Autor': autor, 'Genero': genero, 'Ano': ano, 'Status': 'Não lido'})
            print('Livro cadastrado!')

        case 2:
            buscar = str(input('Digite o nome do livro: '))
            encontrou = 0
            
            for item in biblioteca:
                if item.get('Nome') == buscar:
                    print('Livro encontrado:', item.get('Nome'), '| Autor:', item.get('Autor'), '| Status:', item.get('Status'))
                    encontrou = 1
            
            if encontrou == 0:
                print('Livro não encontrado.')

        case 3:
            buscar = str(input('Buscar por autor: '))
            encontrou = 0
            
            for item in biblioteca:
                if item.get('Autor') == buscar:
                    print('Livro:', item.get('Nome'), '| Ano:', item.get('Ano'))
                    encontrou = 1
            
            if encontrou == 0:
                print('Autor não encontrado.')

        case 4:
            buscar = input('Buscar por gênero: ')
            encontrou = 0
            
            for item in biblioteca:
                if item.get('Genero') == buscar:
                    print('Livro:', item.get('Nome'), '| Autor:', item.get('Autor'))
                    encontrou = 1
            
            if encontrou == 0:
                print('Gênero não encontrado.')

        case 5:
            print('Lista Completa')
            for item in biblioteca:
                print(item.get('Nome'), '|', item.get('Autor'), '|', item.get('Genero'), '|', item.get('Status'))
 
        case 6:
            nome = input('Digite o nome do livro que você leu: ')
            encontrou = 0
            
            for item in biblioteca:
                if item.get('Nome') == nome:
                    item['Status'] = 'Lido'
                    print('Pronto! O livro', item.get('Nome'), 'foi marcado como LIDO.')
                    encontrou = 1
            
            if encontrou == 0:
                print('Livro não encontrado na lista.')
       
        case 7:    
            print('Sair')