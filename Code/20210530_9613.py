import sys

def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    
    for t_idx in range(t):
        gcd_sum = 0
        case_arr = list(map(int, sys.stdin.readline().split()))
        n = case_arr.pop(0)

        gcd_a = 0; gcd_b = 1
        while True:
            gcd_sum += GCD(case_arr[gcd_a], case_arr[gcd_b])
            
            if gcd_a == n - 2 and gcd_b == n - 1:
                print(gcd_sum)
                break
            else:
                if gcd_b == n - 1:
                    gcd_a += 1
                    gcd_b = gcd_a + 1
                else:
                    gcd_b += 1
