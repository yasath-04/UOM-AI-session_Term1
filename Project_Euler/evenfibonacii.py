def sum_of_even_fibo(limit):
    a = 1
    b = 2
    total = 0
    while b <= limit:
        if b%2 == 0:
            total+=b
        a = b
        b = a+b

    return total

limit = 4000000
print(sum_of_even_fibo(limit))
