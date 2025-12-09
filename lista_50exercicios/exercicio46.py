#Leia uma frase e determine o número de palavras, a maior palavra e a menor palavra em termos de tamanho.
frase = input("Digite uma frase: ")

palavras = frase.split()

if len(palavras) > 0:
    
    maior = max(palavras, key=len)
    menor = min(palavras, key=len)
    
    print(f"Total de palavras: {len(palavras)}")
    print(f"Maior palavra:'{maior}' ({len(maior)} letras)")
    print(f"Menor palavra:'{menor}' ({len(menor)} letras)")

else:
    print("Você não digitou nenhuma palavra.")
