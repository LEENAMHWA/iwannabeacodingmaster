# 큰 수의 법칙
"""
문제 
여기서 큰 수의 법칙이란 다양한 수로 이뤄진 배열이 있을 때 주어진 수들을 M번 더해 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과할 수는 없음
 
입력 조건
첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며 각 자연수는 공백으로 구분
둘째줄에 N개의 자연수가 주어짐. 각 자연수는 공백으로 구분. 단, 각각의 자연수는 1이상 10000이하의 수로 주어짐
입력으로 주어지는 K는 항상 M보다 작거나 같다.
 
출력 조건
첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력
 
입력 예시
5 8 3
2 4 5 4 6 
 
출력 예시
46 

"""
import sys

N, M, K = list(map(int,sys.stdin.readline().split()))
n_list = sorted(list(map(int,sys.stdin.readline().split())), reverse=True)

n_sum = 0
for iter_idx in range(M):
    if iter_idx != 0 and iter_idx % K == 0:
        n_sum += n_list[1]
    else:
        n_sum += n_list[0]

print(n_sum)