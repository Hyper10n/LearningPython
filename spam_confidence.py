def spam_confidence(source):

    if source == 'na na boo boo':
        print('NA NA BOO BOO TO YOU -  You have been punk\'d!')
        exit()

    spam_list = []
    spam_line_count = 0
    spam_total = 0

    try:
        fhand = open(source)
    except:
        print('File cannot be opened:', source)

    for line in fhand:
        if line.startswith('X-DSPAM-Confidence: '):
            decimal = float(line[line.find(':')+2:].rstrip())
            spam_list.append(decimal)
            spam_line_count += 1
            spam_total += decimal

            spam_average = spam_total / spam_line_count

    fhand.close()

    return spam_list, spam_average
