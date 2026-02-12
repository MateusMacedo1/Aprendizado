from Animal import animal
nome = (input('Digite um nome: '))
peso = int(input('Digite a peso: '))
raca = (input('Digite o raça: '))

opt = int(input('Animais \n 01 - Ele Pula? \n 02 - Ele voa? \n 03 - Ele nada? \n 04 - Sair \n Digite a Opeção: '))     
    
match opt:
        case 1:
            animal1 = animal(nome, peso, raca)
            animal1.pular()

        case 2:
            animal1 = animal(nome, peso, raca)
            animal1.voar()

        case 3:
            animal1 = animal(nome, peso, raca)
            animal1.nadar()
        case 4:
            print('Nenhuma alternativa')