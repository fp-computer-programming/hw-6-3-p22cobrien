# Author: CMOB 11/15/2021

numbers = input("Please enter any amount of numbers.")

numbers_lst = numbers.split()

lst_sort = numbers_lst.copy()

lst_sort.sort()

if numbers_lst == lst_sort:
    print("The lsit is sorted.")
else:
    print("The lsit is not sorted.")
