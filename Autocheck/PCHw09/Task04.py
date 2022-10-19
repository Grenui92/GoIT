def discount_price(discount):
    def price_calculator(price):
        return price*(1-discount)
    return price_calculator