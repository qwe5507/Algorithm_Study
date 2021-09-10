# 프로그래머스 level 1 제일 작은 수 제거하기


def solution(arr):
    del arr[arr.index(min(arr))]
    return  [-1] if len(arr) == 0 else arr