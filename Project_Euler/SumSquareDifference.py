def sumSquareDifference(n):
    sums = 0
    sqsum = 0

    for i in range(1,n+1):
        sqsum += i**2
        sums += i

    diff = sums**2 - sqsum
    return diff

print(sumSquareDifference(100))
    