import sys

if __name__ == "__main__":
    a, b, c = list(map(int,str(sys.stdin.readline()).split()))
    print((a + b) % c)
    print(((a % c) + (b % c)) % c)
    print((a * b) % c)
    print(((a % c) * (b % c)) % c) 

    