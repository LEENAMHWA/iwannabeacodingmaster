import sys

nanjaeng_arr = []
for n_idx in range(9):
    nanjaeng_arr.append(int(sys.stdin.readline()))

flag = 0
nanjaeng_sum = sum(nanjaeng_arr)
for c_idx in range(0, len(nanjaeng_arr) - 1):
    for sub_idx in range(c_idx+1, len(nanjaeng_arr)):
        if nanjaeng_sum - (nanjaeng_arr[c_idx] + nanjaeng_arr[sub_idx]) == 100:
            nanjaeng_arr[c_idx] = 0
            nanjaeng_arr[sub_idx] = 0
            flag = 1
            break
    if flag == 1:
        break

nanjaeng_arr.sort()
for c_idx in range(len(nanjaeng_arr)):
    if nanjaeng_arr[c_idx] != 0:
        print(nanjaeng_arr[c_idx])
        
            