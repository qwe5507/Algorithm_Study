# 프로그래머스 level 1문제
# 두 정수 사이의 합

def solution(a, b):
    sum = 0
    if a <= b :
        for i in range(a,b+1):
            sum += i
    else:
        for i in range(a,b-1,-1):
            sum += i
    return sum
