def nth_feb(order):
    number= 0
    if  order == 0:
        return  0
    elif order == 1:
        return 1
    
    else :
        for i in range(1,order):
            number = nth_feb(i) +  nth_feb(i-1)




for i in range(1,10):
    print(i, nth_feb(i))