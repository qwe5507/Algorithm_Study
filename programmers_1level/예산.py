# 프로그래머스 Level 1
# 예산

def solution(d, budget):
    answer = 0
    d.sort()

    totalPrice = 0
    for num in d:
        totalPrice += num
        if totalPrice <= budget:
            answer += 1
        else:
            break

    return answer