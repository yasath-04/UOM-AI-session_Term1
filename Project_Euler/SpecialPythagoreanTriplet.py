def find_pythagorean_triplet(target):
    for i in range(1,target):
        for j in range(i+1,target-i):
            k = 1000-i-j
            if(i*i + j*j == k*k):
                print(f'{i},{j},{k}')
                print(i*j*k)

find_pythagorean_triplet(1000)
            
            

            

