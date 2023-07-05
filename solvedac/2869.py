import math

A, B, V = map(int, input().split())
meter_per_day = A - B
answer = math.ceil((V - A) / meter_per_day) + 1
print(answer)