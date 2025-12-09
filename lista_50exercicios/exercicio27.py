# Leia uma frase e exiba todas as palavras em ordem alfabética.

frase = input('Digite uma frase: ')
palavras = frase.split()

palavras.sort()

print(f'Palavras ordenadas: {palavras}')