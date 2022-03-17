# 프로그래머스 level 1문제 - 2019 KAKAO BLIND RECRUITMENT
# 실패율
def solution(N, stages):
    tmpdict = {}
    for i in range(1, N + 1):
        tmpdict[i] = 0

    for i in stages:
        if i == N + 1:
            continue
        tmpdict[i] = tmpdict[i] + 1

    cnt = len(stages)
    for i in range(1, N + 1):
        if tmpdict[i] == 0:
            continue
        tmp = tmpdict[i]
        tmpdict[i] = tmpdict[i] / cnt
        cnt = cnt - tmp

    result = sorted(tmpdict.items(), key=lambda item: item[1], reverse=True)

    return [x for x, y in result]