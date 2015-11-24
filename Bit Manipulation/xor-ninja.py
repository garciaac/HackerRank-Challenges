import math

if __name__ == "__main__":
    with open("input.txt") as infile:
        t = int(input())
        for case in range(t):
            n = int(input())
            arr = list(map(int, input().split()))
            or_result = 0
            for ii in range(len(arr)):
                or_result = (or_result|arr[ii])%(1000000000+7)

            print(int((or_result*(2**(n-1)))%(1000000000+7)))