def unique_words_with_set(source):

    #path = r'C:\Users\limpFish\Documents\Romeo.txt'

    word_set = set()

    try:
        fhand = open(source)
    except:
        print('Couldn\'t open the file')

    for line in fhand:
        for word in line.split():
            word_set.add(word)

    fhand.close()
    word_list = sorted(list(word_set))

    return word_list
