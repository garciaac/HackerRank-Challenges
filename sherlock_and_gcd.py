from fractions import gcd

if __name__ == "__main__":
    t = int(input())
    for test in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        denom = False
        for ii in range(1, len(a)):
            print(str(a[ii])+": "+str(gcd(a[ii]-1, a[ii]))) 
            if gcd(a[ii-1], a[ii]) == 1:
                print("YES")
                denom = True
                break
        
        if not denom:
            print("NO")
            
        
        