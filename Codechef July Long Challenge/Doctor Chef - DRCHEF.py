test = int(input())
while test:
    test -= 1
    N, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0
    low = 0
    while arr[low] <= x/2:
        count += 1
        low += 1
    for i in range(low, N):
        while arr[i] > x:
            x *= 2
            count += 1
        if(arr[i] == x):
            count += 1
            x *= 2
        elif arr[i] < x:
            x = arr[i] * 2
            count += 1
        else:
            pass
    print(count)