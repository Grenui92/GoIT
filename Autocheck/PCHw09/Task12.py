from functools import reduce


def amount_payment(payment):
    return reduce(lambda x, y: x + y, [i for i in payment if i > 0])
    #return reduce(lambda x , y: x + y, filter( lambda x: x > 0, payment))