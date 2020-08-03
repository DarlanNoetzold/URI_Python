a=0
soma=0
i=0
while(True):
    a = int(input())
    if(a < 0):
        break
    soma = soma + a
    i = i+1
media = soma/i
print("{:.2f}".format(media))