def min_number(num_list):
    min_num = None

    for num in num_list:
        if min_num is None or min_num > num:
            min_num = num
            
    return min_num
