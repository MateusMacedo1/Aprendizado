#Simule um sistema de login que exige que nome de usuário e senha não sejam vazios,
# repetindo a solicitação enquanto necessário.


while True:

    usuario = input('Crie seu nome de usuário: ').strip()
    senha = input('Crie sua senha: ').strip()
    

    if usuario == '' or senha == '':
        print('>>> Erro: Todos os campos são obrigatórios! Tente novamente.\n')
    
    else:
        print(f'Cadastro realizado com sucesso! Bem-vindo, {usuario}.')
        break