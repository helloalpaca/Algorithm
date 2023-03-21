arr = list(map(int, input().split()))
a, b, c, d, e, f = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]

for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if a*x+b*y == c and d*x+e*y == f:
            print(x, y)
            break
