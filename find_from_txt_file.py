def find_from_txt_file(source):

    email_list = []

    try:
        fhand = open(source)
    except:
        print('Could not open file')

    for line in fhand:
        for word in line.split():
            if word == 'From':
                email_list.append(line.split()[1])

    fhand.close()

    return email_list
