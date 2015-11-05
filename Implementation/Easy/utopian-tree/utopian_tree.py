numTestCases = int(input())
for ii in range (numTestCases):
    height = 1
    cycles = int(input())
    for jj in range(cycles):
        if (jj+1)%2 == 0:
            height+=1
        else:
            height*=2
    print(height)