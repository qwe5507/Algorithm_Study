# 프로그래머스 코딩테스트 연습
# 해시
# 전화번호 목록

def solution(phone_book):
    prefix = {}

    for phone in phone_book:
        prefix[phone] = 1

    for phone in phone_book:
        keyword = ""
        for key in phone:
            keyword += key
            if keyword in prefix and phone != keyword:
                return False
    return True