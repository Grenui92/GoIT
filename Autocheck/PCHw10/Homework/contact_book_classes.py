from collections import UserDict

def try_error_decorator(func):
    def inner(*user_data):
        try:
            return func(*user_data)
        except IndexError:
            print(f"Index Error with {user_data[1:]}")
        except KeyError:
            print(f"I cant find user with name '{user_data[1]}'")
        except ValueError:
            print(f"'{user_data[2]}' is not a phone number")
    return inner


class AdressBook(UserDict):

    def add_record(self, user):
        self.data[user.name.value] = (user.phones.value, user.emails.value)


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = Phone
        self.emails = Emails

    @try_error_decorator
    def delete_phone(self, which):
        del self.phones.value[which]

    @try_error_decorator
    def delete_email(self, which):
        del self.emails.value[which]

    @try_error_decorator
    def add_or_change_phone(self, which, number):
        self.phones.value[which] = int(number)

    @try_error_decorator
    def add_or_change_email(self, which, email):
        self.emails.value[which] = email


class Field(Record):
    pass

class Name(Field):
    def __init__(self, name):
        self.value = name

class Phone(Field):
    value = {}

class Emails(Field):
    value = {}



# book = AdressBook()
# stas = Record('Stas')
# stas.add_or_change_phone("job", "0500801492")
# stas.add_or_change_email("job", "new_check@gmail.com")
# stas.add_or_change_phone("home", "0500801492")
# stas.add_or_change_phone("new", "asd")
# stas.add_or_change_email("home", "new_check@gmail.com")
# stas.delete_phone("job")
# stas.delete_email("home")
# book.add_record(stas)
# dima = Record("Dima")
# dima.add_or_change_phone("job", "0500801492")
# dima.add_or_change_email("job", "new_check@gmail.com")
# dima.add_or_change_phone("home", "0500801492")
# dima.add_or_change_email("home", "new_check@gmail.com")
# stas.delete_phone("home")
# stas.delete_email("job")
# book.add_record(dima)
# print(book)
# stas.delete_email("asd")