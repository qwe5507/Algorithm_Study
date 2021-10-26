# 프로그래머스 - 같은 숫자는 싫어
def solution(arr):
    answer = []
    j = -1
    for i in arr:
        if i != j:
            j = i
            answer.append(i)

    return answer