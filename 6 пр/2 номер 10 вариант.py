arr = [1, 2, 3, 10, 20, 23, 43, 5, 6, 7] 
print(*arr)
print(*[0 if i < 10 else 1 if i > 20 else i for i in arr])
