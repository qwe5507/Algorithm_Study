# 프로그래머스 level 1문제
# 문자열 내 p와 y의 개수

def solution(s):
    lowerS = s.lower()
    tBox,pBox = 0,0
    for char in lowerS:
        if char == "p":
            tBox += 1
        elif char == "y":
            pBox += 1
    else:
        if tBox == pBox:
            return True
        else:
            return False