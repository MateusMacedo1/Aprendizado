biblioteca = []
opt = 1
while opt != 7:
    opt = int(input("Menu da biblioteca \n 01 - Cadastrar Livro \n 02 - Buscar por Nome \n 03 - Buscar pelo autor \n 04 - Buscar por gênero \n 05 - Listar todos \n 06 - Marcar como lido \n 07 - Sair \n Digite a Opção: "))     
    
    match opt:
        case 1:
            print("Cadastrar livro")
            nome = str(input('Nome: '))
            autor = str(input('Autor: '))
            genero = str(input('Gênero: '))
            ano = int(input('Ano: '))
            status = str(input('Status: '))
            biblioteca.append({'Nome': nome, 'Autor': autor, 'Gênero': genero, 'Ano': ano,'Status': status})
        case 2:
            buscar = input('Digite o nome do livro:' )
            for nome in biblioteca:
                if nome.get('Nome') == buscar :
                    print('livros encontrados: ', nome)
                else:
                    print('Livro não encontrado')
        case 3:
            buscar = input('Buscar por autor: ')
            for autor in biblioteca:
                if autor.get('Autor') == buscar :
                    print('Livro encontrados: ', autor)
                else:
                    print('livro não encontrado')
        case 4:
            buscar = input('Buscar por gênero: ')
            for genero in biblioteca:
                if genero.get('gênero') == buscar :
                    print('Livro encontrado: ', genero)
                else:
                    print('Livro não encontrado')
        case 5:
            print(biblioteca)

        case 6:
            nome = str(input('Digite o nome do livro: '))
            for i,j in enumerate(biblioteca):
                if j.get("Nome") == nome:
                    print("Nome do livro: ", j.get("Nome"))
            status = int(input("1 - Lido\n2 - Não lido\nDigite a opcão: "))
            leu = "Lido" if status == 1 else "Não lido"
            biblioteca[i]['Status'] = leu
        
        case 7:    
            print('Sair')