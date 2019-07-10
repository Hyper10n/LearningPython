def email_list(path):

    emails = set()


    with open(path) as fhand:
        for line in fhand:
            if line.startswith('From:'):
                emails.add(line[6:].rstrip())
