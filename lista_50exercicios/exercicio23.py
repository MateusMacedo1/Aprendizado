#Gere e exiba os 20 primeiros termos da sequência de Fibonacci.
sequencia = [0, 1]


for i in range(18):
    
    ultima = sequencia[-1]
    
    penultima = sequencia[-2]
    
    proxima = ultima + penultima
    
    sequencia.append(proxima)

print(f'A sequencia é: {sequencia}')