if __name__ == "__main__":
    endd, endm, endy = list(map(int, input().split()))
    startd, startm, starty = list(map(int, input().split()))
    
    if endy > starty:
        print("10000")
    elif endm > startm and endy == starty:
        print(str(500*(endm-startm)))
    elif endd > startd and endm == startm:
        print(str(15*(endd-startd)))
    else:
        print("0")