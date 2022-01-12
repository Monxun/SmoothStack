a = [1, 'monkey', 3.14]
print(a)

a = [1, 1, [1, 2]]
print(a[2][1])

# 'b'

dict = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7,
}
print(dict)

a = tuple([1, [2, 3]])
print(a)

a = set("Mississippi")
print(a)

a.add('X')
print(a)

# {1, 2, 3}

####################################
# Question 1

start = 2000
stop = 2500

def find_numbers(start, stop):
    numbers = []
    for i in range(start, stop+1):
        if (i % 7 == 0) and (i % 5 != 0):
            numbers.append(i)
    print(numbers)

find_numbers(start, stop)

####################################
# Question 2

def factorial(x):
    import math

    return math.factorial(x)

####################################
# Question 3

def gen_dict(n):
    dict = {}
    for i in range(1, n+1):
        dict[i] = i * i
    
    return dict

print(gen_dict(7))

####################################
# Question 4

numbers = [1, 2, 3, 4, 5]

def tuple_list(numbers):
    a = list(numbers)
    b = tuple(a)
    return a, b

print(tuple_list(numbers))

####################################
# Question 5 ***********************

class StringObject():

    def __init__(self):
        self.s =""

    
    def getString(self):
        self.s = raw_input()

    
    def printString(self):
        print(self.s.upper())


a = StringObject()
a.getString()
a.printString()