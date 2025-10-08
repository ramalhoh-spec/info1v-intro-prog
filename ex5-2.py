# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V5.2


#begin_inputs
 

#end_inputs

minutos = 0
tartaruga = 1 * minutos + 500 
lebre = 10 * minutos

while tartaruga > lebre:
    tartaruga = round(tartaruga + 1)
    lebre = round(lebre + 10)
    minutos += 1
print("{}".format(minutos))	
