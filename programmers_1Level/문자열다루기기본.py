# 프로그래머스 level 1문제
# 문자열 다루기 기본
def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()
#다른사람풀이
    # return s.isdigit() and len(s) in (4, 6)