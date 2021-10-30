#프로그래머스 - 월간코드 챌린지 시즌3 - 없는 숫자 더하기

# def solution(numbers):
#     return 45 - sum(numbers)

def solution(numbers):
    total = sum([i for i in range(10)])
    return total - sum(numbers)