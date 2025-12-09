# Leia uma linha contendo vários valores separados por espaço.
# Converta os valores válidos para inteiro, ignore os inválidos e exiba a lista final.

digit = input('Digite vários valores (separe por espaço): ')

pedaços = digit.split()

numeros_validos = []

for i in pedaços:
    try:
        numero = int(i)
        
        numeros_validos.append(numero)
        
    except ValueError:
        pass 

print(f'Lista final de números: {numeros_validos}')