from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum([i for i in self.data if i > 0])