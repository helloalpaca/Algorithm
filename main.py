"""
def solution(n, computers):
    answer = 0
    li = [0 for i in range(n)]

    def DFS(idx):
        if(li[idx]==0):
            li[idx]=1
        for i in range(n):
            if(li[i]==0 and computers[idx][i]==1):
                DFS(i)
    i = 0
    while 0 in li:
        if(li[i]==0):
            li[i]=0
            DFS(i)
            answer+=1
        i+=1

    return answer
"""

def BFS(v, visited):

def solution(n, edge):
    answer = 0
    visited = [-1 for i in range(len(edge))]
    
    return answer