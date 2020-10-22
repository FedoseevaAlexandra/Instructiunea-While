i=1
sum_p=0
sum_n=0
np=0
nn=0
nr=0
while i<=12:
    i+=1
    nr=eval(input('introduceti temperatura: '))
    if nr>=0:
        sum_p+=nr
        np+=1
    else:
        sum_n+=nr
        nn+=1
m_p=sum_p/np
m_n=sum_n/nn
print('media temp pozitive=',round((m_p),2), ', media temp negative=',round((m_n),2))