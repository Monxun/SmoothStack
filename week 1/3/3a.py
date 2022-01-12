# question 1

start = 1500
stop = 2700

def find_numbers(start, stop):
    numbers = []
    for i in range(start, stop+1):
        if (i % 7 == 0) and (i % 5 == 0):
            numbers.append(i)
    print(numbers)


find_numbers(start, stop)

#######################
# question 2

def fahrenheit(x):
    return (x - (32 / 9)) * 5


#######################
# question 3
# Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


#######################
# question 4

def reverse(word):
    return word[::-1]


#######################
# question 5

def even_odd(series):
    even = [num for num in series if num % 2 == 0]
    odd = [num for num in series if num % 2 != 0]
    return even, odd


    # for num in series:
    #     if num % 2 == 0:
    #         even.append(num)
    #     else:
    #         odd.append(num)

#######################
# question 6

def list_type(list):
    for item in list:
        print(type(item))


#######################
# question 7

num = 0

while num < 7:
    if num % 3 == 0:
        num += 1
        continue
    if num % 3 != 0:
        print(num)
        num += 1
        continue

# Lambda example
# result = map(lambda num: num+num, numbers)