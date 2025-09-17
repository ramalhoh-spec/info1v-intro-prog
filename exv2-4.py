# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V2.4


#begin_inputs
valor_compra = int(input('Digite o valor da compra:'))
#end_inputs
desconto = valor_compra * 0.91
print(round(desconto, 2))

prestacao5 = valor_compra / 5
print(round(prestacao5, 2))

prestacao10 = (valor_compra * 1.17) / 10
print(round(prestacao10, 2))

