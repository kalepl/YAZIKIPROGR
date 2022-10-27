from random import randint

print ('На отрезке [100, N] (210 < N < 231) найти количество чисел, составленных из цифр a, b, c.')

def poisk (N):
    schet = 0
    b = []
    arr = [i for i in range (0, 10)]
    for i in arr:
        for a in arr:
            for b in arr:
                if b!=a and a!=i and b!=i:
                    c = b * 100 + a * 10 + i
                    if c >=100 and c < N:
                        schet += 1
    return schet
N = int (input('Введите 210 < N < 231'))
while N < 210 or N > 231:
    print ('Вы ввели неверное значение, попробуйте ещё раз')
    N = int(input())
print (poisk(N))

