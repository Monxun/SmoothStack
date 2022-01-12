s = "Hello World"
print(s[8])

s = "thinker"
print(s[2:5])

# e

# m

s = set("Mississippi")
print(s)

# not sure about input
def palindrome(number):
    lines = ""
    for _ in range(number):
        lines+=input()+"\n"
    words = lines.splitlines()
    return [word == word[::-1] for word in words]
