from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 = sum(q1)
    s2 = sum(q2)
    goal = (s1 + s2) // 2
    limit = len(q1) * 2 + len(q2) * 2

    if (s1 + s2) % 2 != 0:  # sum이 홀수이면 달성 불가능
        return -1
    if s1 == s2:
        return 0

    for q in q1:  # queue에 있는 원소 중에 goal보다 큰값이 있으면 -1
        if q > goal:
            return -1
    for q in q2:
        if q > goal:
            return -1

    cnt = 0
    while cnt <= limit:
        if s1 == s2:
            return cnt
        elif s1 < s2:
            target = q2.popleft()
            s1 += target
            s2 -= target
            q1.append(target)
        else:
            target = q1.popleft()
            s2 += target
            s1 -= target
            q2.append(target)
        cnt += 1

    return -1