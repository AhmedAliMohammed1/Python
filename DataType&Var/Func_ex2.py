def my_max2(num1,num2):
    if num1 > num2 :
        return num1
    return num2
def my_max3(num1,num2,num3):
    if num3 > my_max2(num1,num2):
        return num3
    return my_max2(num1,num2)
def my_max4(num1,num2,num3,num4):
    if num4 > my_max3(num1,num2,num3):
        return num4
    return my_max3(num1,num2,num3)
def my_max5(num1,num2,num3,num4,num5):
    if num5 > my_max4(num1,num2,num3,num4):
        return num5
    return my_max4(num1,num2,num3,num4)
def my_max6(num1,num2,num3,num4,num5,num6):
    if num6 > my_max5(num1,num2,num3,num4,num5):
        return num6
    return my_max5(num1,num2,num3,num4,num5)



print(my_max6(5,9,11,18,2,66))