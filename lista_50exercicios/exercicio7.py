# Leia o nome de um usuário e a senha,
# compare com valores pré-definidos e informe se o acesso deve ser permitido ou negado.

usuário = input('Digite o usuário: ')
senha = input('Digite o senha: ')

if usuário == 'Mateus' and senha == '1234':
    print('Acesso permitido')
else:
    print('Acesso negado')