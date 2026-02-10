#Crie um programa que importe a biblioteca datetime e mostre a data atual no formato dia/mês/ano.

from datetime import date
hoje = date.today()

data_br = hoje.strftime("%d/%m/%Y")
print(data_br)