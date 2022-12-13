#БЛОК А
def func(x, n):
    if n == 1: #проверка на выход из рекурсии
        return x
    else:
        return(x * func(x, n-1) / n) #сама рекурсия, формула

x = int(input('Введите х: '))
n = int(input('Введите n: '))
print(func(x, n))
#БЛОК Б 
def func():
    a = int(input('Введите число a: '))
    if a == 0: # проверка на выход из рекурсии
        return 0
    else:
        return max(a, func()) # рекурсия, нахождение максимума в строке натуральных чисел
print(func())
