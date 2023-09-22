def isRoomEmptyAtTime(room, time):  # 방이 비었는지 확인
    for r in room:
        if r[0] <= time[0] < r[1]:
            return False
        elif r[0] < time[1] <= r[1]:
            return False
        elif time[0] <= r[0] and time[1] >= r[1]:
            return False
    return True

def solution(book_time):
    new_book_time = []
    rooms = []

    for i in range(len(book_time)):
        start_time = int(book_time[i][0][:2]) * 60 + int(book_time[i][0][3:])
        end_time = int(book_time[i][1][:2]) * 60 + int(book_time[i][1][3:])
        new_book_time.append([start_time, end_time + 10])
    new_book_time.sort()

    for time in new_book_time:
        flag = False
        for room in rooms:
            if isRoomEmptyAtTime(room, time) and not flag:  # 해당 room이 비었고, 이때까지 다른 room에 넣지 않았다면
                flag = True
                room.append(time)
        if not flag:  # 해당 time을 넣을 수 있는 빈 방이 없다면, 새 방 만들기
            rooms.append([time])

    return len(rooms)