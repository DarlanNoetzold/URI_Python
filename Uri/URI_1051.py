sal = float(input())
if(sal <= 2000.00):
    print("Isento")
elif(sal <= 3000.00):
    imp = 0.08 * (sal - 2000)
    print("R$ {:.2f}".format(imp))
elif(sal <= 4500.00):
    imp = (0.08 * 1000) + ((sal - 3000) * 0.18)
    print("R$ {:.2f}".format(imp))
elif(sal > 4500):
    imp = (0.08 * 1000) + (0.18 * 1500) + ((sal - 4500) * 0.28)
    print("R$ {:.2f}".format(imp))