a=input()
b=input()
a.count(b)
v=[]
while a.rfind(b)!=-1:
    q=a.rfind(b)+1
    v.append(q)
    n=int(a.rfind(b))+len(b)-1
    a=a[0:n]
a=list(reversed(v))
for i in a:
    print(i, end=' ')