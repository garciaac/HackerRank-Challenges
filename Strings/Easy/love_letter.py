def makePalindrome(string):
    total = 0
    for ii in range(int(len(string)/2)):
        total+=abs(ord(string[ii])-ord(string[len(string)-ii-1]))
    return total

if __name__ == '__main__':
    numTests = int(input())
    for ii in range(numTests):
        print(makePalindrome(input().strip()))