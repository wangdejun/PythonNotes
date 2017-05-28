def purify(li):
    new_list = []
    for item in li:
        if item % 2==0:
            new_list.append(item)

    return new_list