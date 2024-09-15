def merge_list(lists):
    if not lists:
        return []
    
    longest_length = 0
    for lst in lists:
        if len(lst) > longest_length:
            longest_length = len(lst)

    result = []
    
    for i in range(longest_length):
        for lst in lists:
            if i < len(lst):
                result.append(lst[i])
            else:
                result.append(None)

    return result