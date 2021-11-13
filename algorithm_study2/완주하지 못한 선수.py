# 프로그래머스 완주하지 못한 선수

def solution(participant, completion):
    temp = {}

    for i in participant:
        temp[i] = temp.get(i, 0) + 1
    for i in completion:
        temp[i] -= 1

    result = [k for (k, v) in temp.items() if v > 0]

    return result[0]