import math

def solution(fees, records):
    answer = []
    dct = {}
    cars = []
    for record in records:
        t, num, status = record.split(" ")
        flag = False
        for i in range(len(cars)): #for문 돌아가면서 cars에 차량번호 있는지 확인
            if cars[i][0] == num: #있으면 기존에 car, time에서 빼서 계산 후 dct에 넣기
                car = cars.pop(i)
                total = (int(t[:2]) - int(car[1][:2])) * 60 + int(t[3:]) - int(car[1][3:])
                if car[0] in dct.keys():
                    dct[car[0]] = dct[car[0]] + total
                else:
                    dct[car[0]] = total
                flag = True
                break

        if not flag: #cars에 없다면 넣어주기
            cars.append([num, t])
    # 남아있는 차 계산하기
    for i in range(len(cars)):
        car = cars[i] #pop(i)를 빼니까 런타임 오류에서 벗어남
        total = (23 - int(car[1][:2])) * 60 + 59 - int(car[1][3:])
        if car[0] in dct.keys():
            dct[car[0]] = dct[car[0]] + total
        else:
            dct[car[0]] = total
    # 정렬
    dct = [[k, dct[k]] for k in dct.keys()]
    dct.sort(key=lambda x: x[0])
    # 금액 계산하기
    for d in dct:
        if d[1] < fees[0]:  # 기본 시간보다 작으면 기본요금만
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((d[1] - fees[0]) / fees[2]) * fees[3])
    return answer