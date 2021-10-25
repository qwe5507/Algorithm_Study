# 프로그래머스 - 같은 숫자는 싫어
# 통과긴 하지만 효율성, 정확성 점수가 높지 않다
def solution(arr):
    answer = []

    j = -1
    for i in arr:
        if i == j:
            continue
        j = i
        answer.append(i)

    return answer