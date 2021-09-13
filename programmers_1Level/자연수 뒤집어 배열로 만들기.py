# 프로그래머스 level 1 자연수 뒤집어 배열로 만들기

def solution(n):
    return [int(str(n)[i]) for i in range(len(str(n))-1,-1,-1)]

    # 다른 사람 풀이
    #return [int(i) for i in str(n)][::-1]