

t = int(input())
while t:
    t -= 1
    N = int(input())
    Matrix = [[0 for x in range(N)] for y in range(N)]
    counter = 1
    for i in range(N):
        if i % 2 != 0:
            for j in range(N-1, -1, -1):
                Matrix[i][j] = counter
                counter += 1
        else:
            for j in range(N):
                Matrix[i][j] = counter
                counter += 1
    for r in range(N):
        for c in range(N):
            print(Matrix[r][c], end=" ")
        print()