t = int(input())

for ii in range(t):
    nk = list(map(int, input().split()))
    n = nk[0]
    k = nk[1]

    arrivalTimes = sorted(map(int, input().split()))
    
    decisionTime = -1
    for ii in range(len(arrivalTimes)):
        if arrivalTimes[ii] > 0:
            decisionTime = ii
            break
    if decisionTime < k:
        print("YES")
    else:
        print("NO")