# Leia a idade de uma pessoa e classifique-a em:
# criança (0–11), adolescente (12–17), adulto (18–59) ou idoso (60+).
# Se a idade for negativa ou maior que 120, informe que a idade é inválida.

try:
    idade = int(input('Digite a idade: '))
    
    if idade >= 0 and idade <= 11:
        print('Criança')
   
    elif idade >= 12 and idade <= 17:
        print('Adolescente')
            
    elif idade >= 18 and idade <= 59:
        print('Adulto')
            
    elif idade >= 60 and idade <= 120:
        print('Idoso') 
    else:
            print('Idade inválida')

except ValueError:
    print('ERRO')