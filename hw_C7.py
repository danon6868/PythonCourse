g=input('Введите функцию')
f=lambda x: eval(g) 
s=float(input('Введите первый предел'))
e=float(input('Введите второй предел'))
n=int(input('Введите число точек'))
cycl=int(input('Введите число циклов'))
import numpy as np
import random

samples=[]
for i in range(cycl):
    
    a=np.linspace(s, e, 1000)
    q={}
    for i in a:
        q[f(i)]=i
    if min(q)<0 and max(q)>=0:    
        b=np.linspace(min(q), max(q), 1000)  
    elif min(q)<0:
        b=np.linspace(min(q), 0, 1000)
    elif min(q)>=0:
        b=np.linspace(0, max(q), 1000)
    
    

    randp=[]
   
    k=0
    for i in range(n):
        randp.append((random.choice(a), random.choice(b)))
   
    if min(q.keys())>=0:
        Sq=1
        k=0
        for i in randp:
            if f(i[0])>=i[1]:
                k+=1
        Sq*=((e-s)*max(q))
        samples.append(k/n*Sq)
    
    else:
        Sq1=1
        Sq2=1
        k1=0
        k2=0
        n1=0
        n2=0       
        for i in randp:
            if i[1]>=0 and f(i[0])>=i[1]:
                k1+=1                  
                n1+=1
            elif i[1]>=0:
                n1+=1
            elif i[1]<0 and f(i[0])<=i[1]:
                k2+=1
                n2+=1
            elif i[1]<0:
                n2+=1
        Sq1*=((e-s)*max(q))
        Sq2*=((s-e)*min(q))
        samples.append(k1/n1*Sq1-k2/n2*Sq2)
        
x=sum(samples)/len(samples)
D=0
for i in samples:
    D+=(i-x)**2
D/=len(samples) 
Se=D**(1/2)/len(samples)**(1/2)
print('I = '+'('+str(x)+ u' \u00B1 ' +str(Se)+')')