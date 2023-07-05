N = int(input())
arr = [d for d in map(int, input().split())]
max_num = max(arr)
new_sum = 0

for ar in arr:
    new_sum += (ar/max_num)*100

print(new_sum/len(arr))