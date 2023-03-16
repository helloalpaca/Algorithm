answer = 0
def DFS(numbers, target, idx, value):
    global answer
    if (len(numbers) == idx):
        if value==target:
            answer+=1
            return
    else:
        DFS(numbers,target,idx+1,value+numbers[idx])
        DFS(numbers,target,idx+1,value-numbers[idx])
def solution(numbers, target):

    DFS(numbers, target, 0, 0)
    return answer
