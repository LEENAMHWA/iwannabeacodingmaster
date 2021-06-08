import sys

def is_prime(num):
    if num == 0 or num == 1:
        return 1

    for idx in range(2, num):
        if num % idx == 0:
            return 1

    return 0

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr_num = list(map(int, sys.stdin.readline().split()))

    prime_cnt = 0
    for num in arr_num:
        if is_prime(num) == 0:
            prime_cnt += 1
    
    print(prime_cnt)
    