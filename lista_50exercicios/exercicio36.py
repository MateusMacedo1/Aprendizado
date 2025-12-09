#Leia um número inteiro digitado pelo usuário e garanta que ele só avance quando o número for válido.
while True:
    try:
        numero = int(input('Digite um número inteiro: '))
        
        print('Número aceito!')
        break
        
    except ValueError:
        print('Erro: Isso não é um número inteiro. Tente novamente.\n')

print(f'O número digitado foi: {numero}')