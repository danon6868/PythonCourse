a=input()
b=input()
q=0
for i in range(len(a)):
    if a[i]!=b[i]:
        q+=1
print(q)