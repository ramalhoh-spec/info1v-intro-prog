# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V4.2


#begin_inputs
 #mantenha esse trecho. o input será manipulado aqui.
contador = 0
for n in range(10):
    idade = int(input())
    if idade >= 18:
        contador += 1
#end_inputs

print(contador)