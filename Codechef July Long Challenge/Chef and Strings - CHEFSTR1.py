test = int(input())
while test:
    test -= 1
    skip_count = 0
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1):
        if arr[i] != arr[i+1]:
            skip_count = skip_count + (abs(arr[i] - arr[i+1]) - 1)
    print(skip_count)