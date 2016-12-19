# class A(object):
#     x = 1
#     gen = (x for _ in xrange(10))

# if __name__ == "__main__":
#     print(list(A.gen))


class A(object):
    x = 1
    gen = (A.x for _ in xrange(10))

if __name__ == "__main__":
    print(list(A.gen))