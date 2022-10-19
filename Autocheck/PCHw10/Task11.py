from collections import UserString


class NumberString(UserString):
    def number_count(self):
        return len([i for i in self.data if i.isdigit()])