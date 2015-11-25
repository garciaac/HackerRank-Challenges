import math
import sys

tree = []

def build(data):
    global tree
    tree = [None]*2*int(math.pow(2, math.ceil(math.log(len(data), 2))))
    return build_r(0, len(data)-1, 0)

def build_r(start, end, current_index):
    global tree
    if start == end:
        tree[current_index] = int(data[start])
        return tree[current_index]
    else:
        mid = int((start+end)/2)
        tree[current_index] = abs(build_r(start, mid, current_index*2+1)) + abs(build_r(mid+1, end, current_index*2+2))
        return tree[current_index]

def update(current_index, start, end, difference):
    global tree
    if tree[current_index] is None:
        return 0
    
    if start != end:
        mid = int((start+end)/2)
        tree[current_index] = abs(update(current_index*2+1, start, mid, difference)) + abs(update(current_index*2+2, mid+1, end, difference))
        return tree[current_index]
    else:
        tree[current_index] += difference
        return tree[current_index]
            
if __name__ == "__main__":
    with open("case12-input.txt") as infile, open("test-output.txt", "w") as outfile:
        n = int(infile.readline())
        data = infile.readline().split()

        build(data)

        q = input()
        q = infile.readline().split()

        for ii in range(15):
            update(0, 0, n-1, int(q[ii]))
            outfile.write(str(tree[0])+"\n")
#        n = int(sys.stdin.readline())
#        data = list(map(int, sys.stdin.readline().split()))
#
#        build(data)
#
#        q = input()
#        q = list(map(int, sys.stdin.readline().split()))
#
#        for ii in range(len(q)):
#            update(0, 0, n-1, q[ii])
#            sys.stdout.write(str(tree[0])+"\n")