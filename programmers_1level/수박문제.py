# 프로그래머스 level 1문제
# 수박수박수박수? 문제
def solution(n):
    return "수박" * (n // 2) + ("수" * (n % 2))