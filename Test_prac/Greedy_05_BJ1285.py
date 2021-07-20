# 동전 뒤집기
import sys

def cal_cols(tmp_list, col_idx):
    result_val = 0

    for r_idx in range(len(tmp_list)):
        result_val += tmp_list[r_idx][col_idx]
    return result_val

N = int(sys.stdin.readline().split()[0])
coin_arr = []
for n_idx in range(N):
    tmp_coin = sys.stdin.readline().rstrip()
    tmp_coin = [0 if coin =='T' else 1 for coin in tmp_coin]
    coin_arr.append(tmp_coin)

print(coin_arr)