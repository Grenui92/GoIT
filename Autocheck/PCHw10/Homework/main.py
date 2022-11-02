from contact_book_classes import AdressBook, Record
def input_error(func):
    def inner(*user_data):
        try:
            return func(*user_data)
        except IndexError:
            print("Получено недостаточно информации. Проверьте корректность ввода.")
        except KeyError:
            print(f"KeyError. Данное значение или команда не найдены.")
        except ValueError:
            print(f"'{user_data[1]}' не является телефонным номером. Телефон может содержать только цифры.")
    return inner


def main():
    print("Команды, которые вы можете использовать: (X / Y в указанных команда = место для ввода пользователя)\n"
          "'create contact X': Создает нового пользователя X.\n"
          "'choice contact X': Выбрать пользователя из уже существующих.\n"
          "'add X Y': Добавляет к записи пользователя номер телефона X(указывает на предназначение по типу 'home/job/own') Y(сам номер телефона).\n"
          "'change X Y': Изменяет у записи пользователя номер телефона X(указывает на предназначение по типу 'home/job/own') Y(сам номер телефона).\n"
          "'save': сохраняет текущий контакт в телефонную книгу.\n"
          "'show phone X': Показывает один номер телефона X('job/home/own') текущего пользователя.\n"
          "'show all': Показывает все номера телефонов пользователя который выбран в данный момент.\n"
          "'good bye/close/exit': Выход из программы.\n"
    )
    while True:

        user_text = input()
        command, user_data = refactor_user_text(user_text)
        if command in  ("create contact", "choice contact"): # Создаем или выбираем контакт с которым будем работать.
            new_record = get_functional(command)(user_data[0])
        else:
            try:
                result = get_functional(command)(new_record, user_data)
            except UnboundLocalError:
                print("Вы не выбрали пользователя для взаимодействия.\n"
                      "Создайте нового с помощью команды 'create contact X' или выберите существующего с помощью 'choice contact X'")
                continue
            if type(result) is str:
                print(result)
        try:
            print(f"На данный момент мы работает с пользователем {new_record.name.value}.\n"
                  f"Не забывайте сохранять данные с помощью команды save в адресную книгу перед сменой пользователя или завершением работы, иначе данные будут "
                  f"утеряны.")
        except:
            print(f"Не удалось найти пользователя {user_data[0]}. Возможно вы не сохранили данные или не корректно ввели имя.")


@input_error
def get_functional(command: str):
    signature = commands[command]
    return signature


@input_error
def refactor_user_text(user_text: str) -> list:
    splited_text = user_text.split()
    # На случай если команда состоит из двух слов через пробел. Такие команды начинаются с нескольких конкретных слов.
    if splited_text[0].lower() in ("show", "good", "create", "choice"):
        return [" ".join(splited_text[:2]).lower(), splited_text[2:]]
    else:
        return [splited_text[0].lower(), splited_text[1:]]


@input_error
def greeting(*_) -> str:
    return "Hello, my dear friend!\n" \
           "How can i help you?\n"

@input_error
def create_new_contact(name):
    return Record(name)

@input_error
def choice_user(name):
    user = book[name]
    return user

@input_error
def add_number(new_record: Record, user_info: list):
    new_record.add_or_change_phone(user_info[0], user_info[1])


@input_error
def change(new_record: Record, user_info: list):
    new_record.add_or_change_phone(user_info[0], user_info[1])

@input_error
def save_to_book(new_record, *_):
    book.add_record(new_record)


@input_error
def show_one_user_number(new_record: Record, user_info: list) -> str:
    return f"{user_info[0]} telephone number is: {new_record.phones.value[user_info[0]]}"


@input_error
def show_all(new_record: Record, *_) -> str:
    return "\n".join(f"{new_record.name.value} contact: '{k}' phone number is: {v}" for k, v in new_record.phones.value.items())


@input_error
def go_away(*_):
    exit("Bye. See you soon.")


contacts = {'Stas': 50, 'Kate': 66}
commands = {"hello": greeting,
            "create contact": create_new_contact,
            "choice contact": choice_user,
            "add": add_number,
            "change": change,
            "save": save_to_book,
            "show phone": show_one_user_number,
            "show all": show_all,
            "good bye": go_away,
            "close": go_away,
            "exit": go_away
            }
if __name__ == "__main__":
    book = AdressBook()
    main()
