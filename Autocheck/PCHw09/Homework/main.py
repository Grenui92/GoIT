def input_error(func):
    def inner(user_data):
        try:
            return func(user_data)
        except TypeError:
            return "To much arguments for this command"
        except IndexError:
            return "Not enough values. You forgot to enter name or phone number."
        except KeyError:
            return f"I cant find user with name '{user_data[0]}'"
        except ValueError:
            return f"'{user_data[1]}' is not a phone number"
    return inner


def main():
    while True:
        user_text = input()
        command, user_data = refactor_user_text(user_text)
        if command in commands:
            result = get_functional(command)(user_data)
            if result:
                print(result)
            else:
                continue
        else:
            print(f"I dont know this command '{command}'")


@input_error
def get_functional(command: str):
    return commands[command]


@input_error
def refactor_user_text(user_text: str) -> list:
    split_text = user_text.split()
    #На случай если команада состоит из двух слов через пробел. Такие команды начинаются с трех конкретных слов.
    if split_text[0].lower() in ("show", "good", "more"):
        return [" ".join(split_text[:2]).lower(), split_text[2:]]
    else:
        return [split_text[0].lower(), split_text[1:]]


@input_error
def greeting(*_) -> str:
    return "Hello, my dear friend!\nHow can i help you?"


@input_error
def add_contact(user_info: list):
    contacts[user_info[0]] = int(user_info[1])


@input_error
def change(user_info: list):
    del contacts[user_info[0]]
    contacts[user_info[0]] = int(user_info[1])


@input_error
def show_one_user_number(user_info: list) -> str:
    return f"{user_info[0]} telephone number is: {contacts[user_info[0]]}"


@input_error
def show_all(*_) -> str:
    return '\n'.join(f"{k} phone number is: {v}" for k, v in contacts.items())


@input_error
def go_away(*_):
    exit("Bye. See you soon.")


contacts = {'Stas': 50, 'Kate': 66}
commands = {"hello": greeting,
            "add": add_contact,
            "change": change,
            "show phone": show_one_user_number,
            "show all": show_all,
            "good bye": go_away,
            "close": go_away,
            "exit": go_away
            }
if __name__ == "__main__":
    main()
