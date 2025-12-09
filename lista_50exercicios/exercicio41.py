#Leia um valor e uma escala de temperatura (C para Celsius, F para Fahrenheit) e faça a conversão, tratando entradas inadequadas.

try:
    valor = float(input('Digite a temperatura: '))
    
    escala = input('Qual a escala atual? (C para Celsius, F para Fahrenheit): ').strip().upper()

    if escala == 'C':
        convertido = (valor * 1.8) + 32
        print(f'Resultado: {valor}°C equivalem a {convertido:.1f}°F')

    elif escala == 'F':
        convertido = (valor - 32) / 1.8
        print(f'Resultado: {valor}°F equivalem a {convertido:.1f}°C')

    else:
        print('Erro: Escala desconhecida! Use apenas C ou F.')

except ValueError:
    print('Erro: Você deve digitar um número válido para a temperatura!')