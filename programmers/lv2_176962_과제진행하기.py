from collections import deque

def calc_time(str):
    return int(str[:2]) * 60 + int(str[3:])

def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])
    q = deque(plans)
    left = []

    while q:
        work = q.popleft() #이전 과제
        new_work = q[0] if q else ('', '99:99', '') #새로운 과제

        title, start, time = work[0], calc_time(work[1]), int(work[2])
        next_start = calc_time(new_work[1])
        free = next_start - (start + time)

        if free < 0: #이전 과제가 끝나기 전에, 다음 과제 시작 -> 이전 과제 남는 시간을 넣어야 한다.
            time -= next_start - start
            left.append([title, start, time])
        else: #이전 과제가 끝난 후에, 다음 과제 시작 -> 중간에 비는 시간이 있다면, stack에서 꺼내서 계산
            answer.append(title)
            while free > 0 and left:
                lf = left.pop()
                if free >= lf[2]:
                    free -= lf[2]
                    answer.append(lf[0])
                else:
                    lf[2] -= free
                    free = 0
                    left.append([lf[0], lf[1], lf[2]])

    while left:
        answer.append(left.pop()[0])

    return answer


def parse_task(task):
    name, time, duty = task
    return name, parse_time(time), int(duty)


def parse_time(time):
    return 60 * int(time[:2]) + int(time[3:])

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))