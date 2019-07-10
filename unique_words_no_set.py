def unique_words_no_set(source):

    word_list = []

    try:
        fhand = open(source)
    except:
        print('Couldn\'t open the file')

    for line in fhand:
        for word in line.split():
            if word in word_list:
                continue
            else:
                word_list.append(word)

    fhand.close()
    word_list.sort()

    return word_list
