def min_number(num_list):
    min_num = None

    for num in num_list:
        if min_num is None or min_num > num:
            min_num = num
            
    return min_num



def determine_max_number(num_list):
    max_num = None

    for num in num_list:
        if max_num is None or max_num < num:
            max_num = num

    return max_num
    


def min_max_from_input():
    
    num_list = []

    while True:
        str_num = input('Enter a number: ')

        if str_num == 'done':
            break
    
        try:
            num = int(str_num)
            num_list.append(num)
        except:
            print('Invalid input')
            continue

    min_num = determine_min_number(num_list)
    max_num = determine_max_number(num_list)

    print('Minimum: ', min_num)
    print('Maximum: ', max_num)
