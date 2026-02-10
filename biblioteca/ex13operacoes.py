#Crie um arquivo com uma função que valide se um número é positivo.
#Em outro programa, importe essa função e utilize-a para validar vários números digitados pelo usuário.

def funcao(a):
    if a <= 0:
        print('Negativo')
    else:
        print('Positivo')
    return a