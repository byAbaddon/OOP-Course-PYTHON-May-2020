def solution():
    def integers():
        for n in range(1, 10000000):
            yield n

    def halves():
        for x in integers():
            yield x / 2

    def take(n, seq):
        arr = []
        for i in seq:
            if len(arr) != n:
                arr.append(i)
            else:
                return arr
      
    return take, halves, integers

