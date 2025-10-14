# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V6.5
from random import randint
n = int(input('tente adivinhar um número de 1 a 100: '))

numero_secreto = randint(1, 100)

while n != numero_secreto:
    if n < numero_secreto:
        print('o valor secreto é maior! Tente novamente')
        n = int(input('tente adivinhar um número de 1 a 100: '))
    elif n > numero_secreto:
        print('o valor secreto é menor! Tente novamente')
        n = int(input('tente adivinhar um número de 1 a 100: '))

print(f'Parabéns, você acertou! O número secreto é: {numero_secreto}')