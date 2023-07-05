while True:
    inp = list(map(int, input().split()))
    inp.sort()
    if inp[0]==0 and inp[1]==0 and inp[2]==0:
        break
    if inp[2]**2 == inp[0]**2 + inp[1]**2:
        print("right")
    else:
        print("wrong")