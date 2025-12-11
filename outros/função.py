
''' - Uma função para ler todas as notas de um aluno
      Essa função deve:
            Perguntar quantas notas o aluno possui.
            Criar um laço dentro da função para ler cada nota (uma por vez).
            Armazenar as notas em uma lista.
            Retornar a lista completa.
- Uma função para calcular a média
      Essa função deve receber uma lista de notas e:
            Somar as notas
            Dividir pela quantidade
            Retornar a média
 - Uma função para classificar o aluno
      Ela deve receber a média e retornar:
            “Aprovado” se média ≥ 6
            “Recuperação” se 4 ≤ média < 6
            “Reprovado” se média < 4
 - Uma função principal que usa todas as outras
      Essa função deve:
            Chamar ler_notas()
            Chamar calcular_media()
            Chamar classificar()
            Exibir um relatório assim:
                  Notas: [...]
                  Média: X
                  Situação: Y

 - No final, o programa deve chamar apenas a função principal'''
def notas():
    quant = int(input('Digite a quantidade de notas do aluno: '))
    notas = []

    for i in range(quant):
        notas.append(float(input('Digite a nota do aluno: ')))
        
    return notas
    
def media(notas):
    media = sum(notas) / len(notas)
    return media

def classificar(media):
    if media < 4:
        return('Reprovado')
    elif media >= 4 and media < 6:
        return('Recuperação')
    else:
        return('Aprovado')

def principal():
    ler_notas = notas()
    chamar_media = media(ler_notas)
    chamar_classif = classificar(chamar_media)
    
    print(f'Notas do aluno: {ler_notas}\nMédia do Aluno: {chamar_media}\nSituação do aluno: {chamar_classif}')

principal()