T = int(input())

for _ in range(T):
    N = int(input())
    one = [0, 1, 1]
    zero = [1, 0, 1]

    def fibonacci(n):
        global one, zero
        if n >= len(one):
            for i in range(len(one), n+1):
                zero.append(zero[i-1]+ zero[i-2])
                one.append(one[i-1]+one[i-2])

    fibonacci(N)
    print(zero[N], one[N])
