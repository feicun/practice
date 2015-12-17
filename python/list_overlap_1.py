a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for numA in a:
    if numA in c:
        None
    elif numA in b:
        c.append(numA)

print c
