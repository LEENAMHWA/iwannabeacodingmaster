#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
    
def search_rank(players, rankers, ranker_score):
    
    rank_arr = []
    
    for p_item in players:
        l_idx = 0
        m_idx = len(rankers) // 2
        r_idx = len(rankers)-1
        
        while l_idx <= r_idx:
            m_idx = (l_idx + r_idx) // 2 
            if rankers[m_idx] < p_item:
                r_idx = m_idx - 1
            else:
                l_idx = m_idx + 1
            
            if rankers[m_idx] == p_item:
                break
                
        if rankers[m_idx] <= p_item:   
            rank_arr.append(ranker_score[m_idx])
        else:
            rank_arr.append(ranker_score[m_idx] + 1)
    
    return rank_arr
        


def climbingLeaderboard(ranked, player):
    # Write your code here

    ranked_score = []    
    result = []
    
    # Rank for the Leader Board
    cur_rank = 1
    for r_idx in range(len(ranked)):
        ranked_score.append(cur_rank)
        if r_idx != len(ranked) - 1 and ranked[r_idx] == ranked[r_idx+1]:
            continue 
        cur_rank += 1                   

    result = search_rank(player, ranked, ranked_score)
        
    return result
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    result.sort(reverse=True)
    
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
