N = int(input())
for _ in range(N):
    inp = list(input())
    q = []
    for i in range(len(inp)):
        if len(q) == 0:
            q.append(inp[i])
        else:
            tmp = q.pop()
            if tmp == inp[i] or (tmp==")" and inp[i] == "("):
                q.append(tmp)
                q.append(tmp)
    if len(q) == 0:
        print("YES")
    else:
        print("NO")