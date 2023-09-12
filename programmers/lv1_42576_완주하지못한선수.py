# 11줄에서 8줄로 3줄 줄임
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            participant[-1] = participant[i]
            break
    return participant[-1]