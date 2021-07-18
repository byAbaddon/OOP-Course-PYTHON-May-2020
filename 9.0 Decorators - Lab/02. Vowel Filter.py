def vowel_filter(fun):
    def wrapper():
        current = fun()
        arr = ['a', 'e', 'o', 'u', 'i', 'y']
        return [x for x in current if x in arr] 
        
    return wrapper
    

# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]

# print(get_letters())