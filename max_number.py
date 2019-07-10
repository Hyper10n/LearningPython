def max_number(num_list):
    max_num = None

    for num in num_list:
        if max_num is None or max_num < num:
            max_num = num

    return max_num
