# 프로그래머스 Level 1
# 이상한 문자 만들기

# s.split() : 공백이 여러개 있어도 무조건 처리한다
# ex) "try     hello                            world" => ['try', 'hello', 'world']
# s.split(" ") : 공백 마다 분리
# ex) "try     hello                            world" => 	['try', '', '', '', '', 'hello', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'world']

# split과 문제를 제대로 이해못해서 시간을 오래잡아먹음..ㅜ 입력된 공백 포함된 문자열이 그대로 반환되어야 통과
def solution(s):
    result = []
    words = s.split(" ")

    for i in words:
        strList = ""
        for j in range(len(i)):
            if j % 2 == 0:
                strList += i[j].upper()
            else:
                strList += i[j].lower()
        result.append(strList)

    return " ".join(result)

if __name__ == '__main__':
    print(solution("           try     hello      world                      "))