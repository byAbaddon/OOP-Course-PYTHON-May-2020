class countdown_iterator:
    def __init__(self, num):
        self.num = num 

    def __iter__(self):
        return self   

    def __next__(self):
        if self.num >= 0:
            current = self.num
            self.num -= 1 
            return current 

        raise StopIteration

