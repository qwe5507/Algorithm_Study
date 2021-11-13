#월간 코드 챌린지 시즌2
#음양 더하기

def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if not signs[i]:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)
