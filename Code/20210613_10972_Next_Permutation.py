import sys

N = int(sys.stdin.readline().split()[0])
n_list = list(map(int,sys.stdin.readline().split()))
len_n = len(n_list)

for idx in range(len_n-2, -2, -1):
    if idx == -1:
        # 탐색 끝
        print(-1)
        break
    elif idx > -1:
        # 탐색 알고리즘
        if n_list[idx] < n_list[idx + 1]:
            max = 0
            max_index = 0
            for sub_idx in range(idx+1,len_n):
                if max < abs(sub_idx - idx) and n_list[sub_idx] > n_list[idx]:
                    max = abs(sub_idx - idx)
                    max_index = sub_idx
            n_list[idx],n_list[max_index] = n_list[max_index], n_list[idx]
            n_list = n_list[:idx+1] + sorted(n_list[idx+1:])
            
            for l_idx in range(len_n):
                print(n_list[l_idx], end=' ')
            
            break
        else:
            continue