A = [19, 88, 123, 1000, 1234, 55, 80, 70, 80, 100, 22, 11]
s = set([v for v in A if A.count(v) > 1])
print(*(s if len(s) > 0 else ['отсутствуют']))