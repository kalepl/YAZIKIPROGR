n = int(input())
N = 1
sum = 0
for a in range(1, n+1):
    for b in range(1, a+1):
        N = N * b
    sum += N
print(sum)
