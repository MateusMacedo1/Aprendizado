#9) Crie a classe Termometro com atributo celsius.
#Crie métodos para_fahrenheit() e para_kelvin().
#Na main, crie 2 termômetros (valores diferentes) e imprima as conversões.
class Termometro:
    def __init__(self, celsius):
        self.celsius = celsius

    def para_fahrenheit(self):
        f = (self.celsius * 1.8) + 32
        print(f'Temperatura em Fahrenheit: {f}')

    def para_kelvin(self):
        k = self.celsius + 273.15
        print(f'Temperatura em Kelvin: {k}')

def main():
    t1 = Termometro(0)   
    t2 = Termometro(100)  
    print('Termômetro 1 (0°C)')
    t1.para_fahrenheit()
    t1.para_kelvin()

    print('Termômetro 2 (100°C)')
    t2.para_fahrenheit()
    t2.para_kelvin()

main()