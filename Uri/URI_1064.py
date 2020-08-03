a = []
for i in range(6):
    n = float(input())
    a.append(float(n))

l=0
soma = 0.0
for j in range(6):
    if (a[j]>0):
        l = l+1
        soma = soma + a[j]

print(l, "valores positivos")
media = soma/l
print("{:.1f}".format(media))