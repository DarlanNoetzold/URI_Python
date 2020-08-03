a = float(input())
if(a >= 0 and a <=25.000):
    print("Intervalo [0,25]")
elif(a >= 25.01 and a <= 50.000):
    print("Intervalo (25,50]")
elif(a >= 50.01 and a <= 75.000):
    print("Intervalo (50,75]")
elif(a >= 75.01 and a <= 100.00):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")