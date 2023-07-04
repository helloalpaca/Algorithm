
#  내가 푼 코드 -> bottom-up인데 그다음걸 미리 계산하는 방법 (176ms)
# N = int(input())
# arr = [0] * (N+1)
#
# for i in range(1, N+1):
#     if i+1 <= N and (arr[i+1] == 0 or arr[i+1] > arr[i]+1) : arr[i+1] = arr[i]+1
#     if 2*i <= N and (arr[2*i] == 0 or arr[2*i] > arr[i]+1) : arr[2*i] = arr[i]+1
#     if 3*i <= N and (arr[3*i] == 0 or arr[3*i] > arr[i]+1) : arr[3*i] = arr[i]+1
#
# print(arr[N])

# Code.plus에서 아이디어 얻고 푼 코드 (144ms)
N = int(input())
arr = [0] * (N+1)

for i in range(2, N+1):
    arr[i] = arr[i-1]+1
    if i%2 == 0 and arr[i] > arr[i//2]+1: arr[i] = arr[i//2] + 1
    if i%3 == 0 and arr[i] > arr[i//3]+1: arr[i] = arr[i//3] + 1
print(arr[N])