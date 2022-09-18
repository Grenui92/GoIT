def cost_delivery(quantity, *_, discount = 0):
	return 5 + (quantity-1)*2 - (5 + (quantity-1)*2)*discount