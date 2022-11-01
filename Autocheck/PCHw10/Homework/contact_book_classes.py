from collections import UserDict

class AdressBook(UserDict):

    def add_record(self, user):
        self.data[user.name.value] = (user.phones.value, user.emails.value)


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = Phone
        self.emails = Emails

    def delete_phone(self, number):
        self.phones.value.remove((number))

    def delete_email(self, email):
        self.emails.value.remove(email)

    def add_phone(self, number):
        self.phones.value.append(number)

    def add_email(self, email):
        self.emails.value.append(email)


class Field(Record):
    pass

class Name(Field):
    def __init__(self, name):
        self.value = name

class Phone(Field):
    value = []

class Emails(Field):
    value = []


stas = Record('Stas')
stas.add_phone("0500801492")
stas.add_email("new_check@gmail.com")

book = AdressBook()
print(book)
book.add_record(stas)
print(book)