import math

# principal
p = 100000

# rate
r = 0.03

# length of payout
l = 103


def monthly_payment(p, r, l):
    return  math.ceil((r/12) * (1/(1-(1+r/12)**(-l)))*p)

print(monthly_payment(p, r, l))
