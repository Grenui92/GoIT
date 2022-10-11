from random import randrange, sample


def get_numbers_ticket(min, max, quantity):
    print(max)
    print(min)
    print(quantity)
    if quantity >= max or min < 1 or max > 1000:
        result = []
    else:
        result = sample(range(min, max), k=quantity)
    return sorted(result)


print(get_numbers_ticket(1, 100, 30))