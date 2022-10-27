m = int(input('введите кол-во строчек'))
n = int(input('Введите кол-во столбиков'))
a = []
for i in range(m):
    b = []
    for k in range (n):
        print ('Введите[',i,',',k,'] элемент')
        b.append(int(input()))
    a.append(b)
def vivod(a):
    for i in range (m):
        for k in range (n):
            print (a[i][k]), end=' ')
        print ()
    print ()
vivod (a)
minimum = float('inf')
maximum = float ('-inf')
for i in range (m):
    for k in range (n):
            if a[i][k] < minimum:
                minimum = a[i][k]
            for j in range (n):
                if a[i][j] > maximum:
                    maximum = a[i][j]
for i in range (m):
    for k in range (n):
            if a[i][k] == maximum:
                a[i][k] = minimum
            elif a[i][k] == minimum:
                a[i][k] = maximum
print ('min=', minimum, 'max=', maximum)
vivod (a)



