def solution(x, y):
    x = int(x)
    y = int(y)
    if y > x:
        x, y = y, x
    r = 0
    while y != 1:
        if not y:
            return 'impossible'
        r += x / y
        x, y = y, x % y
    return str(r + x - 1)
