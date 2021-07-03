import sys

N = int(sys.stdin.readline().split()[0])
n_list = list(map(int,sys.stdin.readline().split()))

for idx in range(N-2, -2, -1):
    if idx == -1:
        # 탐색 끝
        print('-1')
        break
    elif idx > -1:
        # 탐색 알고리즘
        if n_list[idx] < n_list[idx + 1]:
            min = N
            min_index = N-1
            for sub_idx in range(idx+1,N):
                if min > abs(n_list[sub_idx]-n_list[idx]):
                    min = abs(n_list[sub_idx]-n_list[idx])
                    min_index = sub_idx
            n_list[idx],n_list[min_index] = n_list[min_index], n_list[idx]
            
            # 부분 정렬 필요
            n_list = n_list[:idx+1] + sorted(n_list[idx+1:])
            
            for l_idx in range(len(n_list)):
                print(n_list[l_idx], end=' ')

            break
        else:
            continue