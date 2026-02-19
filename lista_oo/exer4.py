#4) Crie a classe Retangulo com atributos largura e altura.
# Crie métodos area() e perimetro().
# Na main, crie 2 retângulos e imprima área e perímetro.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura
    def perimetro(self):
        return 2 * (self.largura + self.altura)

def main():
    r1 = Retangulo(10, 5)
    r2 = Retangulo(7, 3)

    print(f'Um retangulo possui {r1.area()} de area e {r1.area()} de perimetro \n Outro retangulo possui {r2.area()} de area e {r2.area()} de perimetro')

main()