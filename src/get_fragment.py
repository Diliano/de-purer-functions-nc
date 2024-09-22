def get_fragment(lst, start=None, end=None):
    if not lst:
        return []
    
    if start is None:
        start = 0
    if end is None:
        end = len(lst)

    if not 0 <= start <= len(lst) - 1:
        raise IndexError
    if not 0 <= end <= len(lst):
        raise IndexError

    result = []

    for index, value in enumerate(lst):
        if index < start:
            continue
        elif index == end:
            break
        else:
            result.append(value)

    return result