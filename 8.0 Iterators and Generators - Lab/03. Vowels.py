class vowels:
    def __init__(self, text: str):
        self.text = text
        self.index = 0
        self.vowels_list = ['a',  'o', 'i', 'u', 'e', 'y']

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.text):
            current_index = self.index
            self.index += 1
            if self.text[current_index].lower() in self.vowels_list:
                return self.text[current_index]
            else:
                return self.__next__()
        else:
            raise StopIteration()

#----------------------------(2)--------------Fucking Judge----------------------------------
# class vowels:
#     def __init__(self, string):
#         self.string = string
#         self.done = False

#     def __iter__(self):
#         return self
     
#     def __next__(self):
#         if self.done: 
#             raise StopIteration()
#         self.done = True
#         arr = ['A', 'a', 'E', 'e', 'I', 'i', 'U','u', 'O' , 'o', 'Y' ,'y']
#         return '\n'.join([x for x in self.string if x in arr])


# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)