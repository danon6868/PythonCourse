q=[]
b=input()
a=b[::-1]
for i in a:
    if i=='A':
        q.append('T')
    elif i=='T':
        q.append('A')
        
    elif i=='G':
        q.append('C')
    elif i=='C':
        q.append('G')
        
for i in q:
    print(i, end='')