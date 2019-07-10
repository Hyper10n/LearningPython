def count_subject_line(path):
    count = 0
    
    try:
        with open(path) as fhand:
            for line in fhand:
                if line.rstrip().startswith('From:'):
                    count += 1
    except:
        print('Error: Please ensure proper file format, permissions, and spelling.')
        exit()

    return count
