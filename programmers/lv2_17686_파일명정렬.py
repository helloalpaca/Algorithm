def solution(files):
    answer = []
    temp = []

    for i in range(len(files)):
        head = ''
        number = ''
        flag = False
        for j in range(len(files[i])):
            if files[i][j].isdigit() and len(number) < 5:
                flag = True
                number += files[i][j]
            elif not flag:
                head += files[i][j].lower()
            else:
                break
        temp.append([head, int(number), i, files[i]])
    temp.sort()
    answer = [t[3] for t in temp]

    return answer