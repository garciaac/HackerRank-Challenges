if __name__ == "__main__":
    T = int(input())

    for ii in range(T):
        n,c,m = list(map(int, str(input()).split()))
        numChocolates = n // c
        numWrappers = numChocolates
        
        while numWrappers >= m:
            wrapperBonus = numWrappers // m
            numChocolates += wrapperBonus
            numWrappers %= m
            numWrappers += wrapperBonus
     
        print(numChocolates)
