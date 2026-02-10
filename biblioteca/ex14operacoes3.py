#Crie um pequeno projeto com pelo menos três arquivos Python:
#um arquivo com funções de entrada de dados um arquivo com funções de cálculo
#um arquivo principal
#Utilize importação para integrar os arquivos e executar o programa corretamente.

import ex14operacoes
import ex14operacoes2

a = ex14operacoes.entrada()
b = ex14operacoes.entrada()

resultado = ex14operacoes2.calculo(a, b)

print(resultado)