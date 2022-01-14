
orders = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Berry", 3, 32.95],
    [88112, "Einfuhrung in Python3, Bernd Klein", 3, 24.99]
]

updated_orders = list(map(lambda x: (x[0], x[2]*x[3]) if (x[2]*x[3]) >= 100 else (x[0], x[2]*x[3]+10), orders))
print(updated_orders)
