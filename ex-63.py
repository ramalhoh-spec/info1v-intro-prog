# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V6.3


#begin_inputs
n = int(input())
#end_inputs

def inverso(n):
    n_string = str(n)
    invertido = n_string[::-1]
    return invertido


numero_invertido = inverso(n)
print(numero_invertido)