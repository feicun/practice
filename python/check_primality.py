def is_prime(x):
    if x < 3:
        return False
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True

num = raw_input("Give me a number: ")
num = int(num)

if is_prime(num):
    print str(num) + " is a prime number"
else:
    print str(num) + " is NOT a prime number"
