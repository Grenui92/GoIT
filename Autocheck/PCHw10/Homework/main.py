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
    print("Чтоб посмотреть команды введите 'help'")
    while True:
        user_text = input()
        command, user_data = refactor_user_text(user_text)
        if command not in commands:
            print(f"Неизвестная команда '{command}'")
            continue
        main_record = book.setdefault(user_data[0], Record(user_data[0])) if user_data else None
        result = get_functional(command)(main_record, user_data[1:])
        if result:
            if type(result) is list:
                print(*result, sep="\n")
            else:
                print(result)




@input_error
def get_functional(command: str):
    """Получение сигнатуры"""
    signature = commands[command]
    return signature


@input_error
def refactor_user_text(user_text: str) -> list:
    """Обработка введенного пользователем текста и разделение на понятные для программы части"""

    if not user_text:
        return ['', '']
    splited_text = user_text.split()
    # На случай если команда состоит из двух слов через пробел. Такие команды начинаются с нескольких конкретных слов.
    if splited_text[0].lower() in ("show", "good", "delete"):
        return [" ".join(splited_text[:2]).lower(), splited_text[2:]]
    else:
        return [splited_text[0].lower(),  splited_text[1:]]

@input_error
def greeting(*_) -> str:
    return "Hello, my dear friend!\n" \
           "How can i help you?\n"

@input_error
def help_me(*_):
    return "Команды, которые вы можете использовать: (X / Y в указанных команда = место для ввода пользователя)\n"\
          "'add X Y': Добавляет к записи пользователя X номер телефона Y.\n"\
          "'change X Y V': Заменяет для пользователя X номер телефона Y на номер телефона V.\n"\
          "'delete contact Х': Полностью удаляет контакт Х из записной книги.\n" \
          "'show phones X': Показывает все номера телефонов пользователя X.\n"\
          "'show all': Показывает всех пользователей что есть в записной книге и их номера телефонов."\
          "'good bye/close/exit/.': Выход из программы.\n"\


@input_error
def delete_contact(main_record: Record, *_):
    del book[main_record.name.value]
    return f"Контакт {main_record.name.value} удален из телефонной книги "


@input_error
def add_number(main_record: Record, user_info: list):
    main_record.add_phone(int(user_info[0]))
    return f"Номер телефона {user_info[0]} добавлен к пользователю {main_record.name.value}."

@input_error
def change_number(main_record: Record, user_info: list):
    main_record.edit_phone(int(user_info[0]), int(user_info[1]))
    return f"Номер телефона {int(user_info[0])} заменен на номер телефона {int(user_info[1])} для пользователя {main_record.name.value}."

@input_error
def delete_phone(main_record: Record, user_info: list):
    main_record.delete_phone(int(user_info[0]))
    return f"Номер телефона {user_info[0]} удален для пользователя {main_record.name.value}."

@input_error
def show_phones(new_record: Record, *_) -> str:
    return f"{new_record.name.value} contact phone numbers are: {[v.value for v in new_record.phones]}"


@input_error
def show_all(*_):
    full_list = []
    for contact_name, numbers in book.items():
        full_list.append(f"{contact_name} содержит такие номера телефонов: {[v.value for v in numbers.phones]}")
    return full_list



@input_error
def go_away(*_):
    exit("Bye. See you soon.")


commands = {"hello": greeting,
            "help": help_me,
            "delete contact": delete_contact,
            "add": add_number,
            "change": change_number,
            "delete phone": delete_phone,
            "show phones": show_phones,
            "show all": show_all,
            "good bye": go_away,
            "close": go_away,
            "exit": go_away,
            ".":go_away
            }
if __name__ == "__main__":
    book = AdressBook()
    main()
