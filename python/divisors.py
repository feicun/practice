num = int(raw_input("Please choose a number to divide: "))
list_range = list(range(1, num + 1))
divisors = []
for i in list_range:
    if num % i == 0:
        divisors.append(i)
print divisors
