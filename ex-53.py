# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V5.3


#begin_inputs
taipu = 12000
taxa_crescimento_taipu = 10/100 * taipu
cearamirim = 73000
taxa_crescimento_cearamirim = 3/100 * cearamirim
parnamirim = 250000
taxa_crescimento_parnamirim = 1/100 * parnamirim

#end_inputs

ano = 0

while parnamirim > cearamirim and parnamirim > taipu:
    taipu = taipu + taxa_crescimento_taipu
    taxa_crescimento_taipu = 10/100 * taipu
    cearamirim = cearamirim + taxa_crescimento_cearamirim
    taxa_crescimento_cearamirim = 3/100 * cearamirim
    parnamirim = parnamirim + taxa_crescimento_parnamirim
    taxa_crescimento_parnamirim = 1/100 * taxa_crescimento_parnamirim
    ano += 1
print(ano)
