# #a new wrapper layer 一个新的包装层


# def pre_str(pre=""):
#     def decorator(F):
#         def new_F(a,b):
#             print(pre + "input",a,b)
#             return F(a,b)
#         return new_F
#     return decorator


# @pre_str("^_^")
# def square_sum(a,b):
#     return a**2 + b**2

# @pre_str("wangdejun")
# def square_diff(a,b):
#     return a**2 - b**2

# print(square_sum(3,4))
# print(square_diff(3,4))

# new_square_sum  = pre_str("XXXXX ")(square_sum(3,4))
# print new_square_sum

def pre_str(pre=""):
    def decorator(F):
        def new_F(a,b):
            print pre+"input" +", "+ str(a)+", "+ str(b)
            return F(a,b)
        return new_F
    return decorator

@pre_str("This is a pre decorator")
def square_sum(a,b):
    return a**2 + b**2

@pre_str("input:")
def square_diff(a,b):
    return a**2 - b**2

print(square_sum(3,4))
print(square_diff(13,4))