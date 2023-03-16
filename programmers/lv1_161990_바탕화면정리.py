def solution(wallpaper):
    list_x = []
    list_y = []
    x = len(wallpaper)
    y = len(wallpaper[0])
    for i in range(x):
        for j in range(y):
            if wallpaper[i][j] =="#":
                list_x.append(i)
                list_y.append(j)

    print(min(list_x), max(list_x)+1)
    print(min(list_y), max(list_y)+1)

    return [min(list_x), min(list_y), max(list_x)+1, max(list_y)+1]
