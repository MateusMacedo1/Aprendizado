# Jussara é  professora, ela vai aplicar uma prova mas quer automatizar sua correção.
# Faça um sistema para auxiliar Jussara nas 15 questões de sua prova;

questão1 = input('01 - O Brasil é o maior país da América Latina? ')
questão2 = input('02 - O EUA é o pais mais ricos do mundo: ')
questão3 = input('03 - Escolha sequencia correta os 3 pais mais ricos do mundo: A. EUA, Alemanha, Japão. B. Japão, Alemanha, EUA: ')
questão4 = input('04 - A capital da Espanha é Paris.: ')
questão5 = input('05 - O Brasil é banhado pelo oceano atlantico? ')
questão6 = input('06 - O qual é o maior rio do mundo? ')
questão7 = input('07 - Polônia é o maior país da Europa? ')
questão8 = input('08 - O azul possui na Bandeira americana: ')
questão9 = input('09 - A capital do Brasil é São Paulo?: ')
questão10 = input('10 - O Brasil é banhado pelo oceano Pacífico? ')
questão11 = input('11 - O qual é o Menor rio do mundo? ')
questão12 = input('12 - A capital do Brasil é: ')
questão13 = input('13 - A capital da Polônia é: ')
questão14 = input('14 - Digite o ano em que alemanha se rendeu na 2 guerra mundial: ')
questão15 = input('15 - A cor vermelha está presente na bandeira do Brasil: ')


questão1 = input('O Brasil é o maior país da América Latina? ')
match questão1:
    case "Sim":
        print("Certo")
    case "Não":
        print("Errado")
    case _:
        print("Nenhuma das opções")

match questão2:
    case "Sim":
        print("Certo")
    case "Não":
        print("Errado")
    case _:
        print("Nenhuma das opções")

match questão3:
    case "A":
        print("Certo")
    case "B":
        print("Errado")
    case _:
        print("Nenhum das opções")

match questão4:
    case "Não":
        print("Certo")
    case "Sim":
        print("Errado")
    case _:
        print("Nenhum das opções")

match questão5:
    case "Sim":
        print("Certo")
    case "Não":
        print("Errado")
    case _:
        print("Nenhuma das opções")

match questão6:
    case "Rio Amazonas":
        print("Certo")
    case "Rio Eufrates":
        print("Errado")
    case _:
        print("Errado")

match questão7:
    case "Não":
        print("Certo")
    case "Sim":
        print("Errado")
    case _:
        print("Nenhuma das opções")

match questão8:
    case "Sim":
        print("Certo")
    case "Não":
        print("Errado")
    case _:
        print("Nenhuma das opções")

match questão9:
    case "Não":
        print("Certo")
    case "Sim":
        print("Errado")
    case _:
        print("Nenhum das opções")

match questão10:
    case "Não":
        print("Certo")
    case "Sim":
        print("Errado")
    case _:
        print("Errado")

match questão11:
    case "Rio Roe":
        print("Certo")
    case "Rio Eufrates":
        print("Errado")
    case _:
        print("Errado")

match questão12:
    case "Brasilia":
        print("Certo")
    case "Rio de Janeiro":
        print("Errado")
    case _:
        print("Errado")

match questão13:
    case "Varsóvia":
        print("Certo")
    case "Cracóvia":
        print("Errado")
    case _:
        print("Errado")

match questão14:
    case "1945":
        print("Certo")
    case "1944":
        print("Errado")
    case _:
        print("Errado")

match questão15:
    case "Não":
        print("Certo")
    case "Sim":
        print("Errado")
    case _:
        print("Errado")
