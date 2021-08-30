# 프로그래머스 level 1문제
# 행렬의 덧셈

def solution(arr1, arr2):
    print(list(zip(arr1, arr2)))

    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[i]))] for i in range(len(arr1))]
    # 다른 사람 풀이 zip
    # return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1,arr2)]

print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))