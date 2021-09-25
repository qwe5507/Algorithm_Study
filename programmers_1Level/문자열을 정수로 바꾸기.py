# 프로그래머스 level 1문제
# 문자열을 정수로 바꾸기

def solution(s):
    if s in "+-":
        return int(s[1:])
    else:
        return int(s)