frase = 'Curso em video Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[:2:2])
print(len(frase)) #quantidade de caracter
print(frase.count('o')) #conta repetição de caracter
print(frase.find('deo')) #encontra a posição de caracteres
print(frase.find('ana')) #se não tem nos caracter ele mostra -1
print(frase.replace('Python','Android')) #substitui caracteres
print(frase.upper()) # caracteres em maiusculo
print(frase.lower()) # caracteres em minusculo
print(frase.capitalize()) # primeiro caracter em maiusculo
print(frase.title()) # primeiro caracter após espaço em maiusculo
print(frase.strip()) #elimina espaços do inicio e do final da frase
print(frase.rstrip()) #elimina espaços do final da frase
print(frase.lstrip()) #elimina espaços do inicio da frase
print(frase.split()) # separa palavras
print('-'.join(frase))