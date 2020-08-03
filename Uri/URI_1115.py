while(True):
    n = input().split()
    x, y = (int(val) for val in n)

    if(x>0 and y>0):
        print("primeiro")
    elif(x<0 and y>0):
        print("segundo")
    elif(x<0 and y<0):
        print("terceiro")
    elif(x>0 and y<0):
        print("quarto")

    if(x==0 or y==0):
        break