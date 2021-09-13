# 프로그래머스 level 1 정수 내림차으로 배치하기

def solution(n):
    list = [int(i) for i in str(n)]
    list.sort(reverse=True)
    lists = [str(i) for i in list]

    return int("".join(lists))