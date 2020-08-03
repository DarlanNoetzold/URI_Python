t = int(input())
sum=0.0
sum1=0.0
sum2=0.0
dif=0.0
dif1=0.0
dif2=0.0
while(t > 0):
    str1 = str(input())
    x,y,z = input().split()
    x = float(x)
    y = float(y)
    z = float(z)

    sum = sum + x
    sum1 = sum1 + y
    sum2 = sum2 + z

    A, B, C = input().split()
    A = float(A)
    B = float(B)
    C = float(C)

    dif = dif + A
    dif1 = dif1 + B
    dif2 = dif2 + C

    t = t-1

p = (dif * 100.00) / sum
q = (dif1 * 100.00) / sum1
r = (dif2 * 100.00) / sum2

print("Pontos de Saque: {:.2f} %.".format(p))
print("Pontos de Bloqueio: {:.2f} %." .format(q))
print("Pontos de Ataque: {:.2f} %." .format(r), end="\n")