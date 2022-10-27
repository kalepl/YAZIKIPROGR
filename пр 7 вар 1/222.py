def lala (x):
    appa = 0
    for i in range (5):
        appa += x [i]
    print ('Сумма элементов',appa)
    appa = appa/5
    print ('Среднее арифметическое',appa)
    return appa
def zaza (y):
    appa = 0
    for i in range (5):
        appa += y [i]
    print ('Сумма элементов',appa)
    appa = appa/5
    print ('Среднее арифметическое',appa)
    return appa
def haha (z):
    appa = 0
    for i in range (5):
        appa += z [i]
    print ('Сумма элементов',appa)
    appa = appa/5
    print ('Среднее арифметическое',appa)
    return appa
A = []
for i in range (5):
    A.append(int(input('Введите элемент массива A')))
B = []
for i in range (5):
    B.append(int(input('Введите элемент массива B')))
C = []
for i in range (5):
    C.append(int(input('Введите элемент массива C')))
print (lala(A))
print (zaza(B))
print (haha(C))