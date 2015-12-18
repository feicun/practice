def gen_fib():
    count = int(raw_input(
        "How many fibonacci numbers you like to generate? "))
    if count <= 0:
        return [0]
    if count == 1:
        return [1]

    a = 0
    b = 1
    c = 0
    i = 2
    result = [a, b]
    while i <= count:
        c = a + b
        a = b
        b = c
        i += 1
        result.append(c)
    print result
    return result

gen_fib()
