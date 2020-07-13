test = int(input())
flag = 0
while test:
    test = test-1
    strg = input()
    count = 0
    flag = 0
    for j in range(1,len(strg)):
        if flag == 1:
            flag = 0
            continue
        if strg[j-1] == 'x' and strg[j] =='y':
            count += 1
            flag = 1
        elif strg[j-1] == 'y' and strg[j] =='x':
            count += 1
            flag = 1
        else:
            pass
    print(count)