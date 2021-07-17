from itertools import permutations

def possible_permutations(arr):
    for x in permutations(arr):
        yield list(x)
