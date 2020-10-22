nr=1
suma=0
while True:
    nr=eval(input('dati un nr='))
    if (nr%2!=0) and (nr%3==0):
        break
    if nr%2==0:
        suma+=nr
        

print('suma nr pare=',suma)

