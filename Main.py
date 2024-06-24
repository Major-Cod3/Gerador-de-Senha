import random
import string

caracteres = []

letras_minusculas = string.ascii_lowercase  # Corrigido: letras_menusculas -> letras_minusculas
letras_maiusculas = string.ascii_uppercase
numeros = string.digits
caracteres_especiais = string.punctuation

caracteres.extend(letras_minusculas)  # Corrigido: extendindo letras_minusculas ao invés de letras_menusculas
caracteres.extend(letras_maiusculas)
caracteres.extend(numeros)
caracteres.extend(caracteres_especiais)

print('_'*50)
print("Gerador de Senha")
print('_'*50)
print()

while True:
    try:
        digitos = int(input('Sua senha terá quantos caracteres? '))
        break
    except ValueError:
        print('Por favor, digite apenas números.')

print()

senha = ''.join(random.choices(caracteres, k=digitos))
print(senha)
print('_'*50)
