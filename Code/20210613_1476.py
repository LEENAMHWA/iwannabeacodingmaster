import sys

E, S, M = list(map(int,sys.stdin.readline().split()))

guess_num = 1
while True:
    if (guess_num - E) % 15 == 0:
        if (guess_num - S) % 28 == 0:
            if (guess_num - M) % 19 == 0:
                break
    
    guess_num += 1

print(guess_num)