# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V8.3

with open("ex82.txt","r",encoding="utf-8") as arquivo_original:
    conteudo = arquivo_original.read()
with open("ex83.txt","w",encoding="utf-8") as copiar:
     copiar.write(conteudo)  
print("Arquivo copiado com sucesso")