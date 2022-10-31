import pickle


def write_contacts_to_file(filename, contacts):
    with open(f"{filename}", "wb") as file:
        pickle.dump(contacts, file)


def read_contacts_from_file(filename):
    with open(f"{filename}", "rb") as file:
        spisok = pickle.load(file)
    return spisok