a = int(input())
ano =0
mes=0
while(a>=365):
    a -= 365
    ano = ano +1
while(a >= 30):
    a -=30
    mes = mes +1
while(mes>=12):
    mes -= 12
    ano = ano +1

print(ano, "ano(s)")
print(mes, "mes(es)")
print(a, "dia(s)")