# 프로그래머스 level 1문제
# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    return [ x+(x*i) for i in range(n)]
print(solution(5,3))

