import sys

def merge_sort(arr):
    global ans
    if len(arr) == 1:
        return arr

    mid = (len(arr)+1)//2
    l_arr = merge_sort(arr[:mid])
    r_arr = merge_sort(arr[mid:])

    merged_arr = []
    l=0
    r=0
    while l<len(l_arr) and r<len(r_arr):
        if l_arr[l] < r_arr[r]:
            merged_arr.append(l_arr[l])
            ans.append(l_arr[l])
            l+=1
        else:
            merged_arr.append(r_arr[r])
            ans.append(r_arr[r])
            r+=1
    merged_arr += l_arr[l:]
    ans += l_arr[l:]
    merged_arr += r_arr[r:]
    ans += r_arr[r:]
    return merged_arr

N, E = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
ans = []

merge_sort(arr)

if len(ans) >= E:
    print(ans[E-1])
else:
    print(-1)
