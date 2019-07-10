def min_max_from_inputV2():
    inp_list = []

    while True:
        string_num = input('Enter a number: ')

        if string_num == 'done':
            break
        
        try:
            num = int(string_num)
        except:
            print('Invalid input')
            continue

        inp_list.append(num)
    
    maximum = str(max(inp_list)/1)
    minimum = str(min(inp_list)/1)

    print('Maximum: ' + maximum + '\nMinimum: ' + minimum)
