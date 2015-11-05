memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    else:
        f = (fib(n-1)**2)+fib(n-2)
        memo[n] = f
        return f

if __name__ == "__main__":
    a,b,n = list(map(int, input().split()))
    memo[1] = a
    memo[2] = b
    print(fib(n))