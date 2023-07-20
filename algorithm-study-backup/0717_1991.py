import sys

read = sys.stdin.readline
def preorder(v):
    print(v, end='')
    l, r = graph[v]
    if l != '.':
        preorder(l)
    if r != '.':
        preorder(r)

def inorder(v):
    l, r = graph[v]
    if l != '.':
        inorder(l)
    print(v, end='')
    if r != '.':
        inorder(r)

def postorder(v):
    l, r = graph[v]
    if l != '.':
        postorder(l)
    if r != '.':
        postorder(r)
    print(v, end='')

N = int(read().rstrip())
graph = dict()

for _ in range(N):
    n, l, r  = read().rstrip().split()
    graph[n] = [l, r]

preorder('A')
print()
inorder('A')
print()
postorder('A')