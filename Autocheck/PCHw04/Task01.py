def amount_payment(payment):
    result = 0
    for i in payment:
        if i > 0:
            result += i
    return result