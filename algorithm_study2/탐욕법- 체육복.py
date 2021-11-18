# 월간 코드 챌린지 시즌1
# 3진법 뒤집기

def solution(n):
    # 10진법 -> N진법
    # 10진법을 N으로 나누면서 나머지를 표기하면 된다.
    answer = [];
    temp = n
    while temp // 3 != 0 or temp % 3 != 0:
        answer.append(str(temp % 3))
        temp = temp // 3
    print("".join(answer))

    # N진법 -> 10진법
    # 내일 이어서 풀기


