test = int(input())

while test:
    test -= 1
    flag = 0
    mini = 2 << 30
    ele_set = set()
    ele_A = []
    ele_B = []
    lenA = 0
    lenB = 0
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    frq1 = {}
    frq2 = {}
    for i in arr1:
        if i in frq1:
            frq1[i] += 1
        else:
            frq1[i] = 1
            frq2[i] = 0
            ele_set.add(i)

    for i in arr2:
        if i in frq2:
            frq2[i] += 1
        else:
            frq2[i] = 1
            if i not in ele_set:
                frq1[i] = 0
                ele_set.add(i)
    for i in ele_set:
        count1 = frq1[i]
        count2 = frq2[i]
        frq = count1 + count2
        if (count1 + count2) % 2 != 0:
            flag = 1
            break

        if mini > i:
            mini = i

        if count1 < count2:
            for j in range((count2 - count1) >> 1):
                ele_B.append(i)
                lenB += 1
        elif(count2 < count1):
            for j in range((count1 - count2) >> 1):
                ele_A.append(i)
                lenA += 1

    if lenA != lenB:
        flag = 1

    if flag:
        print(-1)
        continue

    ele_A.sort()
    ele_B.sort()

    mini *= 2

    lessMinA = 0
    lessMinB = 0
    for i in ele_A:
        if i > mini:
            break
        lessMinA += 1
    greatMinA = lenA - lessMinA

    for i in ele_B:
        if i > mini:
            break
        lessMinB += 1
    greatMinB = lenB - lessMinB

    cost = 0

    if(lessMinA <= greatMinB):
        for i in ele_A[:lessMinA]:
            cost += i
        for i in ele_B[:lessMinB]:
            cost += i
        cost += (mini * (greatMinA - lessMinB))

    else:
        for i in ele_A[:(greatMinB)]:
            cost += i
        for i in ele_B[:(greatMinA)]:
            cost += i

        i = greatMinB
        j = greatMinA
        for k in range(lessMinB - greatMinA):
            if ele_A[i] < ele_B[j]:
                cost += ele_A[i]
                i += 1
            else:
                cost += ele_B[j]
                j += 1
    print(cost)