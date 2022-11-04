from collections import UserDict
from datetime import date


class AdressBook(UserDict):

    def change_contact_name(self, old_name, new_name: str):
        old = old_name.name.value
        self.data[new_name], self.data[old_name.name.value].name.value = self.data[old_name.name.value], new_name
        del self.data[old]
        return f"Имя {old} успешно изменено на {new_name}."

    def add_record(self, name):
        self.data[name] = Record(name)

    def __iter__(self):
        return self

    def __next__(self, n):


class Record:
    """Класс, в котором хранится весь контакт - список номеров, дата рождения, имя. Имя при создании обьекта обязательно. Номера телефонов - список обьектов
    класса Record. День рождения только в одном экземпляре, не обязателен для ввода, по умолчанию None."""

    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []
        self.birthday = Birthday(birthday) if phone else None

    def delete_phone(self, number):
        """Вносит изменения в класс, удаляет запись Рекорд, содержащую конкретный номер. Возвращает ответ об успешности/провальности операции."""
        try:
            old_number, new_number = int(number)
        except:
            return f"Номер телефона {number} состоит не только из цифр."
        for values in self.phones:
            if values.value == number:
                self.phones.remove(values)
                return f"Номер телефона {number} удален для пользователя {self.name._value}."
        else:
            return f"Я не могу найти {number} у контакта {self.name._value}"

    def edit_phone(self, old_number, new_number):
        """Вносит изменения в класс, изменяет у записи Рекорд, содержащую конкретный номер на новый. Так же проверяет на интование."""
        try:
            old_number, new_number = int(old_number), int(new_number)
        except:
            return f"Один из номеров телефона {old_number, new_number} состоит не только из цифр."
        for values in self.phones:
            if values.value == old_number:
                values.value = new_number
                return f"Номер телефона {old_number} заменен на номер телефона {new_number} для пользователя {self.name._value}."
        else:
            return f"Я не могу найти {old_number} у контакта {self.name._value}"

    def add_phone(self, number):
        """Вносит изменения в класс, изменяет поле phones, добавляя номер телефона. Возвращает ответ об успешности операции. Тут же проверка на интовнаие
        введенных данных. Если нужно, тут же можно воткнуть и проверку на соответствие формату (длинна, коды и тд)."""
        try:
            self.phones.append(Phone(number))
            return f"Номер телефона {number} добавлен к пользователю {self.name._value}."
        except ValueError:
            return f"'{number}' не является телефонным номером. Телефон может содержать только цифры."

    def set_birthday(self, birthdays_data):
        """Устанавливаем дату рождения. Тут же происходит и проверка на формат ввода. Ожидается yyyy.mm.dd"""
        try:
            self.birthday = Birthday(birthdays_data)
            return f"День рождения для контакта {self.name.value} успешно указан {self.birthday.value}"
        except:
            return f"Некоторые из этих значений {birthdays_data} не соответствуют дате в формате yyyy.mm.dd"

    def days_to_birthday(self):
        future_birthday = date(year=date.today().year+1, month=self.birthday.value.month, day=self.birthday.value.day)
        result = (future_birthday - date.today()).days
        return result

class Field:

    def __init__(self, name):
        self.value = name

class Name(Field):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @value.getter
    def value(self):
        return self._value


class Phone(Field):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        self._value = int(new_value)

    @value.getter
    def value(self):
        return self._value

class Birthday(Field):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        new_value = [int(i) for i in new_value.split('.')]
        self._value = date(*new_value)




    @value.getter
    def value(self):
        return self._value




