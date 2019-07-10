def stats_from_input():

    counter = 0
    total = 0

    while True:

        str_num = input('Enter a number: ')

        if str_num == 'done':
            break

        try:
            num = int(str_num)
        except:
            print('Invalid input')
            continue

        counter += 1
        total += num
        average = total/counter

    print('Total: ', total)
    print('Count of numbers entered: ', counter)
    print('Average: ', average)
