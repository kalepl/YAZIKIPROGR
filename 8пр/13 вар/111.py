import math

m = int(input('Введите кол-во строк'))
n = int(input('Введите кол-во столбиков'))
a = []
for i in range (m):
    b = []
    for k in range (n):
        print ('Введите [',i,',',k,'] элемент')
        b.append(int(input()))
    a.append(b)
for i in range (m):
    for k in range (n):
        print (a[i][k], end=' ')
    print ()
for i in range (m):
    if i % 2 !=0:
        mmin = min (a[i])
        print ('min элемент чётных строк', mmin)