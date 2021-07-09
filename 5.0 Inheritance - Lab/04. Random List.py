import random

class RandomList(list):
    def get_random_element(self):
        num = random.choice(self)
        self.remove(num)
        return num
