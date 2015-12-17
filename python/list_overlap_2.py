import random

a = random.sample(range(1, 30), random.randint(1, 15))
b = random.sample(range(1, 30), random.randint(1, 15))
result = [i for i in set(a) if i in b]
print a
print b
print result
