def cutStick(cutLength, stick):
    if stick < cutLength:
        return 0
    else:
        return stick-cutLength

def zeroStick(stick):
    return stick != 0
    
if __name__ == '__main__':
    numSticks = int(input())
    sticks = list(map(int, input().split()))
    sticks = sorted(sticks)
    while len(sticks) > 0:
        print (len(sticks))
        cutLength = sticks[0]
        sticks = [cutStick(cutLength, ii) for ii in sticks]
        sticks = list(filter(zeroStick, sticks))
