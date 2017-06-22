def anti_vowel(text):
    e_list = []
    result = ""
    for c in 'aeiou':
        e_list.append(c)

    for c in text:
        if c.lower() in e_list:
            pass
        else:
            result = result + c

    return result

print anti_vowel("WangDejun!")