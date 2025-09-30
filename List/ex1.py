# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def reverse_in_place(lst):
    for index,data in enumerate(lst):
        if index < (len(lst)/2):
            lst[index] = lst[len(lst)-index-1]
            lst[len(lst) - index -1] = data
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list=[1,2,3,4,5,6]
    reverse_in_place(list)
    print(list)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
