def create_lists_of_three(pairs, extra): #here pairs is tuple of 4 elements
    result = []
    # print(pairs)
    n = len(pairs)
    for i in range(n):
        first = pairs[i][0]
        second = pairs[i][1]
        start_time = pairs[i][2]
        reaching_time = pairs[i][3]
        if i + 1 < n:
            third = pairs[i + 1][1]
        else:
            third = extra
        result.append([first, second, third, start_time, reaching_time])
    return result


