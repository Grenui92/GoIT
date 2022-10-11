from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    result = sum(Decimal(i) for i in number_list)/len(number_list)
    return result