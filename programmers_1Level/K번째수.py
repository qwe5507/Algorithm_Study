# 프로그래머스 정렬
# K번째수

def solution(array, commands):
    answer = []
    for i in commands:
        tempArray = array[i[0] - 1:i[1]]
        tempArray.sort()
        answer.append(tempArray[i[2] - 1])

    return answer