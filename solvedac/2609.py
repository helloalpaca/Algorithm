N, M = map(int, input().split())
mx = max(N, M)

n_arr = [0 for i in range(mx+1)]
m_arr = [0 for i in range(mx+1)]

for i in range(2, mx+1):
    while N%i == 0:
        N //= i
        n_arr[i] += 1
    while M%i == 0:
        M //= i
        m_arr[i] += 1

gcd = 1
lcm = 1
for i in range(2, mx+1):
    m = max(n_arr[i], m_arr[i])
    mi = min(n_arr[i], m_arr[i])
    if mi != 0: gcd *= i ** mi
    if m != 0: lcm *= i ** m
print(gcd)
print(lcm)