if __name__ == "__main__":
    num_tests = int(input())
    
    for test in range(num_tests):
        b, w = list(map(int, input().split()))
        x, y, z = list(map(int, input().split()))
        
        if x+z < y:
            output = ((b+w)*x)+(w*z)
        elif y+z < x:
            output = ((b+w)*y)+(b*z)
        else:
            output = (b*x) + (w*y)
            
        print(output)