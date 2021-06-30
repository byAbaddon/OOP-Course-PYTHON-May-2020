n = int(input())

for u in range(n):
    space = ' ' * (n - 1 - u)
    star = '* ' * (u + 1)
    print(f'{space}{star}')

for d in range(n -2, -1, -1):
    space = ' ' * (n - 1 - d)
    star = '* ' * (d + 1)
    print(f'{space}{star}')