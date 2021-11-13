# 프로그래머스 level 1문제
# 하샤드 수
# 하샤드 수란 ? 각 자릿수의 합으로 나누어 떨어 지는 수

# 주어진 수를 str로 변경하지 않은 풀이
def solution(x):
    temp = x
    total = 0

    y = 10000
    for i in range(4):
        total += temp // y
        temp = temp - (y * (temp // y))
        y = y // 10
    total = total + temp

    return (x % total == 0 if True else False)

# str로 변경 했을 때 풀이
def solution(n):
    return n % sum([int(c) for c in str(n)]) == 0

