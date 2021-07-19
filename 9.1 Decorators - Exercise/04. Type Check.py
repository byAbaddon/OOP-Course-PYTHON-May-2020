def type_check(arg):
    def decorator(fun):
        def wrapper(arg_two):
            if arg == type(arg_two):
                return fun(arg_two)
            return 'Bad Type'
        return wrapper
    return decorator



# @type_check(int)
# def times2(num):
#     return num*2
# print(times2(2))
# print(times2('Not A Number'))