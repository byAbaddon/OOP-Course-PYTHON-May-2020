def even_parameters(fun):
    def wrapper(*args):
        result = 0
        for x in args:
            if isinstance(x, int) and x & 1 == 0:
                pass  
            else:
                return 'Please use only even numbers!'
        return fun(*args)  
    return wrapper




# @even_parameters
# def add(a, b):
#     return a + b

# print(add(2, 4))
# print(add( "Peter", 1))


# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result

# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))