def squares(n):
    result  = 0
    while result < n:
        result += 1
        yield result * result


# print(list(squares(5)))