#######################
# question 1

def hello():
    print("Hello World")


#######################
# question 2

def name_func(name):
    print(f"Hi my name is {name}")


#######################
# question 3

def num_func2(x, y, z):
    if z == True:
        return x
    else:
        return y


#######################
# question 4

def product(x, y):
    return x * y


#######################
# question 5

def is_even(x):
    return True if x % 2 == 0 else False


print(is_even(3))

#######################
# question 6

def is_greater(x, y):
    return True if x > y else False


#######################
# question 7

def sum_nums(*args):
    return sum(args)


#######################
# question 8

def sum_nums(*args):
    return sum([arg for arg in args if arg % 2 == 0])


#######################
# question 9

def alt_string(str):
    line = []
    for index in range(len(str)):
        if index % 2 == 0:
            line.append(str[index].upper())
        else:
            str.append(str[index].lower())

    return ''.join(line)


#######################
# question 10

def eo_nums(x, y):

    if x and y % 2 == 0:
        return min(x, y)
    else:
        return max(x, y)


#######################
# question 11

def start_letter(x, y):
    if x[0] == y[0]:
        return True
    else:
        return False


#######################
# question 12

def exponent(x):
    return x ** x


#######################
# question 13

def alt_string(str):
    line = []
    for index in range(len(str)):
        if 4 == index == 0:
            line.append(str[index].upper())
        else:
            str.append(str[index])

    return ''.join(line)