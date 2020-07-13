test = int(input())
while test:
    val = 0
    test -= 1
    TS = int(input())
    while TS % 2 == 0:
        # '//' is a floor division and is used to give the quotient as integer since sometimes......
        # it cannot handle large float numbers
        TS = TS//2
    val = TS//2
    print(val)