# 프로그래머스 Level 3 동적계획법
# N으로 표현

def solution(N, number):
    s = [set() for x in range(8)]
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    for i in range(len(s)):
        for j in range(i):
            for op1 in s[j]: # 앞에 놓인 수 마련 // op1은 ex) op1 * op2 이렇게 첫번쨰오는 숫자
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:   # 뒤쪽에 오는 수가 0이면 나눗셈을 할 수 없다.
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1

    return answer