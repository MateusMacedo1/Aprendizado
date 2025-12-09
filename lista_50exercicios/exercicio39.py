# Leia um nome de arquivo informado pelo usuário e trate o caso de o arquivo não existir, exibindo uma mensagem adequada.

nome_arquivo = input("Digite o nome do arquivo para abrir (ex: lista.txt): ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        print(f"Sucesso! O arquivo '{nome_arquivo}' foi aberto.")
        
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não existe nesta pasta!")

except PermissionError:
    print("Erro: Você não tem permissão para ler este arquivo.")