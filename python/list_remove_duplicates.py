# Use sets
def dedup_v1(x):
    return list(set(x))

# Use for loop
def dedup_v2(x):
    result = []
    for i in x:
        if i not in result:
            result.append(i)
    return result

a = [1, 2, 3, 3, 4, 2, 43, 5, 5]
print a
print dedup_v1(a)
print dedup_v2(a)

