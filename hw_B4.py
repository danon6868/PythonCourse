import random
n=random.randint(1, 20)
q=True

while True:
    a=int(input())
    if n>a: 
        print('Меньше')
    elif n<a:
        print('Больше')
    else:
        break
print('Молодец!!!')