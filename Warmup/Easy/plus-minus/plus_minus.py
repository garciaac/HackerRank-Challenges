from string import Formatter
if __name__ == '__main__':
    input()
    array = list(map(int, input().split()))
    p, n, z = 0, 0, 0
    for ii in range(len(array)):
        if array[ii] > 0:
            p += 1
        elif array[ii] < 0:
            n += 1
        else:
            z += 1
    print ('{0:.3f}'.format(p/len(array)))
    print ('{0:.3f}'.format(n/len(array)))
    print ('{0:.3f}'.format(z/len(array)))
    