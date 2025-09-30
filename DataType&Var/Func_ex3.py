def is_prime(num):
    if num < 2:
        return False
    for j in range(2, num):
        if num % j == 0:
            return False
    return True



def nth_prime(order):
    num ,i = 0 , 0
    while i != order:
        if is_prime(num):
            i += 1
        num +=1
    return  num -1


for i in range(1,100):
    print(i, nth_prime(i))
