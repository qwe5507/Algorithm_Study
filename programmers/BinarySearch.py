# 프로그래머스 파트3. 배열 더 알아보기: 정렬과 탐색(Sorting & Searching) (2 / 2) 강의 문제
# 이진 탐색 (Birnary Search) 풀이 - 반복문으로 풀이
def solution(L, x):
    lower = 0
    upper = len(L) - 1
    answer = -1
    while lower <= upper:
        middle = (lower + upper) // 2  # //는 나누고 int로 반환
        if L[middle] == x:
            answer = middle
            break
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle - 1
    return answer


if __name__ == '__main__':
    print(solution([1,2,3,4,5,6,7,8],4))
    print(solution([],3))
    print(solution([1,2],3))