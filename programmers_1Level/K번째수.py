# 프로그래머스 정렬
# K번째수

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        tempArray = array[i - 1:j]
        tempArray.sort()
        answer.append(tempArray[k - 1])

    return answer