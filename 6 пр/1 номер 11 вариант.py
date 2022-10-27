a = []
for i in range (10):
    a.append(i)
x = a[0]
for i in a:
    if i > x and i % 2 == 0:
        x = i
print (x)