def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def getPrimeSum(n):
    total = 0
    for i in range(n):
        if(isPrime(i)):
            total += i

    return total

num = 2000000
print(getPrimeSum(num))