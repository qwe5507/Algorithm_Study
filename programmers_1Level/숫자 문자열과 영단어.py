# 2021 카카오 채용연계형 인턴십
# 숫자 문자열과 영단어

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    answer = ""
    temp = ""

    for i in s:
        if i.isdigit():
            answer += str(i)
            continue
        temp += i
        if temp in words:
            answer += str(words.index(temp))
            temp = ""

    return int(answer)
