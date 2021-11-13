# 프로그래머스 level 1문제
# 콜라츠 추측
# 문제 설명  아래 조건의 반복 갯수
# 1-1. 입력된 수가 짝수라면 2로 나눕니다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.

def solution(num):
    answer = -1
    temp = num
    if num == 1 :
        return 0
    for i in range(1,501):
        if temp%2 == 0 :
            temp //= 2
        else:
            temp = temp*3 +1
        if temp == 1 :
            answer = i
            break
    return answer