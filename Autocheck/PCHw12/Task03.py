import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, "w", newline='') as file:
        field_names = ["name", "email", "phone", "favorite"]
        contact_writer = csv.DictWriter(file, fieldnames=field_names)
        contact_writer.writeheader()
        for line in contacts:
            contact_writer.writerow(line)



def read_contacts_from_file(filename):
    result = []
    with open(filename, "r", newline='') as file:
        contact_reader = csv.DictReader(file)
    for row in contact_reader:
        if row["favorite"] == "True":
            row["favorite"] = True
        elif row["favorite"] == "False":
            row["favorite"] = False
        result.append(row)
    return result