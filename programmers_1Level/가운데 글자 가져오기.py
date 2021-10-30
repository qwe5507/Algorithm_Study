# 프로그래머스 1레벨 가운데 글자 가져오기

def solution(s):
    i = len(s) // 2

    if len(s) % 2 != 0:
        return s[i]
    else:
        return s[i - 1:i + 1]