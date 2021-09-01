frase = 'Curso em Vídeo Pyhton'
# Análise #
print(len(frase))
print(frase)
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

# Transformação #
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

# Divisão #
print(frase.split())

# Junção #
print('-'.join(frase))