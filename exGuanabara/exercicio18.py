from math import radians, cos, sin, tan

angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'angulo de {angulo} tem o seno em: {seno:.2f};\nAngulo de {angulo} tem o cosseno em: {cosseno:.2f};\nAngulo de {angulo} tem a tangente em: {tangente:.2f};')
