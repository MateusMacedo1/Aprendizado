def palavras():
    quant = int(input('Digite a quantidade de palavras do aluno: '))
    palavras = []
    for i in range(quant):
        palavras.append(str(input('Digite as palavras do aluno: ')))
        
    return palavras
    

def principal():
    vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'ô', 'ã', 'õ']
    
    ler_palavras = palavras() 
    
    contagem_vogais = 0
    for palavra in ler_palavras:
        for letra in palavra:
            if letra.lower() in vogais:
                contagem_vogais += 1

    if ler_palavras:
        palavra_longa = max(ler_palavras)
    else:
        palavra_longa = "Nenhuma"

    print(f'Você digitou essas palavras: {ler_palavras}')
    print(f'A palavra maior é: {palavra_longa}')
    print(f'Total de {contagem_vogais} vogais.')

principal()