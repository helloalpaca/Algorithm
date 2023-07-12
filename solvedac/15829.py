"""
5
abcde
"""
L = int(input())
st = input()
answer = 0
for i in range(L):
    answer += (ord(st[i])-96)*pow(31, i)
print(answer % 1234567891)