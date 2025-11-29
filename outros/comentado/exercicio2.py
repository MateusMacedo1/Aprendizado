bloco = 2.5
quantidade = int(input('Digite a quantidade: '))
valor = quantidade * bloco
imposto = 0 

if quantidade <= 500: # Se a quantidade for menor ou igual a 500
    imposto = valor * 0.05 # Aplica 5%
    
elif quantidade > 500: # Senão, se a quantidade for maior que 500
    imposto = valor * 0.03 # Aplica 3%

print('Seu valor final: ', valor - imposto)