# @cikey 516022b4ffbecd625ad38e6bd002f85f
# @sid 20251174010023
# @aid V5.3


#begin_inputs
 

#end_inputs

	
ceara_mirim=73000
parnamirim=250000
taipu=12000
ccm=1.03
cp=1.01
ct=1.1
ano=2018

while parnamirim>(ceara_mirim+taipu):
    parnamirim=round(parnamirim*cp)
    ceara_mirim=round(ceara_mirim*ccm)
    taipu=round(taipu*ct)
    ano=(ano+1)
    
print("{}".format(ano))