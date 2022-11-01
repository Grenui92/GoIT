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
        self.data[user.name.value] = user


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



book = AdressBook()
stas = Record('Stas')
stas.add_or_change_phone("job", "380500801492")
stas.add_or_change_email("job", "new_check@gmail.com")
stas.add_or_change_phone("home", "380500801492")
stas.add_or_change_phone("new", "asd")
stas.add_or_change_email("home", "new_check@gmail.com")
stas.delete_phone("job")
stas.delete_email("home")
book.add_record(stas)
dima = Record("Dima")
dima.add_or_change_phone("job", "380500801492")
dima.add_or_change_email("job", "new_check@gmail.com")
dima.add_or_change_phone("home", "380500801492")
dima.add_or_change_email("home", "new_check@gmail.com")
stas.delete_phone("home")
stas.delete_email("job")
book.add_record(dima)
print(book)
stas.delete_email("asd")
print(book["Stas"].phones.value)

# def main():
#     while True:
#         command = input("Если хотите добавить новый контакт - введите 1\n"
#                         "Если хотите удалить уже существующий - введите 2\n"
#                         "Если изменить существующий - введите 3\n"
#                         "Окончить работу - введите 4\n"
#                         "Выберите команду: ")
# if __name__ == "__main__":
#     main()