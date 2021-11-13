# 프로그래머스 level 1문제
# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer

# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]