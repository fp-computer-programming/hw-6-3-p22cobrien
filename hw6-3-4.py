# Author: CMOB 11/15/2021

initial_lst = input("Please input any number or letter seperated by spaces. ")

question = str.lower(input("Do you want the middle or the end? "))

lst1 = initial_lst.split()
length = len(lst1)

if question == "middle":
    print(lst1[1:length - 1])
elif question == "end":
    print(lst1[:1] + lst1[length - 1:])

