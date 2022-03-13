# 프로그래머스 Level 1
# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    answer = 0
    cnt_0 = 0
    for num in lottos:
        if num in win_nums:
            answer = answer + 1
        elif num == 0:
            cnt_0 = cnt_0 + 1

    return rank[answer + cnt_0], rank[answer]
