# cook your dish here
test = int(input())
while test:
    test -= 1
    N = int(input())
    x = []
    y = []
    xx = 0
    yy = 0
    N = 4*N-1
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    for j in range(0, N, 2):
        if j == N-1:
            xx = x[j]
            break
        if x[j] == x[j+1]:
            pass
        else:
            xx = x[j]
            break
    for k in range(0, N, 2):
        if k == N-1:
            yy = y[k]
            break
        if y[k] == y[k+1]:
            pass
        else:
            yy = y[k]
            break
    print(str(xx)+" "+str(yy))