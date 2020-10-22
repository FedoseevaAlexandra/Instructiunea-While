i=1
suma=0
produs=1
n=eval(input('dati nr:'))
while i<=n:
    suma+=i
    produs*=i
    med=suma/n
    i+=1

print('suma=',suma,'  produsul=',produs,'  media aritmetica=', med)