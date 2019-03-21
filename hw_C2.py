a=input()
summ=0
mult=1
for i in a:
    summ+=int(i)
    mult*=int(i)
print(str(summ)+' '+str(mult))