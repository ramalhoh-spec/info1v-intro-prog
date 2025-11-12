# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V8.2

with open("ex82.txt","w+",encoding="utf-8") as linha:
    linha.write("Linha 1\n")
    linha.write("Linha 2\n")
    linha.write("Linha 3\n")
    linha.write("Linha 4\n")
    linha.write("Linha 5")
with open("ex82.txt","r",encoding="utf-8") as linha:  
    linhas = linha.readlines()
print(f"A quantidade de linhas is {len(linhas)}")