# 프로그래머스 level 1문제
# 내적 구하기
def solution(a, b):
    #내가 푼 풀이
    # return sum([a[i]*b[i]for i in range(len(a))])
    #다른사람이 푼 풀이
    return sum([a * b for a, b in zip(a, b)])