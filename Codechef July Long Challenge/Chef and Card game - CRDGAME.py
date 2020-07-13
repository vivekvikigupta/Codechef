test = int(input())
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
while test:
    test -= 1

    N = int(input())

    chef_pt = 0
    morty_pt = 0
    for i in range(N):
        ai, bi = map(int, input().split())
        ai = sum_digits(ai)
        bi = sum_digits(bi)
        if ai > bi:
            chef_pt +=1
        elif ai < bi:
            morty_pt += 1
        else:
            chef_pt += 1
            morty_pt += 1
    if chef_pt > morty_pt:
        print('0' + " " + str(chef_pt))
    elif chef_pt < morty_pt:
        print('1' + " " + str(morty_pt))
    else:
        print('2' + " " + str(chef_pt))
