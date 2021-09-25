# 프로그래머스 level 1문제
# 시저 암호

def solution(s, n):
    tempList = []
    for i in s:
        temp = ord(i) + n
        if (ord(i) >= 65 and ord(i) <= 90) and temp > 90:
            temp = temp - 26
        elif (ord(i) >= 97 and ord(i) <= 122) and temp > 122:
            temp = temp - 26
        elif ord(i) == 32:
            temp = ord(i)

        tempList.append(chr(temp))
    return ''.join(tempList)

print(solution("AB", 1));
print(solution("z", 1));
print(solution("Z", 10));
print(solution("a B z", 4));
print(solution(" aBZ", 20));
print(solution("y X Z", 4));
print(solution(" . h z", 20));