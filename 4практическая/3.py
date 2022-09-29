#Number3
A,B=[int(input()) for i in range (2)]
for i in range (A+A%2-1,B-1,-2):
    print(i)
