nv = 1
while nv==1:
    a = float(input())
    while a < 0.0 or a > 10.0:
        print("nota invalida")
        a = float(input())
    b = float(input())
    while b < 0.0 or b > 10.0:
        print("nota invalida")
        b = float(input())
    media = (a+b)/2
    print("media = {:.2f}".format(media))
    print("novo calculo (1-sim 2-nao)")
    nv = int(input())
    while nv !=1 and nv != 2:
        print("novo calculo (1-sim 2-nao)")
        nv = int(input())