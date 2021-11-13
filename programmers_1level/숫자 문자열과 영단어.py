# 2021 카카오 채용연계형 인턴십
# 숫자 문자열과 영단어

def solution(s):
    words = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
             'eight': '8', 'nine': '9'}
    answer = s
    for i, j in words.items():
        answer = answer.replace(i, j)
    return int(answer)
