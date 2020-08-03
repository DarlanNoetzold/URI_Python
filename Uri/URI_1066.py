x=0
pos=0
neg=0
par=0
imp=0
while(x <5):
    num = int(input())
    if num < 0:
        neg += 1
    elif num > 0:
        pos += 1
    if (num%2) == 0:
        par += 1
    else:
        imp += 1
    x +=1

print(par, "valor(es) par(es)", end="\n")
print(imp, "valor(es) impar(es)", end="\n")
print(pos, "valor(es) positivo(s)", end="\n")
print(neg, "valor(es) negativo(s)", end="\n")