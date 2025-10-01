# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V5.1


#begin_inputs
 

#end_inputs
somatorio = 0
peso = int(input('Digite o peso:'))
somatorio += peso
while somatorio <= 500:
    peso = int(input('Digite o peso:'))
    somatorio += peso
print('Peso excedido')