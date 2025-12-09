# Crie um menu com as opções: cadastrar usuário, listar usuários, remover usuário e sair. Trate cada opção com seleção múltipla.

usuarios = []

while True:
    print('1. Cadastrar usuário')
    print('2. Listar usuários')
    print('3. Remover usuário')
    print('4. Sair')
    print('='*20)

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Digite o nome para adicionar: ')
        usuarios.append(nome)
        print(f'Sucesso! {nome} foi cadastrado.')

    elif opcao == '2':
        if len(usuarios) > 0:
            print(f'Lista atual: {usuarios}')
        else:
            print('A lista está vazia.')

    elif opcao == '3':
        nome = input('Digite o nome para remover: ')
        
        if nome in usuarios:
            usuarios.remove(nome)
            print('Usuário removido.')
        else:
            print('Erro: Usuário não encontrado.')

    elif opcao == '4':
        print('Encerrando o sistema...')

    else:
        print('Opção inválida! Digite apenas 1, 2, 3 ou 4.')