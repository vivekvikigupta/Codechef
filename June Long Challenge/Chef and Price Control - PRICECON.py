test = int(input())
result = []
for i in range(test):
    N, K = map(int, input().split())
    price_list = list(map(int, input().split()))
    sum_min = 0
    sum_max = 0
    for j in range(N):
        sum_max = sum_max + price_list[j]
        if price_list[j] > K:
            sum_min = sum_min + K
        else:
            sum_min = sum_min + price_list[j]
    result.append(sum_max - sum_min)
for i in range(test):
    print(result[i])