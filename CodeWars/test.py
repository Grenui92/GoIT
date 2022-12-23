# Приклад команди
# contact_add_value Stas phone +380501112233
# після парсингу мого буде ось так виглядати
name = "Stas"
info = ["phone", "+380501112233"]

def add_values(self, name, info):
    record = self.book[name]
    field = info[0]
    if field == "phones":
        return record.add_phone(info[1])
    elif field == "emails":
        return record.add_email(info[1])
    elif field == "address":
        return record.add_address(" ".join(info[1:]))
    elif field == "birthday":
        return record.set_birthday(info[1])
    else:
        return f"I can't find field '{field}'."


# Приклад edit_contact_information Stas phones +380501112233 +380667778899
# Приклад для видалення edit_contact_information Stas phones +380501112233 delete
# після парсингу мого
name = "Stas"
data = ["phones", "+380501112233", "+380667778899"]
def edit_information(self, name, data):
    record = self.book[name]  # Check if this record exists
    field, old, new = data[0], data[1], data[2]
    return record.edit_contact_information(field, old, new)


def edit_contact_information(self, field: str, old: str, new: str) -> str:
    point = self.__dict__[field]
    for entry in point:
        if old == entry.value:
            if new == "delete": # це мене Віка питала як видалити якесь значення. Це як варіант можна використати
                self.phones.remove(old)
            entry.value = new
            return f"{old} successfully changed to {new}"
    raise KeyError(f"I can't find old value {old}")