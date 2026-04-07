
def count_digits(n):
    if n == 0: #if in case n is 0, then its 1 digit, 1 will be returned
        return 1
    
    n = abs(n) #this is turn the negative number to positive number

    count = 0
    while n > 0:
        n = n // 10
        count = count+1
    return count

n = 234
result = count_digits(n)
print(result)