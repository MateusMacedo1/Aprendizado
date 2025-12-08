#Leia uma senha e continue pedindo-a até que o usuário digite a senha correta,
# informando ao final quantas tentativas foram realizadas.
senha = '1234'
tentativas = 0

while True:
    senha_digitada = input('Digite a senha: ')
    tentativas += 1

    if senha_digitada == senha:
        print('Senha correta')
        break
    else:
        print('Senha incorreta. Tente novamente.')

print(f'Total de tentativas realizadas: {tentativas}')