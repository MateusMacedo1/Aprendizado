# Jussara é  professora, ela vai aplicar uma prova mas quer automatizar sua correção.
# Faça um sistema para auxiliar Jussara nas 15 questões de sua prova;

questão1 = input('O Brasil é o maior país da América Latina? ')
match questão1:
    case "Sim":
        print("Certo")
    case "Não":
        print("Errado")
    case _:
        print("Nenhuma das opções")

questão2 = input('O EUA é o pais mais ricos do mundo: ')
match questão2:
    case "Sim":
        print("Certo")
    case "Não":
        print("Errado")
    case _:
        print("Nenhuma das opções")

questão3 = input('Escolha sequencia correta os 3 pais mais ricos do mundo: A. EUA, Alemanha, Japão. B. Japão, Alemanha, EUA: ')
match questão3:
    case "A":
        print("Certo")
    case "B":
        print("Errado")
    case _:
        print("Nenhum das opções")
questão4 = input('A capital da Espanha é Paris.: ')
match questão4:
    case "Não":
        print("Certo")
    case "Sim":
        print("Errado")
    case _:
        print("Nenhum das opções")
questão5 = input('O Brasil é banhado pelo oceano atlantico? ')
match questão5:
    case "Sim":
        print("Certo")
    case "Não":
        print("Errado")
    case _:
        print("Nenhuma das opções")
questão6 = input('O qual é o maior rio do mundo? ')
match questão6:
    case "Rio Amazonas":
        print("Certo")
    case "Rio Eufrates":
        print("Errado")
    case _:
        print("Errado")

questão7 = input('Polônia é o maior país da Europa? ')
match questão7:
    case "Não":
        print("Certo")
    case "Sim":
        print("Errado")
    case _:
        print("Nenhuma das opções")
questão8 = input('O azul possui na Bandeira americana: ')
match questão8:
    case "Sim":
        print("Certo")
    case "Não":
        print("Errado")
    case _:
        print("Nenhuma das opções")

questão9 = input('A capital do Brasil é São Paulo?: ')
match questão9:
    case "Não":
        print("Certo")
    case "Sim":
        print("Errado")
    case _:
        print("Nenhum das opções")

questão10 = input('O Brasil é banhado pelo oceano Pacífico? ')
match questão5:
    case "Não":
        print("Certo")
    case "Sim":
        print("Errado")
    case _:
        print("Errado")

questão11 = input('O qual é o Menor rio do mundo? ')
match questão11:
    case "Rio Roe":
        print("Certo")
    case "Rio Eufrates":
        print("Errado")
    case _:
        print("Errado")

questão12 = input('A capital do Brasil é: ')
match questão12:
    case "Brasilia":
        print("Certo")
    case "Rio de Janeiro":
        print("Errado")
    case _:
        print("Errado")

questão13 = input('A capital da Polônia é: ')
match questão13:
    case "Varsóvia":
        print("Certo")
    case "Cracóvia":
        print("Errado")
    case _:
        print("Errado")

questão14 = input('Digite o ano em que alemanha se rendeu na 2 guerra mundial: ')
match questão14:
    case "1945":
        print("Certo")
    case "1944":
        print("Errado")
    case _:
        print("Errado")

questão15 = input('A cor vermelha está presente na bandeira do Brasil: ')
match questão15:
    case "Não":
        print("Certo")
    case "Sim":
        print("Errado")
    case _:
        print("Errado")

