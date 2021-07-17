def read_next( *args):
    for prop in args:
        for el in prop:
            yield str(el)

