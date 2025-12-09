#Leia nome e idade de várias pessoas até que o usuário decida encerrar. Desconsidere idades inválidas.

pessoas = []

print("--- CADASTRO DE PESSOAS ---")
print("Digite 'sair' no nome para encerrar.")

while True:
    nome = input("\nNome: ")
    
    if nome.lower() == 'sair':
        break

    try:
        idade = int(input("Idade: "))
        
        if idade < 0 or idade > 150:
            print("Idade inválida! Esse cadastro será ignorado.")
            continue 
            
        pessoas.append([nome, idade])
        print("Cadastro realizado!")

    except ValueError:
        print(">>> Erro: A idade deve ser um número inteiro! Cadastro ignorado.")

print("\n--- LISTA FINAL ---")
for p in pessoas:
    print(f"Nome: {p[0]} | Idade: {p[1]}")