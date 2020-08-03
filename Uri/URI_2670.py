a = int(input())
b = int(input())
c = int(input())

andarUm = (b*2) + (c*4)
andarDois = (a*2) + (c*2)
andarTres = (a*4) + (b*2)

if(andarUm <= andarDois and andarUm <= andarTres):
    print(andarUm)
elif(andarDois <= andarUm and andarDois <= andarTres):
    print(andarDois)
elif(andarTres <= andarUm and andarTres <= andarDois):
    print(andarTres)