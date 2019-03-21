a=int(input())
b=int(input())
c=int(input())
D=b**2-4*a*c
if D<0:
    print('Нет действительных корней!!!')
elif D==0:
    print('x ='+str(-b/2/a))
else:
    x_1=(-b+(D)**(1/2))/2/a
    x_2=(-b-(D)**(1/2))/2/a
    print('x_1 ='+str(x_1))
    print('x_2 ='+str(x_2))