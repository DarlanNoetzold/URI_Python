a = int(input())
b = int(input())

if(b<a):
    maior = a
    a = b
    b = maior

while(a < b):
    a = a + 1
    if(a%5==3 or a%5==2):
        print(a)