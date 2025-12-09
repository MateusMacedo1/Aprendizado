#Leia várias frases digitadas pelo usuário e ao final exiba quantas foram digitadas,
# quantos caracteres foram registrados e qual frase foi a mais longa,
# além de contar quantas vezes uma palavra-chave aparece no conjunto das frases.

frases = []

print("Digite 'sair' para encerrar a coleta.")

while True:
    texto = input("Digite uma frase: ").strip()
    
    if texto.lower() == 'sair':
        break
    
    if texto != "":
        frases.append(texto)

if len(frases) > 0:
    
    chave = input("\nQual palavra-chave você quer contar? ").strip()
    
    total_caracteres = 0
    ocorrencias_chave = 0
    
    for frase in frases:
        total_caracteres += len(frase)
        
        ocorrencias_chave += frase.lower().count(chave.lower())

    frase_longa = max(frases, key=len)

    print(f"Total de frases: {len(frases)}")
    print(f"Total de caracteres: {total_caracteres}")
    print(f"A palavra '{chave}' apareceu: {ocorrencias_chave} vezes")
    print(f"Frase mais longa: {frase_longa}")
    print(f"(Com {len(frase_longa)} caracteres)")

else:
    print("Nenhuma frase foi registrada.")