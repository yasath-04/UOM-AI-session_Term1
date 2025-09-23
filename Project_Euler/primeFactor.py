def isPrime(n):

    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    else:
        return True
        
def primeFactor(n):
    largest = 0

    for i in range(n,0,-1):
        if n%i==0 and isPrime(i):
            largest = i
            break

    return largest


print(primeFactor(101))