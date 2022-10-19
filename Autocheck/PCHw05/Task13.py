import re


def find_all_emails(text):
    result = re.findall(r'\b[a-zA-Z]{1}[\w.]+[@][a-z.]+\w{2,}\b', text)
    return result

print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.com.ua 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'))