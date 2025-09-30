# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def max_2_numbers(lst):
    max_value=[]
    new_lst = lst.copy()
    for index in range(0,2):
        max_value.append((max(new_lst)))
        new_lst[(new_lst.index(max(new_lst)))]=0
    return sum(max_value)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list=[2,15,1000,4,100,50]
    print(max_2_numbers(list))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
