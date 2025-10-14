# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V6.2


#begin_inputs
n = int(input())
#end_inputs

for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()