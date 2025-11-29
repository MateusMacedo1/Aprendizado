# Até 11 anos → Criança
# Entre 12 e 17 anos → Adolescente
# Entre 18 e 59 anos → Adulto
# 60 + → Idoso
try:
    print(10 * '_', 'DADOS DE IDADE', 10 * '_')
    idade = int(input('Digite sua idade: '))
    
    if idade >= 0 and idade <= 11:
        print('Criança')
   
    elif idade >= 12 and idade <= 17:
        print('Adolescente')
            
    elif idade >= 18 and idade <= 59:
        print('Adulto')
            
    elif idade >= 60 and idade <= 120:
        print('Idoso') 
    else:
            print('dado incorreto')

except ValueError:
    print('Dado incorreto')

