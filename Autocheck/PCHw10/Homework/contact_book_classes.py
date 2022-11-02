from collections import UserDict



class AdressBook(UserDict):
    pass


class Record:

    def __init__(self, name, phone=None, email=None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []


    def delete_phone(self, number):
        for num, value in enumerate(self.phones):
            if value.value == number:
                self.phones.pop(num)
                break
        else:
            print(f"I cant find {number} in user {self.name.value}")

    def edit_phone(self, old_number, new_number):
        for num, values in enumerate(self.phones):
            if values.value == old_number:
                values.value = new_number
                break
        else:
            print(f"I cant find {old_number} in user {self.name.value}")


    def add_phone(self, number):
        self.phones.append(Phone(number))




class Field:
    def __init__(self, name):
        self.value = name


class Name(Field):
    pass

class Phone(Field):
    pass
