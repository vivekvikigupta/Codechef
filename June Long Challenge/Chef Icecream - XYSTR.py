test = int(input())
while test:
    test -= 1
    N = int(input())
    flag = 1
    five_coin = 0
    ten_coin = 0
    coins = list(map(int, input().split()))
    if coins[0] != 5:
        flag = 0
    else:
        for i in range(N):
            if coins[i] == 5:
                five_coin += 1
            elif coins[i] == 10:
                ten_coin += 1
                if five_coin > 0:
                    five_coin -= 1
                else:
                    flag = 0
                    break
            else:
                if ten_coin > 0:
                    ten_coin -= 1
                elif five_coin > 1:
                    five_coin -= 2
                else:
                    flag = 0
                    break
    if flag == 1:
        print("YES")
    else:
        print("NO")
