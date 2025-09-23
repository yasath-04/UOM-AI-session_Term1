def isPalindrome(n):

    num = str(n)
    x = len(num)//2
    if (num[:x] == num[-x:][::-1]):
        return True
    else:
        return False
    
print(isPalindrome(10901))



