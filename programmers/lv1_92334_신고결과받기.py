def solution(id_list, report, k):
    answer = {}
    warn_book = {}
    warned = []
    #초기화
    for id in id_list:
        warn_book[id] = set()
        answer[id] = 0

    for rep in report:
        user, warning = rep.split()
        warn_book[warning].add(user)

    for id in id_list:
        if len(warn_book[id])>=k:
            warned.append(id)

    for id in id_list:
        if id in warned:
            for i in warn_book[id]:
                answer[i]+=1

    print(list(answer.values()))
    return list(answer.values())