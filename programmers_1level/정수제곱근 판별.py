# 프로그래머스 level 정수 제곱근 판별

def solution(n):
    answer = 0
    idx = 1
    while True:
        if idx * idx == n:
            return (idx +1) * (idx +1)
        if idx >= n :
            return -1
        idx += 1