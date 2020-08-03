x = int(input())
a = input()
a = a.split(' ')
n2 = 0
n3 = 0
n4 = 0
n5 = 0

for i in range(x):
    if int(a[i]) % 2 == 0:
        n2 += 1
    if int(a[i]) % 3 == 0:
        n3 += 1
    if int(a[i]) % 4 == 0:
        n4 += 1
    if int(a[i]) % 5 == 0:
        n5 += 1

print('%d Multiplo(s) de 2' %n2)
print('%d Multiplo(s) de 3' %n3)
print('%d Multiplo(s) de 4' %n4)
print('%d Multiplo(s) de 5' %n5)
