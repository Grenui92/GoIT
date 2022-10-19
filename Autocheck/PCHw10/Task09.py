from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        result = []
        for k, v in self.data.items():
            if v == value:
                result.append(k)
        return result