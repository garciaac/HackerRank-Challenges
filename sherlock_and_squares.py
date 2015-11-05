import math

if __name__ == "__main__":
    num_tests = int(input())
    
    for test in range(num_tests):
        a, b = list(map(int, input().split()))
        
        square = b+1
        
        for ii in range(a, b+1):
            if (math.sqrt(ii).is_integer()):
                square = ii
                n = math.sqrt(square)
                break
                
        num_squares = 0        
        while (square <= b):
            square += (2*n)+1
            n += 1
            num_squares += 1
        
        print(num_squares)