orders = [34587, 98762, 77226, 88112]
books = ['Learning Python, Mark Lutz', 'Programming Python, Mark Lutz', 'Head First Python, Paul Barry', 'Einführung in Python3, Bernd Klein']
quantity = [4, 5, 3, 3]
price = [40.95, 56.80, 32.95, 24.99]


shop_list = [orders, books, quantity, price]

print(shop_list)

# USE LAMBDAS!


# data = [
#     [34587, "Learning Python, Mark Lutz", 4, 40.95],
#     [98762, "Programming Python, Mark Lutz", 5, 56.80],
#     [77226, "Head First Python, Paul Berry", 3, 32.95],
#     [88112, "Einfuhrung in Python3, Bernd Klein", 3, 24.99]
# ]

# def condense_to_tuple(lst):
#     order_num = lst[0]
#     price = 0
    
#     if lst[2] * lst[3] > 100:
#         price = lst[2] * lst[3]
#     else:
#         price = (lst[2] * lst[3]) + 10
    
#     return (order_num, price)

# result = map(condense_to_tuple, data)
# print(list(result)) 