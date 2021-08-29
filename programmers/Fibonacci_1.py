# 파트4. 재귀 알고리즘(Recursive Algorithms) 기초 문제
# 피보나치 수열 재귀적 , 반복적 버전

# 재귀
# def solution(x):
#     # answer = 0
#     if x < 2:
#         return x
#     else:
#         return solution(x-1)+solution(x-2)
#반복적 내가 푼거
def solution(x):
    i = 0
    j = 1
    idx = 0
    while True:
        if idx == x:
            break
        idx += 1
        i,j =j, i+j
    return i

# 다른사람 풀이 반복적
# def solution(x):
#     answer = 0
#     fa = 0
#     fb = 1
#     while x > 0:
#         x -= 1
#         fa, fb = fb, fa+fb
#         answer = fa
#     return answer

if __name__ == '__main__':
    print(solution(4))