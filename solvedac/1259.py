while True:
    inp = input()
    if inp == '0':
        break
    answer = True
    for i in range(len(inp)//2):
        if inp[i] != inp[len(inp)-1-i]:
            answer = False
            break
    if answer:
        print("yes")
    else:
        print("no")
