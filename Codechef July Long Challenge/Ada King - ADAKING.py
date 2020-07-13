test = int(input())
while test:
    test -= 1
    arr = [[0 for x in range(8)] for y in range(8)]
    k = int(input())
    arr[0][0] = 'O'
    k -= 1
    for i in range(8):
        for j in range(8):
            if i == 0 and j == 0:
                continue
            if k > 0:
                arr[i][j] = '.'
                k -= 1
            else:
                arr[i][j] = 'X'
    for x in range(8):
        for y in range(8):
            print(arr[x][y], end='')
        print()