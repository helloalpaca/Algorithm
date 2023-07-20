"""
import sys

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == "":
        break
    answer = 1
    while True:
        if answer % N == 0:
            break
        else:
            answer *= 10
            answer += 1
    print(answer)
"""