class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __iter__(self):
        return self 

    def __next__(self):
        if len(self.dictionary):
            for k,v in self.dictionary.items():
                current = (k, v)
                del self.dictionary[k]
                return current
        else:    
            raise StopIteration()

           
      
