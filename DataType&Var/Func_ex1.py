def special_multiplication():
    input_string = input()
    for index , ch in enumerate(input_string):
        print(ch*(index+1))



special_multiplication()