def who_is_next(names: list, r):
    len_names = len(names)
    if r <= len_names: return names[r-1]
    n = 0
    i = 0
    while n * len_names <= r:
        n += 2 ** i
        i += 1
    idx = (r - n*len_names)//2 **(i-1)
    if (r - n*len_names) % 2 **(i-1) == 0:
        return names[idx - 1]
    else:
        return names[idx]



