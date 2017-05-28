def censor(text,word):
    list = text.split(" ")
    for i in range(len(list)):
        if word == list[i]:
            list[i]="*"*len(word)

    word = (" ").join(list)
    return word