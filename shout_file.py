def shout_file():
    source = input('Enter a full file path to text file\t')

    with open(source) as fhand:
        for line in fhand:
            print(line.upper().rstrip())
