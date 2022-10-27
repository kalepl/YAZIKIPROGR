N = int(input('Введите размер матрицы'))
a = []
for i in range (N):
    b = []
    for k in range (N):
        print ('Введите [',i,',',k,']элемент')
        b.append(int(input()))
    a.append(b)
print ('Исходный массив:')
for i in range (N):
    for k in range (N):
        print (a[i][k], end=' ')
        print ()
j = 0
s = 0
for i in range (N):
    for k in range (N):
        if i < k:
            s = s + a[i][k]
            if a[i][k]
                j += 1
print ('Сумма элементов над главнй диагональю: ', s)
print ('Кол-во положительных элементов', j)
