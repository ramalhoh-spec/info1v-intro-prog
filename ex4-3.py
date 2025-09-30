# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V4.3


#begin_inputs
mes = int(input())
#end_inputs
lista_mes = ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
mes_lista = mes -1
if 1 > mes or mes > 12:
    print('mes invalido')
else:
    print(lista_mes[mes_lista])