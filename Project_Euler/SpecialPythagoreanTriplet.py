def isPythTrip(a,b,c):
    data = [a, b, c]
    data.sort()

    if(data[0]**2 + data[1]**2 == data[2]**2):
        return True
    else:
        return False


for i in range(1,1000):
    for j in range(i,1000-i):
        k = 1000-i-j
        if(isPythTrip(i,j,k)):
            return (i*j*k)

            

