# 프로그래머스 level 1문제
# 핸드폰 번호 가리기

def solution(phone_number):
    return (len(phone_number)-4)*'*' + phone_number[-4:]