# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def max_2_numbers_index(lst):
    max_value=[]
    new_lst = lst.copy()
    for index in range(0,2):
        max_value.append((new_lst.index(max(new_lst))))
        new_lst[(new_lst.index(max(new_lst)))]=0
    return max_value
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list=[10,20,30,25,30,17]
    print(max_2_numbers_index(list))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
