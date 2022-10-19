def get_emails(list_contacts):
    return [i for i in map(lambda x: x['email'], list_contacts)]