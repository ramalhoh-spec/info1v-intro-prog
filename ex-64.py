# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V6.4


#begin_inputs

#end_inputs

valor_dado = int(input('valor sorteado no dado: '))

if valor_dado == 7 or valor_dado == 11:
    print('Voce ganhou!')
elif valor_dado == 2 or valor_dado == 3 or valor_dado == 12:
    print('Voce perdeu!')
else:
    ponto = valor_dado
    valor_dado = int(input('valor sorteado no dado: '))
    while True:
        if valor_dado == ponto:
            print('Voce ganhou!')
            break
        elif valor_dado == 7:
            print('Voce perdeu!')
            break
        else:
            valor_dado = int(input('valor sorteado no dado: '))