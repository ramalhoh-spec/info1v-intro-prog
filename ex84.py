# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V8.4

Dados = {}
with open("ex84.txt","w",encoding="utf-8") as dados:
   for n in range(5):
     Nome = input("Escreva seu Nome:")
     Cpf =  input("Escreva seu CPF:")
     Dados[Nome] = Cpf
     dados.write(f"{Nome};{Cpf}\n")
print("_______________________")
with open("ex84.txt","r",encoding="utf-8") as leia:
    ler = leia.read()
    print(ler.strip())