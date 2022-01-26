# 프로그래머스 Level 1
# 완전탐색
# 모의고사

def solution(answers):
    answer = []
    Anw1 = [1, 2, 3, 4, 5]
    Anw2 = [2, 1, 2, 3, 2, 4, 2, 5]
    Anw3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    supoza1 = 0
    supoza2 = 0
    supoza3 = 0

    for i in range(len(answers)):
        num = answers[i]
        if Anw1[i % 5] == num:
            supoza1 += 1
        if Anw2[i % 8] == num:
            supoza2 += 1
        if Anw3[i % 10] == num:
            supoza3 += 1
    sum = [supoza1, supoza2, supoza3]
    maxscore = max(sum)

    for i in range(3):
        if maxscore == sum[i]:
            answer.append(i + 1)

    return answer