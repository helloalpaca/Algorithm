import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
setA = set()
setB = set()

inps = list(map(int, sys.stdin.readline().rstrip().split()))
inps2 = list(map(int, sys.stdin.readline().rstrip().split()))

for inp in inps:
    setA.add(inp)

for inp in inps2:
    setB.add(inp)

symmetric_difference = setA ^ setB

print(len(symmetric_difference))