# 프로그래머스 level 1문제 부족한 금액 계산하기.

def solution(price, money, count):
    total = 0
    for i in range(1,count+1):
        total += price*i
    if total > money:
        return total-money
    else :
        return 0


# 다른사람 풀이

def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))