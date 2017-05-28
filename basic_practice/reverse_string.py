def reverse(text):
    li = ""
    for c in text:
        li = c + li

    return li

print reverse("wangdejun")