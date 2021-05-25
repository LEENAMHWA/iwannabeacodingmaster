import sys

def GCD(a, b):
    if a % b == 0: 
        return b
    else:
        return GCD(b, a%b)

def LCM(a, b):
    return a * b / GCD(a,b)

if __name__ == "__main__":
    a, b = list(map(int, sys.stdin.readline().split()))

    # GCD
    print(int(GCD(a,b)))

    # LCM
    print(int(LCM(a,b)))