# 프로그래머스 Level 1
# 약수의 합

def solution(n):
    answer = 0
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return sum(result)


