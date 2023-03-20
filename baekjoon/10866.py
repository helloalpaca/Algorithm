from collections import deque

def solution(N, cmds):
    answer = ""
    d = deque()

    for i in range(N):
        if len(cmds[i]) == 2:
            if cmds[i][0] == "push_front":
                d.appendleft(cmds[i][1])
            elif cmds[i][0] == "push_back":
                d.append(cmds[i][1])
        else:
            if cmds[i][0] == "pop_front":
                if d:
                    answer += d.popleft()
                else:
                    answer += "-1"
            elif cmds[i][0] == "pop_back":
                if d:
                    answer += d.pop()
                else:
                    answer += "-1"
            elif cmds[i][0] == "size":
                answer += str(len(d))
            elif cmds[i][0] == "empty":
                if d:
                    answer += "0"
                else:
                    answer += "1"
            elif cmds[i][0] == "front":
                if d:
                    answer += str(d[0])
                else:
                    answer += "-1"
            elif cmds[i][0] == "back":
                if d:
                    answer += str(d[-1])
                else:
                    answer += "-1"

            if i < N - 1:
                answer += "\n"


    return answer

if __name__ == '__main__':
    N = int(input())
    cmds = []
    for _ in range(N):
        cmds.append(input().split())

    print(solution(N, cmds))