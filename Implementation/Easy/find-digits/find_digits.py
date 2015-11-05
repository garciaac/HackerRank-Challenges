if __name__ == "__main__":
    t = int(input())
    for testCase in range(t):
        n = input().strip()
        yesDigits = {}
        noDigits = {}
        numDivides = 0
        for ii in range(len(n)):
            if int(n[ii]) == 0:
                pass
            elif n[ii] in yesDigits:
                numDivides += 1
            elif n[ii] in noDigits:
                pass
            elif (int(n) % int(n[ii])) == 0:
                numDivides += 1
                yesDigits[n[ii]] = None
            else:
                noDigits[n[ii]] = None
        print(numDivides)