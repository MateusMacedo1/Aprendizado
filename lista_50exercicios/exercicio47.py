#Leia nomes completos de várias pessoas e ao final exiba quantas foram cadastradas,
# quantas começam com uma letra informada e a lista ordenada alfabeticamente.
nomes = []

print("Digite 'sair' para encerrar.")

while True:
    entrada = input("Digite o nome completo: ").strip()
    
    if entrada.lower() == 'sair' or entrada == "":
        break
    
    nomes.append(entrada.title())

if len(nomes) > 0:
    
    letra_chave = input("\nQual letra você quer contar? ").strip().upper()
    
    nomes.sort()
    
    contador_letra = 0
    for nome in nomes:
        if nome.upper().startswith(letra_chave):
            contador_letra = contador_letra + 1

    print(f"Total de cadastros:  {len(nomes)}")
    print(f"Nomes com a letra '{letra_chave}': {contador_letra}")
    
    for nome in nomes:
        print(f"-> {nome}")

else:
    print("Nenhum nome foi cadastrado.")