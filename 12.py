#Блок А, номер 4
def rec_sum(n, s = 0):
    a, b = divmod(n, 10)
    s += b
    if a == 0:
        return print(s)
    else:
        rec_sum(a, s)
 
rec_sum(int(input()))

#Блок Б, номер 4
n=int(input('Введите число: '))
def isPrime(n):
    for i in range(2, n):
        if n%i==0:
            itog='NO'
            break
        else:
            itog='YES'
    return(itog)
print(isPrime(n))
